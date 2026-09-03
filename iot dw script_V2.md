```tex
Latest Version DEV
===============================================================
已修改的环境：isit
1.添加coss_dm.dm_tmu_more_dev_realtime_minf表的主键
2.修改coss_dwd.dwd_tmu_more_dev_realtime_minf sensor_time 字段的时间类型
===============================================================
isit接口已经废弃 10.66.168.169
新的接口是在pre pro 10.66.169.102
===============================================================
dm_tmu_sensor_data_stg_mini.select sql 要添加到共享文件夹,已经添加

```

# ods

## ods_cmsdms_extract_device_realtime_min（调度）

### ods_cmsdms_tmu_more_dev_realtime_minf

#### create table

```sql
drop table if exists coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf;

create table if not exists coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf (
    device_code      varchar(200),
    sensor_id        varchar(200),
    value            decimal(20,5),
    "time"           bigint,
    ods_update_time  timestamp(6) null default pg_systimestamp(),
    ods_load_time    timestamp(6) null default pg_systimestamp(),
    primary key (device_code)
);
comment on table coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf is 'CMSDMS System More Device Realtime';
comment on column coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf.device_code is 'Device Code';
comment on column coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf.sensor_id is 'Sensor Id';
comment on column coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf.value is 'Sensor Value';
comment on column coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf."time" is 'Sensor Time';
comment on column coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf.ods_load_time is 'Ods Load Time';
```

#### interface

```python
# -*- coding: utf-8 -*-
"""
Multi-device real-time data acquisition and storage script
Function: Retrieve device list from database, batch call API to get real-time data, and finally store it in target database
Optimized: 100-thread concurrent API calls
"""
import requests
import pandas as pd
import config
import gaussdb
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue

# ===================== Configuration =====================
API_URL = 'http://10.66.169.102:8330/share/data/sensor/moreDevRealtime'
HEADERS = {'Content-Type': 'application/json'}
TARGET_TABLE = 'coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf'
CONSTRAINT_KEYS = ['device_code']
MAX_WORKERS = 100
BATCH_SIZE = 500
# =========================================================

result_queue = Queue()

def fetch_device_realtime(device_code):
    try:
        payload = {"deviceCodes": [device_code]}
        response = requests.post(
            url=API_URL,
            json=payload,
            headers=HEADERS,
            timeout=15
        )
        response.raise_for_status()
        res_data = response.json()
        data_list = res_data.get('data', [])

        records = []
        for item in data_list:
            records.append([
                item.get('deviceCode'),
                item.get('sensorId'),
                item.get('value'),
                item.get('time')
            ])
        result_queue.put(records)

    except Exception as e:
        print(f"Device data fetch failed: {device_code}, error: {str(e)}")

def fetch_and_save_realtime_data():
    # Initialize database connection
    try:
        db_conn = gaussdb.GaussDB(**config.GAUSSDB_DWS)
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
        return

    try:
        # Get total device count
        count_sql = "SELECT COUNT(DISTINCT device_code) FROM coss_dim.dim_tmu_iot_device_info"
        total_devices = db_conn.fetch_data(count_sql)[0][0]
        print(f"Total number of devices in database: {total_devices}")

        # Get all device codes by pagination
        all_devices = []
        offset = 0
        while offset < total_devices:
            device_sql = f"""
                SELECT DISTINCT device_code
                FROM coss_dim.dim_tmu_iot_device_info
                ORDER BY device_code
                LIMIT {BATCH_SIZE} OFFSET {offset}
            """
            offset += BATCH_SIZE
            device_records = db_conn.fetch_data(device_sql)
            all_devices.extend([record[0] for record in device_records])

        print(f"All device codes loaded, total: {len(all_devices)}")

        # Concurrent API requests
        print(f"Start concurrent API calls with {MAX_WORKERS} threads...")
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(fetch_device_realtime, code) for code in all_devices]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Thread execution exception: {str(e)}")

        # Collect all results
        all_records = []
        while not result_queue.empty():
            all_records.extend(result_queue.get())

        print(f"All API calls completed, valid data records obtained: {len(all_records)}")

        # Save to database
        if all_records:
            df = pd.DataFrame(
                all_records,
                columns=['device_code', 'sensor_id', 'value', 'time']
            )
            try:
                import request_json
                request_json.save_to_gaussdb(
                    df,
                    config.GAUSSDB_DWS,
                    TARGET_TABLE,
                    CONSTRAINT_KEYS
                )
                print(f"Data saved to database table successfully: {TARGET_TABLE}")
            except Exception as e:
                print(f"Data save to database failed: {e}")
        else:
            print("No valid data to save to database")

    except Exception as e:
        print(f"Main process execution error: {str(e)}")

if __name__ == "__main__":
    fetch_and_save_realtime_data()


```



### ods_cmsdms_tmu_permission_info_df

#### create table

```sql
drop table if exists coss_ods.ods_cmsdms_tmu_permission_info_df;

create table if not exists coss_ods.ods_cmsdms_tmu_permission_info_df (
    device_id        varchar(200) not null,
    device_code      varchar(200),
    device_name      varchar(200),
    org_id           varchar(200),
    business_type    varchar(120),
    group_id         varchar(200),
    sensor_id        varchar(200) not null,
    sensor_code      varchar(200),
    sensor_name      varchar(200),
    unit             varchar(120),
    ods_update_time  timestamp(6) null default current_timestamp,
    ods_load_time    timestamp(6) null default current_timestamp,
    primary key (device_id,org_id,group_id,sensor_id)
);

comment on table coss_ods.ods_cmsdms_tmu_permission_info_df is 'CMSDMS Permission Information';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.device_id is 'Device Id';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.device_code is 'Device Code';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.device_name is 'Device Name';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.org_id is 'Org Id';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.business_type is 'Business Type';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.group_id is 'Group Id';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.sensor_id is 'Sensor Id';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.sensor_code is 'Sensor Code';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.sensor_name is 'Sensor Name';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.unit is 'Unit';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_cmsdms_tmu_permission_info_df.ods_load_time is 'Ods Load Time';
```

#### interface

