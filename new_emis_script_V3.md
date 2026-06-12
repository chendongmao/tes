<center><h1>EMIS 数仓代码</h1></center>

```tex
==================================================================================
修改日期：250528
1. coss_dim.dim_wtw_installation_infoi 添加installation_id字段



==================================================================================
表结构修改情况:
1.coss_dm.dm_wtw_eng_cons_billing_hist_dip 表结构更新为：coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di
2.coss_dm.dm_psr_daily_ps_running_item_di  表结构更新为：coss_dm.dm_psr_monthly_ps_running_item_di
3.coss_dim.dim_ps_installation_info        该表未新增维度表
==================================================================================
数据更新情况:
1.公司opengaussdb 已经更新
2.HK DEV 已经更新
==================================================================================
指标更新情况：
1.抽水站、滤水厂二级页面的 kwh/cum 修改未 kwh/ML  指标数据还已修改
==================================================================================
双周会修改新增表：
1.coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di
2.coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di
3.coss_dim.dim_wtw_installation_info
==================================================================================
EMIS接口抽取数据后数仓代码250916：（数据抽取到dev）
1. 调用emis接口需要在10.66.169.48,在该台window service 调试接口代码
2. 在10.66.168.253 window service 通过MobaXterm 登录dp服务器10.66.169.236执行调度，代码文件为：/opt/app/coss/emis/
目前存在问题：
1. 新版本的指标删除IT_PS_000029，将其合并到IT_PS_000019
2. coss_dm.dm_psr_monthly_ps_running_item_di 更新了2024年后的数据在帆软页面上无法展示
==================================================================================
EMIS接口抽取数据后数仓代码250916：（数据抽取到PRE）
10.66.168.253 window service(开发机器)
10.66.168.212 pre dp
10.66.168.11 pre dp
10.66.168.85 pre dp
https://wiki.sis2.wsd.gov/ems/webresources/reports?loc_id=24&from=2023-01-01&to=2023-02-28
10.66.168.11 tiaoshejiqi
wsd_admin
Wsd@CLOUD9!
==================================================================================
1.预生产AI优化了接口代码
==================================================================================
已修改的环境： 公司 PRE IUAT ISIT DEV
1.建表语句（coss_ods.ods_emis_report_di_year）是否有必要全部是text类型
2.表coss_dm.dm_psr_daily_ps_running_item_di无主键
==================================================================================
用家comment,把原水、抽水站、滤水厂部分监测指标改为KPI
已更新环境：PRE ISIT IUAT DEV 公司
1.更新 coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di 表
2.更新 coss_dm.dm_psr_monthly_ps_running_item_di 表
==================================================================================
用家comment,把原水、抽水站、滤水厂部分监测指标改为KPI,修改维度表
已更新环境：PRE ISIT IUAT DEV 公司
1.更新coss_dim.dim_wtw_installation_info
2.更新coss_dim.dim_ps_installation_info
```

# ods

## ods_emis_extract_report_bills_day(调度任务)

### 1.coss_ods.ods_emis_psr_bills_di_year

#### create table

```sql
drop table if exists coss_ods.ods_emis_psr_bills_di_year;
create table if not exists coss_ods.ods_emis_psr_bills_di_year (
    asset_name varchar(255) null,
    asset_id int4 null,
    bill_date varchar(50) null,
    traiff varchar(255) null,
    traiff_desc varchar(255) null,
    on_peak_kwh numeric(15, 5) null,
    off_peak_kwh numeric(15, 5) null,
    on_peak_kva numeric(15, 5) null,
    off_peak_kva numeric(15, 5) null,
    bill_amount numeric(15, 5) null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    primary key(asset_id, bill_date)
)
with (
    orientation=row,
    compression=no
)
distribute by hash(asset_id)
partition by range (ods_update_time) (
    partition yr_2005 values less than ('2006-01-01 00:00:00'),
    partition yr_2006 values less than ('2007-01-01 00:00:00'),
    partition yr_2007 values less than ('2008-01-01 00:00:00'),
    partition yr_2008 values less than ('2009-01-01 00:00:00'),
    partition yr_2009 values less than ('2010-01-01 00:00:00'),
    partition yr_2010 values less than ('2011-01-01 00:00:00'),
    partition yr_2011 values less than ('2012-01-01 00:00:00'),
    partition yr_2012 values less than ('2013-01-01 00:00:00'),
    partition yr_2013 values less than ('2014-01-01 00:00:00'),
    partition yr_2014 values less than ('2015-01-01 00:00:00'),
    partition yr_2015 values less than ('2016-01-01 00:00:00'),
    partition yr_2016 values less than ('2017-01-01 00:00:00'),
    partition yr_2017 values less than ('2018-01-01 00:00:00'),
    partition yr_2018 values less than ('2019-01-01 00:00:00'),
    partition yr_2019 values less than ('2020-01-01 00:00:00'),
    partition yr_2020 values less than ('2021-01-01 00:00:00'),
    partition yr_2021 values less than ('2022-01-01 00:00:00'),
    partition yr_2022 values less than ('2023-01-01 00:00:00'),
    partition yr_2023 values less than ('2024-01-01 00:00:00'),
    partition yr_2024 values less than ('2025-01-01 00:00:00'),
    partition yr_2025 values less than ('2026-01-01 00:00:00'),
    partition yr_2026 values less than ('2027-01-01 00:00:00'),
    partition yr_future values less than ('9999-01-01 00:00:00')
);

comment on table coss_ods.ods_emis_psr_bills_di_year is 'Bills';
comment on column coss_ods.ods_emis_psr_bills_di_year.asset_name is 'Asset Name';
comment on column coss_ods.ods_emis_psr_bills_di_year.asset_id is 'Asset Id';
comment on column coss_ods.ods_emis_psr_bills_di_year.bill_date is 'Bill Date';
comment on column coss_ods.ods_emis_psr_bills_di_year.traiff is 'Traiff';
comment on column coss_ods.ods_emis_psr_bills_di_year.traiff_desc is 'Traiff Desc';
comment on column coss_ods.ods_emis_psr_bills_di_year.on_peak_kwh is 'On Peak Kwh';
comment on column coss_ods.ods_emis_psr_bills_di_year.off_peak_kwh is 'Off Peak Kwh';
comment on column coss_ods.ods_emis_psr_bills_di_year.on_peak_kva is 'On Peak Kva';
comment on column coss_ods.ods_emis_psr_bills_di_year.off_peak_kva is 'Off Peak Kva';
comment on column coss_ods.ods_emis_psr_bills_di_year.bill_amount is 'Bill Amount';
comment on column coss_ods.ods_emis_psr_bills_di_year.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_emis_psr_bills_di_year.ods_load_time is 'Ods Load Time';
```

#### interface shell

```shell

# Log storage directory
LOG_DIR="/opt/app/coss/emis/log/ods_emis_bills" 

# Create a log directory (if it doesn't exist)
mkdir -p "$LOG_DIR"

# Generate the current date in the format of YYYYMMDD
CURRENT_DATE=$(date +%Y%m%d)

# Log file name
LOG_FILE="${LOG_DIR}/ods_emis_bills_${CURRENT_DATE}.log"

# Run the Python program and redirect the output to the log file
python3 /opt/app/coss/emis/script/ods_emis_psr_bills_di_year.py ${bill_date} >> "$LOG_FILE" 2>&1

# Delete log files that exceed the specified number of days
find "$LOG_DIR" -name "*.log" -type f -mtime +90 -delete
```



### 2.coss_ods.ods_emis_psr_report_di_year

#### create table

```sql
drop table if exists coss_ods.ods_emis_psr_report_di_year;
create table if not exists coss_ods.ods_emis_psr_report_di_year (
    rpt_id varchar(100) null,
    asset_id int8 null,
    pump_num int8 null,
    cat_id varchar(100) null,
    cat_name varchar(255) null,
    drive_id varchar(100) null,
    drive_name text null,
    del_id varchar(100) null,
    del_name varchar(255) null,
    del__asset_id int8 null,
    design_flow varchar(255) null,
    run_hours float8 null,
    pump_qty float8 null,
    avg_suct float8 null,
    avg_del float8 null,
    design_flow_flag int4 null,
    run_hours_flag int4 null,
    pump_qty_flag int4 null,
    avg_suct_flag int4 null,
    avg_del_flag int4 null,
    dw_etl_time varchar(100) null,
    mh varchar(10) null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    primary key(asset_id, mh, del__asset_id, pump_num)
)
with (
    orientation=row,
    compression=no
)
distribute by hash(asset_id)
partition by range (ods_update_time) (
    partition yr_2005 values less than ('2006-01-01 00:00:00'),
    partition yr_2006 values less than ('2007-01-01 00:00:00'),
    partition yr_2007 values less than ('2008-01-01 00:00:00'),
    partition yr_2008 values less than ('2009-01-01 00:00:00'),
    partition yr_2009 values less than ('2010-01-01 00:00:00'),
    partition yr_2010 values less than ('2011-01-01 00:00:00'),
    partition yr_2011 values less than ('2012-01-01 00:00:00'),
    partition yr_2012 values less than ('2013-01-01 00:00:00'),
    partition yr_2013 values less than ('2014-01-01 00:00:00'),
    partition yr_2014 values less than ('2015-01-01 00:00:00'),
    partition yr_2015 values less than ('2016-01-01 00:00:00'),
    partition yr_2016 values less than ('2017-01-01 00:00:00'),
    partition yr_2017 values less than ('2018-01-01 00:00:00'),
    partition yr_2018 values less than ('2019-01-01 00:00:00'),
    partition yr_2019 values less than ('2020-01-01 00:00:00'),
    partition yr_2020 values less than ('2021-01-01 00:00:00'),
    partition yr_2021 values less than ('2022-01-01 00:00:00'),
    partition yr_2022 values less than ('2023-01-01 00:00:00'),
    partition yr_2023 values less than ('2024-01-01 00:00:00'),
    partition yr_2024 values less than ('2025-01-01 00:00:00'),
    partition yr_2025 values less than ('2026-01-01 00:00:00'),
    partition yr_2026 values less than ('2027-01-01 00:00:00'),
    partition yr_future values less than ('9999-01-01 00:00:00')
);

comment on table coss_ods.ods_emis_psr_report_di_year is 'Pump Report';
comment on column coss_ods.ods_emis_psr_report_di_year.rpt_id is 'Rpt Id';
comment on column coss_ods.ods_emis_psr_report_di_year.asset_id is 'Asset Id';
comment on column coss_ods.ods_emis_psr_report_di_year.pump_num is 'Pump Num';
comment on column coss_ods.ods_emis_psr_report_di_year.cat_id is 'Cat Id';
comment on column coss_ods.ods_emis_psr_report_di_year.cat_name is 'Cat Name';
comment on column coss_ods.ods_emis_psr_report_di_year.drive_id is 'Drive Id';
comment on column coss_ods.ods_emis_psr_report_di_year.drive_name is 'Drive Name';
comment on column coss_ods.ods_emis_psr_report_di_year.del_id is 'Del Id';
comment on column coss_ods.ods_emis_psr_report_di_year.del_name is 'Del Name';
comment on column coss_ods.ods_emis_psr_report_di_year.del__asset_id is 'Del Asset Id';
comment on column coss_ods.ods_emis_psr_report_di_year.design_flow is 'Design Flow';
comment on column coss_ods.ods_emis_psr_report_di_year.run_hours is 'Run Hours';
comment on column coss_ods.ods_emis_psr_report_di_year.pump_qty is 'Pump Qty';
comment on column coss_ods.ods_emis_psr_report_di_year.avg_suct is 'Avg Suct';
comment on column coss_ods.ods_emis_psr_report_di_year.avg_del is 'Avg Del';
comment on column coss_ods.ods_emis_psr_report_di_year.design_flow_flag is 'Design Flow Flag';
comment on column coss_ods.ods_emis_psr_report_di_year.run_hours_flag is 'Run Hours Flag';
comment on column coss_ods.ods_emis_psr_report_di_year.pump_qty_flag is 'Pump Qty Flag';
comment on column coss_ods.ods_emis_psr_report_di_year.avg_suct_flag is 'Avg Suct Flag';
comment on column coss_ods.ods_emis_psr_report_di_year.avg_del_flag is 'Avg Del Flag';
comment on column coss_ods.ods_emis_psr_report_di_year.dw_etl_time is 'Dw Etl Time';
comment on column coss_ods.ods_emis_psr_report_di_year.mh is 'Month';
comment on column coss_ods.ods_emis_psr_report_di_year.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_emis_psr_report_di_year.ods_load_time is 'Ods Load Time';
```

#### interface shell

```shell

# Log storage directory
LOG_DIR="/opt/app/coss/emis/log/ods_emis_report" 

# Create a log directory (if it doesn't exist)
mkdir -p "$LOG_DIR"

# Generate the current date in the format of YYYYMMDD
CURRENT_DATE=$(date +%Y%m%d)

# Log file name
LOG_FILE="${LOG_DIR}/ods_emis_report_${CURRENT_DATE}.log"

# Run the Python program and redirect the output to the log file
python3 /opt/app/coss/emis/script/ods_emis_psr_report_di_year.py ${mh1}  >> "$LOG_FILE" 2>&1

# Delete log files that exceed the specified number of days
find "$LOG_DIR" -name "*.log" -type f -mtime +90 -delete
```

## ods_emis_extract_assets_ related_day(调度任务)

### ods_emis_psr_assets_df

#### create table 

```shell
drop table if exists coss_ods.ods_emis_psr_assets_df;
create table coss_ods.ods_emis_psr_assets_df (
    id int8 not null,
    name varchar(255) null,
    description text null,
    loc_code varchar(50) null,
    account_no varchar(50) null,
    active bool null,
    official_name varchar(255) null,
    station_code varchar(50) null,
    billing_active bool null,
    installation_number varchar(50) null,
    region varchar(50) null,
    region_desc varchar(255) null,
    type varchar(50) null,
    type_desc varchar(255) null,
    ods_load_time timestamp(6) null default current_timestamp,
    ods_update_time timestamp(6) null default current_timestamp,
    primary key (id)
)
with (
    orientation=row,
    compression=no,
    storage_type=USTORE,
    segment=off
);

comment on table coss_ods.ods_emis_psr_assets_df is 'EMIS Asset Master Information';
comment on column coss_ods.ods_emis_psr_assets_df.id is 'Unique Asset ID';
comment on column coss_ods.ods_emis_psr_assets_df.name is 'Asset Name';
comment on column coss_ods.ods_emis_psr_assets_df.description is 'Asset Description';
comment on column coss_ods.ods_emis_psr_assets_df.loc_code is 'Location Code';
comment on column coss_ods.ods_emis_psr_assets_df.account_no is 'Account Number';
comment on column coss_ods.ods_emis_psr_assets_df.active is 'Asset Active Status';
comment on column coss_ods.ods_emis_psr_assets_df.official_name is 'Official Asset Name';
comment on column coss_ods.ods_emis_psr_assets_df.station_code is 'Station Code';
comment on column coss_ods.ods_emis_psr_assets_df.billing_active is 'Billing Active Status';
comment on column coss_ods.ods_emis_psr_assets_df.installation_number is 'Installation Number';
comment on column coss_ods.ods_emis_psr_assets_df.region is 'Region Code';
comment on column coss_ods.ods_emis_psr_assets_df.region_desc is 'Region Description';
comment on column coss_ods.ods_emis_psr_assets_df.type is 'Asset Type Code (FW/RW)';
comment on column coss_ods.ods_emis_psr_assets_df.type_desc is 'Asset Type Description';
comment on column coss_ods.ods_emis_psr_assets_df.ods_load_time is 'Data Load Time';
comment on column coss_ods.ods_emis_psr_assets_df.ods_update_time is 'Data Update Time';
```

#### interface shell

```shell
# Record start time
START_TIME=$(date +%s)

# Log directory
LOG_DIR="/opt/app/coss/emis/log/ods_emis_assets"
mkdir -p ${LOG_DIR}

# Current date for log file name
LOG_DATE=$(date +%Y%m%d)
LOG_FILE="${LOG_DIR}/ods_emis_assets_${LOG_DATE}.log"

# Python script path
SCRIPT_PATH="/opt/app/coss/emis/script/ods_emis_psr_assets_df.py"

echo "===== Start assets script execution =====" | tee -a ${LOG_FILE}

# Execute Python script
python3 ${SCRIPT_PATH} | tee -a ${LOG_FILE}

echo "===== Assets script execution completed =====" | tee -a ${LOG_FILE}

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

### ods_emis_psr_pumps_df

#### create table

```sql
drop table if exists coss_ods.ods_emis_psr_pumps_df;
create table coss_ods.ods_emis_psr_pumps_df (
    equipment_number varchar(50) not null,
    loc_id int8 null,
    location varchar(255) null,
    manufacturer varchar(255) null,
    designed_capacity float8 null,
    designed_stage int4 null,
    running_hours_to_overhaul int8 null,
    last_overhaul_date date null,
    suspend bool null,
    ods_load_time timestamp(6) null default current_timestamp,
    ods_update_time timestamp(6) null default current_timestamp,
    primary key(equipment_number,loc_id,location)
);
comment on table coss_ods.ods_emis_psr_pumps_df is 'EMIS Pump Equipment Information';
comment on column coss_ods.ods_emis_psr_pumps_df.equipment_number is 'Unique Equipment Number';
comment on column coss_ods.ods_emis_psr_pumps_df.loc_id is 'Related Asset ID (Refers to ods_emis_psr_assets_df.id)';
comment on column coss_ods.ods_emis_psr_pumps_df.location is 'Equipment Installation Location';
comment on column coss_ods.ods_emis_psr_pumps_df.manufacturer is 'Equipment Manufacturer';
comment on column coss_ods.ods_emis_psr_pumps_df.designed_capacity is 'Designed Capacity';
comment on column coss_ods.ods_emis_psr_pumps_df.designed_stage is 'Designed Stage';
comment on column coss_ods.ods_emis_psr_pumps_df.running_hours_to_overhaul is 'Running Hours Before Overhaul';
comment on column coss_ods.ods_emis_psr_pumps_df.last_overhaul_date is 'Last Overhaul Date';
comment on column coss_ods.ods_emis_psr_pumps_df.suspend is 'Equipment Suspended Status';
comment on column coss_ods.ods_emis_psr_pumps_df.ods_load_time is 'Data Load Time';
comment on column coss_ods.ods_emis_psr_pumps_df.ods_update_time is 'Data Update Time';
```

#### interface shell

```shell
# Record start time
START_TIME=$(date +%s)

