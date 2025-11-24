```tex
Latest Version DEV
```

# ods

## 1.coss_ods.ods_iot_tmu_devinfo_minf

### create table

```sql
DROP TABLE IF EXISTS coss_ods.ods_iot_tmu_device_info_minf;

CREATE TABLE IF NOT EXISTS coss_ods.ods_iot_tmu_device_info_minf (
    device_code VARCHAR(200),
    device_name VARCHAR(200),
    sensor_id VARCHAR(200),
    sensor_name VARCHAR(200),
    sensor_unit VARCHAR(120),
    ods_update_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    ods_load_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    PRIMARY KEY (device_code)
);

COMMENT ON TABLE coss_ods.ods_iot_tmu_device_info_minf IS 'device info';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_device_info_minf.device_code IS 'device code';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_device_info_minf.device_name IS 'device name';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_device_info_minf.sensor_id IS 'sensorid';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_device_info_minf.sensor_name IS 'sensor name';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_device_info_minf.sensor_unit IS 'sensor unit';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_device_info_minf.ods_update_time IS 'ods update time';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_device_info_minf.ods_load_time IS 'ods load time';
```



## 2.ods_iot_tmu_more_dev_realtime_minf

### create table

```sql
DROP TABLE IF EXISTS coss_ods.ods_iot_tmu_more_dev_realtime_minf;

CREATE TABLE IF NOT EXISTS coss_ods.ods_iot_tmu_more_dev_realtime_minf (
    device_code VARCHAR(200),
    sensor_id VARCHAR(200),
    value DECIMAL(20,5),
    "time" BIGINT,
    ods_update_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    ods_load_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    PRIMARY KEY (device_code)
);

COMMENT ON TABLE coss_ods.ods_iot_tmu_more_dev_realtime_minf IS 'more device realtime';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_more_dev_realtime_minf.device_code IS 'device code';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_more_dev_realtime_minf.sensor_id IS 'sensor id';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_more_dev_realtime_minf.value IS 'sensor value';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_more_dev_realtime_minf."time" IS 'sensor time';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_more_dev_realtime_minf.ods_update_time IS 'ods update time';
COMMENT ON COLUMN coss_ods.ods_iot_tmu_more_dev_realtime_minf.ods_load_time IS 'ods load time';
```



# dwd

## 1.coss_dwd.dwd_tmu_more_dev_realtime_minf

### create table

```sql
DROP TABLE IF EXISTS coss_dwd.dwd_tmu_more_dev_realtime_minf;

CREATE TABLE IF NOT EXISTS coss_dwd.dwd_tmu_more_dev_realtime_minf (
    device_code VARCHAR(200),
    sensor_id VARCHAR(200),
    sensor_value DECIMAL(20,5),
    sensor_time TIMESTAMP(6),
    dwd_update_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    dwd_load_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    PRIMARY KEY (device_code)
);

COMMENT ON TABLE coss_dwd.dwd_tmu_more_dev_realtime_minf IS 'more device realtime';
COMMENT ON COLUMN coss_dwd.dwd_tmu_more_dev_realtime_minf.device_code IS 'device code';
COMMENT ON COLUMN coss_dwd.dwd_tmu_more_dev_realtime_minf.sensor_id IS 'sensor id';
COMMENT ON COLUMN coss_dwd.dwd_tmu_more_dev_realtime_minf.sensor_value IS 'sensor value';
COMMENT ON COLUMN coss_dwd.dwd_tmu_more_dev_realtime_minf.sensor_time IS 'sensor time';
COMMENT ON COLUMN coss_dwd.dwd_tmu_more_dev_realtime_minf.dwd_update_time IS 'dwd update time';
COMMENT ON COLUMN coss_dwd.dwd_tmu_more_dev_realtime_minf.dwd_load_time IS 'dwd load time';
```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Terminal User
-- function describe: Terminal User Monitoring For Meter
-- create         by: dongmaochen
-- create       date: 2025-11-13
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_ods.ods_iot_tmu_more_dev_realtime_minf
-- target table
-- coss_dwd.dwd_tmu_more_dev_realtime_minf
-- ****************************************************************************************
INSERT INTO coss_dwd.dwd_tmu_more_dev_realtime_minf (
    device_code,
    sensor_id,
    sensor_value,
    sensor_time,
    dwd_update_time,
    dwd_load_time
)
SELECT
    device_code AS device_code,
    sensor_id AS sensor_id,
    value AS sensor_value,
    TO_TIMESTAMP("time" / 1000) AS sensor_time,
    LOCALTIMESTAMP AS dwd_update_time,
    LOCALTIMESTAMP AS dwd_load_time
FROM coss_ods.ods_iot_tmu_more_dev_realtime_minf
ON DUPLICATE KEY update
    sensor_id = values(sensor_id),
    sensor_value = values(sensor_value),
    sensor_time = values(sensor_time),
    dwd_update_time = values(dwd_update_time)