```python
# -*- coding: utf-8 -*-
# File : ods_cmsdms_tmu_permission_info_df
# Author : CDM
# Date : 2026/07/09 16:59

# -*- coding: utf-8 -*-
"""
CMSDMS Device Permission Sensor Data Synchronization Script
"""
import time
import random
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
from threading import Semaphore
import config
import request_json

# ======================== Global Configuration Area (Centralized management of all hardcoded values) ========================
# API base address and request headers
BASE_URL = "http://10.66.110.106:8325"
API_PATH = "/share/data/permission"
FULL_API_URL = f"{BASE_URL}{API_PATH}"
HEADERS = {
    "Content-Type": "application/json",
    "appId": "123456",
    "task-mark": "sensor-permission-sync-task"  # Business identifier to prevent high-frequency request bursts
}

# Pagination parameters
PAGE_SIZE = 1000

# API rate limit & retry security parameters
MAX_WORKERS = 15               # Maximum thread count of thread pool
SEMAPHORE_LIMIT = 8            # Max instantaneous concurrent requests (core semaphore rate limit)
REQUEST_INTERVAL = 0.3         # Mandatory throttling sleep after each request to reduce QPS
MAX_RETRY_TIMES = 3            # Max retry attempts for network / 5xx server errors
RETRY_BACKOFF_BASE = 1         # Base seconds for exponential backoff

# Tiered timeout (separate connect & read timeout to release stuck threads quickly)
CONNECT_TIMEOUT = 8
READ_TIMEOUT = 20
TIMEOUT_TUPLE = (CONNECT_TIMEOUT, READ_TIMEOUT)

# Batch task submission control, avoid creating massive Futures at once
BATCH_SUBMIT_SIZE = 30

# Memory protection: Queue maximum capacity limit
QUEUE_MAX_CAP = 500

# Target database table and composite primary key
TARGET_TABLE = "coss_ods.ods_cmsdms_tmu_permission_info_df"
CONSTRAINT_KEYS = ["device_id", "org_id", "group_id", "sensor_id"]

# Global thread-safe containers
data_queue = Queue(maxsize=QUEUE_MAX_CAP)
fail_page_list = []
req_semaphore = Semaphore(SEMAPHORE_LIMIT)
# ===================================================================================

# ======================== Common Utility Functions (Decoupled & reusable logic) ========================
def print_log(msg: str, level: str = "INFO") -> None:
    """Unified hierarchical log printing, remove redundant output
    Args:
        msg: Log content text
        level: INFO/WARN/ERROR
    """
    level_prefix = {
        "INFO": "[INFO] ✅",
        "WARN": "[WARN] ⚠️",
        "ERROR": "[ERROR] ❌"
    }.get(level, "[INFO]")
    print(f"{level_prefix} {msg}")


def get_total_page_count() -> int:
    """Initial API request to query total page count (separated initialization logic)
    Returns:
        int: Total page number
    """
    init_payload = {
        "deviceCodes": [],
        "businessType": "",
        "pageNo": 1,
        "pageSize": PAGE_SIZE
    }
    resp = requests.post(
        url=FULL_API_URL,
        json=init_payload,
        headers=HEADERS,
        timeout=TIMEOUT_TUPLE
    )
    resp.raise_for_status()
    res_json = resp.json()
    if not res_json.get("success") or res_json.get("code") != 200:
        raise Exception(f"Initial pagination query failed: {res_json.get('message')}")
    total_pages = res_json["data"]["pages"]
    total_records = res_json["data"]["total"]
    print_log(f"Pagination initialization completed, total records: {total_records}, total pages: {total_pages}")
    return total_pages


def fetch_single_page(page_no: int) -> None:
    """Single page API request: rate limit, auto retry, exception classification, enqueue data
    Args:
        page_no: Current page number to pull
    """
    payload = {
        "deviceCodes": [],
        "businessType": "",
        "pageNo": page_no,
        "pageSize": PAGE_SIZE
    }
    retry_count = 0
    task_success = False

    while retry_count <= MAX_RETRY_TIMES and not task_success:
        try:
            with req_semaphore:
                # Tiny random jitter to avoid synchronized request spikes overwhelming API
                time.sleep(random.uniform(0.05, REQUEST_INTERVAL))
                resp = requests.post(
                    url=FULL_API_URL,
                    json=payload,
                    headers=HEADERS,
                    timeout=TIMEOUT_TUPLE
                )
                # Classify and handle abnormal status codes
                if 400 <= resp.status_code < 500:
                    raise ValueError(f"4xx client error, status code {resp.status_code}, no retry required")
                if resp.status_code >= 500:
                    raise ConnectionError(f"5xx server error, status code {resp.status_code}")
                resp.raise_for_status()
                res_json = resp.json()

                # Business status code validation
                if not res_json.get("success") or res_json.get("code") != 200:
                    raise Exception(f"Business logic failure: {res_json.get('message')}")

                # Parse flattened sensor data
                records = res_json.get("data", {}).get("records", [])
                page_rows = []
                for device in records:
                    dev_id = device.get("deviceId", "")
                    dev_code = device.get("deviceCode", "")
                    dev_name = device.get("deviceName", "")
                    org_id = device.get("orgId", "")
                    bus_type = device.get("businessType", "")
                    group_id = device.get("groupId", "")
                    sensor_arr = device.get("sensors", [])
                    for sensor in sensor_arr:
                        row = [
                            dev_id, dev_code, dev_name, org_id, bus_type,
                            group_id, sensor.get("sensorId", ""),
                            sensor.get("sensorCode", ""),
                            sensor.get("sensorName", ""),
                            sensor.get("unit", "").strip()
                        ]
                        page_rows.append(row)
                data_queue.put(page_rows)
                print_log(f"Page {page_no} request succeeded, parsed detail rows: {len(page_rows)}")
                task_success = True
                # Post-request throttling sleep to control API QPS
                time.sleep(REQUEST_INTERVAL)

        except ValueError as client_err:
            # 4xx errors, permanent failure, no retry
            err_info = str(client_err)
            print_log(f"Page {page_no} non-retriable exception: {err_info}", level="ERROR")
            fail_page_list.append(page_no)
            break
        except (requests.exceptions.RequestException, ConnectionError) as net_err:
            # Network / 5xx errors, perform exponential backoff retry
            retry_count += 1
            err_info = str(net_err)
            if retry_count > MAX_RETRY_TIMES:
                print_log(f"Page {page_no} failed all {MAX_RETRY_TIMES} retries: {err_info}", level="ERROR")
                fail_page_list.append(page_no)
                break
            sleep_sec = RETRY_BACKOFF_BASE * (2 ** (retry_count - 1)) + random.random()
            print_log(f"Page {page_no} request failed, {retry_count}th retry, wait {round(sleep_sec,1)}s | {err_info}", level="WARN")
            time.sleep(sleep_sec)
        except Exception as other_err:
            # Unknown business exception, mark as failed directly
            print_log(f"Page {page_no} terminated due to unknown exception: {str(other_err)}", level="ERROR")
            fail_page_list.append(page_no)
            break


def merge_all_queue_data() -> pd.DataFrame:
    """Aggregate all queue data and build DataFrame (independent data processing logic)"""
    all_data = []
    while not data_queue.empty():
        page_data = data_queue.get()
        all_data.extend(page_data)
    df_cols = [
        "device_id", "device_code", "device_name", "org_id", "business_type",
        "group_id", "sensor_id", "sensor_code", "sensor_name", "unit"
    ]
    sync_df = pd.DataFrame(all_data, columns=df_cols)
    print_log(f"Data aggregation completed, total pending rows to insert: {len(all_data)}")
    return sync_df


def write_to_gaussdb(df: pd.DataFrame) -> None:
    """Bulk DataFrame database write logic, decoupled separately"""
    if df.empty:
        print_log("No valid data, skip database insertion")
        return
    request_json.save_to_gaussdb(
        df,
        config.GAUSSDB_DWS,
        TARGET_TABLE,
        CONSTRAINT_KEYS
    )
    print_log(f"Data insertion finished, target table: {TARGET_TABLE}, written rows: {len(df)}")


def batch_submit_thread_tasks(executor: ThreadPoolExecutor, page_list: list[int]) -> None:
    """Submit pagination tasks in batches to smooth traffic, avoid massive Futures creation at once"""
    total_page = len(page_list)
    for start_idx in range(0, total_page, BATCH_SUBMIT_SIZE):
        batch_pages = page_list[start_idx: start_idx + BATCH_SUBMIT_SIZE]
        print_log(f"Submit page batch: {batch_pages[0]} ~ {batch_pages[-1]}, batch size {len(batch_pages)}")
        futures = [executor.submit(fetch_single_page, page) for page in batch_pages]
        # Wait for current batch to complete before submitting next batch
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as task_err:
                print_log(f"Internal thread task exception: {str(task_err)}", level="ERROR")

# ======================== Main Entry Function ========================
def sync_permission_sensor_data():
    total_start_ts = time.time()
    init_cost = 0.0
    api_cost = 0.0
    data_proc_cost = 0.0
    db_write_cost = 0.0

    try:
        # 1. Initialization phase: query total page count
        init_start_ts = time.time()
        total_pages = get_total_page_count()
        init_cost = round(time.time() - init_start_ts, 2)

        print("==================== Synchronization Task Started [API Rate Limit Protection Mode] ====================")
        print_log(f"Max thread pool size: {MAX_WORKERS}, max instantaneous concurrent requests: {SEMAPHORE_LIMIT}")
        print_log(f"Single request throttling interval: {REQUEST_INTERVAL}s, max retry times: {MAX_RETRY_TIMES}")
        print_log(f"Target database table: {TARGET_TABLE}")
        print("=======================================================================")

        # 2. Multi-thread batch pull API data
        api_start_ts = time.time()
        all_page_nums = list(range(1, total_pages + 1))
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            batch_submit_thread_tasks(pool, all_page_nums)
        api_cost = round(time.time() - api_start_ts, 2)

        # Print summary of failed pages for manual retry
        if fail_page_list:
            print_log(f"Synchronization finished, {len(fail_page_list)} failed pages exist for manual retry: {sorted(fail_page_list)}", level="WARN")
        else:
            print_log("All page requests succeeded, no failed pages")

        # 3. Data processing phase: aggregate queue & build DataFrame
        data_start_ts = time.time()
        sync_df = merge_all_queue_data()
        data_proc_cost = round(time.time() - data_start_ts, 2)

        # 4. Database insertion phase
        db_start_ts = time.time()
        write_to_gaussdb(sync_df)
        db_write_cost = round(time.time() - db_start_ts, 2)

        # Normal exit: print standard segmented execution time
        total_all_cost = round(time.time() - total_start_ts, 2)
        print("\n==================== Segmented Execution Time Summary ====================")
        print(f"Initialization time: {init_cost} s")
        print(f"Batch API pull time: {api_cost} s")
        print(f"Data processing time: {data_proc_cost} s")
        print(f"Database write time: {db_write_cost} s")
        print(f"Total script execution time: {total_all_cost} s")
        print("========================================================\n")

    except Exception as main_err:
        # Global exception fallback, print consumed time even on abnormal exit
        total_all_cost = round(time.time() - total_start_ts, 2)
        print_log(f"Fatal global exception, task aborted: {str(main_err)}", level="ERROR")
        print("\n==================== Abnormal Exit - Segmented Time ====================")
        print(f"Initialization time: {init_cost} s")
        print(f"Batch API pull time: {api_cost} s")
        print(f"Data processing time: {data_proc_cost} s")
        print(f"Database write time: {db_write_cost} s")
        print(f"Total elapsed script time: {total_all_cost} s")
        print("========================================================\n")


if __name__ == "__main__":
    sync_permission_sensor_data()
```



## ods_cmsdms_extract_device_info_day(调度)

### coss_ods.ods_cmsdms_tmu_device_info_df

#### create table

```sql
drop table if exists coss_ods.ods_cmsdms_tmu_device_info_df;

create table if not exists coss_ods.ods_cmsdms_tmu_device_info_df (
    device_code      varchar(200),
    device_name      varchar(200),
    sensor_id        varchar(200),
    sensor_name      varchar(200),
    sensor_unit      varchar(120),
    ods_update_time  timestamp(6) null default pg_systimestamp(),
    ods_load_time    timestamp(6) null default pg_systimestamp(),
    primary key (device_code)
);
comment on table coss_ods.ods_cmsdms_tmu_device_info_df is 'CMSDMS System Device Information Data';
comment on table coss_ods.ods_cmsdms_tmu_device_info_df is 'Device Info';
comment on column coss_ods.ods_cmsdms_tmu_device_info_df.device_code is 'Device Code';
comment on column coss_ods.ods_cmsdms_tmu_device_info_df.device_name is 'Device Name';
comment on column coss_ods.ods_cmsdms_tmu_device_info_df.sensor_id is 'Sensorid';
comment on column coss_ods.ods_cmsdms_tmu_device_info_df.sensor_name is 'Sensor Name';
comment on column coss_ods.ods_cmsdms_tmu_device_info_df.sensor_unit is 'Sensor Unit';
comment on column coss_ods.ods_cmsdms_tmu_device_info_df.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_cmsdms_tmu_device_info_df.ods_load_time is 'Ods Load Time';
```

#### interface