# Log directory
LOG_DIR="/opt/app/coss/emis/log/ods_emis_pumps"
mkdir -p ${LOG_DIR}

# Current date for log file name
LOG_DATE=$(date +%Y%m%d)
LOG_FILE="${LOG_DIR}/ods_emis_pumps_${LOG_DATE}.log"

# Python script path
SCRIPT_PATH="/opt/app/coss/emis/script/ods_emis_psr_pumps_df.py"

echo "===== Start pumps script execution =====" | tee -a ${LOG_FILE}

# Execute Python script
python3 ${SCRIPT_PATH} | tee -a ${LOG_FILE}

echo "===== Pumps script execution completed =====" | tee -a ${LOG_FILE}

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

### ods_emis_psr_tagnames_df

#### create table

```sql
drop table if exists coss_ods.ods_emis_psr_tagnames_df;
create table coss_ods.ods_emis_psr_tagnames_df (
    id int8 not null,
    path text null,
    valid bool null,
    ods_load_time timestamp(6) null default current_timestamp,
    ods_update_time timestamp(6) null default current_timestamp,
    primary key (id,path)
)
with (
    orientation=row,
    compression=no,
    storage_type=USTORE,
    segment=off
);

comment on table coss_ods.ods_emis_psr_tagnames_df is 'Tag Information';
comment on column coss_ods.ods_emis_psr_tagnames_df.id is 'Unique Tag ID';
comment on column coss_ods.ods_emis_psr_tagnames_df.path is 'Full Tag Path';
comment on column coss_ods.ods_emis_psr_tagnames_df.valid is 'Tag Valid Status';
comment on column coss_ods.ods_emis_psr_tagnames_df.ods_load_time is 'Data Load Time';
comment on column coss_ods.ods_emis_psr_tagnames_df.ods_update_time is 'Data Update Time';
```

#### interface shell

```shell
# Record start time
START_TIME=$(date +%s)

# Log directory
LOG_DIR="/opt/app/coss/emis/log/ods_emis_tagnames"
mkdir -p ${LOG_DIR}

# Current date for log file name
LOG_DATE=$(date +%Y%m%d)
LOG_FILE="${LOG_DIR}/ods_emis_tagnames_${LOG_DATE}.log"

# Python script path
SCRIPT_PATH="/opt/app/coss/emis/script/ods_emis_psr_tagnames_df.py"

echo "===== Start tagnames script execution =====" | tee -a ${LOG_FILE}

# Execute Python script
python3 ${SCRIPT_PATH} | tee -a ${LOG_FILE}

echo "===== Tagnames script execution completed =====" | tee -a ${LOG_FILE}

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

## dwd_psr_etl_report_bill_day(调度任务)

### 1.coss_dwd.dwd_psr_billing_details_di_year

#### create table

```sql
drop table if exists coss_dwd.dwd_psr_billing_details_di_year;
create table if not exists coss_dwd.dwd_psr_billing_details_di_year(
    bill_date         timestamp(6),                            -- Bill Date
    asset_id          decimal(11),                             -- Asset Id
    tariff_id         decimal(11),                             -- Tariff Id
    tariff_name       varchar(150),                            -- Tariff Name
    tariff_desc       varchar(300),                            -- Tariff Description
    utility_id        decimal(11),                             -- Utility Id
    utility_name      varchar(150),                            -- Utility Name
    utility_desc      varchar(800),                            -- Utility Description
    kwh_on_peak       decimal(10,0),                           -- Power Consumption Of On Peak (kwh)
    kwh_off_peak      decimal(10,0),                           -- Power Consumption Of Off Peak (kwh)
    kva_on_peak       decimal(10,0),                           -- Capacity Of On Peak (kva)
    kva_off_peak      decimal(10,0),                           -- Capacity Of Off Peak (kva)
    flow_volume       decimal(20,5),                           -- Flow Volume
    avg_pressure      decimal(20,5),                           -- Average Pressure
    payout            decimal(10,0),                           -- Pay Out
    dwd_update_time   timestamp(6) default current_timestamp,  -- Data Update Time
    dwd_load_time     timestamp(6) default current_timestamp,  -- Data Loading Time
    mh                varchar(10),                             -- Billing Month
    primary key(asset_id, bill_date)                    
)
distribute by hash(asset_id)
partition by range (bill_date) (
    partition yr_2005 values less than ('2006-01-01 00:00:00'),
    partition yr_2006 values less than ('2007-01-01 00:00:00'),
    partition yr_2007 values less than ('2008-01-01 00:00:00'),
    partition yr_2008 values less than ('2009-01-01 00:00:00'),
    partition yr_2009 values less than ('2010-01-01 00:00:00'),
    partition yr_2010 values less than ('2011-01-01 00:00:00'),
    partition yr_2011 values less than ('2012-01-01 00:00:00'),
    partition yr_2012 values less than ('2013-01-01 00:00:00'),
    partition yr_2013 values less than ('2014-01-01 00:00:00'),
    partition yr_2014 values less than ('2015-01-01 00:00:00'),
    partition yr_2015 values less than ('2016-01-01 00:00:00'),
    partition yr_2016 values less than ('2017-01-01 00:00:00'),
    partition yr_2017 values less than ('2018-01-01 00:00:00'),
    partition yr_2018 values less than ('2019-01-01 00:00:00'),
    partition yr_2019 values less than ('2020-01-01 00:00:00'),
    partition yr_2020 values less than ('2021-01-01 00:00:00'),
    partition yr_2021 values less than ('2022-01-01 00:00:00'),
    partition yr_2022 values less than ('2023-01-01 00:00:00'),
    partition yr_2023 values less than ('2024-01-01 00:00:00'),
    partition yr_2024 values less than ('2025-01-01 00:00:00'),
    partition yr_2025 values less than ('2026-01-01 00:00:00'),
    partition yr_2026 values less than ('2027-01-01 00:00:00'),
    partition yr_future values less than ('9999-01-01 00:00:00')
);

comment on table coss_dwd.dwd_psr_billing_details_di_year is 'Pump Station Billing Details';
comment on column coss_dwd.dwd_psr_billing_details_di_year.bill_date is 'Bill Date';
comment on column coss_dwd.dwd_psr_billing_details_di_year.asset_id is 'Asset Id';
comment on column coss_dwd.dwd_psr_billing_details_di_year.tariff_id is 'Tariff Id';
comment on column coss_dwd.dwd_psr_billing_details_di_year.tariff_name is 'Tariff Name';
comment on column coss_dwd.dwd_psr_billing_details_di_year.tariff_desc is 'Tariff Description';
comment on column coss_dwd.dwd_psr_billing_details_di_year.utility_id is 'Utility Id';
comment on column coss_dwd.dwd_psr_billing_details_di_year.utility_name is 'Utility Name';
comment on column coss_dwd.dwd_psr_billing_details_di_year.utility_desc is 'Utility Description';
comment on column coss_dwd.dwd_psr_billing_details_di_year.kwh_on_peak is 'Power Consumption Of On Peak (kwh)';
comment on column coss_dwd.dwd_psr_billing_details_di_year.kwh_off_peak is 'Power Consumption Of Off Peak (kwh)';
comment on column coss_dwd.dwd_psr_billing_details_di_year.kva_on_peak is 'Capacity Of On Peak (kva)';
comment on column coss_dwd.dwd_psr_billing_details_di_year.kva_off_peak is 'Capacity Of Off Peak (kva)';
comment on column coss_dwd.dwd_psr_billing_details_di_year.flow_volume is 'Flow Volume';
comment on column coss_dwd.dwd_psr_billing_details_di_year.avg_pressure is 'Average Pressure';
comment on column coss_dwd.dwd_psr_billing_details_di_year.payout is 'Pay Out';
comment on column coss_dwd.dwd_psr_billing_details_di_year.dwd_update_time is 'Data Update Time';
comment on column coss_dwd.dwd_psr_billing_details_di_year.dwd_load_time is 'Data Loading Time';
comment on column coss_dwd.dwd_psr_billing_details_di_year.mh is 'Billing Month';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Bills
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_ods.ods_emis_bills_di_year
-- Target Table
-- coss_dwd.dwd_psr_billing_details_di_year
-- ****************************************************************************************
insert into coss_dwd.dwd_psr_billing_details_di_year
select
    bill_date                              as bill_date,           -- Bill Date
    asset_id                               as asset_id,            -- Asset Id
    null                                   as tariff_id,           -- Tariff Id
    traiff                                 as tariff_name,         -- Tariff Name
    traiff_desc                            as tariff_desc,         -- Tariff Description
    null                                   as utility_id,          -- Utility Id
    null                                   as utility_name,        -- Utility Name
    null                                   as utility_desc,        -- Utility Description
    on_peak_kwh                            as kwh_on_peak,         -- Power Consumption Of On Peak (kwh)
    off_peak_kwh                           as kwh_off_peak,        -- Power Consumption Of Off Peak (kwh)
    on_peak_kva                            as kva_on_peak,         -- Capacity Of On Peak (kva)
    off_peak_kva                           as kva_off_peak,        -- Capacity Of Off Peak (kva)
    null                                   as flow_volume,         -- Flow Volume
    null                                   as avg_pressure,        -- Average Pressure
    bill_amount                            as payout,              -- Pay Out
    localtimestamp                         as dwd_update_time,     -- Data Update Time
    localtimestamp                         as dwd_load_time,       -- Data Loading Time
    to_char(to_date(bill_date), 'yyyyMM')  as mh                   -- Billing Month
from
    coss_ods.ods_emis_bills_di_year
where ods_update_time >= ${dwd_update_time}
on duplicate key update
    tariff_id = values(tariff_id),
    tariff_name = values(tariff_name),
    tariff_desc = values(tariff_desc),
    utility_id = values(utility_id),
    utility_name = values(utility_name),
    utility_desc = values(utility_desc),
    kwh_on_peak = values(kwh_on_peak),
    kwh_off_peak = values(kwh_off_peak),
    kva_on_peak = values(kva_on_peak),
    kva_off_peak = values(kva_off_peak),
    flow_volume = values(flow_volume),
    avg_pressure = values(avg_pressure),
    payout = values(payout),
    dwd_update_time = values(dwd_update_time),
    mh = values(mh);
```



### 2.coss_dwd.dwd_psr_pump_running_details_di_year

#### create table

```sql
drop table if exists coss_dwd.dwd_psr_pump_running_details_di_year;
create table if not exists coss_dwd.dwd_psr_pump_running_details_di_year(
    asset_id           decimal(11),                            -- Assert Id
    pump_num           decimal(11),                            -- Pump Number
    cat_id             decimal(11),                            -- Category Id
    cat_name           varchar(150),                           -- Category Name
    drive_id           decimal(11),                            -- Drive Id
    drive_name         varchar(150),                           -- Drive Name
    del_id             decimal(11),                            -- Delivery To Id
    del_name           varchar(600),                           -- Delivery To Name
    del_asset_id       decimal(11),                            -- Delivery To Asset Id
    design_flow        decimal(20,5),                          -- Flow Rate Design
    run_hours          decimal(20,5),                          -- Hours Run This Month
    pump_qty           decimal(20,5),                          -- Water Pumped This Month
    avg_suct           decimal(20,5),                          -- Average Head Suction
    avg_del            decimal(20,5),                          -- Average Head Delivery
    design_flow_flag   decimal(11),                            -- Flow Rate Design Flag
    run_hours_flag     decimal(11),                            -- Hours Run This Month Flag
    pump_qty_flag      decimal(11),                            -- Water Pumped This Month Flag
    avg_suct_flag      decimal(11),                            -- Average Head Suction Flag
    avg_del_flag       decimal(11),                            -- Average Head Delivery Flag
    rpt_date           timestamp(6),                           -- Report Date
    mh                 varchar(10),                            -- Report Month
    dwd_update_time    timestamp(6) default current_timestamp, -- Data Update Time
    dwd_load_time      timestamp(6) default current_timestamp, -- Data Loading Time
    primary key(asset_id, mh, pump_num, del_asset_id)          
)
distribute by hash(asset_id)
partition by range (rpt_date) (
    partition yr_2005 values less than ('2006-01-01 00:00:00'),
    partition yr_2006 values less than ('2007-01-01 00:00:00'),
    partition yr_2007 values less than ('2008-01-01 00:00:00'),
    partition yr_2008 values less than ('2009-01-01 00:00:00'),
    partition yr_2009 values less than ('2010-01-01 00:00:00'),
    partition yr_2010 values less than ('2011-01-01 00:00:00'),
    partition yr_2011 values less than ('2012-01-01 00:00:00'),
    partition yr_2012 values less than ('2013-01-01 00:00:00'),
    partition yr_2013 values less than ('2014-01-01 00:00:00'),
    partition yr_2014 values less than ('2015-01-01 00:00:00'),
    partition yr_2015 values less than ('2016-01-01 00:00:00'),
    partition yr_2016 values less than ('2017-01-01 00:00:00'),
    partition yr_2017 values less than ('2018-01-01 00:00:00'),
    partition yr_2018 values less than ('2019-01-01 00:00:00'),
    partition yr_2019 values less than ('2020-01-01 00:00:00'),
    partition yr_2020 values less than ('2021-01-01 00:00:00'),
    partition yr_2021 values less than ('2022-01-01 00:00:00'),
    partition yr_2022 values less than ('2023-01-01 00:00:00'),
    partition yr_2023 values less than ('2024-01-01 00:00:00'),
    partition yr_2024 values less than ('2025-01-01 00:00:00'),
    partition yr_2025 values less than ('2026-01-01 00:00:00'),
    partition yr_2026 values less than ('2027-01-01 00:00:00'),
    partition yr_future values less than ('9999-01-01 00:00:00')
);

comment on table coss_dwd.dwd_psr_pump_running_details_di_year is 'Pump Station Billing Details';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.asset_id is 'Assert Id';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.pump_num is 'Pump Number';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.cat_id is 'Category Id';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.cat_name is 'Category Name';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.drive_id is 'Drive Id';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.drive_name is 'Drive Name';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.del_id is 'Delivery To Id';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.del_name is 'Delivery To Name';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.del_asset_id is 'Delivery To Asset Id';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.design_flow is 'Flow Rate Design';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.run_hours is 'Hours Run This Month';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.pump_qty is 'Water Pumped This Month';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.avg_suct is 'Average Head Suction';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.avg_del is 'Average Head Delivery';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.design_flow_flag is 'Flow Rate Design Flag';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.run_hours_flag is 'Hours Run This Month Flag';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.pump_qty_flag is 'Water Pumped This Month Flag';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.avg_suct_flag is 'Average Head Suction Flag';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.avg_del_flag is 'Average Head Delivery Flag';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.rpt_date is 'Report Date';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.mh is 'Report Month';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.dwd_update_time is 'Data Update Time';
comment on column coss_dwd.dwd_psr_pump_running_details_di_year.dwd_load_time is 'Data Loading Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Details
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_ods.ods_emis_psr_report_di_year
-- Target Table
-- coss_dwd.dwd_psr_pump_running_details_di_year
-- ****************************************************************************************
insert into coss_dwd.dwd_psr_pump_running_details_di_year
select
    asset_id                as asset_id,          -- Assert Id
    pump_num                as pump_num,          -- Pump Number
    null                    as cat_id,            -- Category Id
    cat_name                as cat_name,          -- Category Name
    null                    as drive_id,          -- Drive Id
    drive_name              as drive_name,        -- Drive Name
    null                    as del_id,            -- Delivery To Id
    del_name                as del_name,          -- Delivery To Name
    del__asset_id           as del_asset_id,      -- Delivery To Asset Id
    null                    as design_flow,       -- Flow Rate Design
    run_hours               as run_hours,         -- Hours Run This Month
    pump_qty                as pump_qty,          -- Water Pumped This Month
    avg_suct                as avg_suct,          -- Average Head Suction
    avg_del                 as avg_del,           -- Average Head Delivery
    null                    as design_flow_flag,  -- Flow Rate Design Flag
    null                    as run_hours_flag,    -- Hours Run This Month Flag
    null                    as pump_qty_flag,     -- Water Pumped This Month Flag
    null                    as avg_suct_flag,     -- Average Head Suction Flag
    null                    as avg_del_flag,      -- Average Head Delivery Flag
    to_date(mh, 'yyyyMM')   as rpt_date,          -- Report Date
    mh                      as mh,                -- Report Month
    localtimestamp          as dwd_update_time,   -- Data Update Time
    localtimestamp          as dwd_load_time      -- Data Loading Time
