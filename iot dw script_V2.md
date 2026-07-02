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

## ods_iot_extract_device_realtime_min（调度）

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

## ods_iot_extract_device_info_day(调度)

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



## ods_iot_extract_sensor_realtime_min(调度)

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