```python
# -*- coding: utf-8 -*-
"""
Device Information Acquisition and Storage Script
Function: Fetch device information (including sensor details) via API pagination,
          process the data into a DataFrame, and store it in the target database.
Optimized: 100-thread concurrent API requests
"""
import requests
import pandas as pd
import config
import request_json
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue

# ===================== Configuration =====================
API_URL = 'http://10.66.169.102:8330/share/data/devInfo'
HEADERS = {'Content-Type': 'application/json'}
PAGE_SIZE = 2000
MAX_WORKERS = 100  # 固定100线程
TARGET_TABLE = 'coss_ods.ods_cmsdms_tmu_device_info_df'
CONSTRAINT_KEYS = ['device_code']
# =========================================================

# 线程安全队列
result_queue = Queue()

def fetch_single_page(page_num):
    """单页请求 - 线程执行函数"""
    try:
        payload = {
            "page": page_num,
            "pageSize": PAGE_SIZE,
            "deviceCodes": []
        }
        response = requests.post(
            API_URL,
            json=payload,
            headers=HEADERS,
            timeout=120
        )
        response.raise_for_status()
        data = response.json()
        records = data.get("data", {}).get("records", [])

        page_records = []
        for device in records:
            device_code = device.get('deviceCode')
            device_name = device.get('deviceName')
            for sensor in device.get('sensors', []):
                page_records.append([
                    device_code,
                    device_name,
                    sensor.get('sensorId'),
                    sensor.get('sensorName'),
                    sensor.get('unit')
                ])
        result_queue.put(page_records)
        print(f"Page finished: {page_num}")

    except Exception as e:
        print(f"Page failed: {page_num}, error: {str(e)}")

def fetch_and_save_device_info():
    """多线程并发获取设备信息并入库"""
    try:
        # 1. 获取总页数
        initial_payload = {
            "page": 1,
            "pageSize": PAGE_SIZE,
            "deviceCodes": []
        }
        resp = requests.post(API_URL, json=initial_payload, headers=HEADERS, timeout=120)
        resp.raise_for_status()
        total_pages = resp.json()["data"]["totalPage"]
        print(f"Total pages to process: {total_pages}")

        # 2. 100线程并发请求所有页
        print(f"Start concurrent with {MAX_WORKERS} threads...")
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(fetch_single_page, p) for p in range(1, total_pages + 1)]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception:
                    pass

        # 3. 汇总所有数据
        all_records = []
        while not result_queue.empty():
            all_records.extend(result_queue.get())

        print(f"Total valid records obtained: {len(all_records)}")

        # 4. 构建DataFrame
        full_df = pd.DataFrame(
            all_records,
            columns=['device_code', 'device_name', 'sensor_id', 'sensor_name', 'sensor_unit']
        )

        # 5. 保存数据库
        if not full_df.empty:
            print(full_df.head())
            request_json.save_to_gaussdb(
                full_df,
                config.GAUSSDB_DWS,
                TARGET_TABLE,
                CONSTRAINT_KEYS
            )
            print(f"Successfully saved {len(full_df)} records to {TARGET_TABLE}")
        else:
            print("No data to save (DataFrame is empty)")

    except Exception as e:
        print(f"Fatal error during data processing: {str(e)}")

if __name__ == "__main__":
    fetch_and_save_device_info()


```

### ods_cmsdms_tmu_sensor_realtime_minf

#### create table

```sql
drop table if exists coss_ods.ods_cmsdms_tmu_sensor_realtime_minf;

create table if not exists coss_ods.ods_cmsdms_tmu_sensor_realtime_minf (
    sns_code         varchar(100) ,
    value            decimal(20,6),
    time             bigint,
    ods_update_time  timestamp(6) null default current_timestamp,
    ods_load_time    timestamp(6) null default current_timestamp,
    primary key (sns_code)
);

comment on table coss_ods.ods_cmsdms_tmu_sensor_realtime_minf is 'CMSDMS Sensor Realtime Information';
comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.sns_code is 'Sensor Code';
comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.value is 'Value';
comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.time is 'Time';
comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.ods_load_time is 'Ods Load Time';
```

#### interface

```python
# -*- coding: utf-8 -*-
# File : ods_cmsdms_tmu_sensor_realtime_minf.py
# Author : CDM
# Date : 2026/07/09 16:59

# -*- coding: utf-8 -*-
"""
CMSDMS sensor real-time minute data acquisition and storage script
Function: Query unique sensor codes from permission table, call realtime api, write data to GaussDB minute table
"""
import time
import random
import requests
import pandas as pd
from queue import Queue
from threading import Semaphore
from concurrent.futures import ThreadPoolExecutor, as_completed
import config
import gaussdb
import request_json

# ===================== CONFIG CONSTANTS (All Hardcode Here) =====================
# API Basic Info
API_URL = "http://10.66.110.106:8325/share/data/sensor/realtime"
HEADERS = {
    "Content-Type": "application/json",
    "appId": "123456",
    "request-timeout-mark": "sensor-realtime-min-task"
}
# Timeout Split: Connect / Read
CONNECT_TIMEOUT = 8
READ_TIMEOUT = 20
REQUEST_TIMEOUT_TUPLE = (CONNECT_TIMEOUT, READ_TIMEOUT)

# API Flow Control
MAX_API_SEMAPHORE = 10          # Semaphore to control maximum concurrent requests
API_RETRY_TIMES = 3             # Retry attempts for 5xx/network exceptions
RETRY_BASE_SLEEP = 1            # Base seconds for exponential backoff
AFTER_REQ_SLEEP = 0.1           # Mandatory throttling sleep after each request
API_SENSOR_BATCH = 1000         # Number of sensors carried in a single API request
FUTURE_SUBMIT_BATCH_SIZE = 20   # Submit thread tasks in batches to smooth traffic

# Database Config
SOURCE_TABLE = "coss_ods.ods_cmsdms_tmu_permission_info_df"
TARGET_TABLE = "coss_ods.ods_cmsdms_tmu_sensor_realtime_minf"
CONSTRAINT_KEYS = ["sns_code", "time"]  # Fix: Composite primary key
DB_PAGE_BATCH_SIZE = 1000

# Queue Control
QUEUE_MAX_SIZE = 5000           # Queue capacity limit to avoid memory overflow

# Thread Global Vars
api_semaphore = Semaphore(MAX_API_SEMAPHORE)
result_queue = Queue(maxsize=QUEUE_MAX_SIZE)
failed_api_batches = []         # Store failed batches for unified output after execution

# ===================== Private Core Function =====================
def print_log(msg: str, level: str = "INFO") -> None:
    """Unified hierarchical log printing, remove redundant output"""
    level_map = {
        "INFO": "[INFO]",
        "WARN": "[WARN]",
        "ERROR": "[ERROR]"
    }
    prefix = level_map.get(level, "[INFO]")
    print(f"{prefix} {msg}")

def fetch_single_api_batch(sensor_code_batch: list[str]) -> None:
    """
    Single batch sensor API request: rate limiting, retry, exception classification, enqueue data
    Args:
        sensor_code_batch: List of sensor codes
    """
    retry_count = 0
    payload = {"sensorCodes": sensor_code_batch}
    success_flag = False

    while retry_count <= API_RETRY_TIMES and not success_flag:
        try:
            with api_semaphore:
                resp = requests.post(
                    url=API_URL,
                    json=payload,
                    headers=HEADERS,
                    timeout=REQUEST_TIMEOUT_TUPLE
                )
                # Classify HTTP status codes
                if 400 <= resp.status_code < 500:
                    raise ValueError(f"4xx Client Error, Code:{resp.status_code}, No Retry")
                if resp.status_code >= 500:
                    raise ConnectionError(f"5xx Server Error, Code:{resp.status_code}")
                resp.raise_for_status()

                res_json = resp.json()
                # Business status code validation
                if not res_json.get("success") or res_json.get("code") != 200:
                    raise Exception(f"Business Fail: {res_json.get('message')}")

                # Data parsing
                data_list = res_json.get("data", [])
                parse_rows = []
                for item in data_list:
                    parse_rows.append([
                        item.get("snsCode"),
                        item.get("value"),
                        item.get("time")
                    ])
                result_queue.put(parse_rows)
                print_log(f"Batch success, sensor count:{len(sensor_code_batch)}, data rows:{len(parse_rows)}")
                success_flag = True
                time.sleep(AFTER_REQ_SLEEP)

        except ValueError as client_err:
            # 4xx error, abort directly and record failed batch
            err_msg = str(client_err)
            print_log(f"Batch skip, sensor list:{sensor_code_batch[:5]}..., err:{err_msg}", level="ERROR")
            failed_api_batches.append(sensor_code_batch)
            break
        except (requests.exceptions.RequestException, ConnectionError) as net_err:
            # Retry logic for network/5xx errors
            retry_count += 1
            err_msg = str(net_err)
            if retry_count > API_RETRY_TIMES:
                print_log(f"Batch all retry failed, sensor list:{sensor_code_batch[:5]}..., err:{err_msg}", level="ERROR")
                failed_api_batches.append(sensor_code_batch)
                break
            backoff_sleep = RETRY_BASE_SLEEP * (2 ** (retry_count - 1)) + random.random()
            print_log(f"Request fail, retry {retry_count}/{API_RETRY_TIMES}, wait {round(backoff_sleep,1)}s, err:{err_msg}", level="WARN")
            time.sleep(backoff_sleep)
        except Exception as other_err:
            # Unknown business exception, no retry
            print_log(f"Unknown error, batch drop, err:{str(other_err)}", level="ERROR")
            failed_api_batches.append(sensor_code_batch)
            break

def get_all_sensor_codes(db_conn) -> list[str]:
    """Paginate to query all distinct sensor codes, decoupled independent function"""
    # Step1 total count
    count_sql = f"SELECT COUNT(DISTINCT sensor_code) FROM {SOURCE_TABLE}"
    total_sensor = db_conn.fetch_data(count_sql)[0][0]
    print_log(f"Total distinct sensor codes in source table: {total_sensor}")

    all_codes = []
    offset = 0
    while offset < total_sensor:
        page_sql = f"""
            SELECT DISTINCT sensor_code
            FROM {SOURCE_TABLE}
            ORDER BY sensor_code
            LIMIT {DB_PAGE_BATCH_SIZE} OFFSET {offset}
        """
        offset += DB_PAGE_BATCH_SIZE
        page_res = db_conn.fetch_data(page_sql)
        page_codes = [row[0] for row in page_res if row[0]]
        all_codes.extend(page_codes)
    print_log(f"All sensor codes loaded, valid count: {len(all_codes)}")
    return all_codes

def batch_submit_task(executor: ThreadPoolExecutor, batch_list: list[list[str]]) -> None:
    """Submit thread tasks in batches to smooth traffic, avoid creating massive futures at once"""
    task_futures = []
    for idx, api_batch in enumerate(batch_list):
        task_futures.append(executor.submit(fetch_single_api_batch, api_batch))
        # Batch wait to release thread pressure
        if len(task_futures) >= FUTURE_SUBMIT_BATCH_SIZE:
            for future in as_completed(task_futures):
                try:
                    future.result()
                except Exception as e:
                    print_log(f"Thread task exception: {str(e)}", level="ERROR")
            task_futures.clear()
    # Process remaining unfinished tasks
    for future in as_completed(task_futures):
        try:
            future.result()
        except Exception as e:
            print_log(f"Thread task exception: {str(e)}", level="ERROR")

def merge_queue_data() -> list:
    """Aggregate all parsed data from queue, independent decoupled logic"""
    all_rows = []
    while not result_queue.empty():
        all_rows.extend(result_queue.get())
    print_log(f"All api task finished, total valid data rows: {len(all_rows)}")
    return all_rows

def write_data_to_db(data_rows: list) -> None:
    """Separated database writing logic for decoupling"""
    if not data_rows:
        print_log("No data to write into database")
        return
    df = pd.DataFrame(data_rows, columns=["sns_code", "value", "time"])
    request_json.save_to_gaussdb(
        df,
        config.GAUSSDB_DWS,
        TARGET_TABLE,
        CONSTRAINT_KEYS
    )
    print_log(f"Data write success, target table: {TARGET_TABLE}, row count: {len(data_rows)}")

# ===================== Main Entry =====================
def fetch_and_save_realtime_data():
    total_start = time.time()
    init_cost = 0.0
    api_cost = 0.0
    data_proc_cost = 0.0
    db_write_cost = 0.0
    db_conn = None

    # 1. Init DB & Load sensor codes
    init_start = time.time()
    try:
        db_conn = gaussdb.GaussDB(**config.GAUSSDB_DWS)
        print_log("Database connection established")
    except Exception as e:
        print_log(f"Database connect failed: {str(e)}", level="ERROR")
        return

    try:
        sensor_code_list = get_all_sensor_codes(db_conn)
        # Split sensor into api request batch
        api_batch_total = []
        for i in range(0, len(sensor_code_list), API_SENSOR_BATCH):
            api_batch_total.append(sensor_code_list[i:i + API_SENSOR_BATCH])
        print_log(f"Split sensor list into {len(api_batch_total)} api request batches")
        init_cost = round(time.time() - init_start, 2)

        # 2. Concurrent API Request
        api_start = time.time()
        print_log(f"Start concurrent api request, max semaphore limit: {MAX_API_SEMAPHORE}")
        with ThreadPoolExecutor(max_workers=MAX_API_SEMAPHORE) as pool_executor:
            batch_submit_task(pool_executor, api_batch_total)
        api_cost = round(time.time() - api_start, 2)

        # Print failed batch summary
        if failed_api_batches:
            print_log(f"Task finished, total failed api batches: {len(failed_api_batches)}", level="WARN")
            print_log(f"Failed batch sample (first 3): {failed_api_batches[:3]}", level="WARN")
        else:
            print_log("All api batches request success, no failed task")

        # 3. Merge queue data
        data_proc_start = time.time()
        all_data = merge_queue_data()
        data_proc_cost = round(time.time() - data_proc_start, 2)

        # 4. Write to GaussDB
        db_write_start = time.time()
        write_data_to_db(all_data)
        db_write_cost = round(time.time() - db_write_start, 2)

    except Exception as main_err:
        print_log(f"Main process fatal error: {str(main_err)}", level="ERROR")
    finally:
        if db_conn:
            try:
                db_conn.close()
                print_log("Database connection closed normally")
            except Exception:
                pass

    # Print time cost summary
    total_cost = round(time.time() - total_start, 2)
    print("\n==================== Segmented Execution Time Summary ====================")
    print(f"Initialization time: {init_cost} s")
    print(f"Batch API pulling time: {api_cost} s")
    print(f"Data processing time: {data_proc_cost} s")
    print(f"Database write time: {db_write_cost} s")
    print(f"Total full script execution time: {total_cost} s")
    print("========================================================\n")

if __name__ == "__main__":
    fetch_and_save_realtime_data()
```