from
    coss_ods.ods_emis_psr_report_di_year
where ods_update_time>=${dwd_update_time}
on duplicate key update
    cat_id = values(cat_id),
    cat_name = values(cat_name),
    drive_id = values(drive_id),
    drive_name = values(drive_name),
    del_id = values(del_id),
    del_name = values(del_name),
    design_flow = values(design_flow),
    run_hours = values(run_hours),
    pump_qty = values(pump_qty),
    avg_suct = values(avg_suct),
    avg_del = values(avg_del),
    design_flow_flag = values(design_flow_flag),
    run_hours_flag = values(run_hours_flag),
    pump_qty_flag = values(pump_qty_flag),
    avg_suct_flag = values(avg_suct_flag),
    avg_del_flag = values(avg_del_flag),
    dwd_update_time = values(dwd_update_time);
```



# dws

## dws_psr_etl_report_bill_day（调度任务）

### 1.coss_dws.dws_psr_eng_cons_billing_details_di_year

#### create table

```sql
drop table if exists coss_dws.dws_psr_eng_cons_billing_details_di_year;
create table if not exists coss_dws.dws_psr_eng_cons_billing_details_di_year(
    asset_id            decimal(11),          -- Asset Id
    asset_name         varchar(120),         -- Asset Name
    asset_desc         varchar(120),         -- Asset Description
    loca_code          varchar(15),          -- Location Code
    acc_no             varchar(120),         -- Account No
    region_id          decimal(11),          -- Region Id
    region_code        varchar(150),         -- Region Code
    region_desc        varchar(800),         -- Region Description
    i_type_id          decimal(11),          -- Installation Type Id
    i_type_code        varchar(150),         -- Installation Type Code
    i_type_desc        varchar(150),         -- Installation Type  Description
    fw_portion         decimal(20,5),        -- Fresh Portion
    sw_portion         decimal(20,5),        -- Salt Water Portion
    rw_portion         decimal(20,5),        -- Raw Water Portion
    tw_portion         decimal(20,5),        -- Treatment Works Portion
    remarks            varchar(120),         -- Remarks
    is_active          decimal(5),           -- Is Active
    official_name      varchar(120),         -- Official Name
    station_code       varchar(120),         -- Station Code
    is_billing         decimal(5),           -- Billing Is Active
    is_ps              decimal(5),           -- Pump Station Is Active
    is_ecw             decimal(5),           -- Ecw Is Active
    region_rpt         varchar(150),         -- Region Report
    is_hkp             decimal(5),           -- Hkp Is Active
    is_fy              decimal(5),           -- Fy Is Active
    is_water_eff       decimal(5),           -- Water Efficiency Is Active
    water_eff_type_id  decimal(11),          -- Installation Type Id For Water Efficiency
    i_num              varchar(30),          -- Installation Number
    bill_date          timestamp(6),         -- Bill Date
    tariff_id          decimal(11),          -- Tariff Id
    tariff_name        varchar(150),         -- Tariff Name
    tariff_desc        varchar(300),         -- Tariff Description
    utility_id         decimal(11),          -- Utility Id
    utility_name       varchar(150),         -- Utility Name
    utility_desc       varchar(800),         -- Utility Description
    kwh_on_peak        decimal(10,0),        -- Power Consumption Of On Peak (kwh)
    kwh_off_peak       decimal(10,0),        -- Power Consumption Of Off Peak (kwh)
    kva_on_peak        decimal(10,0),        -- Capacity Of On Peak (kva)
    kva_off_peak       decimal(10,0),        -- Capacity Of Off Peak (kva)
    flow_volume        decimal(20,5),        -- Flow Volume
    avg_pressure       decimal(20,5),        -- Average Pressure
    payout             decimal(10,0),        -- Pay Out
    total_kwh          decimal(10,0),        -- Power Consumption Of On Peak (kwh)
    pump_qty           decimal(20,5),        -- Water Pumped This Month
    mh                 varchar(10),          -- Billing Date
    dws_update_time    timestamp(6) default current_timestamp, -- Data Update Time
    dws_load_time      timestamp(6) default current_timestamp, -- Data Loading Time
    primary key(asset_id, bill_date)
)
distribute by hash(asset_id)
partition by range (bill_date) (
    partition yr_2005 values less than ('2006-01-01 00:00:00'),
    partition yr_2006 values less than ('2007-01-01 00:00:00'),
    partition yr_2007 values less than ('2008-01-01 00:00:00'),
    partition yr_2008 values less than ('2009-01-01 00:00:00'),
    partition yr_2009 values less than ('2010-01-01 00:00:00'),
    partition yr_2010 values less than ('2011-01-01 00:00:00'),
    partition yr_2011 values less than ('2012-01-01 00:00:00'),
    partition yr_2012 values less than ('2013-01-01 00:00:00'),
    partition yr_2013 values less than ('2014-01-01 00:00:00'),
    partition yr_2014 values less than ('2015-01-01 00:00:00'),
    partition yr_2015 values less than ('2016-01-01 00:00:00'),
    partition yr_2016 values less than ('2017-01-01 00:00:00'),
    partition yr_2017 values less than ('2018-01-01 00:00:00'),
    partition yr_2018 values less than ('2019-01-01 00:00:00'),
    partition yr_2019 values less than ('2020-01-01 00:00:00'),
    partition yr_2020 values less than ('2021-01-01 00:00:00'),
    partition yr_2021 values less than ('2022-01-01 00:00:00'),
    partition yr_2022 values less than ('2023-01-01 00:00:00'),
    partition yr_2023 values less than ('2024-01-01 00:00:00'),
    partition yr_2024 values less than ('2025-01-01 00:00:00'),
    partition yr_2025 values less than ('2026-01-01 00:00:00'),
    partition yr_2026 values less than ('2027-01-01 00:00:00'),
    partition yr_future values less than ('9999-01-01 00:00:00')
);

comment on table coss_dws.dws_psr_eng_cons_billing_details_di_year is 'Pump Station Running Billing Details';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.asset_id is 'Asset Id';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.asset_name is 'Asset Name';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.asset_desc is 'Asset Description';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.loca_code is 'Location Code';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.acc_no is 'Account No';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.region_id is 'Region Id';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.region_code is 'Region Code';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.region_desc is 'Region Description';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.i_type_id is 'Installation Type Id';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.i_type_code is 'Installation Type Code';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.i_type_desc is 'Installation Type  Description';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.fw_portion is 'Fresh Portion';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.sw_portion is 'Salt Water Portion';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.rw_portion is 'Raw Water Portion';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.tw_portion is 'Treatment Works Portion';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.remarks is 'Remarks';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.is_active is 'Is Active';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.official_name is 'Official Name';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.station_code is 'Station Code';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.is_billing is 'Billing Is Active';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.is_ps is 'Pump Station Is Active';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.is_ecw is 'Ecw Is Active';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.region_rpt is 'Region Report';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.is_hkp is 'Hkp Is Active';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.is_fy is 'Fy Is Active';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.is_water_eff is 'Water Efficiency Is Active';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.water_eff_type_id is 'Installation Type Id For Water Efficiency';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.i_num is 'Installation Number';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.bill_date is 'Bill Date';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.tariff_id is 'Tariff Id';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.tariff_name is 'Tariff Name';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.tariff_desc is 'Tariff Description';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.utility_id is 'Utility Id';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.utility_name is 'Utility Name';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.utility_desc is 'Utility Description';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.kwh_on_peak is 'Power Consumption Of On Peak (kwh)';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.kwh_off_peak is 'Power Consumption Of Off Peak (kwh)';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.kva_on_peak is 'Capacity Of On Peak (kva)';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.kva_off_peak is 'Capacity Of Off Peak (kva)';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.flow_volume is 'Flow Volume';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.avg_pressure is 'Average Pressure';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.payout is 'Pay Out';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.total_kwh is 'Power Consumption Of On Peak (kwh)';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.pump_qty is 'Water Pumped This Month';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.mh is 'Billing Date';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.dws_update_time is 'Data Update Time';
comment on column coss_dws.dws_psr_eng_cons_billing_details_di_year.dws_load_time is 'Data Loading Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Details
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dwd.dwd_psr_billing_details_di_year
-- coss_dim.dim_ass_energy_cons_installation_df
-- coss_dwd.dwd_psr_pump_running_details_di_year
-- Target Table
-- coss_dws.dws_psr_eng_cons_billing_details_di_year
-- ****************************************************************************************
insert into coss_dws.dws_psr_eng_cons_billing_details_di_year
select
    t1.asset_id                     as asset_id,           -- Asset Id
    t1.asset_name                  as asset_name,         -- Asset Name
    t1.asset_desc                  as asset_desc,         -- Asset Description
    t1.loca_code                   as loca_code,          -- Location Code
    t1.acc_no                      as acc_no,             -- Account No
    t1.region_id                   as region_id,          -- Region Id
    t1.region_code                 as region_code,        -- Region Code
    t1.region_desc                 as region_desc,        -- Region Description
    t1.i_type_id                   as i_type_id,          -- Installation Type Id
    t1.i_type_code                 as i_type_code,        -- Installation Type Code
    t1.i_type_desc                 as i_type_desc,        -- Installation Type  Description
    t1.fw_portion                  as fw_portion,         -- Fresh Portion
    t1.sw_portion                  as sw_portion,         -- Salt Water Portion
    t1.rw_portion                  as rw_portion,         -- Raw Water Portion
    t1.tw_portion                  as tw_portion,         -- Treatment Works Portion
    t1.remarks                     as remarks,            -- Remarks
    t1.is_active                   as is_active,          -- Is Active
    t1.official_name               as official_name,      -- Official Name
    t1.station_code                as station_code,       -- Station Code
    t1.is_billing                  as is_billing,         -- Billing Is Active
    t1.is_ps                       as is_ps,              -- Pump Station Is Active
    t1.is_ecw                      as is_ecw,             -- Ecw Is Active
    t1.region_rpt                  as region_rpt,         -- Region Report
    t1.is_hkp                      as is_hkp,             -- Hkp Is Active
    t1.is_fy                       as is_fy,              -- Fy Is Active
    t1.is_water_eff                as is_water_eff,       -- Water Efficiency Is Active
    t1.water_eff_type_id           as water_eff_type_id,  -- Installation Type Id For Water Efficiency
    t1.i_num                       as i_num,              -- Installation Number
    t.bill_date                    as bill_date,          -- Bill Date
    t.tariff_id                    as tariff_id,          -- Tariff Id
    t.tariff_name                  as tariff_name,        -- Tariff Name
    t.tariff_desc                  as tariff_desc,        -- Tariff Description
    t.utility_id                   as utility_id,         -- Utility Id
    t.utility_name                 as utility_name,       -- Utility Name
    t.utility_desc                 as utility_desc,       -- Utility Description
    t.kwh_on_peak                  as kwh_on_peak,        -- Power Consumption Of On Peak (kwh)
    t.kwh_off_peak                 as kwh_off_peak,       -- Power Consumption Of Off Peak (kwh)
    t.kva_on_peak                  as kva_on_peak,        -- Capacity Of On Peak (kva)
    t.kva_off_peak                 as kva_off_peak,       -- Capacity Of Off Peak (kva)
    t.flow_volume                  as flow_volume,        -- Flow Volume
    t.avg_pressure                 as avg_pressure,       -- Average Pressure
    t.payout                       as payout,             -- Pay Out
    t.kwh_on_peak + t.kwh_off_peak as total_kwh,          -- Power Consumption Of On Peak (kwh)
    t2.pump_qty                    as pump_qty,           -- Water Pumped This Month
    t.mh                           as mh,                 -- Partitions For Billing Date
    localtimestamp                 as dws_update_time,    -- Data Update Time
    localtimestamp                 as dws_load_time       -- Data Loading Time
from
    coss_dwd.dwd_psr_billing_details_di_year t
inner join
    coss_dim.dim_ass_energy_cons_installation_df t1 
    on t.asset_id = t1.asset_id
left join
    (
        select 
            mh, 
            asset_id, 
            sum(pump_qty) pump_qty 
        from 
            coss_dwd.dwd_psr_pump_running_details_di_year 
        group by 
            mh, 
            asset_id
    ) t2 
    on t.asset_id = t2.asset_id 
    and t.mh = t2.mh
where
    t1.asset_name like '%PS%'
    and lower(t1.asset_name) not like '%ceased%'
    and lower(t1.asset_name) not like '%decommissi%'
    and lower(t1.asset_name) not like '%TW%'
    and t.mh >= ${mh1}
    and t2.mh >= ${mh1}
on duplicate key update
    asset_name = values(asset_name),
    asset_desc = values(asset_desc),
    loca_code = values(loca_code),
    acc_no = values(acc_no),
    region_id = values(region_id),
    region_code = values(region_code),
    region_desc = values(region_desc),
    i_type_id = values(i_type_id),
    i_type_code = values(i_type_code),
    i_type_desc = values(i_type_desc),
    fw_portion = values(fw_portion),
    sw_portion = values(sw_portion),
    rw_portion = values(rw_portion),
    tw_portion = values(tw_portion),
    remarks = values(remarks),
    is_active = values(is_active),
    official_name = values(official_name),
    station_code = values(station_code),
    is_billing = values(is_billing),
    is_ps = values(is_ps),
    is_ecw = values(is_ecw),
    region_rpt = values(region_rpt),
    is_hkp = values(is_hkp),
    is_fy = values(is_fy),
    is_water_eff = values(is_water_eff),
    water_eff_type_id = values(water_eff_type_id),
    i_num = values(i_num),
    tariff_id = values(tariff_id),
    tariff_name = values(tariff_name),
    tariff_desc = values(tariff_desc),
    utility_id = values(utility_id),
    utility_name = values(utility_name),
    utility_desc = values(utility_desc),
    kwh_on_peak = values(kwh_on_peak),
    kwh_off_peak = values(kwh_off_peak),
    kva_on_peak = values(kva_on_peak),
    kva_off_peak = values(kva_off_peak),
    flow_volume = values(flow_volume),
    avg_pressure = values(avg_pressure),
    payout = values(payout),
    total_kwh = values(total_kwh),
    pump_qty = values(pump_qty),
    dws_update_time = values(dws_update_time);
```

## dws_wtw_etl_report_bill_day(调度任务)

### 1.coss_dws.dws_wtw_eng_cons_billing_details_di_year

#### create table

```sql
drop table if exists coss_dws.dws_wtw_eng_cons_billing_details_di_year;
create table if not exists coss_dws.dws_wtw_eng_cons_billing_details_di_year(
    asset_id            decimal(11),          -- Asset Id
    asset_name         varchar(120),         -- Asset Name
    asset_desc         varchar(120),         -- Asset Description
    loca_code          varchar(15),          -- Location Code
    acc_no             varchar(120),         -- Account No
    region_id          decimal(11),          -- Region Id
    region_code        varchar(150),         -- Region Code
    region_desc        varchar(800),         -- Region Description
    i_type_id          decimal(11),          -- Installation Type Id
    i_type_code        varchar(150),         -- Installation Type Code
    i_type_desc        varchar(150),         -- Installation Type  Description
    fw_portion         decimal(20,5),        -- Fresh Portion
    sw_portion         decimal(20,5),        -- Salt Water Portion
    rw_portion         decimal(20,5),        -- Raw Water Portion
    tw_portion         decimal(20,5),        -- Treatment Works Portion
    remarks            varchar(120),         -- Remarks
    is_active          decimal(5),           -- Is Active
    official_name      varchar(120),         -- Official Name
    station_code       varchar(120),         -- Station Code
    is_billing         decimal(5),           -- Billing Is Active
    is_ps              decimal(5),           -- Pump Station Is Active
    is_ecw             decimal(5),           -- Ecw Is Active
    region_rpt         varchar(150),         -- Region Report
    is_hkp             decimal(5),           -- Hkp Is Active
    is_fy              decimal(5),           -- Fy Is Active
    is_water_eff       decimal(5),           -- Water Efficiency Is Active
    water_eff_type_id  decimal(11),          -- Installation Type Id For Water Efficiency
    i_num              varchar(30),          -- Installation Number
    bill_date          timestamp(6),         -- Bill Date
    tariff_id          decimal(11),          -- Tariff Id
    tariff_name        varchar(150),         -- Tariff Name
    tariff_desc        varchar(300),         -- Tariff Description
    utility_id         decimal(11),          -- Utility Id
    utility_name       varchar(150),         -- Utility Name
    utility_desc       varchar(800),         -- Utility Description
    kwh_on_peak        decimal(10,0),        -- Power Consumption Of On Peak (kwh)
    kwh_off_peak       decimal(10,0),        -- Power Consumption Of Off Peak (kwh)
    kva_on_peak        decimal(10,0),        -- Capacity Of On Peak (kva)
    kva_off_peak       decimal(10,0),        -- Capacity Of Off Peak (kva)
    flow_volume        decimal(20,5),        -- Flow Volume
    avg_pressure       decimal(20,5),        -- Average Pressure
    payout             decimal(10,0),        -- Pay Out
    total_kwh          decimal(10,0),        -- Power Consumption Of On Peak (kwh)
    pump_qty           decimal(20,5),        -- Water Pumped This Month
    mh                 varchar(10),          -- Partitions For Billing Date
    dws_update_time    timestamp(6) default current_timestamp,
    dws_load_time      timestamp(6) default current_timestamp,
    primary key(asset_id, bill_date)
)
distribute by hash(asset_id)
partition by range (bill_date) (
    partition yr_2005 values less than ('2006-01-01 00:00:00'),
    partition yr_2006 values less than ('2007-01-01 00:00:00'),
    partition yr_2007 values less than ('2008-01-01 00:00:00'),
    partition yr_2008 values less than ('2009-01-01 00:00:00'),
    partition yr_2009 values less than ('2010-01-01 00:00:00'),
    partition yr_2010 values less than ('2011-01-01 00:00:00'),
    partition yr_2011 values less than ('2012-01-01 00:00:00'),
    partition yr_2012 values less than ('2013-01-01 00:00:00'),
    partition yr_2013 values less than ('2014-01-01 00:00:00'),
    partition yr_2014 values less than ('2015-01-01 00:00:00'),
    partition yr_2015 values less than ('2016-01-01 00:00:00'),
    partition yr_2016 values less than ('2017-01-01 00:00:00'),
    partition yr_2017 values less than ('2018-01-01 00:00:00'),
    partition yr_2018 values less than ('2019-01-01 00:00:00'),
    partition yr_2019 values less than ('2020-01-01 00:00:00'),
    partition yr_2020 values less than ('2021-01-01 00:00:00'),
    partition yr_2021 values less than ('2022-01-01 00:00:00'),
    partition yr_2022 values less than ('2023-01-01 00:00:00'),
    partition yr_2023 values less than ('2024-01-01 00:00:00'),
    partition yr_2024 values less than ('2025-01-01 00:00:00'),
    partition yr_2025 values less than ('2026-01-01 00:00:00'),
    partition yr_2026 values less than ('2027-01-01 00:00:00'),
    partition yr_future values less than ('9999-01-01 00:00:00')
);

