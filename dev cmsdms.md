# 代码

## ods_cmsdms_tmu_permission_info_df

### 建表

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

### 接口

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



## ods_cmsdms_tmu_sensor_realtime_minf

### create table

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

### 接口

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





## ods_cmsdms_tmu_more_dev_realtime_minf

### 接口

```sql
# -*- coding: utf-8 -*-
# File : ods_cmsdms_tmu_more_dev_realtime_minf.py
# Author : CDM
# Date : 2026/07/09 16:59
# -*- coding: utf-8 -*-
"""
Multi-device real-time data acquisition and storage script
Function: Retrieve device list from database, batch call API to get real-time data, store into GaussDB
Optimization: Semaphore current limit, retry backoff, hierarchical timeout, task batch submit, time cost statistics, exception classification
"""
import time
import json
import logging
from queue import Queue
from typing import List, Set, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Semaphore
from requests.exceptions import RequestException, ConnectionError, Timeout
import requests
import pandas as pd
import config
import gaussdb
import request_json

# ===================== Log Level Configuration =====================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# ===================== Global Unified Configuration Class =====================
class ApiConfig:
    API_URL = "http://10.66.169.102:8330/share/data/sensor/moreDevRealtime"
    BASE_HEADERS = {"Content-Type": "application/json"}
    TRACE_HEADER_KEY = "X-Request-Time"
    # Hierarchical timeout settings
    CONNECT_TIMEOUT = 3
    READ_TIMEOUT = 12
    # Retry configuration
    MAX_RETRY = 3
    RETRY_BASE_DELAY = 1
    # Mandatory sleep throttling after single request
    REQ_THROTTLE_SLEEP = 0.05
    # API semaphore: upper limit of concurrent requests
    API_SEM_LIMIT = 20
    # Max thread pool capacity
    POOL_MAX_WORKERS = 100
    # Batch submission size to smooth traffic spikes
    SUBMIT_BATCH = 200
    # Max result queue capacity to avoid memory overflow
    QUEUE_MAX_SIZE = 10000

class DbConfig:
    TARGET_TABLE = "coss_ods.ods_cmsdms_tmu_more_dev_realtime_minf"
    CONSTRAINT_KEYS = ["device_code"]
    DEVICE_DIM_TABLE = "coss_dim.dim_tmu_iot_device_info"
    PAGE_QUERY_BATCH = 1000

# ===================== Global Variables =====================
result_queue = Queue(maxsize=ApiConfig.QUEUE_MAX_SIZE)
api_sem = Semaphore(ApiConfig.API_SEM_LIMIT)
failed_device_codes: Set[str] = set()

# ===================== Utility Function Layer =====================
def get_request_headers() -> dict:
    """Generate request headers with timestamp anti-frequent-burst identifier"""
    headers = ApiConfig.BASE_HEADERS.copy()
    headers[ApiConfig.TRACE_HEADER_KEY] = str(int(time.time() * 1000))
    return headers

def get_backoff_delay(retry_cnt: int) -> float:
    """Exponential backoff retry interval: 1s, 2s, 4s"""
    return ApiConfig.RETRY_BASE_DELAY * (2 ** retry_cnt)

def dump_failed_devices(file_name: str = "failed_device_list.txt") -> None:
    """Persist failed device codes to disk for manual supplementary data pull"""
    if not failed_device_codes:
        logger.info("No failed device codes, skip writing file")
        return
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(sorted(failed_device_codes)))
        logger.warning(f"Failed device codes saved to {file_name}, total: {len(failed_device_codes)}")
    except Exception as e:
        logger.error(f"Error writing failed device file: {str(e)}")

# ===================== Core API Request Layer (Retry, Flow Control, Exception Classification Built-in) =====================
def pull_single_device_data(device_code: str) -> None:
    """Single-device API data pull with semaphore flow control, auto retry and exception classification"""
    headers = get_request_headers()
    payload = {"deviceCodes": [device_code]}
    timeout_tuple = (ApiConfig.CONNECT_TIMEOUT, ApiConfig.READ_TIMEOUT)
    retry_count = 0
    success_flag = False

    while retry_count <= ApiConfig.MAX_RETRY:
        try:
            # Semaphore to control concurrent requests
            with api_sem:
                resp = requests.post(
                    url=ApiConfig.API_URL,
                    json=payload,
                    headers=headers,
                    timeout=timeout_tuple
                )
            # Distinguish business exceptions
            if 400 <= resp.status_code < 500:
                logger.error(f"[{device_code}] 4xx business error, status={resp.status_code}, stop retry")
                failed_device_codes.add(device_code)
                break
            resp.raise_for_status()
            res_json = resp.json()
            data_rows = res_json.get("data", [])
            records = []
            for item in data_rows:
                records.append([
                    item.get("deviceCode"),
                    item.get("sensorId"),
                    item.get("value"),
                    item.get("time")
                ])
            result_queue.put(records)
            success_flag = True
            break

        except (ConnectionError, Timeout) as net_err:
            retry_count += 1
            if retry_count > ApiConfig.MAX_RETRY:
                logger.error(f"[{device_code}] Max retry reached for network timeout, err: {str(net_err)}")
                failed_device_codes.add(device_code)
                break
            delay = get_backoff_delay(retry_count)
            logger.warning(f"[{device_code}] Network error, retry {retry_count}/{ApiConfig.MAX_RETRY}, wait {delay}s")
            time.sleep(delay)
        except RequestException as server_err:
            # Retry on 5xx server-side errors
            if 500 <= server_err.response.status_code < 600 if hasattr(server_err, "response") else False:
                retry_count += 1
                if retry_count > ApiConfig.MAX_RETRY:
                    logger.error(f"[{device_code}] Max retry reached for 5xx server error")
                    failed_device_codes.add(device_code)
                    break
                delay = get_backoff_delay(retry_count)
                logger.warning(f"[{device_code}] Server 5xx error, retry {retry_count}/{ApiConfig.MAX_RETRY}, wait {delay}s")
                time.sleep(delay)
            else:
                logger.error(f"[{device_code}] Unhandled request exception: {str(server_err)}")
                failed_device_codes.add(device_code)
                break
        except Exception as other_err:
            logger.error(f"[{device_code}] Unknown error: {str(other_err)}")
            failed_device_codes.add(device_code)
            break
    # Mandatory sleep after request completion to throttle QPS
    time.sleep(ApiConfig.REQ_THROTTLE_SLEEP)

# ===================== Database Operation Layer =====================
def load_all_device_codes(db_conn) -> List[str]:
    """Paginate and load full list of device codes"""
    count_sql = f"SELECT COUNT(DISTINCT device_code) FROM {DbConfig.DEVICE_DIM_TABLE}"
    total = db_conn.fetch_data(count_sql)[0][0]
    logger.info(f"Total device count in dimension table: {total}")
    all_devices = []
    offset = 0
    while offset < total:
        page_sql = f"""
            SELECT DISTINCT device_code
            FROM {DbConfig.DEVICE_DIM_TABLE}
            ORDER BY device_code
            LIMIT {DbConfig.PAGE_QUERY_BATCH} OFFSET {offset}
        """
        page_data = db_conn.fetch_data(page_sql)
        batch_dev = [row[0] for row in page_data]
        all_devices.extend(batch_dev)
        offset += DbConfig.PAGE_QUERY_BATCH
    logger.info(f"Loading all device codes completed, total: {len(all_devices)}")
    return all_devices

def batch_save_to_db(raw_records: List[list], db_conn_cfg) -> None:
    """Batch write DataFrame to database"""
    if not raw_records:
        logger.info("No valid data available, skip database write operation")
        return
    df = pd.DataFrame(
        raw_records,
        columns=["device_code", "sensor_id", "value", "time"]
    )
    request_json.save_to_gaussdb(
        df=df,
        db_config=db_conn_cfg,
        table_name=DbConfig.TARGET_TABLE,
        unique_keys=DbConfig.CONSTRAINT_KEYS
    )
    logger.info(f"Successfully wrote {len(df)} rows to {DbConfig.TARGET_TABLE}")

# ===================== Main Scheduling Flow (With Segmented Execution Time Statistics) =====================
def main_task_flow():
    total_start = time.perf_counter()
    init_cost = 0.0
    api_cost = 0.0
    data_proc_cost = 0.0
    db_write_cost = 0.0

    # 1. Initialization Phase: Establish DB Connection
    init_start = time.perf_counter()
    try:
        db_conn = gaussdb.GaussDB(**config.GAUSSDB_DWS)
        logger.info("Database connection initialized successfully")
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return
    init_cost = time.perf_counter() - init_start

    try:
        # Load device list
        device_list = load_all_device_codes(db_conn)
        if not device_list:
            logger.warning("Device list is empty, terminating task")
            dump_failed_devices()
            return

        # 2. Concurrent API Pull Phase (Batch Task Submission)
        api_start = time.perf_counter()
        logger.info(f"Start concurrent API data pull, max thread pool workers: {ApiConfig.POOL_MAX_WORKERS}, batch submission size: {ApiConfig.SUBMIT_BATCH}")
        with ThreadPoolExecutor(max_workers=ApiConfig.POOL_MAX_WORKERS) as executor:
            # Submit tasks in batches to avoid generating thousands of Futures at once
            for batch_idx in range(0, len(device_list), ApiConfig.SUBMIT_BATCH):
                batch_dev = device_list[batch_idx: batch_idx + ApiConfig.SUBMIT_BATCH]
                futures = [executor.submit(pull_single_device_data, code) for code in batch_dev]
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        logger.error(f"Runtime exception in thread task: {str(e)}")
        api_cost = time.perf_counter() - api_start

        # 3. Data Processing Phase: Aggregate queue data
        proc_start = time.perf_counter()
        all_valid_records = []
        while not result_queue.empty():
            all_valid_records.extend(result_queue.get())
        data_proc_cost = time.perf_counter() - proc_start
        logger.info(f"All API tasks completed, total valid data rows: {len(all_valid_records)}")

        # 4. Database Write Phase
        db_start = time.perf_counter()
        batch_save_to_db(all_valid_records, config.GAUSSDB_DWS)
        db_write_cost = time.perf_counter() - db_start

    except Exception as main_err:
        logger.error(f"Fatal error in main workflow: {str(main_err)}", exc_info=True)
    finally:
        # Persist failed device codes to disk
        dump_failed_devices()
        # Print segmented execution time summary
        total_cost = time.perf_counter() - total_start
        print("\n==================== Segmented Execution Time Summary ====================")
        print(f"Initialization Duration: {init_cost:.2f} s")
        print(f"Batch API Fetch Duration: {api_cost:.2f} s")
        print(f"Data Processing Duration: {data_proc_cost:.2f} s")
        print(f"Database Write Duration: {db_write_cost:.2f} s")
        print(f"Total Script Execution Duration: {total_cost:.2f} s")
        print("==========================================================================\n")

if __name__ == "__main__":
    main_task_flow()
```