## ods_cmsdms_extract_sensor_realtime_min(调度)

### ods_cmsdms_tmu_realtime_sensor_mini

#### create table

```sql
drop table if exists coss_ods.ods_cmsdms_tmu_realtime_sensor_mini;
create table if not exists coss_ods.ods_cmsdms_tmu_realtime_sensor_mini
(
    code    varchar(64) not null,
    "time"  timestamp(6) not null,
    status  int4,
    value   float8,
    name    varchar(128),
    unit    varchar(32),
    ods_load_time timestamp(6) default current_timestamp,
    ods_update_time timestamp(6) default current_timestamp,
    primary key (code, "time")
);
comment on table coss_ods.ods_cmsdms_tmu_realtime_sensor_mini is 'CMSDMS System Realtime Sensor Data';
-- Column Comments
comment on column coss_ods.ods_cmsdms_tmu_realtime_sensor_mini.code is 'Sensor Code';
comment on column coss_ods.ods_cmsdms_tmu_realtime_sensor_mini."time" is 'Sensor Date Time';
comment on column coss_ods.ods_cmsdms_tmu_realtime_sensor_mini.status is 'Sensor Status';
comment on column coss_ods.ods_cmsdms_tmu_realtime_sensor_mini.value is 'Sensor Value';
comment on column coss_ods.ods_cmsdms_tmu_realtime_sensor_mini.name is 'Sensor Name';
comment on column coss_ods.ods_cmsdms_tmu_realtime_sensor_mini.unit is 'Measurement Unit';
comment on column coss_ods.ods_cmsdms_tmu_realtime_sensor_mini.ods_load_time is 'Load Time';
comment on column coss_ods.ods_cmsdms_tmu_realtime_sensor_mini.ods_update_time is 'Update Time';
```

#### interface

```shell
#!/bin/bash

# ==============================
# Function: Execute TMU realtime sensor mini Python script
# Log Path: /opt/app/coss/iot/log/ods_cmsdms_tmu_realtime_sensor_mini/
# ==============================

# Record start time
START_TIME=$(date +%s)

# Log directory
LOG_DIR="/opt/app/coss/iot/log/ods_cmsdms_tmu_realtime_sensor_mini"
mkdir -p ${LOG_DIR}

# Current date for log file name
LOG_DATE=$(date +%Y%m%d)
LOG_FILE="${LOG_DIR}/ods_cmsdms_tmu_realtime_sensor_mini_${LOG_DATE}.log"

# Python script path
SCRIPT_PATH="/opt/app/coss/iot/script/ods_cmsdms_tmu_realtime_sensor_mini.py"

echo "===== Start realtime sensor mini script execution =====" | tee -a ${LOG_FILE}

# Execute Python script
python3 ${SCRIPT_PATH} | tee -a ${LOG_FILE}

echo "===== Realtime sensor mini script execution completed =====" | tee -a ${LOG_FILE}

# Calculate total execution time
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))
HOURS=$((DURATION / 3600))
MINUTES=$(((DURATION % 3600) / 60))
SECONDS=$((DURATION % 60))

# Print total execution time
echo "============================================================"
echo "Total Script Execution Time: ${HOURS}h ${MINUTES}m ${SECONDS}s"
echo "============================================================"
```

# dwd

## dwd_tmu_etl_device_realtime_min（调度）

### coss_dwd.dwd_tmu_more_dev_realtime_minf

#### create table

```sql
drop table if exists coss_dwd.dwd_tmu_more_dev_realtime_minf;

create table if not exists coss_dwd.dwd_tmu_more_dev_realtime_minf (
    device_code      varchar(200),
    sensor_id        varchar(200),
    sensor_value     decimal(20,5),
    sensor_time      timestamp(6),
    dwd_update_time  timestamp(6) null default current_timestamp,
    dwd_load_time    timestamp(6) null default current_timestamp,
    primary key (device_code)
);

comment on table coss_dwd.dwd_tmu_more_dev_realtime_minf is 'Meter Read Realtime Data';
comment on column coss_dwd.dwd_tmu_more_dev_realtime_minf.device_code is 'Device Code';
comment on column coss_dwd.dwd_tmu_more_dev_realtime_minf.sensor_id is 'Sensor Id';
comment on column coss_dwd.dwd_tmu_more_dev_realtime_minf.sensor_value is 'Sensor Value';
comment on column coss_dwd.dwd_tmu_more_dev_realtime_minf.sensor_time is 'Sensor Time';
comment on column coss_dwd.dwd_tmu_more_dev_realtime_minf.dwd_update_time is 'Dwd Update Time';
comment on column coss_dwd.dwd_tmu_more_dev_realtime_minf.dwd_load_time is 'Dwd Load Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function Describe: Terminal User Monitoring For Meter
-- Create         By: dongmaochen
-- Create       Date: 2025-11-13
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf
-- Target Table:  coss_dwd.dwd_tmu_more_dev_realtime_minf
-- ****************************************************************************************
insert into coss_dwd.dwd_tmu_more_dev_realtime_minf (
    device_code,
    sensor_id,
    sensor_value,
    sensor_time,
    dwd_update_time,
    dwd_load_time
)
select
    device_code as device_code,
    sensor_id as sensor_id,
    value as sensor_value,
    to_timestamp("time" / 1000) as sensor_time,
    current_timestamp as dwd_update_time,
    current_timestamp as dwd_load_time
from coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf
on duplicate key update
    sensor_id = values(sensor_id),
    sensor_value = values(sensor_value),
    sensor_time = values(sensor_time),
    dwd_update_time = values(dwd_update_time);
```