comment on table coss_dws.dws_wtw_eng_cons_billing_details_di_year is 'Pump Station Running Billing Details';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.asset_id is 'Asset Id';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.asset_name is 'Asset Name';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.asset_desc is 'Asset Description';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.loca_code is 'Location Code';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.acc_no is 'Account No';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.region_id is 'Region Id';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.region_code is 'Region Code';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.region_desc is 'Region Description';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.i_type_id is 'Installation Type Id';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.i_type_code is 'Installation Type Code';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.i_type_desc is 'Installation Type  Description';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.fw_portion is 'Fresh Portion';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.sw_portion is 'Salt Water Portion';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.rw_portion is 'Raw Water Portion';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.tw_portion is 'Treatment Works Portion';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.remarks is 'Remarks';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.is_active is 'Is Active';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.official_name is 'Official Name';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.station_code is 'Station Code';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.is_billing is 'Billing Is Active';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.is_ps is 'Pump Station Is Active';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.is_ecw is 'Ecw Is Active';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.region_rpt is 'Region Report';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.is_hkp is 'Hkp Is Active';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.is_fy is 'Fy Is Active';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.is_water_eff is 'Water Efficiency Is Active';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.water_eff_type_id is 'Installation Type Id For Water Efficiency';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.i_num is 'Installation Number';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.bill_date is 'Bill Date';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.tariff_id is 'Tariff Id';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.tariff_name is 'Tariff Name';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.tariff_desc is 'Tariff Description';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.utility_id is 'Utility Id';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.utility_name is 'Utility Name';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.utility_desc is 'Utility Description';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.kwh_on_peak is 'Power Consumption Of On Peak (kwh)';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.kwh_off_peak is 'Power Consumption Of Off Peak (kwh)';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.kva_on_peak is 'Capacity Of On Peak (kva)';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.kva_off_peak is 'Capacity Of Off Peak (kva)';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.flow_volume is 'Flow Volume';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.avg_pressure is 'Average Pressure';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.payout is 'Pay Out';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.total_kwh is 'Power Consumption Of On Peak (kwh)';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.pump_qty is 'Water Pumped This Month';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.mh is 'Partitions For Billing Date';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.dws_update_time is 'Data Update Time';
comment on column coss_dws.dws_wtw_eng_cons_billing_details_di_year.dws_load_time is 'Data Loading Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Treatment Works
-- Function Describe: Water Treatment Works Bills Detail
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dwd.dwd_psr_billing_details_di_year
-- coss_dim.dim_ass_energy_cons_installation_df
-- coss_dwd.dwd_psr_pump_running_details_di_year
-- Target Table
-- coss_dws.dws_wtw_eng_cons_billing_details_di_year
-- ****************************************************************************************
insert into coss_dws.dws_wtw_eng_cons_billing_details_di_year
select
    t1.asset_id                     as asset_id,           -- Asset Id
    t1.asset_name                  as asset_name,         -- Asset Name
    t1.asset_desc                  as asset_desc,         -- Asset Description
    t1.loca_code                   as loca_code,          -- Location Code
    t1.acc_no                      as acc_no,             -- Account No
    t1.region_id                   as region_id,          -- Region Id
    t1.region_code                 as region_code,        -- Region Code
    t1.region_desc                 as region_desc,        -- Region Description
    t1.i_type_id                   as i_type_id,          -- Installation Type Id
    t1.i_type_code                 as i_type_code,        -- Installation Type Code
    t1.i_type_desc                 as i_type_desc,        -- Installation Type  Description
    t1.fw_portion                  as fw_portion,         -- Fresh Portion
    t1.sw_portion                  as sw_portion,         -- Salt Water Portion
    t1.rw_portion                  as rw_portion,         -- Raw Water Portion
    t1.tw_portion                  as tw_portion,         -- Treatment Works Portion
    t1.remarks                     as remarks,            -- Remarks
    t1.is_active                   as is_active,          -- Is Active
    t1.official_name               as official_name,      -- Official Name
    t1.station_code                as station_code,       -- Station Code
    t1.is_billing                  as is_billing,         -- Billing Is Active
    t1.is_ps                       as is_ps,              -- Pump Station Is Active
    t1.is_ecw                      as is_ecw,             -- Ecw Is Active
    t1.region_rpt                  as region_rpt,         -- Region Report
    t1.is_hkp                      as is_hkp,             -- Hkp Is Active
    t1.is_fy                       as is_fy,              -- Fy Is Active
    t1.is_water_eff                as is_water_eff,       -- Water Efficiency Is Active
    t1.water_eff_type_id           as water_eff_type_id,  -- Installation Type Id For Water Efficiency
    t1.i_num                       as i_num,              -- Installation Number
    t.bill_date                    as bill_date,          -- Bill Date
    t.tariff_id                    as tariff_id,          -- Tariff Id
    t.tariff_name                  as tariff_name,        -- Tariff Name
    t.tariff_desc                  as tariff_desc,        -- Tariff Description
    t.utility_id                   as utility_id,         -- Utility Id
    t.utility_name                 as utility_name,       -- Utility Name
    t.utility_desc                 as utility_desc,       -- Utility Description
    t.kwh_on_peak                  as kwh_on_peak,        -- Power Consumption Of On Peak (kwh)
    t.kwh_off_peak                 as kwh_off_peak,       -- Power Consumption Of Off Peak (kwh)
    t.kva_on_peak                  as kva_on_peak,        -- Capacity Of On Peak (kva)
    t.kva_off_peak                 as kva_off_peak,       -- Capacity Of Off Peak (kva)
    t.flow_volume                  as flow_volume,        -- Flow Volume
    t.avg_pressure                 as avg_pressure,       -- Average Pressure
    t.payout                       as payout,             -- Pay Out
    t.kwh_on_peak + t.kwh_off_peak as total_kwh,          -- Power Consumption Of On Peak (kwh)
    t2.pump_qty                    as pump_qty,           -- Water Pumped This Month
    t.mh                           as mh,                 -- Billing Date
    localtimestamp                 as dws_update_time,    -- Data Update Time
    localtimestamp                 as dws_load_time       -- Data Loading Time
from
    coss_dwd.dwd_psr_billing_details_di_year t
inner join
    coss_dim.dim_ass_energy_cons_installation_df t1 
    on t.asset_id = t1.asset_id
left join
    (
        select 
            mh, 
            asset_id, 
            sum(pump_qty) pump_qty 
        from 
            coss_dwd.dwd_psr_pump_running_details_di_year 
        group by 
            mh, 
            asset_id
    ) t2 
    on t.asset_id = t2.asset_id 
    and t.mh = t2.mh
where
    t1.asset_name like '%WTW%'
    and lower(t1.asset_name) not like '%ceased%'
    and lower(t1.asset_name) not like '%decommissi%'
    and t.mh >= ${mh1}
    and t2.mh >= ${mh1}
on duplicate key update
    asset_name = values(asset_name),
    asset_desc = values(asset_desc),
    loca_code = values(loca_code),
    acc_no = values(acc_no),
    region_id = values(region_id),
    region_code = values(region_code),
    region_desc = values(region_desc),
    i_type_id = values(i_type_id),
    i_type_code = values(i_type_code),
    i_type_desc = values(i_type_desc),
    fw_portion = values(fw_portion),
    sw_portion = values(sw_portion),
    rw_portion = values(rw_portion),
    tw_portion = values(tw_portion),
    remarks = values(remarks),
    is_active = values(is_active),
    official_name = values(official_name),
    station_code = values(station_code),
    is_billing = values(is_billing),
    is_ps = values(is_ps),
    is_ecw = values(is_ecw),
    region_rpt = values(region_rpt),
    is_hkp = values(is_hkp),
    is_fy = values(is_fy),
    is_water_eff = values(is_water_eff),
    water_eff_type_id = values(water_eff_type_id),
    i_num = values(i_num),
    tariff_id = values(tariff_id),
    tariff_name = values(tariff_name),
    tariff_desc = values(tariff_desc),
    utility_id = values(utility_id),
    utility_name = values(utility_name),
    utility_desc = values(utility_desc),
    kwh_on_peak = values(kwh_on_peak),
    kwh_off_peak = values(kwh_off_peak),
    kva_on_peak = values(kva_on_peak),
    kva_off_peak = values(kva_off_peak),
    flow_volume = values(flow_volume),
    avg_pressure = values(avg_pressure),
    payout = values(payout),
    total_kwh = values(total_kwh),
    pump_qty = values(pump_qty),
    dws_update_time = values(dws_update_time);
```

# dm

## dm_psr_etl_report_bill_day（调度任务）

### 1.coss_dm.dm_psr_annual_pump_station_item_di

#### create table

```sql
drop table if exists coss_dm.dm_psr_monthly_pump_station_item_di;
create table if not exists coss_dm.dm_psr_monthly_pump_station_item_di(
    id                           varchar(50),
    statistical_month            decimal(10,0),
    region_abbr                 varchar(120),
    inter_item_code             varchar(120),
    item_value                  decimal(20,5),
    dm_update_time              timestamp(6) default current_timestamp,
    dm_load_time                timestamp(6) default current_timestamp,
    primary key (statistical_month, region_abbr, inter_item_code)
)
with (orientation = row, compression = no)
distribute by hash(statistical_month, region_abbr);
comment on table coss_dm.dm_psr_monthly_pump_station_item_di is 'The Annual Pump Station items';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.id is 'Primary Key';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.statistical_month is 'Statistical Month';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.region_abbr is 'Regional Abbreviation';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.inter_item_code is 'Internal Item Code';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.item_value is 'Item Value';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.dm_update_time is 'Data Update Time';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.dm_load_time is 'Data Loading Time';
```

#### 1.1 累计抽水量和电耗量

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Details
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_psr_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_psr_annual_pump_station_item_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_psr_annual_pump_station_item_di_01;
create table if not exists coss_tmp.dm_psr_annual_pump_station_item_di_01(
    id                           varchar(50),
    statistical_year             decimal(10,0),
    region_abbr                 varchar(120),
    inter_item_code              varchar(120),
    item_value                   decimal(20,5),
    dm_update_time               timestamp(6) default current_timestamp,
    dm_load_time                 timestamp(6) default current_timestamp
);

with t_af as (
    select
        round(mh/100) as yr,
        region_rpt as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty  -- Convert ML To Mcm
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'FW'
       -- and mh >= ${mh1}
    group by
        yr,
        region_rpt
),
t_ar as (
    select
        round(mh/100) as yr,
        region_rpt as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty  -- Convert ML To Mcm
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'RW'
        -- and mh >= ${mh1}
    group by
        yr,
        region_rpt
),
t_as as (
    select
        round(mh/100) as yr,
        region_rpt as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty  -- Convert ML To Mcm
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'SW'
        -- and mh >= ${mh1}
    group by
        yr,
        region_rpt
),
t_afs as (
    select
        round(mh/100) as yr,
        region_rpt as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty  -- Convert ML To Mcm
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'Combine'
        -- and mh >= ${mh1}
    group by
        yr,
        region_rpt
),
t_bf as (
    select
        round(mh/100) as yr,
        'HKSAR' as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty  -- Convert ML To Mcm
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'FW'
        -- and mh >= ${mh1}
    group by
        yr
),
t_br as (
    select
        round(mh/100) as yr,
        'HKSAR' as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty  -- Convert ML To Mcm
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'RW'
        -- and mh >= ${mh1}
    group by
        yr
),
t_bs as (
    select
        round(mh/100) as yr,
        'HKSAR' as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty  -- Convert ML To Mcm
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'SW'
        -- and mh >= ${mh1}
    group by
        yr
),
t_bfs as (
    select
        round(mh/100) as yr,
        'HKSAR' as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty  -- Convert ML To Mcm
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'Combine'
        -- and mh >= ${mh1}
    group by
        yr
)
insert into coss_tmp.dm_psr_annual_pump_station_item_di_01
select
    id,
    yr as statistical_year,
    region as region_abbr,
    item_code as inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    (
        select
            uuid() as id,
            region as region,
            'IT_PS_000001' as item_code,
            '食水抽水站电耗量' as item_name_cn,
            '食水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Fresh Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_bf t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000001' as item_code,
            '食水抽水站电耗量' as item_name_cn,
            '食水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Fresh Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_af t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000002' as item_code,
            '原水抽水站电耗量' as item_name_cn,
            '原水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Raw Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_br t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000002' as item_code,
            '原水站电耗量' as item_name_cn,
            '原水食水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Raw Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_ar t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000003' as item_code,
            '海水抽水站电耗量' as item_name_cn,
            '海水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Salt Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_bs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000003' as item_code,
            '海水抽水站电耗量' as item_name_cn,
            '海水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Salt Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_as t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000005' as item_code,
            '其他(combine)抽水站电耗量' as item_name_cn,
            '其他(combine)抽水站電耗量' as item_name_tc,
            'Power Consumption Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_bfs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000005' as item_code,
            '其他(combine)抽水站电耗量' as item_name_cn,
            '其他(combine)抽水站電耗量' as item_name_tc,
            'Power Consumption Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_afs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000007' as item_code,
            '食水抽水站抽水量' as item_name_cn,
            '食水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Fresh Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_bf t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000007' as item_code,
            '食水抽水站抽水量' as item_name_cn,
            '食水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Fresh Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_af t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000008' as item_code,
            '原水抽水站抽水量' as item_name_cn,
            '原水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Raw Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_br t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000008' as item_code,
            '原水抽水站抽水量' as item_name_cn,
            '原水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Raw Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_ar t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000009' as item_code,
            '海水抽水站抽水量' as item_name_cn,
            '海水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Salt Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_bs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000009' as item_code,
            '海水抽水站抽水量' as item_name_cn,
            '海水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Salt Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_as t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000011' as item_code,
            '食水海水抽水站抽水量' as item_name_cn,
            '食水海水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_bfs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000011' as item_code,
            '食水海水抽水站抽水量' as item_name_cn,
            '食水海水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.yr as yr
        from
            t_afs t
    ) t_sub;

insert into coss_dm.dm_psr_annual_pump_station_item_di
select
    id,
    statistical_year,
    region_abbr,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    coss_tmp.dm_psr_annual_pump_station_item_di_01
on duplicate key update
    id = values(id),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time);
```

#### 1.2 吨水电耗

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Details
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_psr_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_psr_annual_pump_station_item_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_psr_annual_pump_station_item_di_01;
create table if not exists coss_tmp.dm_psr_annual_pump_station_item_di_01(
    id                           varchar(50),
    statistical_year             decimal(10,0),
    region_abbr                 varchar(120),
    inter_item_code              varchar(120),
    item_value                   decimal(20,5),
    dm_update_time               timestamp(6) default current_timestamp,
    dm_load_time                 timestamp(6) default current_timestamp
);