## sql update



```
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



# 提示词

## ods_cmsdms_tmu_permission_info_df

### 建表

按照下列要求生成见表语句：

1. 按照下列要求生成一张gaussdb的见表语句,表名称为：coss_ods.ods_cmsdms_tmu_permission_info_df

2. 见表语句的主键为 device_id 和sensor_id ,字段名和关键字用小写字母,把字段的驼峰命名改为下划线

3. 字段的comment 的英文单词首字母大写，数据接收表的字段需要按照下面的jason提供的字段生成

   ```sql
           {
                   "deviceId": "000043160453",
                   "deviceCode": "000043160453",
                   "deviceName": "000043160453-测试设备",
                   "orgId": "8",
                   "businessType": "poc",
                   "groupId": "697514034",
                   "sensors": [
                       {
                           "sensorId": "000043160453-A7",
                           "sensorCode": "000043160453A7",
                           "sensorName": "A7",
                           "unit": " "
                       },
                       {
                           "sensorId": "000043160453-A8",
                           "sensorCode": "000043160453A8",
                           "sensorName": "A8",
                           "unit": " "
                       },
                       {
                           "sensorId": "000043160453-A9",
                           "sensorCode": "000043160453A9",
                           "sensorName": "A9",
                           "unit": " "
                       }
                   ]
               },
   ```

4. 生成的样例sql为：

   ```sql
   drop table if exists coss_ods.ods_iot_tmu_device_info_minf;
   
   create table if not exists coss_ods.ods_iot_tmu_device_info_minf (
       device_code      varchar(200),
       device_name      varchar(200),
       sensor_id        varchar(200),
       sensor_name      varchar(200),
       sensor_unit      varchar(120),
       ods_update_time  timestamp(6) null default pg_systimestamp(),
       ods_load_time    timestamp(6) null default pg_systimestamp(),
       primary key (device_code)
   );
   
   comment on table coss_ods.ods_iot_tmu_device_info_minf is 'Device Info';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.device_code is 'Device Code';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.device_name is 'Device Name';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.sensor_id is 'Sensorid';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.sensor_name is 'Sensor Name';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.sensor_unit is 'Sensor Unit';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.ods_update_time is 'Ods Update Time';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.ods_load_time is 'Ods Load Time';
   ```

## 接口



```
接口优化需求：
并发限流 + 信号量控制：新增线程信号量，严格控制同时发起请求数量，避免瞬间打满接口连接
请求自动重试机制：网络超时、5xx 服务错误自动重试 3 次，间隔退避，不丢失分页
分级超时控制：连接超时 + 读取超时分离，卡死请求快速释放线程
请求间隔节流：每个请求完成强制休眠，降低接口 QPS 压力
异常分类处理：区分 4xx 业务错误 / 5xx 服务错误 / 网络异常，不无限重试无效请求
并发队列容量限制：防止内存堆积海量分页数据
请求头统一超时标识、防高频爆破
分页任务分批提交：不一次性创建上千个并发 future，分批执行平滑流量
失败分页记录落盘：执行结束输出失败页码，支持手动补拉，避免丢数据
日志分级打印：区分成功 / 警告 / 错误，便于定位接口过载问题