## dwd_tmu_etl_sensor_realtime_min(调度)

### dwd_tmu_sensor_data_mini_month

#### create table

```sql
drop table if exists coss_dwd.dwd_tmu_sensor_data_mini_month;

create table if not exists coss_dwd.dwd_tmu_sensor_data_mini_month (
    sensor_code     varchar(100),
    sensor_value    decimal(20,6),
    sensor_time     timestamp(6),
    dwd_update_time timestamp(6) default current_timestamp,
    dwd_load_time   timestamp(6) default current_timestamp,
    primary key (sensor_code, sensor_time)
)
partition by range (sensor_time) (
    -- 2025 monthly partitions
    partition mh_202501 values less than ('2025-02-01 00:00:00'),
    partition mh_202503 values less than ('2025-04-01 00:00:00'),
    partition mh_202505 values less than ('2025-06-01 00:00:00'),
    partition mh_202507 values less than ('2025-08-01 00:00:00'),
    partition mh_202509 values less than ('2025-10-01 00:00:00'),
    partition mh_202511 values less than ('2025-12-01 00:00:00'),

    -- 2026 monthly partitions
    partition mh_202601 values less than ('2026-02-01 00:00:00'),
    partition mh_202603 values less than ('2026-04-01 00:00:00'),
    partition mh_202605 values less than ('2026-06-01 00:00:00'),
    partition mh_202607 values less than ('2026-08-01 00:00:00'),
    partition mh_202609 values less than ('2026-10-01 00:00:00'),
    partition mh_202611 values less than ('2026-12-01 00:00:00'),

    -- 2027 monthly partitions
    partition mh_202701 values less than ('2027-02-01 00:00:00'),
    partition mh_202703 values less than ('2027-04-01 00:00:00'),
    partition mh_202705 values less than ('2027-06-01 00:00:00'),
    partition mh_202707 values less than ('2027-08-01 00:00:00'),
    partition mh_202709 values less than ('2027-10-01 00:00:00'),
    partition mh_202711 values less than ('2027-12-01 00:00:00'),

    -- 2028 monthly partitions
    partition mh_202801 values less than ('2028-02-01 00:00:00'),
    partition mh_202803 values less than ('2028-04-01 00:00:00'),
    partition mh_202805 values less than ('2028-06-01 00:00:00'),
    partition mh_202807 values less than ('2028-08-01 00:00:00'),
    partition mh_202809 values less than ('2028-10-01 00:00:00'),

    -- Future partition, avoid insertion failure for unexpected time data
    partition mh_future values less than ('9999-01-01 00:00:00')
);

-- Add table comment
comment on table coss_dwd.dwd_tmu_sensor_data_mini_month is 'Water Quality Realtime Data';

-- Add column comments
comment on column coss_dwd.dwd_tmu_sensor_data_mini_month.sensor_code is 'Sensor Code';
comment on column coss_dwd.dwd_tmu_sensor_data_mini_month.sensor_value is 'Sensor Value';
comment on column coss_dwd.dwd_tmu_sensor_data_mini_month.sensor_time is 'Sensor Time';
comment on column coss_dwd.dwd_tmu_sensor_data_mini_month.dwd_update_time is 'Data Update Time';
comment on column coss_dwd.dwd_tmu_sensor_data_mini_month.dwd_load_time is 'Data Loading Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function Describe: Terminal User Monitoring For Sensor Data
-- Create         By: dongmaochen
-- Create       Date: 2026-05-21
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table: coss_ods.ods_cmsdms_tmu_realtime_sensor_mini
-- Target Table: coss_dwd.dwd_tmu_sensor_data_mini_month
-- ****************************************************************************************
insert into coss_dwd.dwd_tmu_sensor_data_mini_month
select 
    code sensor_code,
    case when abs(value) < power(10,14) then value else null end sensor_value,
    time sensor_time,
    current_timestamp dwd_update_time,
    current_timestamp dwd_load_time
from coss_ods.ods_cmsdms_tmu_realtime_sensor_mini
    where ods_update_time >= '${dwd_update_time}'
on duplicate key update nothing;
```

# dim

## dim_tmu_iot_device_info

### create table

```sql
drop table if exists coss_dim.dim_tmu_iot_device_info;

create table if not exists coss_dim.dim_tmu_iot_device_info (
    device_code      varchar(200),
    device_name      varchar(200),
    meter_type_code  varchar(20),
    meter_type_desc  varchar(100),
    premise_id       varchar(110),
    serial_no        varchar(16),
    rcv_date         timestamp(6),
    region_abbr      varchar(30),
    sensor_id        varchar(200),
    sensor_name      varchar(200),
    sensor_unit      varchar(120),
    dim_update_time  timestamp(6) null default current_timestamp,
    dim_load_time    timestamp(6) null default current_timestamp,
    primary key (device_code)
);

comment on table coss_dim.dim_tmu_iot_device_info is 'Device Information';
comment on column coss_dim.dim_tmu_iot_device_info.device_code      is 'Device Code';
comment on column coss_dim.dim_tmu_iot_device_info.device_name      is 'Device Name';
comment on column coss_dim.dim_tmu_iot_device_info.meter_type_code  is 'Meter Type Code';
comment on column coss_dim.dim_tmu_iot_device_info.meter_type_desc  is 'Meter Type Desc ';
comment on column coss_dim.dim_tmu_iot_device_info.premise_id       is 'Premise Id';
comment on column coss_dim.dim_tmu_iot_device_info.serial_no        is 'Serial No ';
comment on column coss_dim.dim_tmu_iot_device_info.rcv_date         is 'Receive Date';
comment on column coss_dim.dim_tmu_iot_device_info.region_abbr      is 'Region Abbr';
comment on column coss_dim.dim_tmu_iot_device_info.sensor_id        is 'Sensorid';
comment on column coss_dim.dim_tmu_iot_device_info.sensor_name      is 'Sensor Name';
comment on column coss_dim.dim_tmu_iot_device_info.sensor_unit      is 'Sensor Unit';
comment on column coss_dim.dim_tmu_iot_device_info.dim_update_time  is 'Dim Update Time';
comment on column coss_dim.dim_tmu_iot_device_info.dim_load_time    is 'Dim Load Time';
```

### select sql

```sql
drop table if exists coss_tmp.dim_tmu_iot_device_info_tmp_04;
create table  coss_tmp.dim_tmu_iot_device_info_tmp_04 as
with t_a as 
(select
   t."METER_NO"             as device_code
   ,t."METER_TYPE_CODE"     as meter_type_code
   ,t1."METER_TYPE_DESC"    as meter_type_dcsc
   ,t2."PREMISE_ID"         as premise_id
   ,t."SERIAL_NO"           as serial_no
   ,t."RCV_DATE"            as rcv_date
from wcdms."METER" t
inner join wcdms."CFG_METER_TYPE" t1 on t."METER_TYPE_CODE" = t1."METER_TYPE_CODE"
inner join coss_tmp.dim_tmu_iot_device_info_tmp_01 t2 on t."METER_NO" = t2."METER_NO")
select 
    t1.device_code,
    t1.device_name,
    t.meter_type_code,
    t.meter_type_desc,
    t.premise_id,
    t.serial_no,
    t.rcv_date,
    CASE
        WHEN t1.device_code % 10 >= 0 AND t1.device_code % 10 <= 1 THEN 'HKI'
        WHEN t1.device_code % 10 >= 2 AND t1.device_code % 10 <= 3 THEN 'K'
        WHEN t1.device_code % 10 >= 4 AND t1.device_code % 10 <= 6 THEN 'NTW'
        WHEN t1.device_code % 10 >= 7 AND t1.device_code % 10 <= 9 THEN 'HKI'
    END AS region_abbr,
    t1.sensor_id,
    t1.sensor_name,
    t1.sensor_unit,
    current_timestamp dim_update_time,
    current_timestamp dim_load_time
from t_a t 
inner join coss_tmp.dim_tmu_iot_device_info_tmp_03 t1 on t.device_code = t1.device_code
```

## dim_sz_device_info

### create table