with t_af as (
    select
        round(mh/100) as yr,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where (i_type_code = 'FW')
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr,
        region_rpt
),
t_ar as (
    select
        round(mh/100) as yr,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where (i_type_code = 'RW')
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr,
        region_rpt
),
t_as as (
    select
        round(mh/100) as yr,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'SW'
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr,
        region_rpt
),
t_afs as (
    select
        round(mh/100) as yr,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'Combine'
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr,
        region_rpt
),
t_bf as (
    select
        round(mh/100) as yr,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where (i_type_code = 'FW'
        or i_type_code = 'RW')
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr
),
t_br as (
    select
        round(mh/100) as yr,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where (i_type_code = 'RW')
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr
),
t_bs as (
    select
        round(mh/100) as yr,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'SW'
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr
),
t_bfs as (
    select
        round(mh/100) as yr,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'Combine'
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr
)
insert into coss_tmp.dm_psr_annual_pump_station_item_di_01
select
    id,
    yr statistical_year,
    region region_abbr,
    item_code inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from (
    select
        uuid() as id,
        region as region,
        'IT_PS_000019' as item_code,
        '食水抽水站单位电耗' as item_name_cn,
        '食水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Pump Station' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_bf t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000019' as item_code,
        '食水抽水站单位电耗' as item_name_cn,
        '食水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Pump Station' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_af t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000020' as item_code,
        '原水抽水站单位电耗' as item_name_cn,
        '原水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Pump Station' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_br t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000020' as item_code,
        '原水抽水站单位电耗' as item_name_cn,
        '原水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Pump Station' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_ar t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000021' as item_code,
        '海水抽水站单位电耗' as item_name_cn,
        '海水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Salt Water Pumping Stations' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_bs t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000021' as item_code,
        '海水抽水站单位电耗' as item_name_cn,
        '海水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Salt Water Pumping Stations' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_as t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000023' as item_code,
        '食水海水抽水站单位电耗' as item_name_cn,
        '食水海水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit  Of Fresh&Salt Water Pumping Stations' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_bfs t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000023' as item_code,
        '食水海水抽水站单位电耗' as item_name_cn,
        '食水海水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Fresh&Salt Water Pumping Stations' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_afs t
);

insert into coss_dm.dm_psr_annual_pump_station_item_di
select
    id,
    statistical_year,
    region_abbr,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    coss_tmp.dm_psr_annual_pump_station_item_di_01
on duplicate key update
    id = values(id),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time);
```



#### 1.3 食水电耗量和吨水电耗量同比增长率{年离散计算}

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Details
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_psr_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_psr_annual_pump_station_item_di
-- ****************************************************************************************

drop table if exists coss_tmp.dm_psr_annual_pump_station_item_di_01;
create table if not exists coss_tmp.dm_psr_annual_pump_station_item_di_01(
    id                           varchar(50),
    statistical_year             decimal(10,0),
    region_abbr                 varchar(120),
    inter_item_code              varchar(120),
    item_value                   decimal(20,5),
    dm_update_time               timestamp(6) default current_timestamp,
    dm_load_time                 timestamp(6) default current_timestamp
);

with t_af as (
    select
        round(mh/100) as yr,
        region_rpt region,
        sum(total_kwh) total_kwh,
        sum(pump_qty)/1000 pump_qty  -- convert ML to mcm
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'FW'
        -- and round(mh/100, 0) = round(${mh1}/100, 0)
        -- or mh in (select distinct mh-100 mh from coss_dws.dws_wtw_eng_cons_billing_details_di_year where round(mh/100, 0) = round(${mh1}/100, 0))
    group by
        yr,
        region_rpt
),
t_bf as (
    select
        round(mh/100) as yr,
        'HKSAR' region,
        sum(total_kwh) total_kwh,
        sum(pump_qty)/1000 pump_qty  -- convert ML to mcm
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'FW'
        -- and round(mh/100, 0) = round(${mh1}/100, 0)
        -- or mh in (select distinct mh-100 mh from coss_dws.dws_wtw_eng_cons_billing_details_di_year where round(mh/100, 0) = round(${mh1}/100, 0))
    group by
        yr
)
insert into coss_tmp.dm_psr_annual_pump_station_item_di_01
select
    id,
    yr statistical_year,
    region region_abbr,
    item_code inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from (
    select
        uuid() as id,
        t.region as region,
        'IT_PS_000030' as item_code,
        '食水抽水站kwh/Ml同比整张率' as item_name_cn,
        '食水抽水站kwh/Ml年比成長率' as item_name_tc,
        'Year on Year Growth Rate Of Power Consumption kwh/Ml Of Fresh Water Pumping Stations' as item_name_en,
        ((t.total_kwh/(t.pump_qty*1000)) - (t1.total_kwh/(t1.pump_qty*1000)))/(t1.total_kwh/(t1.pump_qty*1000)) * 100 as item_value,  -- convert pump_qty mcm to Ml
        '%' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_bf t
        left join t_bf t1 on t.region = t1.region and t.yr = t1.yr+1
    where t.pump_qty is not null
        and t.pump_qty != 0
        and t1.pump_qty is not null
        and t1.pump_qty != 0
        and t.yr = round(${mh1}/100, 0)

    union all
    select
        uuid() as id,
        t.region as region,
        'IT_PS_000030' as item_code,
        '食水抽水站kwh/Ml同比整张率' as item_name_cn,
        '食水抽水站kwh/Ml年比成長率' as item_name_tc,
        'Year on Year Growth Rate Of Power Consumption kwh/Ml Of Fresh Water Pumping Stations' as item_name_en,
        ((t.total_kwh/(t.pump_qty*1000)) - (t1.total_kwh/(t1.pump_qty*1000)))/(t1.total_kwh/(t1.pump_qty*1000)) * 100 as item_value,  -- convert pump_qty mcm to Ml
        '%' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_af t
        left join t_af t1 on t.region = t1.region and t.yr = t1.yr+1
    where t.pump_qty is not null
        and t.pump_qty != 0
        and t1.pump_qty is not null
        and t1.pump_qty != 0
        and t.yr = round(${mh1}/100, 0)

    union all
    select
        uuid() as id,
        t.region as region,
        'IT_PS_000031' as item_code,
        '食水抽水站抽水量同比增长率' as item_name_cn,
        '食水抽水站抽水量年比成長率' as item_name_tc,
        'Year on Year Growth Rate Of Pumping Volume Of Fresh Water Pumping Stations' as item_name_en,
        (t.pump_qty - t1.pump_qty)/t1.pump_qty * 100 as item_value,
        '%' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_bf t
        left join t_bf t1 on t.region = t1.region and t.yr = t1.yr+1
    where t1.pump_qty is not null
        and t1.pump_qty != 0
        and t.yr = round(${mh1}/100, 0)

    union all
    select
        uuid() as id,
        t.region as region,
        'IT_PS_000031' as item_code,
        '食水抽水站抽水量同比增长率' as item_name_cn,
        '食水抽水站抽水量年比成長率' as item_name_tc,
        'Year on Year Growth Rate Of Pumping Volume Of Fresh Water Pumping Stations' as item_name_en,
        (t.pump_qty - t1.pump_qty)/t1.pump_qty * 100 as item_value,
        '%' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_af t
        left join t_af t1 on t.region = t1.region and t.yr = t1.yr+1
    where t1.pump_qty is not null
        and t1.pump_qty != 0
        and t.yr = round(${mh1}/100, 0)
);

insert into coss_dm.dm_psr_annual_pump_station_item_di
select
    id,
    statistical_year,
    region_abbr,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    coss_tmp.dm_psr_annual_pump_station_item_di_01
on duplicate key update
    id = values(id),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time);
```

### 2.coss_dm.dm_psr_monthly_pump_station_item_di

#### create table

```sql
drop table if exists coss_dm.dm_psr_monthly_pump_station_item_di;
create table if not exists coss_dm.dm_psr_monthly_pump_station_item_di(
    id                           varchar(50),
    statistical_month            decimal(10,0),
    region_abbr                 varchar(120),
    inter_item_code             varchar(120),
    item_value                  decimal(20,5),
    dm_update_time              timestamp(6) default current_timestamp,
    dm_load_time                timestamp(6) default current_timestamp,
    primary key (statistical_month, region_abbr, inter_item_code)
)
with (orientation = row, compression = no)
distribute by hash(statistical_year, region_abbr);
comment on table coss_dm.dm_psr_monthly_pump_station_item_di is 'The Annual Pump Station items';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.id is 'Primary Key';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.statistical_month is 'Statistical Month';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.region_abbr is 'Regional Abbreviation';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.inter_item_code is 'Internal Item Code';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.item_value is 'Item Value';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.dm_update_time is 'Data Update Time';
comment on column coss_dm.dm_psr_monthly_pump_station_item_di.dm_load_time is 'Data Loading Time';
```

#### 2.1 吨水电耗指标

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Details
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_psr_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_psr_monthly_pump_station_item_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_psr_monthly_pump_station_item_di_01;
create table if not exists coss_tmp.dm_psr_monthly_pump_station_item_di_01(
    id                           varchar(50),
    statistical_month            decimal(10,0),
    region_abbr                 varchar(120),
    inter_item_code             varchar(120),
    item_value                  decimal(20,5),
    dm_update_time              timestamp(6) default current_timestamp,
    dm_load_time                timestamp(6) default current_timestamp
);

with t_af as (
    select
        mh as mh,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where (i_type_code = 'FW')
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt
),
t_ar as (
    select
        mh as mh,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where (i_type_code = 'RW')
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt
),
t_as as (
    select
        mh as mh,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'SW'
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt
),
t_afs as (
    select
        mh as mh,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'Combine'
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt
),
t_bf as (
    select
        mh as mh,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where (i_type_code = 'FW')
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh
),
t_br as (
    select
        mh as mh,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where (i_type_code = 'RW')
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh
),
t_bs as (
    select
        mh as mh,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'SW'
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh
),
t_bfs as (
    select
        mh as mh,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where i_type_code = 'Combine'
        and pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh
)
insert into coss_tmp.dm_psr_monthly_pump_station_item_di_01
select
    id,
    mh as statistical_month,
    region as region_abbr,
    item_code as inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from (
    select
        uuid() as id,
        region as region,
        'IT_PS_000019' as item_code,
        '食水抽水站单位电耗' as item_name_cn,
        '食水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Pump Station' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_bf t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000019' as item_code,
        '食水抽水站单位电耗' as item_name_cn,
        '食水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Pump Station' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_af t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000020' as item_code,
        '原水抽水站单位电耗' as item_name_cn,
        '原水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Pump Station' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_br t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000020' as item_code,
        '原水抽水站单位电耗' as item_name_cn,
        '原水食水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Pump Station' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_ar t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000021' as item_code,
        '海水抽水站单位电耗' as item_name_cn,
        '海水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Salt Water Pumping Stations' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_bs t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000021' as item_code,
        '海水抽水站单位电耗' as item_name_cn,
        '海水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Salt Water Pumping Stations' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_as t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000023' as item_code,
        '食水海水抽水站单位电耗' as item_name_cn,
        '食水海水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit  Of Fresh&Salt Water Pumping Stations' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_bfs t

    union all
    select
        uuid() as id,
        region as region,
        'IT_PS_000023' as item_code,
        '食水海水抽水站单位电耗' as item_name_cn,
        '食水海水抽水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Fresh&Salt Water Pumping Stations' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_afs t
);

insert into coss_dm.dm_psr_monthly_pump_station_item_di
select
    id,
    statistical_month,
    region_abbr,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from coss_tmp.dm_psr_monthly_pump_station_item_di_01
on duplicate key update
    id = values(id),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time);

```

#### 2.2抽水量、电耗量、账单金额

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Details
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_psr_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_psr_monthly_pump_station_item_di
-- ****************************************************************************************

drop table if exists coss_tmp.dm_psr_monthly_pump_station_item_di_01;
create table if not exists coss_tmp.dm_psr_monthly_pump_station_item_di_01(
    id                           varchar(50),
    statistical_month            decimal(10,0),
    region_abbr                 varchar(120),
    inter_item_code             varchar(120),
    item_value                  decimal(20,5),
    dm_update_time              timestamp(6) default current_timestamp,
    dm_load_time                timestamp(6) default current_timestamp
);

with t_af as (
    select
        mh,
        region_rpt as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty,  -- Convert ML To Mcm
        sum(payout) as payout
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'FW'
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt
),
t_ar as (
    select
        mh,
        region_rpt as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty,  -- Convert ML To Mcm
        sum(payout) as payout
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'RW'
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt
),
t_as as (
    select
        mh,
        region_rpt as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty,  -- Convert ML To Mcm
        sum(payout) as payout
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'SW'
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt
),
t_afs as (
    select
        mh,
        region_rpt as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty,  -- Convert ML To Mcm
        sum(payout) as payout
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'Combine'
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt
),
t_bf as (
    select
        mh,
        'HKSAR' as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty,  -- Convert ML To Mcm
        sum(payout) as payout
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'FW'
        -- and mh >= ${mh1}
    group by
        mh
),
t_br as (
    select
        mh,
        'HKSAR' as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty,  -- Convert ML To Mcm
        sum(payout) as payout
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'RW'
        -- and mh >= ${mh1}
    group by
        mh
),
t_bs as (
    select
        mh,
        'HKSAR' as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty,  -- Convert ML To Mcm
        sum(payout) as payout
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'SW'
        -- and mh >= ${mh1}
    group by
        mh
),
t_bfs as (
    select
        mh,
        'HKSAR' as region,
        sum(total_kwh) as total_kwh,
        sum(pump_qty)/1000 as pump_qty,  -- Convert ML To Mcm
        sum(payout) as payout
    from
        coss_dws.dws_psr_eng_cons_billing_details_di_year
    where
        i_type_code = 'Combine'
        -- and mh >= ${mh1}
    group by
        mh
)
insert into coss_tmp.dm_psr_monthly_pump_station_item_di_01
select
    id,
    mh as statistical_month,
    region as region_abbr,
    item_code as inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    (
        select
            uuid() as id,
            region as region,
            'IT_PS_000001' as item_code,
            '食水抽水站电耗量' as item_name_cn,
            '食水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Fresh Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_bf t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000001' as item_code,
            '食水抽水站电耗量' as item_name_cn,
            '食水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Fresh Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_af t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000002' as item_code,
            '原水抽水站电耗量' as item_name_cn,
            '原水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Raw Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_br t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000002' as item_code,
            '原水站电耗量' as item_name_cn,
            '原水食水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Raw Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_ar t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000003' as item_code,
            '海水抽水站电耗量' as item_name_cn,
            '海水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Salt Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_bs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000003' as item_code,
            '海水抽水站电耗量' as item_name_cn,
            '海水抽水站電耗量' as item_name_tc,
            'Power Consumption Of Salt Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_as t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000005' as item_code,
            '其他(combine)抽水站电耗量' as item_name_cn,
            '其他(combine)抽水站電耗量' as item_name_tc,
            'Power Consumption Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_bfs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000005' as item_code,
            '其他(combine)抽水站电耗量' as item_name_cn,
            '其他(combine)抽水站電耗量' as item_name_tc,
            'Power Consumption Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.total_kwh as item_value,
            'kwh' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_afs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000007' as item_code,
            '食水抽水站抽水量' as item_name_cn,
            '食水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Fresh Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_bf t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000007' as item_code,
            '食水抽水站抽水量' as item_name_cn,
            '食水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Fresh Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_af t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000008' as item_code,
            '原水抽水站抽水量' as item_name_cn,
            '原水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Raw Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_br t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000008' as item_code,
            '原水抽水站抽水量' as item_name_cn,
            '原水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Raw Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_ar t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000009' as item_code,
            '海水抽水站抽水量' as item_name_cn,
            '海水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Salt Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_bs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000009' as item_code,
            '海水抽水站抽水量' as item_name_cn,
            '海水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Salt Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_as t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000011' as item_code,
            '食水海水抽水站抽水量' as item_name_cn,
            '食水海水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_bfs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000011' as item_code,
            '食水海水抽水站抽水量' as item_name_cn,
            '食水海水抽水站抽水量' as item_name_tc,
            'Pumping Volume Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.pump_qty as item_value,
            'mcm' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_afs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000031' as item_code,
            '食水抽水站账单金额' as item_name_cn,
            '食水抽水站帳單金額' as item_name_tc,
            'Bill Amount Of Fresh Water Pumping Stations' as item_name_en,
            t.payout as item_value,
            '$HK' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_bf t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000031' as item_code,
            '食水抽水站账单金额' as item_name_cn,
            '食水抽水站帳單金額' as item_name_tc,
            'Bill Amount Of Fresh Water Pumping Stations' as item_name_en,
            t.payout as item_value,
            '$HK' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_af t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000032' as item_code,
            '原水抽水站账单金额' as item_name_cn,
            '原水抽水站帳單金額' as item_name_tc,
            'Bill Amount Of Raw Water Pumping Stations' as item_name_en,
            t.payout as item_value,
            '$HK' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_br t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000032' as item_code,
            '原水站账单金额' as item_name_cn,
            '原水食水抽水站帳單金額' as item_name_tc,
            'Bill Amount Of Raw Water Pumping Stations' as item_name_en,
            t.payout as item_value,
            '$HK' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_ar t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000033' as item_code,
            '海水抽水站账单金额' as item_name_cn,
            '海水抽水站帳單金額' as item_name_tc,
            'Bill Amount Of Salt Water Pumping Stations' as item_name_en,
            t.payout as item_value,
            '$HK' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_bs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000033' as item_code,
            '海水抽水站账单金额' as item_name_cn,
            '海水抽水站帳單金額' as item_name_tc,
            'Bill Amount Of Salt Water Pumping Stations' as item_name_en,
            t.payout as item_value,
            '$HK' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_as t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000034' as item_code,
            '其他(combine)抽水站账单金额' as item_name_cn,
            '其他(combine)抽水站帳單金額' as item_name_tc,
            'Bill Amount Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.payout as item_value,
            '$HK' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_bfs t

        union all
        select
            uuid() as id,
            region as region,
            'IT_PS_000034' as item_code,
            '其他(combine)抽水站账单金额' as item_name_cn,
            '其他(combine)抽水站帳單金額' as item_name_tc,
            'Bill Amount Of Fresh&Salt Water Pumping Stations' as item_name_en,
            t.payout as item_value,
            '$HK' as unit,
            localtimestamp as dm_update_time,
            localtimestamp as dm_load_time,
            t.mh as mh
        from
            t_afs t

    ) t_sub;
    
insert into coss_dm.dm_psr_monthly_pump_station_item_di
select
    id,
    statistical_month,
    region_abbr,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from coss_tmp.dm_psr_monthly_pump_station_item_di_01
on duplicate key update
    id = values(id),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time);
```