代码风格优化：
分层解耦，可读性强
可维护性扩展优化
代码冗余清理优化，去除不必要的日志输出


接口代码执行时长打印需求：
初始化 接口拉取 数据处理 入库 合计 时长 的代码执行时长

====================分段执行时长汇总====================
初始化耗时：0.04 s
接口批量拉取耗时：3.16 s
数据处理耗时：0.01 s
数据库入库耗时：1.2 s
脚本全部执行合计耗时：4.43 s
========================================================

```

需要生成python读取接口数据，然后把数据写入到数据库中

1. Base URLs:[http://10.66.110.106:8325](http://10.66.110.106:8325/)

2. 接口的基本信息

   ```
   POST 获取数据权限范围v4.0
   POST /share/data/permission
   
   Body 请求参数
   
   {
       "deviceCodes": [],
       "pageSize": 10,
       "pageNo": 1
   }
   请求参数
   名称	位置	类型	必选	说明
   appId	header	string	是	none
   body	body	object	否	none
   » deviceCodes	body	[string]	否	设备编码集合(非必填)
   » businessType	body	string	否	业务类型（非必填）
   » pageNo	body	number	是	当前页
   » pageSize	body	number	是	每页显示条数
   返回示例
   
   {
       "success": true,
       "code": 200,
       "message": "success",
       "data": {
           "records": [
               {
                   "deviceId": "000043160453",
                   "deviceCode": "000043160453",
                   "deviceName": "000043160453-测试设备",
                   "orgId": "8",
                   "businessType": "poc",
                   "groupId": "697514034",
                   "sensors": [
                       {
                           "sensorId": "000043160453-A7",
                           "sensorCode": "000043160453A7",
                           "sensorName": "A7",
                           "unit": " "
                       },
                       {
                           "sensorId": "000043160453-A8",
                           "sensorCode": "000043160453A8",
                           "sensorName": "A8",
                           "unit": " "
                       },
                       {
                           "sensorId": "000043160453-A9",
                           "sensorCode": "000043160453A9",
                           "sensorName": "A9",
                           "unit": " "
                       }
                   ]
               },
               {
                   "deviceId": "861562076922241",
                   "deviceCode": "861562076922241",
                   "deviceName": "22251284 (St. Paul's Hospital - Block B AC system)",
                   "orgId": "8",
                   "businessType": "poc",
                   "groupId": "866529801",
                   "sensors": [
                       {
                           "sensorId": "861562076922241-Q1",
                           "sensorCode": "861562076922241Q1",
                           "sensorName": "Q1（正向累积流量）",
                           "unit": "m³"
                       }
                   ]
               },
               {
                   "deviceId": "PLC4.PLC4",
                   "deviceCode": "PLC4.PLC4",
                   "deviceName": "L004 (Lantau Island Catchwater - Section 214)",
                   "orgId": "8",
                   "businessType": "poc",
                   "groupId": "206778262",
                   "sensors": [
                       {
                           "sensorId": "PLC4.PLC4-Value1",
                           "sensorCode": "PLC4.PLC4Value1",
                           "sensorName": "Water Level",
                           "unit": "m"
                       },
                       {
                           "sensorId": "PLC4.PLC4-Value2",
                           "sensorCode": "PLC4.PLC4Value2",
                           "sensorName": "Battery Voltage",
                           "unit": "mV"
                       },
                       {
                           "sensorId": "PLC4.PLC4-Value3",
                           "sensorCode": "PLC4.PLC4Value3",
                           "sensorName": "Solar Panel Voltage",
                           "unit": "mV"
                       }
                   ]
               }
           ],
           "total": 419,
           "size": 10,
           "current": 1,
           "pages": 42
       },
       "timestamp": 1781250853279,
       "requestId": "IBatlPEyqGeJteVbG5vq",
       "msg": "success"
   }
   返回结果
   状态码	状态码含义	说明	数据模型
   200	OK	none	Inline
   返回数据结构
   状态码 200
   
   名称	类型	必选	约束	中文名	说明
   » success	boolean	true	none		是否成功
   » code	integer	true	none		状态码
   » message	string	true	none		提示信息
   » data	object	true	none		业务数据
   »» records	[object]	true	none		记录列表
   »»» deviceCode	string	false	none		设备编码
   »»» deviceName	string	false	none		设备名称
   »»» orgId	string	false	none		组织ID
   »»» businessType	string	false	none		业务类型
   »»» groupId	string	false	none		分组ID
   »»» sonsors	[object]	false	none		传感器列表
   »»»» sonsorCode	string	false	none		传感器编码
   »»»» sonsorName	string	false	none		传感器名称
   »»»» unit	string	false	none		单位
   »» total	integer	true	none		总记录数
   »» size	integer	true	none		每页显示条数
   »» current	integer	true	none		当前页
   »» pages	integer	true	none		总页数
   » timestamp	integer	true	none		时间戳
   » requestId	string	true	none		请求ID
   » cause	string	true	none		原因
   » msg	string	true	none		提示信息
   ```

3. 要把读取的接口数据写入到数据库中的数据表，数据表为：

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
       primary key (device_id, sensor_id)
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

4. 参考的python代码

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

   















## ods_cmsdms_tmu_sensor_realtime_minf

### 建表

按照下列要求生成见表语句：

1. 按照下列要求生成一张gaussdb的见表语句,表名称为：coss_ods.ods_cmsdms_tmu_sensor_realtime_minf

2. 见表语句的主键为 sns_code 和time,字段名和关键字用小写字母,把字段的驼峰命名改为下划线

3. 字段的comment 的英文单词首字母大写，数据接收表的字段需要按照下面的jason提供的字段生成

   ```sql
   {
               "snsCode": "WLIS_1023_digital_in_1",
               "value": 625.0,
               "time": 1781250900095
           }
   ```

4. 生成的样例sql为：

   ```sql
   drop table if exists coss_ods.ods_iot_tmu_device_info_minf;
   
   create table if not exists coss_ods.ods_iot_tmu_device_info_minf (
       device_code      varchar(200),
       device_name      varchar(200),
       sensor_id        varchar(200),
       sensor_name      varchar(200),
       sensor_unit      varchar(120),
       ods_update_time  timestamp(6) null default pg_systimestamp(),
       ods_load_time    timestamp(6) null default pg_systimestamp(),
       primary key (device_code)
   );
   
   comment on table coss_ods.ods_iot_tmu_device_info_minf is 'Device Info';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.device_code is 'Device Code';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.device_name is 'Device Name';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.sensor_id is 'Sensorid';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.sensor_name is 'Sensor Name';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.sensor_unit is 'Sensor Unit';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.ods_update_time is 'Ods Update Time';
   comment on column coss_ods.ods_iot_tmu_device_info_minf.ods_load_time is 'Ods Load Time';
   ```

### 接口

```
按照以下要求优化代码：
1.接口优化需求：
并发限流 + 信号量控制：新增线程信号量，严格控制同时发起请求数量，避免瞬间打满接口连接
请求自动重试机制：网络超时、5xx 服务错误自动重试 3 次，间隔退避，不丢失分页
分级超时控制：连接超时 + 读取超时分离，卡死请求快速释放线程
请求间隔节流：每个请求完成强制休眠，降低接口 QPS 压力
异常分类处理：区分 4xx 业务错误 / 5xx 服务错误 / 网络异常，不无限重试无效请求
并发队列容量限制：防止内存堆积海量分页数据
请求头统一超时标识、防高频爆破
分页任务分批提交：不一次性创建上千个并发 future，分批执行平滑流量
失败分页记录落盘：执行结束输出失败页码，支持手动补拉，避免丢数据
日志分级打印：区分成功 / 警告 / 错误，便于定位接口过载问题