```sql
drop table if exists coss_dim.dim_sz_device_info;
create table if not exists coss_dim.dim_sz_device_info(
    supply_id        varchar(100),
    supply_code      varchar(100),
    device_code      varchar(100),
    device_name      varchar(100),
    sensor_code      varchar(100),
    sensor_name      varchar(100),
    unit             varchar(100),
    coordinate_x     decimal(20,6),
    coordinate_y     decimal(20,6),
    dim_update_time  timestamp(6) default current_timestamp,
    dim_load_time    timestamp(6) default current_timestamp,
    primary key(supply_id, device_code, sensor_code)
);
comment on table coss_dim.dim_sz_device_info                   is 'Supply  Zone Monitoring Device Information';
comment on column coss_dim.dim_sz_device_info.supply_id        is 'Supply ID';
comment on column coss_dim.dim_sz_device_info.supply_code      is 'Supply Code';
comment on column coss_dim.dim_sz_device_info.device_code      is 'Device Code';
comment on column coss_dim.dim_sz_device_info.device_name      is 'Device Name';
comment on column coss_dim.dim_sz_device_info.sensor_code      is 'Sensor Code';
comment on column coss_dim.dim_sz_device_info.sensor_name      is 'Sensor Name';
comment on column coss_dim.dim_sz_device_info.unit             is 'Unit';
comment on column coss_dim.dim_sz_device_info.coordinate_x     is 'X-Axis Coordinate';
comment on column coss_dim.dim_sz_device_info.coordinate_y     is 'Y-Axis Coordinate';
comment on column coss_dim.dim_sz_device_info.dim_update_time  is 'Update Time';
comment on column coss_dim.dim_sz_device_info.dim_load_time    is 'Load Time';
```

### select sql

```sql
-- 1.在源系统导出数据
select 
	0 supply_id,
	0 supply_code,
	t.code device_code,
	t.name device_name,
	t1.code sensor_code,
	t1.name sensor_name,
	t1."unit",
	string_to_array(gps_position, ',')[1]  coordinate_x,
	string_to_array(gps_position, ',')[2] coordinate_y,
	current_timestamp dim_update_time,
	current_timestamp dim_load_time
from 
(
	select 
	id,
	code,
	name,
	gps_position
	from iot.device where "type" ='gw111'
) t 
inner join (
	select
	device, 
	code, 
	"name" ,
	"unit"  
	from sensor where name in(
    'pH',
    'Temperature',
    'FCL',
    'Conductivity',
    'Turbidity'
	)
) t1 on t.id = t1.device

-- 2.把导出来的数据用豆包转换coordinate_x和coordinate_y的经纬度数

-- 3.转换sensor_name和unit的代码值
select 
	supply_id,
	supply_code,
	device_code,
	device_name,
	sensor_code,
    CASE
        WHEN sensor_name = 'Turbidity' THEN 'TURBITIDY'
        WHEN sensor_name = 'Conductivity' THEN 'COND'
        WHEN sensor_name = 'FCL' THEN 'CHLORINE'
        WHEN sensor_name = 'pH' THEN 'PH'
        WHEN sensor_name = 'Temperature' THEN 'TEMP'
        ELSE sensor_name  -- 其他值保持不变
    END AS sensor_name,
	CASE
	    WHEN unit = 'NTU' THEN 'NTU'
	    WHEN unit = 'V4'  THEN 'uS/cm'
	    WHEN unit = 'CL'  THEN 'mg/L'
	    WHEN unit = 'PH'  THEN ''   -- 你写的目标为空
	    WHEN unit = 'C'   THEN 'C'
    ELSE unit  -- 其他不变
	END AS unit,
	coordinate_x,
	coordinate_y,
	dim_update_time,
	dim_load_time
from coss_dim.dim_sz_device_info
```



# dm

## dm_tmu_etl_water_quality_realtime_min（调度）

### dm_tmu_sensor_data_mini_month

#### create table

```sql
drop table if exists coss_dm.dm_tmu_sensor_data_mini_month;

create table if not exists coss_dm.dm_tmu_sensor_data_mini_month (
    id              varchar(100),
    sensor_code     varchar(100),
    sensor_value    decimal(20,6),
    sensor_time     timestamp(6),
    dm_update_time  timestamp(6) default current_timestamp,
    dm_load_time    timestamp(6) default current_timestamp,
    primary key (sensor_code, sensor_time)
)
partition by range (sensor_time) (
    -- 2025 monthly partitions
    partition mh_202501 values less than ('2025-02-01 00:00:00'),
    partition mh_202503 values less than ('2025-04-01 00:00:00'),
    partition mh_202505 values less than ('2025-06-01 00:00:00'),
    partition mh_202507 values less than ('2025-08-01 00:00:00'),
    partition mh_202509 values less than ('2025-10-01 00:00:00'),
    partition mh_202511 values less than ('2025-12-01 00:00:00'),

    -- 2026 monthly partitions
    partition mh_202601 values less than ('2026-02-01 00:00:00'),
    partition mh_202603 values less than ('2026-04-01 00:00:00'),
    partition mh_202605 values less than ('2026-06-01 00:00:00'),
    partition mh_202607 values less than ('2026-08-01 00:00:00'),
    partition mh_202609 values less than ('2026-10-01 00:00:00'),
    partition mh_202611 values less than ('2026-12-01 00:00:00'),

    -- 2027 monthly partitions
    partition mh_202701 values less than ('2027-02-01 00:00:00'),
    partition mh_202703 values less than ('2027-04-01 00:00:00'),
    partition mh_202705 values less than ('2027-06-01 00:00:00'),
    partition mh_202707 values less than ('2027-08-01 00:00:00'),
    partition mh_202709 values less than ('2027-10-01 00:00:00'),
    partition mh_202711 values less than ('2027-12-01 00:00:00'),

    -- 2028 monthly partitions
    partition mh_202801 values less than ('2028-02-01 00:00:00'),
    partition mh_202803 values less than ('2028-04-01 00:00:00'),
    partition mh_202805 values less than ('2028-06-01 00:00:00'),
    partition mh_202807 values less than ('2028-08-01 00:00:00'),
    partition mh_202809 values less than ('2028-10-01 00:00:00'),

    -- Future partition, avoid insertion failure for unexpected time data
    partition mh_future values less than ('9999-01-01 00:00:00')
);

-- Add table comment
comment on table coss_dm.dm_tmu_sensor_data_mini_month is 'Water Quality Realtime Data';

-- Add column comments
comment on column coss_dm.dm_tmu_sensor_data_mini_month.id is 'ID';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.sensor_code is 'Sensor Code';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.sensor_value is 'Sensor Value';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.sensor_time is 'Sensor Time';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.dm_update_time is 'Data Update Time';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.dm_load_time is 'Data Loading Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function Describe: Terminal User Monitoring For Water Quality
-- Create         By: dongmaochen
-- Create       Date: 2026-05-21
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table: coss_dwd.dwd_tmu_sensor_data_mini_month
-- Target Table: coss_dm.dm_tmu_sensor_data_mini_month
-- ****************************************************************************************
insert into coss_dm.dm_tmu_sensor_data_mini_month
select 
    uuid() id,
    sensor_code,
    sensor_value,
    sensor_time,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_tmu_sensor_data_mini_month
    where dwd_update_time >= '${dm_update_time}'
on duplicate key update nothing

```



### dm_tmu_sensor_data_minf

#### create table

```sql
drop table if exists coss_dm.dm_tmu_sensor_data_minf;

create table if not exists coss_dm.dm_tmu_sensor_data_minf (
    id              varchar(100),
    sensor_code     varchar(100),
    sensor_value    decimal(20,6),
    sensor_time     timestamp(6),
    dm_update_time  timestamp(6) default current_timestamp,
    dm_load_time    timestamp(6) default current_timestamp,
    primary key (sensor_code)
);

-- Add table comment
comment on table coss_dm.dm_tmu_sensor_data_minf is 'Water Quality Realtime Data';

-- Add column comments
comment on column coss_dm.dm_tmu_sensor_data_minf.id is 'ID';
comment on column coss_dm.dm_tmu_sensor_data_minf.sensor_code is 'Sensor Code';
comment on column coss_dm.dm_tmu_sensor_data_minf.sensor_value is 'Sensor Value';
comment on column coss_dm.dm_tmu_sensor_data_minf.sensor_time is 'Sensor Time';
comment on column coss_dm.dm_tmu_sensor_data_minf.dm_update_time is 'Data Update Time';
comment on column coss_dm.dm_tmu_sensor_data_minf.dm_load_time is 'Data Loading Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function Describe: Terminal User Monitoring For Water Quality
-- Create         By: dongmaochen
-- Create       Date: 2026-07-07
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table: coss_dwd.dwd_tmu_sensor_data_mini_month
-- Target Table: coss_dm.dm_tmu_sensor_data_minf
-- ****************************************************************************************
insert into coss_dm.dm_tmu_sensor_data_minf 
select 
    uuid() id,
    sensor_code,
    sensor_value,
    sensor_time,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from (
    select 
        sensor_code,
        sensor_value,
        sensor_time,
        row_number() over (partition by sensor_code order by sensor_time desc) as rn
    from coss_dwd.dwd_tmu_sensor_data_mini_month
    where dwd_update_time >= '${dm_update_time}'
) t
where rn = 1
on duplicate key update 
    id = values(id),
    sensor_value = values(sensor_value),
    sensor_time = values(sensor_time),
    dm_update_time = values(dm_update_time),
    dm_load_time = values(dm_load_time)
```

## dm_tmu_etl_device_realtime_min（调度）

### coss_dm.dm_tmu_more_dev_realtime_minf

#### create table