### 3.coss_dm.dm_psr_daily_ps_running_item_di

#### create table

```sql
-- Drop table
drop table if exists coss_dm.dm_psr_daily_ps_running_item_di;

-- Create table
create table if not exists coss_dm.dm_psr_daily_ps_running_item_di (
    asset_id              numeric(10) null,
    region                varchar(50) null,
    sub_region            varchar(50) null,
    installation_no       varchar(50) null,
    offical_eng_name      varchar(100) null,
    offical_chi_name      varchar(100) null,
    address_eng           varchar(100) null,
    address_chi           varchar(100) null,
    kwh_ml                numeric(20, 5) null,
    running_pumps         numeric(20, 5) null,
    total_pumps           numeric(20, 5) null,
    mh                    numeric(10) null,
    dm_update_time        timestamp(6) default current_timestamp,
    dm_load_time          timestamp(6) default current_timestamp,
    primary key(asset_id, mh)
)
with (
    orientation = row,
    compression = no
);

comment on table coss_dm.dm_psr_daily_ps_running_item_di is 'The Daily Pump Station Running Items';

-- Column comments
comment on column coss_dm.dm_psr_daily_ps_running_item_di.asset_id is 'Asset Id';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.region is 'Region';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.sub_region is 'Sub Region';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.installation_no is 'Installation No';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.offical_eng_name is 'Offical English Name';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.offical_chi_name is 'Offical Chinese Name';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.address_eng is 'Address English';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.address_chi is 'Address Chinese';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.kwh_ml is 'Kwh/Ml';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.running_pumps is 'Running Pumps';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.total_pumps is 'Total Pumps';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.mh is 'MH';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.dm_update_time is 'Dm Update Time';
comment on column coss_dm.dm_psr_daily_ps_running_item_di.dm_load_time is 'Dm Load Time';
```

#### 3.1 泵站运行情况&吨水电耗

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Details
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_psr_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_psr_daily_ps_running_item_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_psr_daily_ps_running_item_di_01;

create table if not exists coss_tmp.dm_psr_daily_ps_running_item_di_01 (
    asset_id              numeric(10) null,
    region                varchar(50) null,
    sub_region            varchar(50) null,
    installation_no       varchar(50) null,
    offical_eng_name      varchar(100) null,
    offical_chi_name      varchar(100) null,
    address_eng           varchar(100) null,
    address_chi           varchar(100) null,
    kwh_ml                numeric(20, 5) null,
    running_pumps         numeric(20, 5) null,
    total_pumps           numeric(20, 5) null,
    mh                    numeric(10) null,
    dm_update_time        timestamp(6) default current_timestamp,
    dm_load_time          timestamp(6) default current_timestamp
);

with t_a as (
    select
        t.asset_id,
        t.kwh_ml,
        t1.running_pumps,
        t1.total_pumps,
        t.mh
    from (
        select
            asset_id,
            total_kwh/pump_qty as kwh_ml,
            mh
        from coss_dws.dws_psr_eng_cons_billing_details_di_year
        where pump_qty != 0
            and pump_qty is not null
            -- and mh >= ${mh1}
    ) t
    left join (
        select
            mh,
            asset_id,
            sum(if(run_hours > 0, 1, 0)) as running_pumps,
            count(pump_num) as total_pumps
        from coss_dwd.dwd_psr_pump_running_details_di_year
        -- where mh >= ${mh1}
        group by
            mh,
            asset_id
    ) t1 on t.mh = t1.mh and t.asset_id = t1.asset_id
)
insert into coss_tmp.dm_psr_daily_ps_running_item_di_01
select
    t.asset_id as asset_id,
    t1.region_abbr as region,
    t1.sub_region as sub_region,
    t1.i_code as installation_no,
    t1.ps_en as offical_eng_name,
    t1.ps_cn as offical_chi_name,
    t1.address_en as address_eng,
    t1.address_cn as address_chi,
    t.kwh_ml as kwh_ml,
    t.running_pumps as running_pumps,
    t.total_pumps as total_pumps,
    t.mh as mh
from t_a t
left join coss_dim.dim_ps_installation_info t1 on t1.asset_id = t.asset_id;

insert into coss_dm.dm_psr_daily_ps_running_item_di
select
    asset_id,
    region,
    sub_region,
    installation_no,
    offical_eng_name,
    offical_chi_name,
    address_eng,
    address_chi,
    kwh_ml,
    running_pumps,
    total_pumps,
    mh,
    dm_update_time,
    dm_load_time
from
    coss_tmp.dm_psr_daily_ps_running_item_di_01 
on duplicate key update
    region = values(region),
    sub_region = values(sub_region),
    installation_no = values(installation_no),
    offical_eng_name = values(offical_eng_name),
    offical_chi_name = values(offical_chi_name),
    address_eng = values(address_eng),
    address_chi = values(address_chi),
    kwh_ml = values(kwh_ml),
    running_pumps = values(running_pumps),
    total_pumps = values(total_pumps),
    dm_update_time = values(dm_update_time);

```

### 4.coss_dm.dm_psr_monthly_ps_running_item_di

> 抽水站一张图-泵房泵机运行情况

#### create table

```sql
-- Drop table if exists
drop table if exists coss_dm.dm_psr_monthly_ps_running_item_di;

-- Create table
create table if not exists coss_dm.dm_psr_monthly_ps_running_item_di(
    statistical_month  varchar(10),
    asset_id           decimal(10),
    region_abbr        varchar(50),
    sub_region         varchar(50),
    installation_no    varchar(50),
    ps_en              varchar(100),
    ps_cn              varchar(100),
    address_en         varchar(100),
    address_cn         varchar(100),
    total_kwh          decimal(20,5),
    pump_qty           decimal(20,5),
    payout             decimal(20,5),
    kwh_ml             decimal(20,5),
    running_pumps      decimal(20,5),
    total_pumps        decimal(20,5),
    dm_update_time     timestamp(6) default current_timestamp,
    dm_load_time       timestamp(6) default current_timestamp,
    primary key (statistical_month, region_abbr, asset_id)
)
with (orientation = row, compression = no);
-- distribute by hash (statistical_month, region_abbr)

-- Table comment
comment on table coss_dm.dm_psr_monthly_ps_running_item_di is 'The Monthly Pump Station Running Items';

-- Column comments
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.statistical_month is 'Statistical Month';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.asset_id is 'Asset Id';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.region_abbr is 'Region Abbr';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.sub_region is 'Sub Region';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.installation_no is 'Installation No';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.ps_en is 'Pump Station En Name';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.ps_cn is 'Pump Station Cn Name';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.address_en is 'Address En Name';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.address_cn is 'Address Cn Name';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.total_kwh is 'Total kwh';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.pump_qty is 'Pump Quantity';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.payout is 'Pay Out';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.kwh_ml is 'Kwh/Ml';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.running_pumps is 'Running Pump Number';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.total_pumps is 'Total Pump Number';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.dm_update_time is 'Dm Update Time';
comment on column coss_dm.dm_psr_monthly_ps_running_item_di.dm_load_time is 'Dm Load Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Pump Station Running
-- Function Describe: Pump Station Running Details
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_psr_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_psr_monthly_ps_running_item_di
-- ****************************************************************************************
-- Drop table if exists
drop table if exists coss_tmp.dm_psr_monthly_ps_running_item_di_01;

-- Create table
create table if not exists coss_tmp.dm_psr_monthly_ps_running_item_di_01(
    statistical_month  varchar(10),
    asset_id           decimal(10),
    region_abbr        varchar(50),
    sub_region         varchar(50),
    installation_no    varchar(50),
    ps_en              varchar(100),
    ps_cn              varchar(100),
    address_en         varchar(100),
    address_cn         varchar(100),
    total_kwh          decimal(20,5),
    pump_qty           decimal(20,5),
    payout             decimal(20,5),
    kwh_ml             decimal(20,5),
    running_pumps      decimal(20,5),
    total_pumps        decimal(20,5),
    dm_update_time     timestamp(6) default current_timestamp,
    dm_load_time       timestamp(6) default current_timestamp
);

with t_a as (
    select
        asset_id                  as asset_id,
        mh                       as mh,
        sum(if(run_hours > 0, 1, 0)) as running_pumps,
        count(1)                 as total_pumps
    from coss_dwd.dwd_psr_pump_running_details_di_year
--    where mh >= ${mh1}
    group by
        asset_id,
        mh
), t_b as (
    select
        asset_id            as asset_id,
        mh                 as mh,
        sum(total_kwh) as total_kwh,
        sum(pump_qty) as pump_qty,
        sum(payout) as payout,
        sum(total_kwh)/sum(pump_qty) as kwh_ml
    from coss_dws.dws_psr_eng_cons_billing_details_di_year
    where pump_qty is not null and pump_qty != 0
 --       and mh >= ${mh1}
    group by
        asset_id,
        mh
)
insert into  coss_tmp.dm_psr_monthly_ps_running_item_di_01
select
    t.mh as statistical_month,
    t2.asset_id,
    t2.region_abbr,
    t2.sub_region,
    t2.i_code as installation_no,
    t2.ps_en,
    t2.ps_cn,
    t2.address_en,
    t2.address_cn,
    t1.total_kwh,
    t1.pump_qty,
    t1.payout,
    t1.kwh_ml,
    t.running_pumps,
    t.total_pumps,
    localtimestamp as dm_update_time,
    localtimestamp as dm_load_time
from t_a t
inner join t_b t1 on t.asset_id = t1.asset_id and t.mh = t1.mh
inner join coss_dim.dim_ps_installation_info t2 on t.asset_id = t2.asset_id;

insert into coss_dm.dm_psr_monthly_ps_running_item_di
select 
    statistical_month,
    asset_id,
    region_abbr,
    sub_region,
    installation_no,
    ps_en,
    ps_cn,
    address_en,
    address_cn,
    total_kwh,
    pump_qty,
    payout,
    kwh_ml,
    running_pumps,
    total_pumps,
    dm_update_time,
    dm_load_time
from 
    coss_tmp.dm_psr_monthly_ps_running_item_di_01
on duplicate key update
    sub_region = values(sub_region),
    installation_no = values(installation_no),
    ps_en = values(ps_en),
    ps_cn = values(ps_cn),
    address_en = values(address_en),
    address_cn = values(address_cn),
    total_kwh = values(total_kwh),
    pump_qty = values(pump_qty),
    payout = values(payout),
    kwh_ml = values(kwh_ml),
    running_pumps = values(running_pumps),
    total_pumps = values(total_pumps),
    dm_update_time = values(dm_update_time)
```

## dm_wtw_etl_report_bill_day（调度任务）





### 1.coss_dm.dm_wtw_annual_water_treatment_works_item_di

#### create table

```sql
drop table if exists coss_dm.dm_wtw_annual_water_treatment_works_item_di;
create table if not exists coss_dm.dm_wtw_annual_water_treatment_works_item_di(
    id                           varchar(50),
    statistical_year             decimal(10,0),
    region_abbr                  varchar(120),
    inter_item_code              varchar(120),
    item_value                   decimal(20,5),
    dm_update_time               timestamp(6) default current_timestamp,
    dm_load_time                 timestamp(6) default current_timestamp,
    primary key (statistical_year, region_abbr, inter_item_code)
)
with (orientation = row, compression = no)
distribute by hash (statistical_year, region_abbr);

comment on table coss_dm.dm_wtw_annual_water_treatment_works_item_di is 'The Annual Pump Station items';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_di.id is 'Primary Key';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_di.statistical_year is 'Statistical Year';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_di.region_abbr is 'Regional Abbreviation';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_di.inter_item_code is 'Internal Item Code';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_di.item_value is 'Item Value';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_di.dm_update_time is 'Data Update Time';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_di.dm_load_time is 'Data Loading Time';
```

#### 1.1 吨水电耗

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Treatment Works
-- Function Describe: Water Treatment Works Bills Detail
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_wtw_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_wtw_annual_water_treatment_works_item_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_wtw_annual_water_treatment_works_item_di_01;
create table if not exists coss_tmp.dm_wtw_annual_water_treatment_works_item_di_01(
    id                           varchar(50),
    statistical_year             decimal(10,0),
    region_abbr                  varchar(120),
    inter_item_code              varchar(120),
    item_value                   decimal(20,5),
    dm_update_time               timestamp(6) default current_timestamp,
    dm_load_time                 timestamp(6) default current_timestamp
);

with t_af as (
    select
        round(mh/100) as yr,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_wtw_eng_cons_billing_details_di_year
    where pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr,
        region_rpt
),
t_bf as (
    select
        round(mh/100) as yr,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_wtw_eng_cons_billing_details_di_year
    where pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        yr
)
insert into coss_tmp.dm_wtw_annual_water_treatment_works_item_di_01
select
    id,
    yr as statistical_year,
    region as region_abbr,
    item_code as inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from (
    select
        uuid() as id,
        region as region,
        'IT_TW_000025' as item_code,
        '滤水厂单位电耗' as item_name_cn,
        '濾水廠單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Treatment Works' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_bf t

    union all
    select
        uuid() as id,
        region as region,
        'IT_TW_000025' as item_code,
        '滤水厂单位电耗' as item_name_cn,
        '濾水廠水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Treatment Works' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_af t
);

insert into coss_dm.dm_wtw_annual_water_treatment_works_item_di
select
    id,
    statistical_year,
    region_abbr,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    coss_tmp.dm_wtw_annual_water_treatment_works_item_di_01
on duplicate key update
    id = values(id),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time)
```

#### 1.2 吨水电耗同比增长率{年离散计算}

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Treatment Works
-- Function Describe: Water Treatment Works Bills Detail
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_wtw_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_wtw_annual_water_treatment_works_item_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_wtw_annual_water_treatment_works_item_di_01;
create table if not exists coss_tmp.dm_wtw_annual_water_treatment_works_item_di_01(
    id                           varchar(50),
    statistical_year             decimal(10,0),
    region_abbr                  varchar(120),
    inter_item_code              varchar(120),
    item_value                   decimal(20,5),
    dm_update_time               timestamp(6) default current_timestamp,
    dm_load_time                 timestamp(6) default current_timestamp
);

with t_af as (
    select
        round(mh/100) as yr,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_wtw_eng_cons_billing_details_di_year
    where pump_qty is not null and pump_qty != 0
        -- and round(mh/100, 0) = round(${mh1}/100, 0)
        -- or mh in (select distinct mh-100 mh from coss_dws.dws_wtw_eng_cons_billing_details_di_year where round(mh/100, 0) = round(${mh1}/100, 0))
    group by
        yr,
        region_rpt
),
t_bf as (
    select
        round(mh/100) as yr,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_wtw_eng_cons_billing_details_di_year
    where pump_qty is not null and pump_qty != 0
        -- and round(mh/100, 0) = round(${mh1}/100, 0)
        -- or mh in (select distinct mh-100 mh from coss_dws.dws_wtw_eng_cons_billing_details_di_year where round(mh/100, 0) = round(${mh1}/100, 0))
    group by
        yr
)
insert into coss_tmp.dm_wtw_annual_water_treatment_works_item_di_01
select
    id,
    yr as statistical_year,
    region as region_abbr,
    item_code as inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from (
    select
        uuid() as id,
        t.region as region,
        'IT_TW_000027' as item_code,
        '滤水厂单位电耗同比增长率' as item_name_cn,
        '濾水廠單位電耗同比增長率' as item_name_tc,
        'Year on Year Growth Rate Of Electricity Consumption Per Unit In Water Treatment Works' as item_name_en,
        case
            when t1.kwh_qty is null or t1.kwh_qty = 0 then 0
            else (t.kwh_qty - t1.kwh_qty)/t1.kwh_qty * 100
        end as item_value,
        '%' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_bf t
        left join t_bf t1 on t.yr = t1.yr+1 and t.region = t1.region
    -- where t.yr = round(${mh1}/100, 0)

    union all
    select
        uuid() as id,
        t.region as region,
        'IT_TW_000027' as item_code,
        '滤水厂单位电耗同比增长率' as item_name_cn,
        '濾水廠水站單位電耗同比增長率' as item_name_tc,
        'Year on Year Growth Rate Of Electricity Consumption Per Unit In Water Treatment Works' as item_name_en,
        case
            when t1.kwh_qty is null or t1.kwh_qty = 0 then 0
            else (t.kwh_qty - t1.kwh_qty)/t1.kwh_qty * 100
        end as item_value,
        '%' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_af t
        left join t_af t1 on t.yr = t1.yr+1 and t.region = t1.region
    -- where t.yr = round(${mh1}/100, 0)
);


insert into coss_dm.dm_wtw_annual_water_treatment_works_item_di
select
    id,
    statistical_year,
    region_abbr,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    coss_tmp.dm_wtw_annual_water_treatment_works_item_di_01
on duplicate key update
    id = values(id),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time)