2.代码风格优化：
分层解耦，可读性强
可维护性扩展优化
代码冗余清理优化，去除不必要的日志输出


3.接口代码执行时长打印需求：
初始化 接口拉取 数据处理 入库 合计 时长 的代码执行时长

====================分段执行时长汇总====================
初始化耗时：0.04 s
接口批量拉取耗时：3.16 s
数据处理耗时：0.01 s
数据库入库耗时：1.2 s
脚本全部执行合计耗时：4.43 s
========================================================

```

需要生成python读取接口数据，然后把数据写入到数据库中

1. Base URLs:[http://10.66.110.106:8325](http://10.66.110.106:8325/)

2. appid: 123456

3. 接口的基本信息

   ```
   POST 获取采集项实时数据v4.0
   POST /share/data/sensor/realtime
   
   Body 请求参数
   
   {
       "sensorCodes": [
           "WLIS_1023_voltage_1",
           "WLIS_1023_voltage_2",
           "WLIS_1023_digital_in_1"
       ]
   }
   请求参数
   名称	位置	类型	必选	说明
   appId	header	string	是	none
   body	body	object	否	none
   » sensorCodes	body	[string]	是	传感器编码
   返回示例
   
   {
       "success": true,
       "code": 200,
       "message": "success",
       "data": [
           {
               "snsCode": "WLIS_1023_digital_in_1",
               "value": 625.0,
               "time": 1781250900095
           },
           {
               "snsCode": "WLIS_1023_voltage_1",
               "value": 31988.0,
               "time": 1781250900095
           },
           {
               "snsCode": "WLIS_1023_voltage_2",
               "value": 13223.0,
               "time": 1781250900095
           }
       ],
       "timestamp": 1781250949464,
       "requestId": "jG9YWPBTBnXM_gfKnyFI",
       "msg": "success"
   }
   返回结果
   状态码	状态码含义	说明	数据模型
   200	OK	none	Inline
   返回数据结构
   状态码 200
   
   名称	类型	必选	约束	中文名	说明
   » success	boolean	true	none		是否成功
   » code	integer	true	none		状态码
   » message	string	true	none		提示信息
   » data	[object]	true	none		业务数据
   »» snsCode	string	false	none		传感器编码
   »» time	integer	false	none		时间
   »» value	integer	false	none		数据值
   » timestamp	integer	true	none		时间戳
   » requestId	string	true	none		请求ID
   » cause	string	true	none		原因
   » msg	string	true	none		提示信息
   ```

4. 要把读取的接口数据写入到数据库中的数据表，数据表为：

   ```sql
   drop table if exists coss_ods.ods_cmsdms_tmu_sensor_realtime_minf;
   
   create table if not exists coss_ods.ods_cmsdms_tmu_sensor_realtime_minf (
       sns_code         varchar(100) not null,
       value            decimal(20,6),
       time             bigint not null,
       ods_update_time  timestamp(6) null default current_timestamp,
       ods_load_time    timestamp(6) null default current_timestamp,
       primary key (sns_code, time)
   );
   
   comment on table coss_ods.ods_cmsdms_tmu_sensor_realtime_minf is 'CMSDMS Sensor Realtime Information';
   comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.sns_code is 'Sensor Code';
   comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.value is 'Value';
   comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.time is 'Time';
   comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.ods_update_time is 'Ods Update Time';
   comment on column coss_ods.ods_cmsdms_tmu_sensor_realtime_minf.ods_load_time is 'Ods Load Time';
   ```

5. 接口的入参sensorCodes为：

   ```sql
   select distinct sensor_code  from coss_ods.ods_cmsdms_tmu_permission_info_df
   ```

6. 参考的python代码

   ```sql
   
   # -*- coding: utf-8 -*-
   """
   IOT sensor real-time data acquisition and storage script
   Function: Retrieve sensor codes from database, batch call IOT API to get real-time data, and store in target GaussDB table
   Optimization: Concurrent API calls with configurable thread pool
   """
   import requests
   import pandas as pd
   import json
   from concurrent.futures import ThreadPoolExecutor, as_completed
   from queue import Queue
   # Please replace with actual database connection module and config
   # You need to implement gaussdb module and config file according to your environment
   import config
   import gaussdb
   
   # ===================== Configuration =====================
   # API endpoint for real-time sensor data
   API_URL = 'http://10.66.169.58:8001/iot3/rest/api/v1/realtime.json'
   # HTTP request headers
   HEADERS = {'Content-Type': 'application/json'}
   # Target database table for data storage
   TARGET_TABLE = 'coss_ods.ods_cmsdms_tmu_realtime_sensor_mini'
   # Primary key constraint columns for the target table
   CONSTRAINT_KEYS = ['code', 'time']
   # Maximum concurrent threads for API calls
   MAX_WORKERS = 100
   # Batch size for fetching sensor codes from database
   BATCH_SIZE = 500
   # ===================== Global Variables =====================
   # Thread-safe queue to store API response data
   result_queue = Queue()
   
   def fetch_sensor_realtime(sensor_code):
       """
       Fetch real-time data for a single sensor via API
       :param sensor_code: Unique identifier of the sensor
       """
       try:
           # Construct API request payload
           payload = {"codes": [sensor_code]}
           # Send POST request to API
           response = requests.post(
               url=API_URL,
               json=payload,
               headers=HEADERS,
               timeout=15  # 15 seconds timeout for API request
           )
           # Raise exception for HTTP error status codes
           response.raise_for_status()
           # Parse JSON response
           res_data = response.json()
   
           # Extract valid data from response
           data_list = res_data.get('data', [])
           records = []
           for item in data_list:
               # Map API response fields to target table columns
               records.append([
                   item.get('code'),          # Sensor Unique Code
                   item.get('time'),          # Data Report Time With Timezone
                   item.get('status'),        # Sensor Running Status
                   item.get('value'),         # Sensor Collected Measurement Value
                   item.get('name'),          # Sensor Measurement Type Name
                   item.get('unit')           # Measurement Unit
               ])
           # Put parsed records into thread-safe queue
           result_queue.put(records)
   
       except Exception as e:
           # Print error message for failed sensor data fetch
           print(f"Sensor data fetch failed: {sensor_code}, error: {str(e)}")
   
   def fetch_and_save_realtime_data():
       """
       Main function:
       1. Connect to database
       2. Fetch all sensor codes
       3. Concurrent API calls to get real-time data
       4. Save data to target database table
       """
       # Initialize database connection
       try:
           db_conn = gaussdb.GaussDB(**config.GAUSSDB_DWS)
           print("Database connection successful")
       except Exception as e:
           print(f"Database connection failed: {e}")
           return
   
       try:
           # Step 1: Get total count of unique sensor codes
           count_sql = "SELECT COUNT(DISTINCT sensor_code) FROM coss_dim.dim_sz_device_info"
           total_sensors = db_conn.fetch_data(count_sql)[0][0]
           print(f"Total number of sensors in database: {total_sensors}")
   
           # Step 2: Fetch all sensor codes with pagination to avoid memory issues
           all_sensors = []
           offset = 0
           while offset < total_sensors:
               sensor_sql = f"""
                   SELECT DISTINCT sensor_code
                   FROM coss_dim.dim_sz_device_info
                   ORDER BY sensor_code
                   LIMIT {BATCH_SIZE} OFFSET {offset}
               """
               offset += BATCH_SIZE
               sensor_records = db_conn.fetch_data(sensor_sql)
               # Extract sensor codes from query results
               all_sensors.extend([record[0] for record in sensor_records])
   
           print(f"All sensor codes loaded, total: {len(all_sensors)}")
   
           # Step 3: Execute concurrent API calls
           print(f"Start concurrent API calls with {MAX_WORKERS} threads...")
           with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
               # Submit all sensor code fetch tasks to thread pool
               futures = [executor.submit(fetch_sensor_realtime, code) for code in all_sensors]
               # Wait for all tasks to complete and handle exceptions
               for future in as_completed(futures):
                   try:
                       future.result()
                   except Exception as e:
                       print(f"Thread execution exception: {str(e)}")
   
           # Step 4: Collect all results from thread-safe queue
           all_records = []
           while not result_queue.empty():
               all_records.extend(result_queue.get())
   
           print(f"All API calls completed, valid data records obtained: {len(all_records)}")
   
           # Step 5: Save data to target database table
           if all_records:
               # Create DataFrame with target table column names
               df = pd.DataFrame(
                   all_records,
                   columns=['code', 'time', 'status', 'value', 'name', 'unit']
               )
               try:
                   # Save DataFrame to GaussDB (replace with actual save logic)
                   # The save_to_gaussdb function should handle UPSERT based on constraint keys
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
       finally:
           # Close database connection if exists
           try:
               db_conn.close()
           except:
               pass
   
   if __name__ == "__main__":
       # Execute main function when script is run directly
       fetch_and_save_realtime_data()
   
   ```

# sis

```python
# -*- coding: utf-8 -*-
# File : ods_sis_pnw_pipe_tag_monitored.py
# Author : XJH
# Date : 2025/10/14 16:59