```sql
drop table if exists coss_dm.dm_tmu_more_dev_realtime_minf;

create table if not exists coss_dm.dm_tmu_more_dev_realtime_minf (
    device_code      varchar(200),
    device_name      varchar(200),
    meter_type_code  varchar(20),
    meter_type_desc  varchar(100),
    premise_id       varchar(110),
    serial_no        varchar(16),
    rcv_date         timestamp(6),
    region_abbr      varchar(30),
    sensor_id        varchar(200),
    sensor_name      varchar(200),
    sensor_unit      varchar(120),
    sensor_value     numeric(20, 5),
    sensor_time      timestamp(6),
    dm_update_time   timestamp(6) null default pg_systimestamp(),
    dm_load_time     timestamp(6) null default pg_systimestamp(),
    primary key (device_code)
);

comment on table coss_dm.dm_tmu_more_dev_realtime_minf is 'Meter Read Realtime Data';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.device_code      is 'Device Code';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.device_name      is 'Device Name';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.meter_type_code  is 'Meter Type Code';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.meter_type_desc  is 'Meter Type Desc ';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.premise_id       is 'Premise Id';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.serial_no        is 'Serial No ';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.rcv_date         is 'Receive Date';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.region_abbr      is 'Region Abbr';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.sensor_id        is 'Sensorid';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.sensor_name      is 'Sensor Name';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.sensor_unit      is 'Sensor Unit';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.sensor_value     is 'Sensor Value';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.sensor_time      is 'Sensor Time';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.dm_update_time   is 'Dm Update Time';
comment on column coss_dm.dm_tmu_more_dev_realtime_minf.dm_load_time     is 'Dm Load Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Terminal User
-- function describe: Terminal User Monitoring For Meter
-- create         by: dongmaochen
-- create       date: 2025-11-13
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dim.dim_tmu_iot_device_info
-- coss_dwd.dwd_tmu_more_dev_realtime_minf
-- target table
-- coss_dm.dm_tmu_more_dev_realtime_minf
-- ****************************************************************************************
insert into coss_dm.dm_tmu_more_dev_realtime_minf (
    device_code,
    device_name,
    meter_type_code,
    meter_type_desc,
    premise_id,
    serial_no,
    rcv_date,
    region_abbr,
    sensor_id,
    sensor_name,
    sensor_unit,
    sensor_value,
    sensor_time,
    dm_update_time,
    dm_load_time
)
select
    t1.device_code,
    t1.device_name,
    t1.meter_type_code,
    t1.meter_type_desc,
    t1.premise_id,
    t1.serial_no,
    t1.rcv_date,
    t1.region_abbr,
    t1.sensor_id,
    t1.sensor_name,
    t1.sensor_unit,
    t.sensor_value,
    t.sensor_time,
    localtimestamp as dm_update_time,
    localtimestamp as dm_load_time
from coss_dwd.dwd_tmu_more_dev_realtime_minf t
inner join coss_dim.dim_tmu_iot_device_info t1 
    on t.device_code = t1.device_code 
    and t.sensor_id = t1.sensor_id
on duplicate key update
    sensor_id    = values(sensor_id),
    sensor_name  = values(sensor_name),
    sensor_unit  = values(sensor_unit),
    sensor_value = values(sensor_value),
    sensor_time  = values(sensor_time),
    dm_update_time = values(dm_update_time)
```



# python code 

## 1.ods_cmsdms_tmu_devinfo_minf

```python
# -*- coding: utf-8 -*-
"""
Device Information Acquisition and Storage Script
Function: Fetch device information (including sensor details) via API pagination,
          process the data into a DataFrame, and store it in the target database.
"""
import requests
import pandas as pd
import config
import request_json


def fetch_and_save_device_info():
    """Fetch device information with pagination from API and save to database"""
    # API configuration
    api_url = 'http://10.66.168.69:8330/share/data/devInfo'
    headers = {'Content-Type': 'application/json'}
    page_size = 2000  # Number of records per page

    # Database configuration
    target_table = 'coss_ods.ods_cmsdms_tmu_device_info_minf'
    constraint_keys = ['device_code']

    try:
        # Get total pages by initial request
        initial_payload = {
            "page": 1,
            "pageSize": page_size,
            "deviceCodes": []
        }

        # Send initial request to get pagination info
        response = requests.post(
            api_url,
            json=initial_payload,
            headers=headers,
            timeout=1000  # Add timeout to prevent infinite waiting
        )
        response.raise_for_status()  # Raise exception for HTTP errors
        total_pages = response.json()["data"]["totalPage"]
        print(f"Total pages to process: {total_pages}")

        # Initialize empty DataFrame to store all records
        full_df = pd.DataFrame(
            columns=['device_code', 'device_name', 'sensor_id', 'sensor_name', 'sensor_unit']
        )

        # Iterate through all pages to fetch data
        for page_num in range(1, total_pages + 1):
            # Prepare payload for current page
            payload = {
                "page": page_num,
                "pageSize": page_size,
                "deviceCodes": []
            }

            # Send request for current page
            try:
                page_response = requests.post(
                    api_url,
                    json=payload,
                    headers=headers,
                    timeout=1000
                )
                page_response.raise_for_status()
                page_data = page_response.json()["data"]["records"]
            except Exception as e:
                print(f"Failed to fetch page {page_num}: {str(e)}. Skipping this page.")
                continue

            # Parse records and extract required fields
            page_records = []
            for device in page_data:
                device_code = device['deviceCode']
                device_name = device['deviceName']

                # Process sensor information nested in device records
                for sensor in device['sensors']:
                    page_records.append([
                        device_code,
                        device_name,
                        sensor['sensorId'],
                        sensor['sensorName'],
                        sensor['unit']
                    ])

            # Convert current page records to DataFrame and merge
            page_df = pd.DataFrame(
                page_records,
                columns=['device_code', 'device_name', 'sensor_id', 'sensor_name', 'sensor_unit']
            )
            full_df = pd.concat([full_df, page_df], axis=0, ignore_index=True)
            print(f"Processed page {page_num}/{total_pages}. Cumulative records: {len(full_df)}")

        # Save data to database if not empty
        print(full_df.head())
        if not full_df.empty:
            try:
                request_json.save_to_gaussdb(
                    full_df,
                    config.GAUSSDB_DWS,
                    target_table,
                    constraint_keys
                )
                print(f"Successfully saved {len(full_df)} records to {target_table}")
            except Exception as e:
                print(f"Failed to save data to database: {str(e)}")
        else:
            print("No data to save (DataFrame is empty)")

    except Exception as e:
        print(f"Fatal error during data processing: {str(e)}")


if __name__ == "__main__":
    fetch_and_save_device_info()

```

## 2.ods_cmsdms_tmu_more_dev_realtime_minf

```python
# -*- coding: utf-8 -*-
"""
Multi-device real-time data acquisition and storage script
Function: Retrieve device list from database, batch call API to get real-time data, and finally store it in target database
"""
import requests
import pandas as pd
import config
import request_json
import gaussdb


def fetch_and_save_realtime_data():
    """Fetch real-time data from multiple devices and save to database"""
    # API endpoint configuration
    api_url = 'http://10.66.168.69:8330/share/data/sensor/moreDevRealtime'
    headers = {'Content-Type': 'application/json'}  # Unified request header configuration
    
    # Target database table configuration
    target_table = 'coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf'
    constraint_keys = ['device_code']

    # Connect to GaussDB database
    try:
        db_conn = gaussdb.GaussDB(** config.GAUSSDB_DWS)
    except Exception as e:
        print(f"Database connection failed: {str(e)}")
        return

    try:
        # Get total number of unique devices
        count_sql = "SELECT COUNT(DISTINCT device_code) FROM coss_dim.dim_tmu_iot_device_info"
        total_devices = db_conn.fetch_data(count_sql)[0][0]  # Directly get count result
        print(f"Total number of devices: {total_devices}")

        offset = 0
        batch_size = 9000  # Batch processing size

        # Pagination to get device list and process
        while offset < total_devices:
            # Pagination query for device codes
            device_sql = f"""
                SELECT device_code 
                FROM coss_dim.dim_tmu_iot_device_info 
                ORDER BY device_code 
                LIMIT {batch_size} OFFSET {offset}
            """
            offset += batch_size
            print(f"Processing batch {offset//batch_size}, current offset: {offset}")

            # Extract device code list
            device_records = db_conn.fetch_data(device_sql)
            device_codes = [record[0] for record in device_records]  # Simplify with list comprehension

            # Construct API request data
            request_data = {"deviceCodes": device_codes}

            # Call API to get real-time data
            try:
                response = requests.post(api_url, json=request_data, headers=headers, timeout=1000)
                response.raise_for_status()  # Check if request is successful
            except requests.exceptions.RequestException as e:
                print(f"0API request failed: {str(e)}, skipping current batch")
                continue

            # Parse API response data
            try:
                api_response = response.json()
                realtime_data = api_response.get('data', [])  # Safely get data field
            except json.JSONDecodeError:
                print("API response parsing failed, skipping current batch")
                continue

            # Convert data to DataFrame
            if realtime_data == None:
                data_list = []
                print("The result list is null")
            else:
                data_list = [
                    [
                        item['deviceCode'],
                        item['sensorId'],
                        item['value'],
                        item['time']
                    ] 
                    for item in realtime_data
                ]
            
            df = pd.DataFrame(
                data_list,
                columns=['device_code', 'sensor_id', 'value', 'time']
            )

            # Print batch data preview
            print(f"Fetched {len(df)} records in current batch")
            if not df.empty:
                # Save data to database
                try:
                    request_json.save_to_gaussdb(
                        df, 
                        config.GAUSSDB_DWS, 
                        target_table, 
                        constraint_keys
                    )
                    print(f"Data successfully saved to {target_table}")
                except Exception as e:
                    print(f"Data saving failed: {str(e)}")

    except Exception as e:
        print(f"Error occurred during processing: {str(e)}")
    finally:
        # Ensure database connection is closed (if supported by gaussdb library)
        if 'db_conn' in locals():
            try:
                db_conn.close()
            except:
                pass


if __name__ == "__main__":
    fetch_and_save_realtime_data()

```



# shell

```shell
# 授权命令
cd /opt/app/coss/iot/
chmod -R 777 *
```

# data Profile