```

### 2.coss_dm.dm_wtw_monthly_water_treatment_works_item_di

#### create table

```sql
drop table if exists coss_dm.dm_wtw_monthly_water_treatment_works_item_di;
create table if not exists coss_dm.dm_wtw_monthly_water_treatment_works_item_di(
    id                           varchar(50),
    statistical_month            decimal(10,0),
    region_abbr                 varchar(120),
    inter_item_code             varchar(120),
    item_value                  decimal(20,5),
    dm_update_time              timestamp(6) default current_timestamp,
    dm_load_time                timestamp(6) default current_timestamp,
    primary key (statistical_month, region_abbr, inter_item_code)
)
with (orientation = row, compression = no)
distribute by hash (statistical_month, region_abbr);

comment on table coss_dm.dm_wtw_monthly_water_treatment_works_item_di is 'The Annual Pump Station items';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_di.id is 'Primary Key';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_di.statistical_month is 'Statistical Month';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_di.region_abbr is 'Regional Abbreviation';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_di.inter_item_code is 'Internal Item Code';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_di.item_value is 'Item Value';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_di.dm_update_time is 'Data Update Time';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_di.dm_load_time is 'Data Loading Time';
```

#### 2.1 吨水电耗

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Treatment Works
-- Function Describe: Water Treatment Works Bills Detail
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_wtw_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_wtw_monthly_water_treatment_works_item_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_wtw_monthly_water_treatment_works_item_di_01;
create table if not exists coss_tmp.dm_wtw_monthly_water_treatment_works_item_di_01(
    id                          varchar(50),
    statistical_month           decimal(10,0),
    region_abbr                 varchar(120),
    inter_item_code             varchar(120),
    item_value                  decimal(20,5),
    dm_update_time              timestamp(6) default current_timestamp,
    dm_load_time                timestamp(6) default current_timestamp
);

with t_af as (
    select
        mh as mh,
        region_rpt region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_wtw_eng_cons_billing_details_di_year
    where pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt
),
t_bf as (
    select
        mh as mh,
        'HKSAR' region,
        sum(total_kwh)/sum(pump_qty) kwh_qty
    from coss_dws.dws_wtw_eng_cons_billing_details_di_year
    where pump_qty is not null and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh
)
insert into coss_tmp.dm_wtw_monthly_water_treatment_works_item_di_01
select
    id,
    mh as statistical_month,
    region as region_abbr,
    item_code as inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from (
    select
        uuid() as id,
        region as region,
        'IT_TW_000025' as item_code,
        '滤水厂单位电耗' as item_name_cn,
        '濾水廠單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Treatment Works' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/ML' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_bf t

    union all
    select
        uuid() as id,
        region as region,
        'IT_TW_000025' as item_code,
        '滤水厂单位电耗' as item_name_cn,
        '濾水廠水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Treatment Works' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/ML' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_af t
);

insert into coss_dm.dm_wtw_monthly_water_treatment_works_item_di
select
    id,
    statistical_month,
    region_abbr,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    coss_tmp.dm_wtw_monthly_water_treatment_works_item_di_01
on duplicate key update
    id = values(id),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time);
```



### 3.coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di

#### create table

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Treatment Works
-- Function Describe: Definition of Annual Water Treatment Works Item Detail Table
-- Create         By: dongmaochen (consistent with previous creation info)
-- Create       Date: 2025-11-17 (consistent with previous creation info)
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Target Table
-- coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di
-- ****************************************************************************************
-- Drop table if exists
drop table if exists coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di;

-- Create table
create table if not exists coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di (
    id                          varchar(50) not null, -- Primary Key
    statistical_year            numeric(10) null, -- Statistical Year
    region_abbr                 varchar(120) null, -- Regional Abbreviation
    asset_id                    int4 null, -- Asset Id
    wtw_name_en                 varchar(250) null, -- Water Treatment Work English Name
    inter_item_code             varchar(120) null, -- Internal Item Code
    item_value                  numeric(20, 5) null, -- Item Value
    dm_update_time              timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time                timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key (statistical_year, region_abbr, wtw_name_en, inter_item_code)
)
with (
    orientation = row,
    compression = no
);

-- Table comment
comment on table coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di is 'The Water Treatment Works items';

-- Column comments
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di.id is 'Primary Key';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di.statistical_year is 'Statistical Year';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di.region_abbr is 'Regional Abbreviation';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di.asset_id is 'Asset Id';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di.wtw_name_en is 'Water Treatment Work English Name';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di.inter_item_code is 'Internal Item Code';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di.item_value is 'Item Value';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di.dm_update_time is 'Data Update Time';
comment on column coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di.dm_load_time is 'Data Loading Time';
```

#### 3.1 单位电耗&单位电耗同比增长率

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Treatment Works
-- Function Describe: Water Treatment Works Bills Detail
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_wtw_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_wtw_annual_water_treatment_works_item_detail_di_01;
create table if not exists coss_tmp.dm_wtw_annual_water_treatment_works_item_detail_di_01 (
    id                          varchar(50) not null, -- Primary Key
    statistical_year            numeric(10) null, -- Statistical Year
    region_abbr                 varchar(120) null, -- Regional Abbreviation
    asset_id                    int4 null, -- Asset Id
    wtw_name_en                 varchar(250) null, -- Water Treatment Work English Name
    inter_item_code             varchar(120) null, -- Internal Item Code
    item_value                  numeric(20, 5) null, -- Item Value
    dm_update_time              timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time                timestamp(6) null default pg_systimestamp() -- Data Loading Time
)
with (
    orientation = row,
    compression = no
);

with t_af as (
    select
        round(mh/100) as yr,
        region_rpt region,
        asset_id,
        asset_name as wtw_name_en,
        sum(total_kwh)/sum(pump_qty) as kwh_qty
    from coss_dws.dws_wtw_eng_cons_billing_details_di_year
    where pump_qty is not null and pump_qty != 0
        -- mh>= ${mh1}
    group by
        yr,
        region_rpt,
        wtw_name_en,
        asset_id
)
insert into coss_tmp.dm_wtw_annual_water_treatment_works_item_detail_di_01
select
    id,
    yr as statistical_year,
    region as region_abbr,
    asset_id,
    wtw_name_en,
    item_code as inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from (
    select
        uuid() as id,
        region as region,
        asset_id,
        wtw_name_en as wtw_name_en,
        'IT_TW_000025' as item_code,
        '滤水厂单位电耗' as item_name_cn,
        '濾水廠水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Treatment Works' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_af t

    union all
    select
        uuid() as id,
        t.region as region,
        t.asset_id,
        t.wtw_name_en as wtw_name_en,
        'IT_TW_000027' as item_code,
        '滤水厂单位电耗同比增长率' as item_name_cn,
        '濾水廠水站單位電耗同比增長率' as item_name_tc,
        'Year on Year Growth Rate Of Electricity Consumption Per Unit In Water Treatment Works' as item_name_en,
        case
            when t1.kwh_qty is null or t1.kwh_qty = 0 then 0
            else (t.kwh_qty - t1.kwh_qty)/t1.kwh_qty * 100
        end as item_value,
        '%' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.yr as yr
    from t_af t
        left join t_af t1 on t.yr = t1.yr+1 and t.region = t1.region and t.wtw_name_en = t1.wtw_name_en
);


insert into coss_dm.dm_wtw_annual_water_treatment_works_item_detail_di
select
    id,
    statistical_year,
    region_abbr,
    asset_id,
    wtw_name_en,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    coss_tmp.dm_wtw_annual_water_treatment_works_item_detail_di_01
on duplicate key update
    id = values(id),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time)
```



### 4.coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di

#### create table

```sql
drop table if exists coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di;

-- Create table
create table if not exists coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di (
    id                          varchar(50) not null, -- Primary Key
    statistical_month           numeric(10) null, -- Statistical Month
    region_abbr                 varchar(120) null, -- Regional Abbreviation
    asset_id                    int4 null, -- Asset_id
    wtw_name_en                 varchar(250) null, -- Water Treatment Works
    inter_item_code             varchar(120) null, -- Internal Item Code
    item_value                  numeric(20, 5) null, -- Item Value
    dm_update_time              timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time                timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key (statistical_month, asset_id, inter_item_code)
)
with (
    orientation = row,
    compression = no
);

-- Table comment (retained original business description)
comment on table coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di is 'The Annual Pump Station items';

-- Column comments
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di.id is 'Primary Key';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di.statistical_month is 'Statistical Month';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di.region_abbr is 'Regional Abbreviation';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di.asset_id is 'Asset_id';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di.wtw_name_en is 'Water Treatment Works';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di.inter_item_code is 'Internal Item Code';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di.item_value is 'Item Value';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di.dm_update_time is 'Data Update Time';
comment on column coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di.dm_load_time is 'Data Loading Time';
```

#### 4.1 单位电耗

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Treatment Works
-- Function Describe: Water Treatment Works Bills Detail
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_dws.dws_wtw_eng_cons_billing_details_di_year
-- Target Table
-- coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_wtw_monthly_water_treatment_works_item_detail_di_01;
create table if not exists coss_tmp.dm_wtw_monthly_water_treatment_works_item_detail_di_01 (
    id                          varchar(50) not null, -- Primary Key
    statistical_month           numeric(10) null, -- Statistical Month
    region_abbr                 varchar(120) null, -- Regional Abbreviation
    asset_id                    int4 null, -- Asset_id
    wtw_name_en                 varchar(250) null, -- Water Treatment Works
    inter_item_code             varchar(120) null, -- Internal Item Code
    item_value                  numeric(20, 5) null, -- Item Value
    dm_update_time              timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time                timestamp(6) null default pg_systimestamp()
);

with t_af as (
    select
        mh as mh,
        region_rpt region,
        asset_id,
        asset_name as wtw_name_en,
        sum(total_kwh)/sum(pump_qty) as kwh_qty
    from coss_dws.dws_wtw_eng_cons_billing_details_di_year
    where pump_qty is not null
        and pump_qty != 0
        -- and mh >= ${mh1}
    group by
        mh,
        region_rpt,
        wtw_name_en,
        asset_id
)
insert into coss_tmp.dm_wtw_monthly_water_treatment_works_item_detail_di_01
select
    id,
    mh as statistical_month,
    region as region_abbr,
    asset_id,
    wtw_name_en,
    item_code as inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from (
    select
        uuid() as id,
        region as region,
        asset_id,
        wtw_name_en as wtw_name_en,
        'IT_TW_000025' as item_code,
        '滤水厂单位电耗' as item_name_cn,
        '濾水廠水站單位電耗' as item_name_tc,
        'Electricity Consumption Per Unit Of Water Treatment Works' as item_name_en,
        t.kwh_qty as item_value,
        'kwh/Ml' as unit,
        localtimestamp as dm_update_time,
        localtimestamp as dm_load_time,
        t.mh as mh
    from t_af t
);
insert into coss_dm.dm_wtw_monthly_water_treatment_works_item_detail_di
select
    id,
    statistical_month,
    region_abbr,
    asset_id,
    wtw_name_en,
    inter_item_code,
    item_value,
    dm_update_time,
    dm_load_time
from
    coss_tmp.dm_wtw_monthly_water_treatment_works_item_detail_di_01
on duplicate key update
    id = values(id),
    wtw_name_en = values(wtw_name_en),
    item_value = values(item_value),
    dm_update_time = values(dm_update_time)
```



### 5.coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di

> 滤水厂一张图-水厂能耗历史数据
> 供水运行一张图-水厂能耗历史数据

#### create table

```sql
-- Drop table if exists
drop table if exists coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di;

-- Create table
create table if not exists coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di(
    statistical_month     decimal(10),
    asset_id              decimal(11),
    asset_name            varchar(120),
    asset_desc            varchar(120),
    installation_id       varchar(36),
    i_type_code           varchar(150),
    i_type_desc           varchar(150),
    region_rpt            varchar(150),
    bill_date             timestamp(6),
    tariff_name           varchar(150),
    tariff_desc           varchar(300),
    utility_name          varchar(150),
    utility_desc          varchar(800),
    kwh_on_peak           decimal(10,0),
    kwh_off_peak          decimal(10,0),
    payout                decimal(10,0),
    total_kwh             decimal(10,0),
    pump_qty              decimal(20,5),
    kwh_ml             decimal(20,5),
    dm_update_time        timestamp(6) default current_timestamp,
    dm_load_time          timestamp(6) default current_timestamp,
    primary key (asset_id, bill_date)
)
with (orientation = row, compression = no)
distribute by hash (asset_id);

-- Table comment
comment on table coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di is 'Pump Station Running Billing History';

-- Column comments

comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.asset_id is 'Asset Id';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.asset_name is 'Asset Name';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.asset_desc is 'Asset Description';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.installation_id is 'Installation ID';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.i_type_code is 'Installation Type Code';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.i_type_desc is 'Installation Type Description';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.region_rpt is 'Region Report';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.bill_date is 'Bill Date';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.tariff_name is 'Tariff Name';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.tariff_desc is 'Tariff Description';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.utility_name is 'Utility Name';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.utility_desc is 'Utility Description';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.kwh_on_peak is 'Power Consumption Of On Peak (kwh)';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.kwh_off_peak is 'Power Consumption Of Off Peak (kwh)';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.payout is 'Pay Out';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.total_kwh is 'Power Consumption Of Total (kwh), The Calculation Logic Is (kwh_on_peak + kwh_off_peak)';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.pump_qty is 'Water Pumped This Month';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.kwh_ml is 'Kwh/Ml';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.dm_update_time is 'Dm Update Time';
comment on column coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di.dm_load_time is 'Dm Load Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Treatment Works
-- Function Describe: Water Treatment Works Bills Detail
-- Create         By: dongmaochen
-- Create       Date: 2025-11-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table               : coss_dws.dws_wtw_eng_cons_billing_details_di_year
-- Target Table               : coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di
-- ****************************************************************************************
insert into coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di
select
    mh               as statistical_month,
    asset_id         as asset_id,
    asset_name       as asset_name,
    asset_desc       as asset_desc,
    i_type_code      as i_type_code,
    i_type_desc      as i_type_desc,
    region_rpt       as region_rpt,
    bill_date        as bill_date,
    tariff_name      as tariff_name,
    tariff_desc      as tariff_desc,
    utility_name     as utility_name,
    utility_desc     as utility_desc,
    kwh_on_peak      as kwh_on_peak,
    kwh_off_peak     as kwh_off_peak,
    payout           as payout,
    total_kwh        as total_kwh,
    pump_qty         as pump_qty,
    if(pump_qty is not null and pump_qty !=0 ,( total_kwh/pump_qty),0) as kwh_ml,
    localtimestamp   as dm_update_time,
    localtimestamp   as dm_load_time
from coss_dws.dws_wtw_eng_cons_billing_details_di_year
-- where mh >= ${mh1}
on duplicate key update
    statistical_month = values(statistical_month),
    asset_name = values(asset_name),
    asset_desc = values(asset_desc),
    i_type_code = values(i_type_code),
    i_type_desc = values(i_type_desc),
    region_rpt = values(region_rpt),
    tariff_name = values(tariff_name),
    tariff_desc = values(tariff_desc),
    utility_name = values(utility_name),
    utility_desc = values(utility_desc),
    kwh_on_peak = values(kwh_on_peak),
    kwh_off_peak = values(kwh_off_peak),
    payout = values(payout),
    total_kwh = values(total_kwh),
    pump_qty = values(pump_qty),
    kwh_ml = values(kwh_ml),
    dm_update_time = values(dm_update_time)
```



# dim

## 1.coss_dim.dim_ass_energy_cons_installation_df

```sql
drop table if exists coss_dim.dim_ass_energy_cons_installation_df;
create table if not exists coss_dim.dim_ass_energy_cons_installation_df(
    asset_id                    decimal(11),        -- Asset Id
    asset_name                 varchar(120),       -- Asset Name
    asset_desc                 varchar(120),       -- Asset Description
    loca_code                  varchar(15),        -- Location Code
    acc_no                     varchar(120),       -- Account No
    region_id                  decimal(11),        -- Region Id
    region_code                varchar(150),       -- Region Code
    region_desc                varchar(800),       -- Region Description
    i_type_id                  decimal(11),        -- Installation Type Id
    i_type_code                varchar(150),       -- Installation Type Code
    i_type_desc                varchar(150),       -- Installation Type  Description
    fw_portion                 decimal(20,5),      -- Fresh Portion
    sw_portion                 decimal(20,5),      -- Salt Water Portion
    rw_portion                 decimal(20,5),      -- Raw Water Portion
    tw_portion                 decimal(20,5),      -- Treatment Works Portion
    remarks                    varchar(120),       -- Remarks
    is_active                  decimal(5),         -- Is Active
    official_name              varchar(120),       -- Official Name
    station_code               varchar(120),       -- Station Code
    is_billing                 decimal(5),         -- Billing Is Active
    is_ps                      decimal(5),         -- Pump Station Is Active
    is_ecw                     decimal(5),         -- Ecw Is Active
    region_rpt                 varchar(150),       -- Region Report
    is_hkp                     decimal(5),         -- Hkp Is Active
    is_fy                      decimal(5),         -- Fy Is Active
    is_water_eff               decimal(5),         -- Water Efficiency Is Active
    water_eff_type_id          decimal(11),        -- Installation Type Id For Water Efficiency
    i_num                      varchar(30),        -- Installation Number
    dim_update_time            timestamp(6) default current_timestamp,
    dim_load_time              timestamp(6) default current_timestamp,
    dt                         decimal(10),        -- Date Time
    primary key(asset_id)
)
distribute by hash(asset_id);