import random
import threading
import time
import traceback
from datetime import datetime
from queue import Queue
import pandas as pd
import request_json
import gaussdb
import config

# Create thread-safe data containers and locks
collected_data = []
data_lock = threading.Lock()

# Define the worker thread function
def worker(_current_update_time):
    """
    Worker thread function to process page data from task queue

    Continuously retrieves page data from the task queue, processes it with a random delay
    to avoid frequent requests, and handles exceptions during processing.

    Parameters:
        _current_update_time: The timestamp or identifier for the current update cycle
                             Used in data processing to mark when the update occurred
    """
    while True:
        # Add random delay to avoid too frequent requests
        time.sleep(random.uniform(0.5, 1.5))

        # Get page data from task queue
        my_page_data = task_queue.get()

        # Check for termination signal
        if my_page_data is None:  # Termination signal
            break

        try:
            # Process current page data
            process_page_data(my_page_data, _current_update_time)
        except Exception as e:
            print(f'Error processing page data: {e}')
            traceback.print_exc()  # Output full stack trace
        finally:
            # Mark task as completed
            task_queue.task_done()

def process_page_data(_page_data, _current_update_time) -> None:
    """
    Process a single page of data records by fetching corresponding SIS data through API requests,
    and collect valid data in a thread-safe manner.

    This function iterates through each record in the page data, sends API requests to retrieve
    SIS data for each tag, measures request performance, and safely collects non-empty results
    into a shared data structure using a lock.

    Args:
        _page_data: A list of records to process in this page. Each record is a tuple
                                 where the first element is the SIS tag identifier.
        _current_update_time: The timestamp used as the reference time for data queries.
                              Should be a datetime object.

    Returns:
        None: This function doesn't return a value but appends results to the global collected_data list.
    """
    if not _page_data:  # Skip processing if page data is empty
        return

    # Process each record in the current page
    for record in _page_data:
        try:
            # Extract SIS tag from the record (first element of the tuple)
            sis_tag = record[0]

            # Fetch SIS data through API, and calculate request duration and print information
            start_time = time.time()
            df = request_json.fetch_nearest_data(sis_tag, _current_update_time)
            end_time = time.time()
            print(f'API request time: {end_time - start_time} seconds')

            if df is None:
                print(f'SIS API request exception: {sis_tag}, {_current_update_time}')
                continue

            # Collect data in a thread-safe manner if DataFrame is not empty
            if not df.empty:
                with data_lock:
                    collected_data.append(df)

        except Exception as e:
            print(f'Failed to process data: {e}')
            traceback.print_exc()