```sql
-- 获取远传表的水表ID 和住所ID
create table  coss_tmp.dim_tmu_iot_device_info_tmp_01 as
with t_a as 
(select
t."PREMISE_METER_ID" 
,t."PREMISE_ID"
,t."INSTALL_DATE" 
,t1."METER_ID"
,t1."METER_NO"
from 
wcdms."PREMISE_METER" t
inner  join 
(select "METER_ID" ,t."METER_NO"  from wcdms."METER" t
inner join coss_dim.dim_tmu_iot_device_info t1 on t."METER_NO" = t1.device_code ) t1
on t."METER_ID" = t1."METER_ID"
)
select 
*
from 
(select 
"METER_NO"
,"INSTALL_DATE"
,"PREMISE_METER_ID"
,"PREMISE_ID"
,ROW_NUMBER() OVER (PARTITION BY "METER_NO" ORDER BY "INSTALL_DATE" DESC) AS rn
from t_a ) t
WHERE rn =  1
```

```sql
-- 备份和更新数据
create table coss_tmp.dim_tmu_iot_device_info_tmp_03 as 
select * from coss_dim.dim_tmu_iot_device_info
-- 获取填报数据
drop table if exists coss_tmp.dim_tmu_iot_device_info_tmp_04;
create table  coss_tmp.dim_tmu_iot_device_info_tmp_04 as
with t_a as 
(select
   t."METER_NO"             as device_code
   ,t."METER_TYPE_CODE"     as meter_type_code
   ,t1."METER_TYPE_DESC"    as meter_type_dcsc
   ,t2."PREMISE_ID"         as premise_id
   ,t."SERIAL_NO"           as serial_no
   ,t."RCV_DATE"            as rcv_date
from wcdms."METER" t
inner join wcdms."CFG_METER_TYPE" t1 on t."METER_TYPE_CODE" = t1."METER_TYPE_CODE"
inner join coss_tmp.dim_tmu_iot_device_info_tmp_01 t2 on t."METER_NO" = t2."METER_NO")
select 
    t1.device_code,
    t1.device_name,
    t.meter_type_code,
    t.meter_type_dcsc,
    t.premise_id,
    t.serial_no,
    t.rcv_date,
    CASE
        WHEN t1.device_code % 10 >= 0 AND t1.device_code % 10 <= 1 THEN 'HKI'
        WHEN t1.device_code % 10 >= 2 AND t1.device_code % 10 <= 3 THEN 'K'
        WHEN t1.device_code % 10 >= 4 AND t1.device_code % 10 <= 6 THEN 'NTW'
        WHEN t1.device_code % 10 >= 7 AND t1.device_code % 10 <= 9 THEN 'HKI'
    END AS region_abbr,
    t1.sensor_id,
    t1.sensor_name,
    t1.sensor_unit,
    current_timestamp dim_update_time,
    current_timestamp dim_load_time
from t_a t 
inner join coss_tmp.dim_tmu_iot_device_info_tmp_03 t1 on t.device_code = t1.device_code



insert into coss_dim.dim_tmu_iot_device_info select * from coss_tmp.dim_tmu_iot_device_info_tmp_04

```





# 代码备份

## ods_cmsdms_tmu_more_dev_realtime_minf.py

> 循环读取接口数据的版本

```python
# -*- coding: utf-8 -*-
"""
Multi-device real-time data acquisition and storage script
Function: Retrieve device list from database, batch call API to get real-time data, and finally store it in target database
"""
import requests
import pandas as pd
import config
import gaussdb
import request_json

def fetch_and_save_realtime_data():
    """Fetch real-time data from multiple devices and save to database"""
    # API endpoint configuration
    api_url = 'http://10.66.169.102:8330/share/data/sensor/moreDevRealtime'
    headers = {'Content-Type': 'application/json'}  # Unified request header configuration

    # Target database table configuration
    target_table = 'coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf'
    constraint_keys = ['device_code']

    # Connect to GaussDB database
    try:
        db_conn = gaussdb.GaussDB(** config.GAUSSDB_DWS)
    except Exception as e:
        print(f"Database connection failed: {str(e)}")
        return

    try:
        # Get total number of unique devices
        count_sql = "SELECT COUNT(DISTINCT device_code) FROM coss_dim.dim_tmu_iot_device_info"
        total_devices = db_conn.fetch_data(count_sql)[0][0]  # Directly get count result
        print(f"Total number of devices: {total_devices}")

        offset = 0
        batch_size = 500  # Batch processing size

        # Pagination to get device list and process
        while offset < total_devices:
            # Pagination query for device codes
            device_sql = f"""
                SELECT device_code
                FROM coss_dim.dim_tmu_iot_device_info
                ORDER BY device_code
                LIMIT {batch_size} OFFSET {offset}
            """
            offset += batch_size
            print(f"Processing batch {offset//batch_size}, current offset: {offset}")

            # Extract device code list
            device_records = db_conn.fetch_data(device_sql)
            device_codes = [record[0] for record in device_records]  # Simplify with list comprehension

            # Construct API request data
            request_data = {"deviceCodes": device_codes}

            # Call API to get real-time data
            try:
                response = requests.post(api_url, json=request_data, headers=headers, timeout=1000)
                response.raise_for_status()  # Check if request is successful
            except requests.exceptions.RequestException as e:
                print(f"0API request failed: {str(e)}, skipping current batch")
                continue

            # Parse API response data
            try:
                api_response = response.json()
                realtime_data = api_response.get('data', [])  # Safely get data field
            except json.JSONDecodeError:
                print("API response parsing failed, skipping current batch")
                continue

            # Convert data to DataFrame
            if realtime_data == None:
                data_list = []
                print("The result list is null")
            else:
                data_list = [
                    [
                        item['deviceCode'],
                        item['sensorId'],
                        item['value'],
                        item['time']
                    ]
                    for item in realtime_data
                ]

            df = pd.DataFrame(
                data_list,
                columns=['device_code', 'sensor_id', 'value', 'time']
            )

            # Print batch data preview
            print(f"Fetched {len(df)} records in current batch")
            if not df.empty:
                # Save data to database
                try:
                    request_json.save_to_gaussdb(
                        df,
                        config.GAUSSDB_DWS,
                        target_table,
                        constraint_keys
                    )
                    print(f"Data successfully saved to {target_table}")
                except Exception as e:
                    print(f"Data saving failed: {str(e)}")

    except Exception as e:
        print(f"Error occurred during processing: {str(e)}")
    finally:
        # Ensure database connection is closed (if supported by gaussdb library)
        if 'db_conn' in locals():
            try:
                db_conn.close()
            except:
                pass


if __name__ == "__main__":
    fetch_and_save_realtime_data()


```

## ods_cmsdms_tmu_devinfo_minf.py

> 循环读取接口数据的版本

```python
# -*- coding: utf-8 -*-
"""
Device Information Acquisition and Storage Script
Function: Fetch device information (including sensor details) via API pagination,
          process the data into a DataFrame, and store it in the target database.
"""
import requests
import pandas as pd
import config
import request_json


def fetch_and_save_device_info():
    """Fetch device information with pagination from API and save to database"""
    # API configuration
    api_url = 'http://10.66.169.102:8330/share/data/devInfo'
    headers = {'Content-Type': 'application/json'}
    page_size = 2000  # Number of records per page

    # Database configuration
    target_table = 'coss_ods.ods_cmsdms_tmu_device_info_minf'
    constraint_keys = ['device_code']

    try:
        # Get total pages by initial request
        initial_payload = {
            "page": 1,
            "pageSize": page_size,
            "deviceCodes": []
        }

        # Send initial request to get pagination info
        response = requests.post(
            api_url,
            json=initial_payload,
            headers=headers,
            timeout=1000  # Add timeout to prevent infinite waiting
        )
        response.raise_for_status()  # Raise exception for HTTP errors
        total_pages = response.json()["data"]["totalPage"]
        print(f"Total pages to process: {total_pages}")

        # Initialize empty DataFrame to store all records
        full_df = pd.DataFrame(
            columns=['device_code', 'device_name', 'sensor_id', 'sensor_name', 'sensor_unit']
        )

        # Iterate through all pages to fetch data
        for page_num in range(1, total_pages + 1):
            # Prepare payload for current page
            payload = {
                "page": page_num,
                "pageSize": page_size,
                "deviceCodes": []
            }

            # Send request for current page
            try:
                page_response = requests.post(
                    api_url,
                    json=payload,
                    headers=headers,
                    timeout=1000
                )
                page_response.raise_for_status()
                page_data = page_response.json()["data"]["records"]
            except Exception as e:
                print(f"Failed to fetch page {page_num}: {str(e)}. Skipping this page.")
                continue

            # Parse records and extract required fields
            page_records = []
            for device in page_data:
                device_code = device['deviceCode']
                device_name = device['deviceName']

                # Process sensor information nested in device records
                for sensor in device['sensors']:
                    page_records.append([
                        device_code,
                        device_name,
                        sensor['sensorId'],
                        sensor['sensorName'],
                        sensor['unit']
                    ])

            # Convert current page records to DataFrame and merge
            page_df = pd.DataFrame(
                page_records,
                columns=['device_code', 'device_name', 'sensor_id', 'sensor_name', 'sensor_unit']
            )
            full_df = pd.concat([full_df, page_df], axis=0, ignore_index=True)
            print(f"Processed page {page_num}/{total_pages}. Cumulative records: {len(full_df)}")

        # Save data to database if not empty
        print(full_df.head())
        if not full_df.empty:
            try:
                request_json.save_to_gaussdb(
                    full_df,
                    config.GAUSSDB_DWS,
                    target_table,
                    constraint_keys
                )
                print(f"Successfully saved {len(full_df)} records to {target_table}")
            except Exception as e:
                print(f"Failed to save data to database: {str(e)}")
        else:
            print("No data to save (DataFrame is empty)")

    except Exception as e:
        print(f"Fatal error during data processing: {str(e)}")


if __name__ == "__main__":
    fetch_and_save_device_info()

```