comment on table coss_dim.dim_ass_energy_cons_installation_df is 'Energy Consumption Installations';
comment on column coss_dim.dim_ass_energy_cons_installation_df.asset_id is 'Asset Id';
comment on column coss_dim.dim_ass_energy_cons_installation_df.asset_name is 'Asset Name';
comment on column coss_dim.dim_ass_energy_cons_installation_df.asset_desc is 'Asset Description';
comment on column coss_dim.dim_ass_energy_cons_installation_df.loca_code is 'Location Code';
comment on column coss_dim.dim_ass_energy_cons_installation_df.acc_no is 'Account No';
comment on column coss_dim.dim_ass_energy_cons_installation_df.region_id is 'Region Id';
comment on column coss_dim.dim_ass_energy_cons_installation_df.region_code is 'Region Code';
comment on column coss_dim.dim_ass_energy_cons_installation_df.region_desc is 'Region Description';
comment on column coss_dim.dim_ass_energy_cons_installation_df.i_type_id is 'Installation Type Id';
comment on column coss_dim.dim_ass_energy_cons_installation_df.i_type_code is 'Installation Type Code';
comment on column coss_dim.dim_ass_energy_cons_installation_df.i_type_desc is 'Installation Type  Description';
comment on column coss_dim.dim_ass_energy_cons_installation_df.fw_portion is 'Fresh Portion';
comment on column coss_dim.dim_ass_energy_cons_installation_df.sw_portion is 'Salt Water Portion';
comment on column coss_dim.dim_ass_energy_cons_installation_df.rw_portion is 'Raw Water Portion';
comment on column coss_dim.dim_ass_energy_cons_installation_df.tw_portion is 'Treatment Works Portion';
comment on column coss_dim.dim_ass_energy_cons_installation_df.remarks is 'Remarks';
comment on column coss_dim.dim_ass_energy_cons_installation_df.is_active is 'Is Active';
comment on column coss_dim.dim_ass_energy_cons_installation_df.official_name is 'Official Name';
comment on column coss_dim.dim_ass_energy_cons_installation_df.station_code is 'Station Code';
comment on column coss_dim.dim_ass_energy_cons_installation_df.is_billing is 'Billing Is Active';
comment on column coss_dim.dim_ass_energy_cons_installation_df.is_ps is 'Pump Station Is Active';
comment on column coss_dim.dim_ass_energy_cons_installation_df.is_ecw is 'Ecw Is Active';
comment on column coss_dim.dim_ass_energy_cons_installation_df.region_rpt is 'Region Report';
comment on column coss_dim.dim_ass_energy_cons_installation_df.is_hkp is 'Hkp Is Active';
comment on column coss_dim.dim_ass_energy_cons_installation_df.is_fy is 'Fy Is Active';
comment on column coss_dim.dim_ass_energy_cons_installation_df.is_water_eff is 'Water Efficiency Is Active';
comment on column coss_dim.dim_ass_energy_cons_installation_df.water_eff_type_id is 'Installation Type Id For Water Efficiency';
comment on column coss_dim.dim_ass_energy_cons_installation_df.i_num is 'Installation Number';
comment on column coss_dim.dim_ass_energy_cons_installation_df.dim_update_time is 'Data Update Time';
comment on column coss_dim.dim_ass_energy_cons_installation_df.dim_load_time is 'Data Loading Time';
comment on column coss_dim.dim_ass_energy_cons_installation_df.dt is 'Date Time';
```

Load Date

> 这部分不要放在数仓代码中

```sql
insert into coss_dim.dim_ass_energy_cons_installation_df
select
    asset_id                                -- Energy Consumption Installations
    ,asset_name                             -- Asset Id
    ,asset_desc                             -- Asset Name
    ,loca_code                              -- Asset Description
    ,acc_no                                 -- Location Code
    ,region_id                              -- Account No
    ,region_code                            -- Region Id
    ,region_desc                            -- Region Code
    ,i_type_id                              -- Region Description
    ,i_type_code                            -- Installation Type Id
    ,i_type_desc                            -- Installation Type Code
    ,fw_portion                             -- Installation Type  Description
    ,sw_portion                             -- Fresh Portion
    ,rw_portion                             -- Salt Water Portion
    ,tw_portion                             -- Raw Water Portion
    ,remarks                                -- Treatment Works Portion
    ,is_active                              -- Remarks
    ,official_name                          -- Is Active
    ,station_code                           -- Official Name
    ,is_billing                             -- Station Code
    ,is_ps                                  -- Billing Is Active
    ,is_ecw                                 -- Pump Station Is Active
    ,region_rpt                             -- Ecw Is Active
    ,is_hkp                                 -- Region Report
    ,is_fy                                  -- Hkp Is Active
    ,is_water_eff                           -- Fy Is Active
    ,water_eff_type_id                      -- Water Efficiency Is Active
    ,i_num                                  -- Installation Type Id For Water Efficiency
    ,localtimestamp dim_update_time         -- Installation Number
    ,localtimestamp dim_load_time           -- Data Update Time
    ,dt                                     -- Data Loading Time
from
    coss_dwd.dim_ass_energy_cons_installation_dfp;
```

## 2.coss_dim.dim_wtw_installation_info

```sql

-- coss_dim.dim_wtw_installation_info definition

-- Drop table
-- drop table coss_dim.dim_wtw_installation_info;

create table coss_dim.dim_wtw_installation_info (
    asset_id numeric(11) not null, -- Asset Id 
    asset_name varchar(120) null, -- Asset Name
    asset_desc varchar(120) null, -- Asset Descrip
    installation_id varchar(36) null, -- Installation ID
    loca_code varchar(15) null, -- Local Code
    region_abbr varchar(150) null, -- Region
    i_type_id numeric(11) null, -- Installation Type Id 
    i_type_code varchar(150) null, -- Installation Code 
    i_type_desc varchar(150) null, -- Installation Type Descrip
    dim_update_time timestamp(6) null default pg_systimestamp(), -- Dm Update Time
    dim_load_time timestamp(6) null default pg_systimestamp(), -- Dm Load Time
    constraint dim_wtw_installation_info_pkey primary key (asset_id)
)
with (
    orientation=row,
    compression=no
);
comment on table coss_dim.dim_wtw_installation_info is 'The Water Treatment Works Items';

-- Column comments
comment on column coss_dim.dim_wtw_installation_info.asset_id is 'Asset Id ';
comment on column coss_dim.dim_wtw_installation_info.asset_name is 'Asset Name';
comment on column coss_dim.dim_wtw_installation_info.asset_desc is 'Asset Descrip';
comment on column coss_dim.dim_wtw_installation_info.installation_id is 'Installation ID';
comment on column coss_dim.dim_wtw_installation_info.loca_code is 'Local Code';
comment on column coss_dim.dim_wtw_installation_info.region_abbr is 'Region';
comment on column coss_dim.dim_wtw_installation_info.i_type_id is 'Installation Type Id ';
comment on column coss_dim.dim_wtw_installation_info.i_type_code is 'Installation Code ';
comment on column coss_dim.dim_wtw_installation_info.i_type_desc is 'Installation Type Descrip';
comment on column coss_dim.dim_wtw_installation_info.dim_update_time is 'Dm Update Time';
comment on column coss_dim.dim_wtw_installation_info.dim_load_time is 'Dm Load Time';
```

## 3.coss_dim.dim_ps_installation_info

```sql
-- coss_dim.dim_ps_installation_info definition

-- Drop table
drop table coss_dim.dim_ps_installation_info;

create table coss_dim.dim_ps_installation_info (
    asset_id numeric(10) not null, -- Asset Id
    region_abbr varchar(50) null, -- Region Abbr
    sub_region varchar(50) null, -- Sub Region
    i_code varchar(50) null, -- Installation_no
    i_type_code varchar(100), -- Installation Type Code
    i_type_desc varchar(100), -- Installation Type  Description
    ps_en varchar(100) null, -- Pump Station En Name
    ps_cn varchar(100) null, -- Pump Station Cn Name
    address_en varchar(100) null, -- Address En Name
    address_cn varchar(100) null, -- Address Cn Name
    dim_update_time timestamp(6) null default pg_systimestamp(), -- Dm Update Time
    dim_load_time timestamp(6) null default pg_systimestamp(), -- Dm Load Time
    constraint dim_ps_installation_info_pkey_g primary key (asset_id) by global index
)
with (
    orientation=row,
    compression=no
);
comment on table coss_dim.dim_ps_installation_info is 'The Monthly Pump Station Running Items';

-- Column comments
comment on column coss_dim.dim_ps_installation_info.asset_id is 'Asset Id';
comment on column coss_dim.dim_ps_installation_info.region_abbr is 'Region Abbr';
comment on column coss_dim.dim_ps_installation_info.sub_region is 'Sub Region';
comment on column coss_dim.dim_ps_installation_info.i_code is 'Installation_no';
comment on column coss_dim.dim_ps_installation_info.i_type_code is 'Installation Type Code';
comment on column coss_dim.dim_ps_installation_info.i_type_desc is 'Installation Type  Description';
comment on column coss_dim.dim_ps_installation_info.ps_en is 'Pump Station En Name';
comment on column coss_dim.dim_ps_installation_info.ps_cn is 'Pump Station Cn Name';
comment on column coss_dim.dim_ps_installation_info.address_en is 'Address En Name';
comment on column coss_dim.dim_ps_installation_info.address_cn is 'Address Cn Name';
comment on column coss_dim.dim_ps_installation_info.dim_update_time is 'Dm Update Time';
comment on column coss_dim.dim_ps_installation_info.dim_load_time is 'Dm Load Time';
```



# 附件

## 白名单电子邮件

```
Dear Mr. Hui,

Kindly note due to we have several different environments (development, integrated UAT, pre-production, etc.), so the IPs to be whitelisted are required for different environments, kindly see the below updates on the whitelist IPs:

 

Development environment
1.      10.66.169.48 ,10.66.169.209,10.66.169.236:  these three IPs are already whitelisted and still need to be used in development environment, so cannot be removed from the whitelist

2.      10.66.94.131, 10.66.94.146,10.66.94.113,10.66.94.88 can be removed from whitelist

 

2.      New IPs to be whitelisted for IUAT environment (5 IPs)

3.      10.66.168.174, 10.66.168.41, 10.66.168.113, 10.66.168.151, 10.66.5.94

 

3.      New IPs to be whitelisted for pre-production environment (4 IPs)

4.      10.66.168.212, 10.66.168.11, 10.66.168.85, 10.66.168.253

 

Let me know if you have any questions, many thanks for your help.
```

## comment code

```sql
select
     to_char(coalesce(max(bill_date), '1900-01-01 00:00:00')- INTERVAL '6 months','yyyyMM')  as bill_date
from coss_ods.ods_emis_bills_di_year


select
     coalesce(max(bill_date), '1900-01-01 00:00:00') as bill_date
from coss_ods.ods_emis_bills_di_year

```













```sql
# -*- coding: utf-8 -*-
"""
EMS Pump Report Data Acquisition and Storage Script
Function:
1. Parse start/end date parameters (supports command-line input for start date: YYYYMM format)
2. Fetch distinct asset IDs from GaussDB dimension table
3. Call EMS API to get pump report data for each asset
4. Standardize irregular data into 2D array and convert to DataFrame
5. Insert data into GaussDB target table (coss_ods.ods_emis_report_di_year)
Dependencies: requests, pandas, gaussdb, config, request_json
"""
# 1. Import modules (sorted by: standard library → third-party → custom)
import sys
from datetime import datetime
import requests
import json
import pandas as pd

# Custom modules (project-specific DB connector and API functions)
import config
import request_json
import gaussdb


def fetch_and_save_ems_pump_report():
    """
    Main function to handle EMS pump report data flow:
    - Initialize date range parameters
    - Connect to GaussDB and fetch asset IDs
    - Fetch report data via EMS API
    - Standardize and load data to DataFrame
    - Save to GaussDB and release resources
    """
    # --------------------------
    # Step 1: Initialize Date Range
    # --------------------------
    # Default end date: Current date (format: YYYY-MM-DD)
    end_date = datetime.now().strftime("%Y-%m-%d")
    # Default start date: Empty string (API uses default range if not provided)
    start_date = ""

    # Parse command-line argument for start date (input format: YYYYMM, e.g., 202501 → 2025-01-01)
    if len(sys.argv) == 2:
        input_date_str = sys.argv[1]
        # Validate input format (6-digit numeric string for YYYYMM)
        if len(input_date_str) == 6 and input_date_str.isdigit():
            start_date = f"{input_date_str[:4]}-{input_date_str[4:]}-01"
        else:
            print(f"[ERROR] Invalid input format! Use YYYYMM (e.g., '202501' for January 2025)")
            return  # Exit if input is invalid

    print(f"[INFO] Data fetch range - Start: {start_date if start_date else 'API Default'}, End: {end_date}")

    # --------------------------
    # Step 2: Connect to GaussDB (Fetch Asset IDs)
    # --------------------------
    db_conn = None  # Initialize DB connection variable
    try:
        # Create GaussDB connection using config
        db_conn = gaussdb.GaussDB(**config.GAUSSDB_DWS)
        print(f"[INFO] Successfully connected to GaussDB")

        # Fetch distinct asset IDs from dimension table
        asset_sql = "SELECT DISTINCT asset_id FROM coss_dim.dim_ass_energy_cons_installation_df"
        asset_records = db_conn.fetch_data(asset_sql)
        
        # Extract asset IDs from query results (fix original variable name error: 'records' → 'asset_records')
        asset_list = [record[0] for record in asset_records]  # record[0] since fetch_data returns tuple per row
        print(f"[INFO] Fetched {len(asset_list)} distinct asset IDs from dimension table")

        if not asset_list:
            print(f"[WARNING] No asset IDs found in dimension table. Exiting...")
            return

    except Exception as db_err:
        print(f"[ERROR] GaussDB operation failed: {str(db_err)}")
        return
    finally:
        # Close DB connection immediately after fetching asset IDs (no further DB ops here)
        if db_conn:
            try:
                db_conn.close()
                print(f"[INFO] GaussDB connection closed")
            except Exception as close_err:
                print(f"[WARNING] Failed to close GaussDB connection: {str(close_err)}")

    # --------------------------
    # Step 3: Fetch EMS Pump Report Data via API
    # --------------------------
    raw_report_data = []  # Store raw API response for each asset

    for asset_id in asset_list:
        try:
            # Construct API URL with current asset ID and date range
            api_url = f"https://wiki.sis2.wsd.gov/ems/webresources/reports?loc_id={asset_id}&from={start_date}&to={end_date}"
            
            # Call custom API function to get pump report (pass asset_id for tracking)
            asset_report = request_json.get_pump_report(api_url, asset_id)
            
            if asset_report:
                raw_report_data.append(asset_report)
                print(f"[INFO] Successfully fetched report for asset ID: {asset_id}")
            else:
                print(f"[WARNING] No report data returned for asset ID: {asset_id}")

        except Exception as api_err:
            print(f"[ERROR] Failed to fetch report for asset ID {asset_id}: {str(api_err)}")
            continue  # Skip to next asset if API request fails

    # --------------------------
    # Step 4: Standardize Data & Convert to DataFrame
    # --------------------------
    # Flatten irregular nested array into standard 2D array
    standardized_data = []
    for asset_data in raw_report_data:
        for item in asset_data:
            standardized_data.append(item)

    print(f"[INFO] Total standardized report records: {len(standardized_data)}")

    # Define DataFrame columns (align with EMS API response structure)
    report_columns = [
        "rpt_id", "asset_id", "pump_num", "cat_id", "cat_name",
        "drive_id", "drive_name", "del_id", "del_name", "del__asset_id",
        "design_flow", "run_hours", "pump_qty", "avg_suct", "avg_del",
        "design_flow_flag", "run_hours_flag", "pump_qty_flag",
        "avg_suct_flag", "avg_del_flag", "dw_etl_time", "mh"
    ]

    # Create DataFrame and add load time timestamp
    try:
        df_report = pd.DataFrame(standardized_data, columns=report_columns)
        df_report["ods_load_time"] = pd.Timestamp.now()  # Add ETL load time
        print(f"[INFO] DataFrame created with {len(df_report)} rows")
    except Exception as df_err:
        print(f"[ERROR] Failed to create DataFrame: {str(df_err)}")
        return

    # --------------------------
    # Step 5: Save Data to GaussDB
    # --------------------------
    target_table = "coss_ods.ods_emis_psr_report_di_year_tmp"
    constraint_keys = []  # No unique constraint keys defined for this table

    if not df_report.empty:
        try:
            # Call custom function to save DataFrame to GaussDB
            request_json.save_to_gaussdb(
                df=df_report,
                db_config=config.GAUSSDB_DWS,
                table_name=target_table,
                constraint_keys=constraint_keys
            )
            print(f"[SUCCESS] Saved {len(df_report)} records to {target_table}")
        except Exception as save_err:
            print(f"[ERROR] Failed to save data to GaussDB: {str(save_err)}")
    else:
        print(f"[WARNING] No data to save (DataFrame is empty)")


# --------------------------
# Script Entry Point
# --------------------------
if __name__ == "__main__":
    fetch_and_save_ems_pump_report()

```