```



# dim

## 1.coss_dim.dim_tmu_iot_device_info

### create table

```sql

DROP TABLE IF EXISTS coss_dim.dim_tmu_iot_device_info;
CREATE TABLE IF NOT EXISTS coss_dim.dim_tmu_iot_device_info (
    device_code VARCHAR(200),
    device_name VARCHAR(200),
    meter_type_code varchar(20),
    meter_type_desc varchar(100),
    premise_id varchar(110),
    serial_no varchar(16),
    rcv_date timestamp(6),
    region_abbr VARCHAR(30),
    sensor_id VARCHAR(200),
    sensor_name VARCHAR(200),
    sensor_unit VARCHAR(120),
    dim_update_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    dim_load_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    PRIMARY KEY (device_code)
);
COMMENT ON TABLE coss_dim.dim_tmu_iot_device_info IS 'device info';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.device_code      IS 'device code';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.device_name      IS 'device name';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.meter_type_code  IS 'meter type code';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.meter_type_desc  IS 'meter type desc ';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.premise_id       IS 'premise id';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.serial_no        IS 'serial no ';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.rcv_date         IS 'receive date';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.region_abbr      IS 'region abbr';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.sensor_id        IS 'sensorid';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.sensor_name      IS 'sensor name';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.sensor_unit      IS 'sensor unit';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.dim_update_time  IS 'dim update time';
COMMENT ON COLUMN coss_dim.dim_tmu_iot_device_info.dim_load_time    IS 'dim load time';
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
    localtimestamp dim_update_time,
    localtimestamp dim_load_time
from t_a t 
inner join coss_tmp.dim_tmu_iot_device_info_tmp_03 t1 on t.device_code = t1.device_code
```



# dm

## 1.coss_dm.dm_tmu_more_dev_realtime_minf

### create table

```sql
DROP TABLE IF EXISTS coss_dm.dm_tmu_more_dev_realtime_minf;

CREATE TABLE IF NOT EXISTS coss_dm.dm_tmu_more_dev_realtime_minf (
    device_code VARCHAR(200),
    device_name VARCHAR(200),
    meter_type_code varchar(20),
    meter_type_desc varchar(100),
    premise_id varchar(110),
    serial_no varchar(16),
    rcv_date timestamp(6),
    region_abbr VARCHAR(30),
    sensor_id VARCHAR(200),
    sensor_name VARCHAR(200),
    sensor_unit VARCHAR(120),
    sensor_value NUMERIC(20, 5),
    sensor_time TIMESTAMP(6),
    dm_update_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    dm_load_time TIMESTAMP(6) NULL DEFAULT pg_systimestamp(),
    primary key(device_code)
);

COMMENT ON TABLE coss_dm.dm_tmu_more_dev_realtime_minf IS 'more device realtime';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.device_code IS 'device code';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.device_name IS 'device name';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.meter_type_code  IS 'meter type code';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.meter_type_desc  IS 'meter type desc ';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.premise_id       IS 'premise id';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.serial_no        IS 'serial no ';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.rcv_date         IS 'receive date';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.region_abbr      IS 'region abbr';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.sensor_id IS 'sensorid';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.sensor_name IS 'sensor name';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.sensor_unit IS 'sensor unit';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.sensor_value IS 'sensor value';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.sensor_time IS 'sensor time';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.dm_update_time IS 'dm update time';
COMMENT ON COLUMN coss_dm.dm_tmu_more_dev_realtime_minf.dm_load_time IS 'dm load time';
```

### select sql

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
INSERT INTO coss_dm.dm_tmu_more_dev_realtime_minf (
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
SELECT
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
    LOCALTIMESTAMP AS dm_update_time,
    LOCALTIMESTAMP AS dm_load_time
FROM coss_dwd.dwd_tmu_more_dev_realtime_minf t
INNER JOIN coss_dim.dim_tmu_iot_device_info t1 
    ON t.device_code = t1.device_code 
    AND t.sensor_id = t1.sensor_id
ON DUPLICATE KEY update
    sensor_id    = values(sensor_id),
    sensor_name  = values(sensor_name),
    sensor_unit  = values(sensor_unit),
    sensor_value = values(sensor_value),
    sensor_time  = values(sensor_time),
    dm_update_time = values(dm_update_time)
```



# python code 

## 1.ods_iot_tmu_devinfo_minf

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
    target_table = 'coss_ods.ods_iot_tmu_device_info_minf'
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

## 2.ods_iot_tmu_more_dev_realtime_minf

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
    target_table = 'coss_ods.ods_iot_tmu_more_dev_realtime_minf'
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
    localtimestamp dim_update_time,
    localtimestamp dim_load_time
from t_a t 
inner join coss_tmp.dim_tmu_iot_device_info_tmp_03 t1 on t.device_code = t1.device_code



insert into coss_dim.dim_tmu_iot_device_info select * from coss_tmp.dim_tmu_iot_device_info_tmp_04

```