def main(current_update_time = None) -> None:
    """
    Main entry point to execute the SIS data fetching and storage workflow.

    This function coordinates the entire process: initializing data collection, fetching SIS tags from GaussDB,
    creating worker threads to process tag data in batches, collecting API response data, merging results,
    and inserting the combined data into real-time and historical GaussDB tables.

    Args:
        current_update_time (Optional[datetime]): Reference timestamp for SIS data queries.
            If not provided, it defaults to the current datetime when the function is called.

    Returns:
        None: The function executes workflow steps and prints logs, with no explicit return value.
    """
    # Declare global variable to modify the shared data collection list
    global collected_data
    # Initialize the global data container to ensure it's empty before processing
    collected_data = []

    # Set default query time if not provided (current datetime)
    if current_update_time is None:
        current_update_time = datetime.now()

    # Record the overall workflow start time for execution duration calculation
    workflow_start_time = time.time()

    # SQL query to fetch SIS tags that need data update, sorted by installation ID
    tag_query_sql = (
        f"SELECT scada_tag FROM {config.SIS_TAG_TABLE_NAME} "
        f"ORDER BY installation_id"
    )

    # Establish GaussDB connection and fetch SIS tags
    try:
        gauss_conn = gaussdb.GaussDB(**config.GAUSSDB_DWS)
        scada_tags = gauss_conn.fetch_data(tag_query_sql)
        print(f'Total number of SIS tags retrieved: {len(scada_tags)}')
    except Exception as db_err:
        print(f'Failed to fetch SIS tags from GaussDB: {db_err}')
        traceback.print_exc()
        return  # Terminate workflow if tag fetch fails

    # Configure batch processing parameters
    batch_size = 100  # Number of tags per batch
    # Calculate total batches (round up to include remaining tags)
    total_batches = (len(scada_tags) + batch_size - 1) // batch_size
    print(f'Total batches to process: {total_batches}')

    # Configure and start worker threads
    max_workers = min(total_batches, 100)  # Limit to 100 workers max
    worker_threads = []

    for _ in range(max_workers):
        # Create worker thread (assumes "worker" function is defined elsewhere)
        worker_thread = threading.Thread(
            target=worker,
            args=(current_update_time,)
        )
        worker_thread.daemon = True  # Set as daemon to exit with main thread
        worker_thread.start()
        worker_threads.append(worker_thread)

    # Split tags into batches and put into task queue
    for batch_idx in range(total_batches):
        # Calculate start and end indices for current batch
        start_pos = batch_idx * batch_size
        end_pos = min(start_pos + batch_size, len(scada_tags))
        batch_data = scada_tags[start_pos:end_pos]

        # Add batch to task queue
        task_queue.put(batch_data)
        print(f'Enqueued batch {batch_idx + 1}/{total_batches} | Number of tags in batch: {len(batch_data)}')

    # Wait for all tasks in the queue to be completed
    task_queue.join()
    print('All batch processing tasks completed')

    # Send termination signal (None) to all worker threads
    for _ in range(max_workers):
        task_queue.put(None)

    # Wait for all worker threads to exit gracefully
    for thread in worker_threads:
        thread.join()
    print('All worker threads have exited')

    # Start unified data insertion after all API requests are done
    print('********** All SIS API requests completed. Starting unified data insertion **********')

    # Merge collected DataFrames and insert into GaussDB
    if collected_data:
        try:
            # Merge all non-empty DataFrames into one (ignore index to avoid duplication)
            merged_df = pd.concat(collected_data, ignore_index=True)
            if 'sis3-omitted' in merged_df.columns:
                del merged_df['sis3-omitted']
            print(f'Total number of records after merging: {len(merged_df)}')

            # Insert merged data into both real-time and historical tables
            insert_conn = gaussdb.GaussDB(**config.GAUSSDB_DWS)
            #print(merged_df)

            # Insert into real-time table (keep connection open after first insert)
            insert_conn.insert_data(
                merged_df,
                config.ODS_SIS_TABLE_NAME_RT,
                config.ODS_SIS_TABLE_RT_CONSTRAINT_KEYS
            )

            # Insert into historical table (close connection after insert)
            insert_conn.insert_data(
                merged_df,
                config.ODS_SIS_TABLE_NAME_HST,
                config.ODS_SIS_TABLE_HST_CONSTRAINT_KEYS
            )

        except Exception as merge_insert_err:
            print(f'Error during data merging or insertion: {merge_insert_err}')
            traceback.print_exc()
    else:
        print('No valid data collected from API requests. Skipping data insertion.')

    # Calculate and print total workflow execution time
    workflow_end_time = time.time()
    total_execution_time = workflow_end_time - workflow_start_time
    print(f'Total workflow execution time: {total_execution_time:.2f} seconds')

if __name__ == '__main__':
    # Create a task queue
    task_queue = Queue()
    date_now = datetime.now()
    main(current_update_time = date_now)

```

