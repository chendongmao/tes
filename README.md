> 修改了开发环境的表结构，需要把新的表结构更新到 IUAT PRE ISIT Envrenment
# coss_dm.dm_cus_water_quality_wo_details_mini

## 备份数据

```sql
create table coss_tmp.dm_cus_water_quality_wo_details_mini_arch260430 as 
select * from coss_dm.dm_cus_water_quality_wo_details_mini
```

## 新表建表语句

```sql
drop table if exists coss_dm.dm_cus_water_quality_wo_details_mini;

create table if not exists coss_dm.dm_cus_water_quality_wo_details_mini (
	ordernum varchar(150) not null, -- Order Num
	region_abbr varchar(200) null, -- Region
	admin_division_code varchar(100) null, -- Administrative Area Code
	cpt_type_code varchar(100) null, -- Complaint Code
	urgency_code varchar(100) null, -- Urgency Code
	water_type_code varchar(100) null, -- Water Supply Type Code
	wo_status_code varchar(100) null, -- Ticket Status Code
	org_type_code varchar(100) null, -- Channel Status Code
	wq_cpt_type_code varchar(100) null, -- Water Quality Type Code
	dma_code varchar(100) null, -- Dma Code
	street varchar(200) null, -- Street
	estate varchar(200) null, -- Estate
	term varchar(200) null, -- Term
	village varchar(200) null, -- Village
	affect_building_code varchar(200) null, -- Affect Building Code
	building_tc varchar(100) null, -- Building Tc
	building_en varchar(100) null, -- Building En
	floor varchar(200) null, -- Floor
	isrepeatedcomplaint int4 null, -- Is Repeated Complaint
	relateorder varchar(150) null, -- Relate Order
	service_content varchar(500) null, -- Service Content
	post varchar(100) null, -- Position Of Responsible Person
	functionary varchar(100) null, -- Functionary Of Responsible Person
	phone varchar(100) null, -- Phone Of Responsible Person
	coordinate_x numeric(20, 6) null, -- X-Axis Coordinate
	coordinate_y numeric(20, 6) null, -- Y-Axis Coordinate
	region_receiving_date timestamp(6) null, -- Region Receiving Date
	create_time timestamp(6) null, -- Create Time
	finishtime timestamp(6) null, -- Create Time
	dm_update_time timestamp(6) null default pg_systimestamp(), -- Work Order Completion Time
	dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
	primary key (ordernum)
)
with (
	orientation=row,
	compression=no
);
comment on table coss_dm.dm_cus_water_quality_wo_details_mini is 'Customer Service Water Quality Word Order Details';

-- column comments

comment on column coss_dm.dm_cus_water_quality_wo_details_mini.ordernum is 'Order Num';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.region_abbr is 'Region';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.admin_division_code is 'Administrative Area Code';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.cpt_type_code is 'Complaint Code';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.urgency_code is 'Urgency Code';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.water_type_code is 'Water Supply Type Code';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.wo_status_code is 'Ticket Status Code';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.org_type_code is 'Channel Status Code';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.wq_cpt_type_code is 'Water Quality Type Code';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.dma_code is 'Dma Code';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.street is 'Street';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.estate is 'Estate';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.term is 'Term';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.village is 'Village';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.affect_building_code is 'Affect Building Code';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.building_tc is 'Building Tc';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.building_en is 'Building En';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.floor is 'Floor';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.isrepeatedcomplaint is 'Is Repeated Complaint';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.relateorder is 'Relate Order';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.service_content is 'Service Content';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.post is 'Position Of Responsible Person';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.functionary is 'Functionary Of Responsible Person';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.phone is 'Phone Of Responsible Person';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.coordinate_x is 'X-Axis Coordinate';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.coordinate_y is 'Y-Axis Coordinate';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.region_receiving_date is 'Region Receiving Date';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.create_time is 'Create Time';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.finishtime is 'Finish Time';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.dm_update_time is 'Update Time';
comment on column coss_dm.dm_cus_water_quality_wo_details_mini.dm_load_time is 'Loading Time';
```

## 恢复数据

```sql
insert into coss_dm.dm_cus_water_quality_wo_details_mini
select * from coss_tmp.dm_cus_water_quality_wo_details_mini_arch260430
```



# dm_wtw_opc_data_latest_minf

## 备份数据

```sql
create table coss_tmp.dm_wtw_opc_data_latest_minf_arch260430 as 
select * from coss_dm.dm_wtw_opc_data_latest_minf
```

## 新表建表语句

```
drop table if exists coss_dm.dm_wtw_opc_data_latest_minf;
create table if not exists coss_dm.dm_wtw_opc_data_latest_minf (
	id bigserial not null,
	i_code varchar(50) not null,
    region_abbr  varchar(50) ,
    wtw_name_en  varchar(128) null,
    wtw_name_cn  varchar(128) null,
    wtw_name_tc  varchar(128) null,
    tag_name_cn  varchar(128) null,
    tag_name_tc  varchar(128) null,
    units        varchar(128) null,
    tag_type     varchar(128) null,
	tag_name     varchar(128) null,
	tag_value     decimal(25,5) null,
    tag_value_avg decimal(25,5) null,
    tag_value_min decimal(25,5) null,
    tag_value_max decimal(25,5) null,
    quality  int,
	tag_time timestamp not null,
	dm_update_time timestamp(6) not null,
    dm_load_time timestamp(6) not null,
    primary key(i_code, tag_name)
)
with (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
);
comment on table  coss_dm.dm_wtw_opc_data_latest_minf                     is 'Water Treatment Work Tag Opc Data Latest';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.id                  is 'Id';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.i_code              is 'Install Code';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.region_abbr         is 'Region Abbreviation';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.wtw_name_en         is 'Water Treatment Work English Name';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.wtw_name_cn         is 'Water Treatment Work Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.wtw_name_tc         is 'Water Treatment Work Traditional Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.tag_name_cn         is 'Tag Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.tag_name_tc         is 'Tag Traditional Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.units               is 'Tag Units';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.tag_type            is 'Tag Type';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.tag_name            is 'Tag Name';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.tag_value           is 'Tag Value';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.tag_value_avg       is 'Tag Value Avg';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.tag_value_min       is 'Tag Value Min';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.tag_value_max       is 'Tag Value Max';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.quality             is 'Quality';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.tag_time            is 'Tag Time';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.dm_update_time      is 'Update Time';
comment on column coss_dm.dm_wtw_opc_data_latest_minf.dm_load_time        is 'Load Time';
```

## 恢复数据

```sql
insert into coss_dm.dm_wtw_opc_data_latest_minf
select 
  id
  ,i_code
  ,region_abbr
  ,wtw_name_en
  ,wtw_name_cn
  ,wtw_name_tc
  ,tag_name_cn
  ,tag_name_tc
  ,units
  ,tag_type
  ,tag_name
  ,tag_value
  ,null tag_value_avg
  ,null tag_value_min
  ,null tag_value_max
  ,quality
  ,tag_time
  ,current_timestamp dm_update_time
  ,current_timestamp dm_load_time
from 
	coss_tmp.dm_wtw_opc_data_latest_minf_arch260430 
```

# dm_wtw_opc_data_mini_month

## 备份数据

```sql
create table coss_tmp.dm_wtw_opc_data_mini_month_arch260430 as 
select * from coss_dm.dm_wtw_opc_data_mini_month
```

## 新表建表语句

```sql
-- Drop table if exists
drop table if exists coss_dm.dm_wtw_opc_data_mini_month;

-- Create table with range partition and storage parameters
create table if not exists coss_dm.dm_wtw_opc_data_mini_month (
    id              bigserial      not null,
    i_code          varchar(50)    not null,
    region_abbr     varchar(50)    null,
    wtw_name_en     varchar(128)   null,
    wtw_name_cn     varchar(128)   null,
    wtw_name_tc     varchar(128)   null,
    tag_name_cn     varchar(128)   null,
    tag_name_tc     varchar(128)   null,
    units           varchar(128)   null,
    tag_type        varchar(128)   null,
    tag_name        varchar(128)   null,
    tag_value       decimal(25,5)  null,
    tag_value_avg   decimal(25,5)  null,
    tag_value_min   decimal(25,5)  null,
    tag_value_max   decimal(25,5)  null,
    quality         int            null,
    tag_time        timestamp      not null,
    dm_update_time  timestamp(6)      not null,
    dm_load_time    timestamp(6)   not null,
    primary key (i_code, tag_name, tag_time)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
partition by range (tag_time) (
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
-- Add table and column comments
comment on table coss_dm.dm_wtw_opc_data_mini_month is 'Water Treatment Work Tag Opc History Data';
comment on column coss_dm.dm_wtw_opc_data_mini_month.id is 'Id';
comment on column coss_dm.dm_wtw_opc_data_mini_month.i_code is 'Install Code';
comment on column coss_dm.dm_wtw_opc_data_mini_month.region_abbr is 'Region Abbreviation';
comment on column coss_dm.dm_wtw_opc_data_mini_month.wtw_name_en is 'Water Treatment Work English Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.wtw_name_cn is 'Water Treatment Work Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.wtw_name_tc is 'Water Treatment Work Traditional Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_name_cn is 'Tag Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_name_tc is 'Tag Traditional Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.units is 'Tag Units';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_type is 'Tag Type';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_name is 'Tag Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_value is 'Tag Value';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_value_avg is 'Tag Value Avg';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_value_min is 'Tag Value Min';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_value_max is 'Tag Value Max';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_value_avg is 'Tag Value Avg';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_value_min is 'Tag Value Min';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_value_max is 'Tag Value Max';
comment on column coss_dm.dm_wtw_opc_data_mini_month.quality is 'Quality';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_time is 'Tag Time';
comment on column coss_dm.dm_wtw_opc_data_mini_month.dm_update_time is 'Update Time';
comment on column coss_dm.dm_wtw_opc_data_mini_month.dm_load_time is 'Load Time';

```

## 恢复数据

```sql
insert into coss_dm.dm_wtw_opc_data_mini_month
select 
  id
  ,i_code
  ,region_abbr
  ,wtw_name_en
  ,wtw_name_cn
  ,wtw_name_tc
  ,tag_name_cn
  ,tag_name_tc
  ,units
  ,tag_type
  ,tag_name
  ,tag_value
  ,null tag_value_avg
  ,null tag_value_min
  ,null tag_value_max
  ,quality
  ,tag_time
  ,current_timestamp dm_update_time
  ,current_timestamp dm_load_time
from 
	coss_tmp.dm_wtw_opc_data_mini_month_arch260430 
```


















# pakkong

## ods_dcs_extract_pakkong_min(调度任务)

### ods_dcs_wtw_opc_data_pakkong_minf

#### create table

```sql
drop table if exists coss_ods.ods_dcs_wtw_opc_data_pakkong_minf;
create table if not exists coss_ods.ods_dcs_wtw_opc_data_pakkong_minf (
    id bigserial not null,
    tag_name varchar(128) null,
    tag_value decimal(25,5) null,
    tag_value_avg decimal(25,5) null,
    tag_value_min decimal(25,5) null,
    tag_value_max decimal(25,5) null,
    quality int4 not null,
    tag_time timestamp not null,
    ms_sql_time timestamp not null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time   timestamp(6) default current_timestamp,
    primary key (tag_name)
);
comment on table  coss_ods.ods_dcs_wtw_opc_data_pakkong_minf                   is 'water treatment work tag poc data latest';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.id                is 'id';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.tag_name          is 'tag name';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.tag_value         is 'tag value';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.tag_value_avg     is 'tag value avg';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.tag_value_min     is 'tag value min';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.tag_value_max     is 'tag value max';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.quality           is 'quality';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.tag_time          is 'tag time';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.ms_sql_time       is 'ms sql time';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.ods_update_time   is 'ods update time';
comment on column coss_ods.ods_dcs_wtw_opc_data_pakkong_minf.ods_load_time     is 'ods load time';
```

#### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Monitoring For pakkong
-- create         by: dongmaochen
-- create       date: 2026-03-30
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dcs.opc_data_pakkong
-- coss_dim.dim_wtw_tag_info
-- target table
-- coss_ods.ods_dcs_wtw_opc_data_pakkong_minf
-- ****************************************************************************************
-- insert into coss_ods.ods_dcs_wtw_opc_data_pakkong_minf
select
    t.id,                              -- id
    t.tag_name,                        -- tag name
    t.tag_value,                       -- tag value
    t.tag_value_avg,                   -- tag value avg
    t.tag_value_min,                   -- tag value min
    t.tag_value_max,                   -- tag value max
    t.quality,                         -- quality
    t.tag_time,                        -- tag time
    t.ms_sql_time,                     -- ms sql time
    current_timestamp ods_update_time, -- ods update time
    current_timestamp ods_load_time    -- ods load time
from coss_dcs.opc_data_pakkong t
  inner join coss_dim.dim_wtw_tag_info t1 on t.tag_name = t1.tag_name_en where t1.i_code = 'TW020'
```



### ods_dcs_wtw_opc_data_full_pakkong_mini_month

#### create table

```sql
drop table if exists coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month;
create table if not exists coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month (
    id bigserial not null,
    tag_name varchar(128) not null,
    tag_value decimal(25,5) null,
    tag_value_avg decimal(25,5) null,
    tag_value_min decimal(25,5) null,
    tag_value_max decimal(25,5) null,
    quality int4 not null,
    tag_time timestamp not null,
    ms_sql_time timestamp not null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time   timestamp(6) default current_timestamp,
    primary key (tag_name, tag_time)
)
partition by range (tag_time)
(
    partition mh_202506 values less than ('2025-07-01 00:00:00'),
    partition mh_202512 values less than ('2026-01-01 00:00:00'),
    partition mh_202606 values less than ('2026-07-01 00:00:00'),
    partition mh_202612 values less than ('2027-01-01 00:00:00'),
    partition mh_202706 values less than ('2027-07-01 00:00:00'),
    partition mh_202712 values less than ('2028-01-01 00:00:00'),
    partition mh_202806 values less than ('2028-07-01 00:00:00'),
    partition mh_202812 values less than ('2029-01-01 00:00:00'),
    partition mh_future values less than ('9999-01-01 00:00:00')
);
comment on table  coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month                   is 'water treatment work tag poc history data';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.id                is 'id';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.tag_name          is 'tag name';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.tag_value         is 'tag value';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.tag_value_avg     is 'tag value avg';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.tag_value_min     is 'tag value min';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.tag_value_max     is 'tag value max';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.quality           is 'quality';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.tag_time          is 'tag time';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.ms_sql_time       is 'ms sql time';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.ods_update_time   is 'ods update time';
comment on column coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month.ods_load_time     is 'ods load time';

```

#### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Monitoring For pakkong
-- create         by: dongmaochen
-- create       date: 2025-10-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table: coss_ods.ods_dcs_wtw_opc_data_pakkong_minf
-- target table: coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month
-- ****************************************************************************************
insert into coss_ods.ods_dcs_wtw_opc_data_full_pakkong_mini_month (
    id,
    tag_name,
    tag_value,
    tag_value_avg,
    tag_value_min,
    tag_value_max,
    quality,
    tag_time,
    ms_sql_time,
    ods_update_time,
    ods_load_time
)
select
    t.id,                              -- id
    t.tag_name,                        -- tag name
    t.tag_value,                       -- tag value
    t.tag_value_avg,                   -- tag value avg
    t.tag_value_min,                   -- tag value min
    t.tag_value_max,                   -- tag value max
    t.quality,                         -- quality
    t.tag_time,                        -- tag time
    t.ms_sql_time,                     -- ms sql time
    current_timestamp as ods_update_time, -- ods update time
    current_timestamp as ods_load_time    -- ods load time
from coss_ods.ods_dcs_wtw_opc_data_pakkong_minf t
on duplicate key update nothing;
```



## dwd_wtw_etl_pakkong_monitoring_min（调度任务）

### dwd_wtw_opc_data_latest_minf

#### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Monitoring For pakkong
-- create         by: dongmaochen
-- create       date: 2025-10-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_ods.ods_dcs_wtw_opc_data_pakkong_minf
-- coss_dim.dim_wtw_tag_info
-- target table
-- coss_dwd.dwd_wtw_opc_data_latest_minf
-- ****************************************************************************************
insert into coss_dwd.dwd_wtw_opc_data_latest_minf (
    id,
    i_code,
    tag_name,
    tag_value,
    tag_value_avg,
    tag_value_min,
    tag_value_max,
    quality,
    tag_time,
    dwd_update_time,
    dwd_load_time
)
select
    id,                                 -- id
    'TW020' as i_code,                  -- install code
    tag_name,                           -- tag name
    case
        when tag_name in ('HVPumpSuctionPress_Press', 'JunkBayDeliveryPress_Press')
        then tag_value / 9.81
        else tag_value
    end as tag_value, -- KPa转m（m = KPa/9.81）

    case
        when tag_name in ('HVPumpSuctionPress_Press', 'JunkBayDeliveryPress_Press')
        then tag_value_avg / 9.81
        else tag_value_avg
    end as tag_value_avg, -- KPa转m（m = KPa/9.81）

    case
        when tag_name in ('HVPumpSuctionPress_Press', 'JunkBayDeliveryPress_Press')
        then tag_value_min / 9.81
        else tag_value_min
    end as tag_value_min, -- KPa转m（m = KPa/9.81）

    case
        when tag_name in ('HVPumpSuctionPress_Press', 'JunkBayDeliveryPress_Press')
        then tag_value_max / 9.81
        else tag_value_max
    end as tag_value_max, -- KPa转m（m = KPa/9.81）
    quality,                            -- quality
    tag_time,                           -- tag time
    current_timestamp as dwd_update_time,  -- dwd update time
    current_timestamp as dwd_load_time     -- dwd load time
from coss_ods.ods_dcs_wtw_opc_data_pakkong_minf
on duplicate key update
    id = values(id),
    tag_value = values(tag_value),
    tag_value_avg = values(tag_value_avg),
    tag_value_min = values(tag_value_min),
    tag_value_max = values(tag_value_max),
    quality = values(quality),
    tag_time = values(tag_time),
    dwd_update_time = values(dwd_update_time);
```







### dwd_wtw_opc_data_mini_month

#### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Monitoring For pakkong
-- create         by: dongmaochen
-- create       date: 2025-10-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dwd_wtw_opc_data_latest_minf
-- target table
-- coss_dwd.dwd_wtw_opc_data_mini_month
-- ****************************************************************************************
insert into coss_dwd.dwd_wtw_opc_data_mini_month (
    id,
    i_code,
    tag_name,
    tag_value,
    tag_value_avg,
    tag_value_min,
    tag_value_max,
    quality,
    tag_time,
    dwd_update_time,
    dwd_load_time
)
select
    id,                                    -- id
    i_code,                                -- install code
    tag_name,                              -- tag name
    tag_value,                             -- tag value
    tag_value_avg,                         -- tag value avg
    tag_value_min,                         -- tag value min
    tag_value_max,                         -- tag value max
    quality,                               -- quality
    tag_time,                              -- tag time
    current_timestamp as dwd_update_time,  -- dwd update time
    current_timestamp as dwd_load_time     -- dwd load time
from coss_dwd.dwd_wtw_opc_data_latest_minf t
where i_code = 'TW020'
on duplicate key update nothing;
```

## dm_wtw_etl_pakkong_monitoring_min（调度任务）

### dm_wtw_opc_data_latest_minf

#### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Monitoring For pakkong
-- create         by: dongmaochen
-- create       date: 2025-10-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dwd_wtw_opc_data_latest_minf
-- coss_dim.dim_wtw_tag_info
-- target table
-- coss_dm.dm_wtw_opc_data_latest_minf
-- ****************************************************************************************
insert into coss_dm.dm_wtw_opc_data_latest_minf (
    id,
    i_code,
    region_abbr,
    wtw_name_en,
    wtw_name_cn,
    wtw_name_tc,
    tag_name_cn,
    tag_name_tc,
    units,
    tag_type,
    tag_name,
    tag_value,
    tag_value_avg,
    tag_value_min,
    tag_value_max,
    quality,
    tag_time,
    dm_update_time,
    dm_load_time
)
select
    t.id,                              -- id
    t1.i_code,                         -- install code
    t1.region_abbr,                    -- region abbreviation
    t1.wtw_name_en,                    -- water treatments work english name
    t1.wtw_name_cn,                    -- water treatments work chinese name
    t1.wtw_name_tc,                    -- water treatments work traditional chinese name
    t1.tag_name_cn,                    -- tag chinese name
    t1.tag_name_tc,                    -- tag traditional chinese name
    t1.units,                          -- tag units
    t1.tag_type,                       -- tag type
    t.tag_name,                        -- tag name
    t.tag_value,                       -- tag value
    t.tag_value_avg,                   -- tag value avg
    t.tag_value_min,                   -- tag value min
    t.tag_value_max,                   -- tag value max
    t.quality,                         -- quality
    t.tag_time,                        -- tag time
    current_timestamp as dm_update_time,  -- dm update time
    current_timestamp as dm_load_time     -- dm load time
from coss_dwd.dwd_wtw_opc_data_latest_minf t
inner join coss_dim.dim_wtw_tag_info t1
    on t.tag_name = t1.tag_name_en
where t1.i_code = 'TW020'
on duplicate key update     id = values(id),
    region_abbr = values(region_abbr),
    wtw_name_en = values(wtw_name_en),
    wtw_name_cn = values(wtw_name_cn),
    wtw_name_tc = values(wtw_name_tc),
    tag_name_cn = values(tag_name_cn),
    tag_name_tc = values(tag_name_tc),
    units = values(units),
    tag_type = values(tag_type),
    tag_value = values(tag_value),
    tag_value_avg = values(tag_value_avg),
    tag_value_min = values(tag_value_min),
    tag_value_max = values(tag_value_max),
    quality = values(quality),
    tag_time = values(tag_time),
    dm_load_time = values(dm_load_time);
```



### dm_wtw_opc_data_mini_month

#### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Monitoring For pakkong
-- create         by: dongmaochen
-- create       date: 2025-10-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dm.dm_wtw_opc_data_latest_minf
-- target table
-- coss_dm.dm_wtw_opc_data_mini_month
-- ****************************************************************************************
insert into coss_dm.dm_wtw_opc_data_mini_month (
    id,
    i_code,
    region_abbr,
    wtw_name_en,
    wtw_name_cn,
    wtw_name_tc,
    tag_name_cn,
    tag_name_tc,
    units,
    tag_type,
    tag_name,
    tag_value,
    tag_value_avg,
    tag_value_min,
    tag_value_max,
    quality,
    tag_time,
    dm_update_time,
    dm_load_time
)
select
    id,                                -- id
    i_code,                            -- install code
    region_abbr,                       -- region abbreviation
    wtw_name_en,                       -- water treatments work english name
    wtw_name_cn,                       -- water treatments work chinese name
    wtw_name_tc,                       -- water treatments work traditional chinese name
    tag_name_cn,                       -- tag chinese name
    tag_name_tc,                       -- tag traditional chinese name
    units,                             -- tag units
    tag_type,                          -- tag type
    tag_name,                          -- tag name
    tag_value,                         -- tag value
    tag_value_avg,                     -- tag value avg
    tag_value_min,                     -- tag value min
    tag_value_max,                     -- tag value max
    quality,                           -- quality
    tag_time,                          -- tag time
    current_timestamp as dm_update_time,    -- dm update time
    current_timestamp as dm_load_time       -- dm load time
from coss_dm.dm_wtw_opc_data_latest_minf t
where t.i_code = 'TW020'
on duplicate key update nothing;
```









1. 预生产数据库权限开通
   - 数据库链接：jdbc:postgresql://10.66.110.64:8000,10.66.110.151:8000,10.66.110.194:8000,10.66.110.235:8000/wsd
   - coss账号开通ohap schema 的可读权限
2. uat数据库权限开通
   - 数据库链接：
   - dms_reader账号开通 dms_uat 的可读权限
   - 10.66.169.207 window 的网络能通
3. ISIT 数据库权限开通
   - 数据库链接：jdbc:postgresql://10.66.110.64:8000,10.66.110.151:8000,10.66.110.194:8000,10.66.110.235:8000/wsd_dm
   - coss账号开通pems schema 的可读权限









https://www.map.gov.hk/gm/map/



ods_pems_cus_water_sample_number_di


drop table if exists coss_dim.dim_tmu_dict_info;
CREATE TABLE if not exists coss_dim.dim_tmu_dict_info (
	code varchar(12) NOT NULL, -- Dictionary Code
	origin_code varchar(36) NULL, -- Origin Code
	"type" varchar(36) NOT NULL, -- Type
	name_cn varchar(64) NULL, -- Simplified Chinese Name
	name_tc varchar(64) NULL, -- Traditional Chinese Name
	name_en varchar(64) NULL, -- English Name
	dim_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Load Time
	dim_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	PRIMARY KEY (code, type)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dim.dim_tmu_dict_info IS 'Terminal User Dictionary Information';
COMMENT ON COLUMN coss_dim.dim_tmu_dict_info.code IS 'Dictionary Code';
COMMENT ON COLUMN coss_dim.dim_tmu_dict_info.origin_code IS 'Origin Code';
COMMENT ON COLUMN coss_dim.dim_tmu_dict_info."type" IS 'Type';
COMMENT ON COLUMN coss_dim.dim_tmu_dict_info.name_cn IS 'Simplified Chinese Name';
COMMENT ON COLUMN coss_dim.dim_tmu_dict_info.name_tc IS 'Traditional Chinese Name';
COMMENT ON COLUMN coss_dim.dim_tmu_dict_info.name_en IS 'English Name';
COMMENT ON COLUMN coss_dim.dim_tmu_dict_info.dim_load_time IS 'Data Load Time';
COMMENT ON COLUMN coss_dim.dim_tmu_dict_info.dim_update_time IS 'Data Update Time';




drop table if exists coss_dm.dm_tmu_user_customer_meter_item_di;
CREATE TABLE if not exists coss_dm.dm_tmu_user_customer_meter_item_di (
	statistical_year varchar(10) NOT NULL, -- Statistical Year
	region_abbr varchar(120) NOT NULL, -- Regional Abbreviation
	inter_item_code varchar(120) NOT NULL, -- internal item code
	item_value numeric(20, 5) NULL, -- item value
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time
	PRIMARY KEY (statistical_year,region_abbr,inter_item_code)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_tmu_user_customer_meter_item_di IS 'The Annual Customer Meter items';
COMMENT ON COLUMN coss_dm.dm_tmu_user_customer_meter_item_di.statistical_year IS 'Statistical Year';
COMMENT ON COLUMN coss_dm.dm_tmu_user_customer_meter_item_di.region_abbr IS 'Regional Abbreviation';
COMMENT ON COLUMN coss_dm.dm_tmu_user_customer_meter_item_di.inter_item_code IS 'internal item code';
COMMENT ON COLUMN coss_dm.dm_tmu_user_customer_meter_item_di.item_value IS 'item value';
COMMENT ON COLUMN coss_dm.dm_tmu_user_customer_meter_item_di.dm_update_time IS 'Data Update Time';
COMMENT ON COLUMN coss_dm.dm_tmu_user_customer_meter_item_di.dm_load_time IS 'Data Loading Time';






https://docs.qq.com/sheet/DWkdsQ2J4elhUcU5I?tab=000001



http://10.66.168.83/COSS/dashboard/workbench



Kwun Tong HL FWSR (Hach)

> FCL(DPD)
>
> FCL(CLT10SC)


<img width="361" height="504" alt="image-20260415102238943" src="https://github.com/user-attachments/assets/f7a6a918-6444-45e2-9190-a40be1089530" />





select device_name , count(1) aa  from coss_dim.dim_sz_device_info 
group by 
device_name 
order by 
device_name 





<img width="901" height="238" alt="image" src="https://github.com/user-attachments/assets/b39b020b-b2a7-4eb4-b9ca-367a1985063c" />



数仓连接：https://docs.qq.com/sheet/DUGdOTE9rdnJwb2xI?no_promotion=1&tab=fl8tx0
巡检表：https://docs.qq.com/sheet/DVG1CRE1wbExHWEVk?tab=000001


<img width="1672" height="782" alt="image" src="https://github.com/user-attachments/assets/f7d0e6d3-0b1b-4d6b-bf6a-378f8281cf04" />




-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function Describe: Terminal User Monitoring For Water Quality
-- Create         By: dongmaochen
-- Create       Date: 2026-04-08
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- Target Table:  
-- ****************************************************************************************
insert into coss_dm.dm_tmu_sensor_data_mini_month
select
	id,
	sensor_code,
	sensor_value,
	sensor_time,
	dm_update_time,
	dm_load_time
from
coss_dm.dm_tmu_sensor_data_stg_mini
on duplicate key update nothing






-- Get the latest one data record per sensor code with row number
with ranked_data as (
    select
        id,                                   -- Data id
        code as sensor_code,                  -- Sensor code
        value as sensor_value,                -- Sensor measure value
        to_timestamp(time / 1000) as sensor_time, -- Sensor data time
        -- Group by code, order by time desc to pick the latest record
        row_number() over (partition by code order by time desc) as rn
    from iot.data_gw
    where code in (
        'FWBDKN05002Q00101',
        'FWBDKN05002Q00102',
        'FWBDKN05002Q00103',
        'FWBDKN05002Q00104',
        'FWBDKN05002Q00105',
        'FWPHNW04006Q00101',
        'FWPHNW04006Q00102',
        'FWPHNW04006Q00103',
        'FWPHNW04006Q00104',
        'FWPHNW04006Q00105',
        'FWPRKN04052Q00101',
        'FWPRKN04052Q00102',
        'FWPRKN04052Q00103',
        'FWPRKN04052Q00104',
        'FWPRKN04052Q00105',
        'FWPRKN04052Q00201',
        'FWSRKN02229Q00101',
        'FWSRKN02229Q00102',
        'FWSRKN02229Q00103',
        'FWSRKN02229Q00104',
        'FWSRKN02229Q00105',
        'FWSRKN03085Q00101',
        'FWSRKN03085Q00102',
        'FWSRKN03085Q00103',
        'FWSRKN03085Q00104',
        'FWSRKN03085Q00105',
        'FWSRKN03085Q00201',
        'FWSRKN04011Q00101',
        'FWSRKN04011Q00102',
        'FWSRKN04011Q00103',
        'FWSRKN04011Q00110',
        'FWSRKN04020Q00101',
        'FWSRKN04020Q00103',
        'FWSRKN04020Q00104',
        'FWSRKN05058Q00104',
        'FWSRKN05058Q00105',
        'FWSRKN05058Q00110',
        'FWSRKN05058Q00111',
        'FWSRKN05074Q00101',
        'FWSRKN05074Q00102',
        'FWSRKN05074Q00103',
        'FWSRKN05074Q00104',
        'FWSRKN05074Q00107',
        'FWSRKN05074Q00201',
        'FWSRNW04023Q00101',
        'FWSRNW04023Q00102',
        'FWSRNW04023Q00103',
        'FWSRNW04023Q00104',
        'FWSRNW04023Q00105',
        'FWSRNW01109Q00101',
        'FWSRNW01109Q00102',
        'FWSRNW01109Q00103',
        'FWSRNW01109Q00104',
        'FWSRNW01109Q00105',
        'FWSRNW04082Q00101',
        'FWSRNW04082Q00102',
        'FWSRNW04082Q00103',
        'FWSRNW04082Q00104',
        'FWSRNW04082Q00105',
        'FWWMNW03001Q00101',
        'FWWMNW03001Q00102',
        'FWWMNW03001Q00103',
        'FWWMNW03001Q00104',
        'FWWMNW03001Q00105',
        'FWWMNW04001Q00101',
        'FWWMNW04001Q00102',
        'FWWMNW04001Q00103',
        'FWWMNW04001Q00104',
        'FWWMNW04001Q00105',
        'FWWSKN02005Q00101',
        'FWWSKN02005Q00102',
        'FWWSKN02005Q00103',
        'FWWSKN02005Q00104',
        'FWWSKN02005Q00105'
    )
)
select
    id,
    sensor_code,
    sensor_value,
    sensor_time,
    current_timestamp as dm_update_time,      -- Data warehouse update time
    current_timestamp as dm_load_time         -- Data warehouse load time
from ranked_data
where rn = 1;











https://docs.qq.com/sheet/DUGdOTE9rdnJwb2xI?no_promotion=1&tab=fl8tx0


https://www.map.gov.hk/gm/map/search/xy/wgs84



select 
* 
from 
coss_dm.dm_cus_water_quality_wo_details_mini
where ordernum in 
('202505161427287554795',
'202505178427287551516',
'202505178427287554524',
'202505178427287551513',
'202505178427287554546',
'202505178427287554515',
'202505178427287554513',
'202505178427287554550',
'202505178427287554547',
'202505178427287551518',
'202505178427287551522',
'202505178427287551519',
'202505178427287551524',
'202505161427287554794',
'202505178427287554553',
'202505178427287554544',
'202505178427287554541',
'202505161427287554796',
'202505178427287554520',
'202505178427287554514',
'202505178427287551510',
'202505178427287551520',
'202505178427287554519',
'202505178427287551521',
'202505178427287554549',
'202505178427287554511',
'202505178427287554543',
'202505178427287551515',
'202505178427287551523',
'202505178427287551511',
'202505178427287551517',
'202505161427287554793',
'202505178427287554517',
'202505178427287554510',
'202505178427287554518',
'202505178427287551514',
'202505178427287554522',
'202505178427287554552',
'202505178427287554548',
'202505178427287554545',
'202505178427287554512',
'202505178427287551512',
'202505178427287554542',
'202505178427287554554',
'202505178427287554551',
'202505178427287554521',
'202505178427287554523',
'202505178427287554516')







<img width="1866" height="906" alt="image" src="https://github.com/user-attachments/assets/426f5319-5cd8-4b98-8765-4b32fe76b6b6" />





<img width="1683" height="850" alt="image-20260408181827059" src="https://github.com/user-attachments/assets/fc292b35-ebd9-422b-bc1a-733b11f5cc76" />



| CODE | DESC         |
| ---- | ------------ |
| 数分 | 数据分析     |
| 数开 | 数据开发     |
| 数配 | 页面数据配置 |
| 原改 | 原型修改     |
| 优化 | 页面优化     |


-- coss_dim.dim_wqp_dict_info definition

-- Drop table

-- DROP TABLE coss_dim.dim_wqp_dict_info;

CREATE TABLE coss_dim.dim_wqp_dict_info (
	code varchar(12) NOT NULL, -- Dictionary Code
	origin_code varchar(36) NULL, -- Origin Code
	"type" varchar(36) NOT NULL, -- Type
	name_cn varchar(64) NULL, -- Simplified Chinese Name
	name_tc varchar(64) NULL, -- Traditional Chinese Name
	name_en varchar(64) NULL, -- English Name
	dim_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Load Time
	dim_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	CONSTRAINT dim_wqp_dict_info_pkey PRIMARY KEY (code,"type")
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dim.dim_wqp_dict_info IS 'Water Quality Parameters Dictionary Information';

-- Column comments

COMMENT ON COLUMN coss_dim.dim_wqp_dict_info.code IS 'Dictionary Code';
COMMENT ON COLUMN coss_dim.dim_wqp_dict_info.origin_code IS 'Origin Code';
COMMENT ON COLUMN coss_dim.dim_wqp_dict_info."type" IS 'Type';
COMMENT ON COLUMN coss_dim.dim_wqp_dict_info.name_cn IS 'Simplified Chinese Name';
COMMENT ON COLUMN coss_dim.dim_wqp_dict_info.name_tc IS 'Traditional Chinese Name';
COMMENT ON COLUMN coss_dim.dim_wqp_dict_info.name_en IS 'English Name';
COMMENT ON COLUMN coss_dim.dim_wqp_dict_info.dim_load_time IS 'Data Load Time';
COMMENT ON COLUMN coss_dim.dim_wqp_dict_info.dim_update_time IS 'Data Update Time';







import requests
import json

# API基础配置
API_URL = "http://10.66.169.58:8001/iot3/rest/api/v1/realtime.json"
HEADERS = {
    "Content-Type": "application/json; charset=utf-8",
}

request_data = {
  "codes": [
    "FWWSKN02005Q00101",
    "FWBDKN05002Q00102",
    "FWSRNW04023Q00102",
    "FWSRNW04023Q00103",
    "FWWSKN02005Q00102",
    "FWBDKN05002Q00102",
    "FWSRNW04023Q00101",
    "FWSRNW04023Q00104",
    "FWSRNW04023Q00105",
    "FWWSKN02005Q00103",
    "FWBDKN05002Q00103",
    "FWBDKN05002Q00104",
    "FWBDKN05002Q00105",
    "FWWSKN02005Q00104",
    "FWWSKN02005Q00105"
  ]
}

def get_iot_realtime_data():
    try:
        response = requests.post(
            url=API_URL,
            headers=HEADERS,
            json=request_data,
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        print("API调用成功，返回数据：")
        print(json.dumps(result, ensure_ascii=False, indent=4))
        return result
    except Exception as e:
        print(f"请求失败：{str(e)}")
    return None

if __name__ == "__main__":
    get_iot_realtime_data()



{
    "code": 9999,
    "message": "could not extract ResultSet; SQL [n/a]; nested exception is org.hibernate.exception.SQLGrammarException: could not extract ResultSet"
}




<img width="1217" height="730" alt="image" src="https://github.com/user-attachments/assets/0a6348fd-0dea-4950-a7fc-5f3ec6861508" />



jdbc:postgresql://10.66.110.219:8000,10.66.110.206:8000,10.66.110.11:8000/wsd?loadBalance=true


1. 

```python
import requests
import json

# API基础配置
API_URL = "http://10.66.169.58:8001/iot3/rest/api/v1/realtime.json"  # 完整接口地址
HEADERS = {
    "Content-Type": "application/json; charset=utf-8",  # 必传JSON格式请求头
    # 若接口需要鉴权（如token/cookie），可在此添加："Authorization": "Bearer xxx"
}

# 请求参数（与接口要求一致）
request_data = {
  "codes": [
    "25",
    "18",
    "41"
  ]
}

def get_iot_realtime_data():
    """调用IoT历史数据API，返回响应结果"""
    try:
        # 发送POST请求，JSON格式传参
        response = requests.post(
            url=API_URL,
            headers=HEADERS,
            data=json.dumps(request_data),  # 字典转JSON字符串
            timeout=30  # 超时时间30秒，可根据需求调整
        )
        # 校验请求状态码
        response.raise_for_status()  # 非200状态码抛出异常
        # 解析JSON响应结果
        result = response.json()
        print("API调用成功，返回数据：")
        print(json.dumps(result, ensure_ascii=False, indent=4))
        return result
    except requests.exceptions.ConnectTimeout:
        print(f"错误：连接接口{API_URL}超时，请检查网络或服务器状态")
    except requests.exceptions.ConnectionError:
        print(f"错误：无法连接到接口{API_URL}，请检查地址/端口是否正确，或服务器是否启动")
    except requests.exceptions.HTTPError as e:
        print(f"错误：接口返回异常状态码，详情：{e}")
    except json.JSONDecodeError:
        print("错误：接口返回非JSON格式数据，解析失败")
    except Exception as e:
        print(f"未知错误：{str(e)}")
    return None

# 执行调用
if __name__ == "__main__":
    get_iot_realtime_data()
```

返回结果

```tex
API调用成功，返回数据：
{
    "code": 9999,
    "message": "could not extract ResultSet; SQL [n/a]; nested exception is org.hibernate.exception.SQLGrammarException: could not extract ResultSet"
}
```




1. 凤山阁：
   坐标北(米): 816305, 坐标东(米): 840581
    坐标： 840581 816300

2. 富山阁

   坐标北(米): 816338, 坐标东(米): 840543

   坐标： 840543  816338

3. 怡山阁

   坐标北(米): 816262, 坐标东(米): 840543

   坐标：840543   816262

4. 宝山阁

   坐标北(米): 816263, 坐标东(米): 840652
   坐标：840652   816263



   




https://docs.qq.com/sheet/DUHdhaEZXRE1pZW1x?no_promotion=1&is_blank_or_template=blank&tab=BB08J2
840581.591510	816290.587100

http://10.66.168.83/COSS/dashboard/workbench
账号：admin
密码：admin




select * from coss_dm.dm_wqm_accident_tag_monitored_day_mini 
dim_water_quality_accident_sz_installation_info


TW_ClearWaterTank_Level_E_Level
TW_ClearWaterTank_Level_W_Level
TW_FilterCommonDevices_InFlow_Flow
TW_FilterCommonDevices_OutFlow
TW_FinalWater_ES_Fluoride_Fluoride
TW_FinalWater_ES_PH_PH
TW_FinalWater_ES_ResChlorine_ResidualChlorine
TW_FinalWater_ES_Turbidity_Turbidity
TW_FinalWater_WS_Fluoride_Fluoride
TW_FinalWater_WS_PH_PH
TW_FinalWater_WS_ResChlorine_ResidualChlorine
TW_FinalWater_WS_Turbidity_Turbidity
TW_RawWater_ES_PH_PH
TW_RawWater_ES_Turbidity_Turbidity
TW_RawWater_WS_PH_PH
TW_RawWater_WS_Turbidity_Turbidity






TW_ClearWaterTank_Level_E.Level
TW_ClearWaterTank_Level_W.Level
TW_FilterCommonDevices.InFlow_Flow
TW_FilterCommonDevices.OutFlow
TW_FinalWater_ES_Fluoride.Fluoride
TW_FinalWater_ES_PH.PH
TW_FinalWater_ES_ResChlorine.ResidualChlorine
TW_FinalWater_ES_Turbidity.Turbidity
TW_FinalWater_WS_Fluoride.Fluoride
TW_FinalWater_WS_PH.PH
TW_FinalWater_WS_ResChlorine.ResidualChlorine
TW_FinalWater_WS_Turbidity.Turbidity
TW_RawWater_ES_PH.PH
TW_RawWater_ES_Turbidity.Turbidity
TW_RawWater_WS_PH.PH
TW_RawWater_WS_Turbidity.Turbidity




<img width="345" height="305" alt="image" src="https://github.com/user-attachments/assets/b6ca9abc-0c41-4ecb-ad1e-ba28ac1b1425" />




dm_pnw_daily_water_distribution_detail_di




<img width="1899" height="841" alt="image" src="https://github.com/user-attachments/assets/c1aec7a7-fd27-4bdc-882e-8338a6feb562" />




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



create table coss_dm.dm_tmu_sensor_data_mini_month(
	id                  varchar(100),
	sensor_code         varchar(100),
	sensor_value        decimal(20,6),
	sensor_time         timestamp(6),
	dm_update_time      timestamp(6) default current_timestamp,
	dm_load_time        timestamp(6) default current_timestamp,
	primary key (sensor_code, sensor_time)
)
partition by range (sensor_time)
(
    -- 2025 Monthly Partitions
    PARTITION mh_202501 VALUES LESS THAN ('2025-02-01 00:00:00'),
    PARTITION mh_202503 VALUES LESS THAN ('2025-04-01 00:00:00'),
    PARTITION mh_202505 VALUES LESS THAN ('2025-06-01 00:00:00'),
    PARTITION mh_202507 VALUES LESS THAN ('2025-08-01 00:00:00'),
    PARTITION mh_202509 VALUES LESS THAN ('2025-10-01 00:00:00'),
    PARTITION mh_202511 VALUES LESS THAN ('2025-12-01 00:00:00'),
    
    -- 2026 Monthly Partitions
    PARTITION mh_202601 VALUES LESS THAN ('2026-02-01 00:00:00'),
    PARTITION mh_202603 VALUES LESS THAN ('2026-04-01 00:00:00'),
    PARTITION mh_202605 VALUES LESS THAN ('2026-06-01 00:00:00'),
    PARTITION mh_202607 VALUES LESS THAN ('2026-08-01 00:00:00'),
    PARTITION mh_202609 VALUES LESS THAN ('2026-10-01 00:00:00'),
    PARTITION mh_202611 VALUES LESS THAN ('2026-12-01 00:00:00'),
    
    -- 2027 Monthly Partitions
    PARTITION mh_202701 VALUES LESS THAN ('2027-02-01 00:00:00'),
    PARTITION mh_202703 VALUES LESS THAN ('2027-04-01 00:00:00'),
    PARTITION mh_202705 VALUES LESS THAN ('2027-06-01 00:00:00'),
    PARTITION mh_202707 VALUES LESS THAN ('2027-08-01 00:00:00'),
    PARTITION mh_202709 VALUES LESS THAN ('2027-10-01 00:00:00'),
    PARTITION mh_202711 VALUES LESS THAN ('2027-12-01 00:00:00'),
    
    -- 2028 Monthly Partitions
    PARTITION mh_202801 VALUES LESS THAN ('2028-02-01 00:00:00'),
    PARTITION mh_202803 VALUES LESS THAN ('2028-04-01 00:00:00'),
    PARTITION mh_202805 VALUES LESS THAN ('2028-06-01 00:00:00'),
    PARTITION mh_202807 VALUES LESS THAN ('2028-08-01 00:00:00'),
    PARTITION mh_202809 VALUES LESS THAN ('2028-10-01 00:00:00'),
    -- Future Partition (avoids insertion failure for unplanned time data)
    PARTITION mh_future VALUES LESS THAN ('9999-01-01 00:00:00')
);
comment on table coss_dm.dm_tmu_sensor_data_mini_month                 is 'Terminal User Sensor MOnitoring Data';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.id             is 'ID';     
comment on column coss_dm.dm_tmu_sensor_data_mini_month.sensor_code    is 'Sensor Code';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.sensor_value   is 'Sensor Value';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.sensor_time    is 'Sensor Time';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.dm_update_time is 'Data Update Time';
comment on column coss_dm.dm_tmu_sensor_data_mini_month.dm_load_time   is 'Data Loading Time';






840527.734740000218153 816342.75913999974727631 0
840527.79779999982565641 816350.60683000087738037 0
840542.27347999997437 816334.39853999949991703 0
840550.40034000016748905 816337.14028000086545944 0

富山閣



http://10.66.109.116:8075/webroot/decision/v10/entry/access/fd54ea64-5d5e-4db5-8cff-b2ff9d30e610?preview=true&page_number=1


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







OBJECTID	BUILDINGID	ENGLISHBUILDINGNAME	CHINESEBUILDINGNAME	BUILDINGTOPLEVEL	BUILDINGBASELEVEL	SITECODE	LASTUPDATEDATE	Shape_Length	Shape_Area	Shape
143538	1103134778	Fullview Garden Block 6	富景花園第６座	88.30000305	7	76178	2014-07-01T00:00:00.000Z	191.1129874	612.4117325	MultiPolygon Z (((844050.07031000033020973 813673.25977000035345554 0, 844049.82031000033020973 813667.12012000009417534 0, 844052.10936999972909689 813667.01953000016510487 0, 844052.35936999972909689 813673.1601599995046854 0, 844054.96875 813673.07031000033020973 0, 844054.89843999966979027 813671.90038999915122986 0, 844057.05858999956399202 813671.79979999922215939 0, 844056.85156000033020973 813666.50977000035345554 0, 844056.35156000033020973 813666.53027000091969967 0, 844056.23828000016510487 813663.37012000009417534 0, 844058.94921999983489513 813663.20020000077784061 0, 844058.94921999983489513 813663.40038999915122986 0, 844064.44921999983489513 813663.17968999966979027 0, 844064.26171999983489513 813658.4101599995046854 0, 844058.76171999983489513 813658.62987999990582466 0, 844058.23046999983489513 813647.87987999990582466 0, 844063.82031000033020973 813647.6601599995046854 0, 844063.60156000033020973 813642.8896500002592802 0, 844058.07811999972909689 813643.08008000068366528 0, 844058.07811999972909689 813643.71972999908030033 0, 844055.42968999966979027 813643.82031000033020973 0, 844055.33983999956399202 813640.75 0, 844055.83983999956399202 813640.73046999983489513 0, 844055.66016000043600798 813635.42968999966979027 0, 844053.46093999966979027 813635.50977000035345554 0, 844053.42186999972909689 813634.30956999957561493 0, 844050.80858999956399202 813634.40038999915122986 0, 844051.05858999956399202 813640.54003999941051006 0, 844048.76953000016510487 813640.6396500002592802 0, 844048.51953000016510487 813634.5 0, 844045.89061999972909689 813634.62012000009417534 0, 844045.94141000043600798 813635.76953000016510487 0, 844043.80078000016510487 813635.87012000009417534 0, 844044.03906000033020973 813641.1396500002592802 0, 844044.53906000033020973 813641.12012000009417534 0, 844044.67968999966979027 813644.30956999957561493 0, 844041.89843999966979027 813644.40038999915122986 0, 844041.91016000043600798 813643.73046999983489513 0, 844036.37891000043600798 813644.00977000035345554 0, 844036.55858999956399202 813648.76953000016510487 0, 844042.05858999956399202 813648.55956999957561493 0, 844042.17968999966979027 813651.91991999931633472 0, 844039.58983999956399202 813652.01953000016510487 0, 844039.73828000016510487 813654.58008000068366528 0, 844042.21875 813654.6103499997407198 0, 844042.46875 813659.30956999957561493 0, 844036.96875 813659.51953000016510487 0, 844037.19921999983489513 813664.29003999941051006 0, 844042.69141000043600798 813664.01953000016510487 0, 844042.67968999966979027 813663.82031000033020973 0, 844045.41016000043600798 813663.76953000016510487 0, 844045.53906000033020973 813666.96972999908030033 0, 844045.03906000033020973 813666.99022999964654446 0, 844045.26171999983489513 813672.28027000091969967 0, 844047.42186999972909689 813672.17968999966979027 0, 844047.46093999966979027 813673.34961000084877014 0, 844050.07031000033020973 813673.25977000035345554 0)))
<img width="793" height="604" alt="image" src="https://github.com/user-attachments/assets/7dbf59f9-c3a4-4e6f-963d-a3ce3fb1ad9f" />






insert into coss_dm.dm_wqm_accident_tag_monitored_day_mini 
select 
installation_id
,tag_name
,comment
,value
,time +66 "time"
,unit
,water_biz_type
,current_timestamp dm_update_time
,current_timestamp dm_load_time
from 
coss_dm.dm_wqm_accident_tag_monitored_day_mini 
where "time" >= '2026-01-13 00:00:00.000'
and "time" <= '2026-01-13 23:59:59.000'

60到66






[[[839808.41999999992549419,817008.49000000022351742],[839868.06300000008195639,816979.48200000077486038],[840049.81589999981224537,816891.1465000007301569],[840120.49010000005364418,816856.76789999939501286],[840177.96339999977499247,816828.82560000009834766],[840237.84999999962747097,816799.71000000089406967],[840279.59250000026077032,816791.57269999943673611],[840339.02780000027269125,816780.30040000006556511],[840375.02080000005662441,816773.3863999992609024],[840673.21999999973922968,816715.76999999955296516],[840748.93960000015795231,816680.60620000027120113],[840818.02539999969303608,816648.52300000004470348],[840940.0400000000372529,816591.85999999940395355],[840986.31579999998211861,816545.25650000013411045],[841178.63999999966472387,816351.57000000029802322],[841185.5,816358.38000000081956387],[841194.05999999959021807,816360.25],[841234.44000000040978193,816400.5],[841235.5,816400.93999999947845936],[841237.75,816400.75],[841250,816388.56000000052154064],[841250,816384.68999999947845936],[841209.55999999959021807,816344.38000000081956387],[841207.25,816334.25],[841201.47589999996125698,816328.59339999966323376],[841259.04899999964982271,816270.57950000092387199],[841264.83000000007450581,816276.41000000014901161],[841273.79999999981373549,816277.84999999962747097],[841314.75999999977648258,816318.83000000007450581],[841318.25999999977648258,816319.06000000052154064],[841330.40000000037252903,816306.93999999947845936],[841330.76999999955296516,816303.08999999985098839],[841290.26999999955296516,816262.44999999925494194],[841287.30999999959021807,816253.81000000052154064],[841281.56630000006407499,816247.99340000003576279],[841294.31529999990016222,816235.26579999923706055],[841210.30350000038743019,816150.25760000012814999],[841250,816119.8607999999076128],[841348.39389999955892563,816020.10610000044107437],[841351.79660000000149012,816017.08880000002682209],[841359.0400000000372529,816013.69999999925494194],[841359.0610999995842576,816013.70480000041425228],[841681.89900000020861626,816013.72199999913573265],[841732.3397000003606081,816020.78830000013113022],[841777.91999999992549419,816021.30000000074505806],[841806.14279999956488609,816032.4164000004529953],[841874.7099999999627471,816059.41999999992549419],[841890.84999999962747097,816053.24000000022351742],[841893.95590000040829182,816042.06259999983012676],[842009.21129999961704016,816053.4635000005364418],[842005.98869999963790178,816067.22369999997317791],[842079.28909999970346689,816083.34830000065267086],[842096.87000000011175871,816109.5],[842101.67530000023543835,816106.08980000019073486],[842107.91999999992549419,816110.41000000014901161],[842115.25999999977648258,816119.49000000022351742],[842122.19000000040978193,816126.65000000037252903],[842123,816126.98000000044703484],[842123.91000000014901161,816126.90000000037252903],[842128.37999999988824129,816125.33000000007450581],[842130.65000000037252903,816124.86999999918043613],[842131.55999999959021807,816125],[842132.58000000007450581,816125.41000000014901161],[842133.61000000033527613,816126.05000000074505806],[842134.25999999977648258,816126.68999999947845936],[842135.66999999992549419,816129.38000000081956387],[842135.63999999966472387,816131.49000000022351742],[842135.03000000026077032,816133.02999999932944775],[842133.67999999970197678,816135.13000000081956387],[842132.62999999988824129,816137.68999999947845936],[842147.83999999985098839,816147.59999999962747097],[842153.58999999985098839,816149.61999999918043613],[842156.25999999977648258,816148.98000000044703484],[842179.26190000027418137,816131.16970000043511391],[842181.30840000044554472,816129.73520000092685223],[842183.33579999953508377,816127.53119999915361404],[842184.55250000022351742,816125.46289999969303608],[842185.43109999969601631,816122.91059999912977219],[842240.2571000000461936,816083.64509999938309193],[842245.26090000011026859,816065.86400000005960464],[842298.27269999962300062,815980.41169999912381172],[842445.55999999959021807,815867.65000000037252903],[842326.11899999994784594,815775.72800000011920929],[842265.24000000022351742,815782.98000000044703484],[842185.82730000000447035,815861.53940000012516975],[842014.17169999983161688,815810.97859999909996986],[841916.34999999962747097,815806.48000000044703484],[841889.741499999538064,815704.5506999995559454],[841896.07000000029802322,815388.14000000059604645],[841869.68400000035762787,815265.17310000024735928],[841864.02649999968707561,815235.03639999963343143],[841860.91660000011324883,815214.8953000009059906],[841892.56300000008195639,815202.48320000059902668],[841931.29499999992549419,815189.79600000008940697],[841899.68910000007599592,815172.48760000057518482],[841863.16999999992549419,815171.39000000059604645],[841846.00519999954849482,815165.61950000002980232],[841824.94479999970644712,815116.51209999993443489],[841837.7900000000372529,815074.93999999947845936],[841761.52950000017881393,815080.05900000035762787],[841744.60230000037699938,815083.64800000004470348],[841711.26090000011026859,815097.23489999957382679],[841688.4232999999076128,815112.19449999928474426],[841587.25420000031590462,815210.47939999960362911],[841562.629700000397861,815194.59479999914765358],[841471.28839999996125698,815247.62549999915063381],[841467.17970000021159649,815237.12010000087320805],[841465.14460000023245811,815232.50320000015199184],[841463.30209999997168779,815230.08229999989271164],[841461.62019999977201223,815228.41650000028312206],[841451.63750000018626451,815220.55350000038743019],[841418.70689999964088202,815198.88470000028610229],[841413.96150000020861626,815196.73890000022947788],[841408.61230000015348196,815195.24359999969601631],[841398.34520000033080578,815193.56719999946653843],[841395.59100000001490116,815193.43459999933838844],[841393.23049999959766865,815193.58980000019073486],[841384.80080000031739473,815195.04979999922215939],[841375.41019999980926514,815202.23049999959766865],[841373.98049999959766865,815203.16990000009536743],[841364.41359999962151051,815211.34850000031292439],[841362.14059999957680702,815212.44040000066161156],[841353.34599999990314245,815218.42620000056922436],[841261.95650000032037497,815346.86559999920427799],[841211.05920000001788139,815551.39829999953508377],[841207.34690000023692846,815556.43359999917447567],[841202.5284000001847744,815561.68359999917447567],[841197.14290000032633543,815566.35019999928772449],[841191.26059999968856573,815570.37240000069141388],[841184.95810000039637089,815573.69789999909698963],[841178.31759999971836805,815576.28329999931156635],[841177.13420000020414591,815576.65489999949932098],[841011.20700000040233135,815615.4874000009149313],[841006.37079999968409538,815616.53869999945163727],[840991.85059999953955412,815619.14450000040233135],[840977.20990000013262033,815620.95340000092983246],[840966.74480000045150518,815621.75219999998807907],[840913.33609999995678663,815615.53179999999701977],[840867.3525000000372529,815611.82840000092983246],[840844.04870000015944242,815608.41919999942183495],[840831.73359999991953373,815605.57819999940693378],[840819.90500000026077032,815602.10070000030100346],[840796.4117000000551343,815593.76720000058412552],[840771.39059999957680702,815584.53999999910593033],[840734.73020000010728836,815572.79350000061094761],[840683.83889999985694885,815564.87040000036358833],[840654.52670000027865171,815580.14760000072419643],[840648.2159000001847744,815585.70130000077188015],[840645.03349999990314245,815589.1522000003606081],[840641.78949999995529652,815592.88419999927282333],[840636.01410000026226044,815603.33630000054836273],[840628.44259999971836805,815627.54199999943375587],[840610.16909999959170818,815667.19380000047385693],[840556.1190999997779727,815797.80550000071525574],[840542.20000000018626451,815790.97000000067055225],[840537.21999999973922968,815787.90000000037252903],[840531.5400000000372529,815783.90000000037252903],[840524.86000000033527613,815778.36999999918043613],[840519.87999999988824129,815773.53999999910593033],[840514.30999999959021807,815767.24000000022351742],[840510.4599999999627471,815762.10999999940395355],[840506.15000000037252903,815755.33999999985098839],[840502.83000000007450581,815749.03999999910593033],[840499.87000000011175871,815742.32000000029802322],[840497.37000000011175871,815735.41000000014901161],[840495.37000000011175871,815728.34999999962747097],[840493.58000000007450581,815719.41000000014901161],[840492.7099999999627471,815712.16000000014901161],[840492.34999999962747097,815704.83999999985098839],[840492.50999999977648258,815697.42999999970197678],[840493.17999999970197678,815690.03999999910593033],[840494.62000000011175871,815681.44999999925494194],[840496.15000000037252903,815675.34999999962747097],[840498.65000000037252903,815667.89000000059604645],[840503.76999999955296516,815643.19999999925494194],[840516.57440000027418137,815622.67459999956190586],[840491.46050000004470348,815609.49019999988377094],[840469.92200000025331974,815637.17100000008940697],[840454.348000000230968,815668.30700000002980232],[840423.61070000007748604,815686.0284000001847744],[840378.88100000005215406,815690.67100000008940697],[840330.65500000026077032,815671.25799999944865704],[840227.87600000016391277,815644.95500000007450581],[840152.23000000044703484,815607.14800000004470348],[840057.67200000025331974,815586.01999999955296516],[840022.70519999973475933,815599.53140000067651272],[840014.73060000035911798,815635.38859999924898148],[840000.6759000001475215,815697.08980000019073486],[839979.89809999987483025,815704.0397999994456768],[839940.91959999967366457,815724.66259999945759773],[839900.43549999967217445,815748.64230000041425228],[839863.94979999959468842,815765.12839999981224537],[839846.95650000032037497,815766.12759999930858612],[839835.96069999970495701,815766.62710000015795231],[839826.464499999769032,815774.62040000036358833],[839819.46719999983906746,815787.10989999957382679],[839808.47149999998509884,815802.09720000065863132],[839794.47699999995529652,815819.0828000009059906],[839778.48330000042915344,815830.57320000045001507],[839745.49619999993592501,815837.06770000047981739],[839754.99249999970197678,815864.54450000077486038],[839784.02269999962300062,815935.91850000061094761],[839806.69749999977648258,815969.10109999962151051],[839791.01999999955296516,816110.49210000038146973],[839790.9599999999627471,816126.5],[839796.44990000035613775,816138.37849999964237213],[839807.26999999955296516,816162.32000000029802322],[839810.78849999979138374,816209.88250000029802322],[839747.10460000019520521,816264.02429999969899654],[839695.5826000003144145,816336.3539000004529953],[839654.68400000035762787,816466.25510000064969063],[839633.83980000019073486,816512.73630000092089176],[839618.33999999985098839,816576.32000000029802322],[839592.34910000022500753,816636.60600000061094761],[839582.97659999970346689,816667.83489999920129776],[839572.36309999972581863,816676.79040000028908253],[839565.65890000015497208,816682.43349999934434891],[839445.9247000003233552,816679.16689999960362911],[839483.45129999984055758,816723.81530000083148479],[839494.89300000015646219,816753.53580000065267086],[839496.37990000005811453,816759.48100000061094761],[839496.89450000040233135,816764.43150000087916851],[839496.83019999973475933,816769.70340000092983246],[839495.60790000017732382,816774.65389999933540821],[839493.54930000007152557,816779.21859999932348728],[839491.04040000028908253,816783.9119000006467104],[839486.85900000017136335,816789.18390000052750111],[839484.27489999961107969,816791.92469999939203262],[839480.60809999983757734,816795.01070000045001507],[839453.24920000042766333,816815.41990000009536743],[839409.64329999964684248,816839.991499999538064],[839392.14780000038444996,816847.23760000057518482],[839353.68919999990612268,816862.35979999974370003],[839315.00980000011622906,816875.77850000001490116],[839295.46520000044256449,816881.1342999991029501],[839254.01190000027418137,816890.74320000037550926],[839245.38700000010430813,816895.30870000086724758],[839252.37519999966025352,817005.54900000058114529],[839092.17050000000745058,817003.48829999938607216],[838549.12799999956041574,816885.02899999916553497],[838495.11209999956190586,817130.27800000086426735],[838546.87440000008791685,817141.81739999912679195],[838639.63819999992847443,817158.61500000022351742],[838632.19000000040978193,817193.61999999918043613],[838622.44000000040978193,817201.5],[838621.80999999959021807,817204.06000000052154064],[838621.12000000011175871,817209.43999999947845936],[838623.80999999959021807,817220.81000000052154064],[838611.30999999959021807,817278],[838611.30999999959021807,817278.81000000052154064],[838611.75,817279.93999999947845936],[838612.69000000040978193,817280.93999999947845936],[838613.62000000011175871,817281.38000000081956387],[838630,817285],[838630.75,817284.88000000081956387],[838631.94000000040978193,817284.31000000052154064],[838632.69000000040978193,817283.43999999947845936],[838632.94000000040978193,817282.81000000052154064],[838645.87999999988824129,817224.61999999918043613],[838651.12000000011175871,817217.5],[838652.5,817210.75],[838653.44000000040978193,817207.31000000052154064],[838648.58279999997466803,817196.79939999990165234],[838655.97070000041276217,817161.57249999977648258],[838738.05429999995976686,817176.43610000051558018],[838741.37999999988824129,817194.75],[838731.75,817239.81000000052154064],[838727.12000000011175871,817243],[838724.94000000040978193,817252.81000000052154064],[838726.87999999988824129,817262.18999999947845936],[838714.69000000040978193,817317.56000000052154064],[838714.55999999959021807,817318.43999999947845936],[838715.05999999959021807,817319.81000000052154064],[838715.75,817320.56000000052154064],[838716.75,817321.11999999918043613],[838732.75,817324.61999999918043613],[838734.05999999959021807,817324.61999999918043613],[838734.94000000040978193,817324.31000000052154064],[838735.87999999988824129,817323.56000000052154064],[838736.37999999988824129,817322.61999999918043613],[838748.55999999959021807,817266.56000000052154064],[838754.25,817259.38000000081956387],[838756.25,817250.11999999918043613],[838753.37999999988824129,817244.56000000052154064],[838762.80999999959021807,817200.88000000081956387],[838774.30999999959021807,817184.31000000052154064],[838775.36469999980181456,817184.42500000074505806],[838775.95509999990463257,817181.74379999935626984],[838966.85580000001937151,817223.94299999997019768],[838974.62999999988824129,817231.15000000037252903],[838979.4599999999627471,817236.25999999977648258],[838980.01999999955296516,817242.31000000052154064],[838978.9599999999627471,817258.32000000029802322],[838975.79999999981373549,817269.42999999970197678],[838974.75320000015199184,817294.05269999988377094],[838982.58820000011473894,817294.43889999948441982],[838986.11000000033527613,817297.13000000081956387],[838985.91999999992549419,817301.77999999932944775],[838985.23000000044703484,817302.22000000067055225],[838982.28000000026077032,817354.41999999992549419],[838983.33999999985098839,817355.96000000089406967],[838984.84999999962747097,817355.99000000022351742],[838985.94000000040978193,817354.85999999940395355],[838989.08000000007450581,817302.35999999940395355],[838988.65000000037252903,817301.91999999992549419],[838988.87000000011175871,817298],[838993.66220000013709068,817294.94419999979436398],[839001.40950000006705523,817295.5227000005543232],[839002.62000000011175871,817270.74000000022351742],[839001.91999999992549419,817261.26999999955296516],[839001.75999999977648258,817244.75],[839001.53000000026077032,817213],[839001.90000000037252903,817209.47000000067055225],[839002.82000000029802322,817205.13000000081956387],[839003.70000000018626451,817202.66999999992549419],[839004.24000000022351742,817201.50999999977648258],[839149.73990000039339066,817173.99929999932646751],[839153.04999999981373549,817191.76999999955296516],[839159.11000000033527613,817190.33000000007450581],[839155.87000000011175871,817172.84999999962747097],[839296.16999999992549419,817146.32000000029802322],[839444.92999999970197678,817098.33999999985098839],[839452.5,817121.94999999925494194],[839477.67999999970197678,817115.21000000089406967],[839474.95000000018626451,817106.40000000037252903],[839456.00999999977648258,817112.55000000074505806],[839450.83999999985098839,817096.42999999970197678],[839558.2384000001475215,817061.78460000082850456],[839559,817064.13000000081956387],[839611.7099999999627471,817046.84999999962747097],[839610.7900000000372529,817044.16999999992549419],[839622.5115999998524785,817040.3217999991029501],[839624.50999999977648258,817042.57000000029802322],[839627.44000000040978193,817041.60999999940395355],[839627.36000000033527613,817038.73000000044703484],[839651.09999999962747097,817030.81000000052154064],[839668.54550000000745058,817050.08039999939501286],[839808.41999999992549419,817008.49000000022351742]]]





select * from coss_dim.dim_water_quality_accident_sz_installation_info  where ordernum = '202505178427287551519'

select * from coss_dim.dim_sz_info where 
supply_id = 133 and supply_code = '1.35&1.55'





接口响应状态码： 200
接口响应内容： {
  "code": 9999,
  "message": "could not extract ResultSet; SQL [n/a]; nested exception is org.hibernate.exception.SQLGrammarException: could not extract ResultSet"
}



http://10.66.169.58:9878




level2 
--泵房机房运行情况
select offical_eng_name ,offical_chi_name ,running_pumps ,total_pumps ,mh  from coss_dm.dm_psr_daily_ps_running_item_di
where 
mh>= 202501 and mh <= 202512
and offical_eng_name  != ''


--泵房千吨电耗量
select offical_eng_name ,offical_chi_name ,kwh_ml ,mh   from coss_dm.dm_psr_daily_ps_running_item_di
where 
mh>= 202501 and mh <= 202512
and offical_eng_name  != ''

--泵张抽水量
select * from coss_dm.dm_psr_monthly_pump_station_item_di 
where 
statistical_month >= 202501 and statistical_month <= 202512


--泵张电耗量
select * from coss_dm.dm_psr_monthly_pump_station_item_di 
where 
statistical_month >= 202501 and statistical_month <= 202512


--泵张电账单
select * from coss_dm.dm_psr_monthly_pump_station_item_di 
where 
statistical_month >= 202501 and statistical_month <= 202512






level3 
--水厂制水量
select asset_name ,pump_qty, statistical_month  from coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di dwmecbhd 
where 
statistical_month >= 202501 and statistical_month <= 202512
and pump_qty is not null 





jdbc:postgresql://10.66.110.64:8000,10.66.110.151:8000,10.66.110.194:8000,10.66.110.235:8000/wsd_isit?loadBalanceHosts=true&refreshCNIpListTime=3




import http.client
import json

conn = http.client.HTTPSConnection("10.11.0.82", 8330)
payload = json.dumps({
   "deviceCodes": [
      "14537005",
      "14537007",
      "14537010"
   ]
})
headers = {
   'Content-Type': 'application/json'
}
conn.request("POST", "/share/data/sensor/moreDevRealtime", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))





drop table coss_dm.dm_rws_rw_supply_hist_dip;
CREATE TABLE coss_dm.dm_rws_rw_supply_hist_dip (
	rw_id varchar(20) NULL,
	rw_name varchar(200) NULL,
	rw_cname varchar(300) NULL,
	region_code varchar(10) NULL,
	source_rw varchar(2) NULL,
	p_qty numeric(12, 4) NULL,
	qty_del numeric(12, 4) NULL,
	present_storage numeric(16, 8) NULL,
	capacity numeric(12, 4) NULL,
	min_storage numeric(12, 4) NULL,
	rec_dt timestamp(6) NULL,
	dt numeric(10) null,
	primary key(rw_id,rec_dt)
)
WITH (
	orientation=row,
	compression=no
);








create table coss_tmp.dm_ass_annual_pipe_asset_region_item_di_arch_260310 as 
select * from coss_dm.dm_ass_annual_pipe_asset_region_item_di

update coss_dm.dm_ass_annual_pipe_asset_region_item_di
set item_value = 0
where inter_item_code in(
'PN_AS_000004',
'PN_AS_000005',
'PN_AS_000006',
'PN_AS_000059',
'PN_AS_000060'
)








select min(completion_date) 
from 
coss_dwd.dwd_ass_water_mains_di a
inner join 
coss_ods.ods_dms_ass_bitumen_priority_jn_di b
on a.facility_id = b.facility_i




insert into coss_dm.dm_ass_annual_pipe_asset_region_item_di
select 
2024 as statistical_year,
region_abbr,
inter_item_code,
item_value,
dm_load_time,
dm_update_time
from coss_dm.dm_ass_annual_pipe_asset_region_item_di where statistical_year = 2025
on duplicate key update nothing;

insert into coss_dm.dm_ass_annual_pipe_asset_main_type_item_di
select 
2024 as statistical_year,
region_abbr,
main_type_code,
inter_item_code,
item_value,
dm_load_time,
dm_update_time
from coss_dm.dm_ass_annual_pipe_asset_main_type_item_di where statistical_year = 2025
on duplicate key update nothing;

insert into coss_dm.dm_ass_annual_pipe_asset_water_type_item_di
select 
2024 as statistical_year,
region_abbr,
water_type_code,
inter_item_code,
item_value,
dm_load_time,
dm_update_time
from coss_dm.dm_ass_annual_pipe_asset_water_type_item_di where statistical_year = 2025
on duplicate key update nothing;







SIS：
FLUORIDE
FLOW
ALARM
PH
CHLORINE
LEVEL
PRESSURE
TURBIDITY





新的码值
discoloured water
excessive chlorine
unknown odour other than solvent smell and excessive chlorine
bitumen particles in water
unknown particles other than bitumen and sand in water
sand in water
water gathering ground
odour with solvent smell

Diarrhea Pot Quality Complaint
TMF / Flushing Water Quality Complaint
Potable Water Quality Complaint
Other Technical Complaint
Salinity Quality Complaint
Odor/Taste Quality Comp
Worm Quality Complaint
Water Quality Sample Collection
<img width="73" height="350" alt="image" src="https://github.com/user-attachments/assets/d453bb47-b045-4901-9e42-724dad29988b" />






jdbc:postgresql://10.66.168.36:8000,10.66.168.52:8000,10.66.168.235:8000/isms

1. ISIT 环境为COSS开通可读权限

   数据库链接： jdbc:postgresql://10.66.110.64:8000,10.66.110.151:8000,10.66.110.194:8000,10.66.110.235:8000/wsd_dm?loadBalanceHosts=true&refreshCNIpListTime=3

   数据库schema: db_mid_ctccbs_0926

2. PrePro 环境为COSS开通可读权限
   数据库链接： jdbc:postgresql://10.66.110.64:8000,10.66.110.151:8000,10.66.110.194:8000,10.66.110.235:8000/wsd
   数据库schema:  wcdms

jdbc:postgresql://10.66.110.64:8000,10.66.110.151:8000,10.66.110.194:8000,10.66.110.235:8000/wsd_dm?loadBalanceHosts=true&refreshCNIpListTime=3	coss	COSS@wsd2nd
pems	cms_complaint	
<img width="1103" height="45" alt="image" src="https://github.com/user-attachments/assets/1bd349ca-8409-4daf-a760-6c9978d28fbb" />



select count(*) from coss_dm.dm_cus_monthly_skill_hotline_item_di
union all select count(*) from coss_dm.dm_cus_monthly_water_quality_cpt_di
union all select count(*) from coss_dm.dm_cus_monthly_skill_hotline_wo_item_di
union all select count(*) from coss_dm.dm_rws_daily_rw_yield_di
union all select count(*) from coss_dm.dm_rws_monthly_rw_yield_di
union all select count(*) from coss_dm.dm_rws_annual_rw_yield_di
union all select count(*) from coss_dm.dm_rws_daily_ir_storage_yield_di
union all select count(*) from coss_dm.dm_rws_daily_ir_level_storage_di
union all select count(*) from coss_dm.dm_rws_region_day_kpi_dip
union all select count(*) from coss_dm.dm_rws_region_month_kpi_dip
union all select count(*) from coss_dm.dm_rws_region_year_kpi_dip
union all select count(*) from coss_dm.dm_srs_daily_sr_wl_qty_item_di
union all select count(*) from coss_dm.dm_srs_monthly_sr_qty_di
union all select count(*) from coss_dm.dm_srs_annual_sr_pool_stopped_di
union all select count(*) from coss_dm.dm_tmu_water_consumption_di
union all select count(*) from coss_dm.dm_tmu_customer_meter_number_di
union all select count(*) from coss_dm.dm_psr_annual_pump_station_item_di
union all select count(*) from coss_dm.dm_psr_monthly_pump_station_item_di
union all select count(*) from coss_dm.dm_wtw_annual_water_treatment_works_item_di
union all select count(*) from coss_dm.dm_wtw_monthly_water_treatment_works_item_di
union all select count(*) from coss_dm.dm_psr_daily_ps_running_item_di
union all select count(*) from coss_dm.dm_psr_monthly_ps_running_item_di
union all select count(*) from coss_dm.dm_wtw_monthly_eng_cons_billing_hist_di
union all select count(*) from coss_dm.dm_wtw_water_quality_qualification_rate_di
union all select count(*) from coss_dm.dm_wtw_water_quality_verification_item_di

418
190
418
7576
251
22
75666
128657
121712
4036
360
1196019
4213
2073
40
45
1072
16161
144
796
19309
18232
3697
1154
57763








创建一个存储过程：coss_arch(tb)
归档tb,把tb归档到coss_tmp schema下
例如归档表的命名规范coss_tmp.tbn_arch_2602051928
2602051928是时间后缀










DROP TABLE if exists coss_dm.dm_tmu_device_alarm_minf;

CREATE TABLE if not exists coss_dm.dm_tmu_device_alarm_minf (
	region_abbr varchar(20) NOT NULL, -- Regional Abbreviation
	device_code varchar(60) NOT NULL, -- Device Name
	alarm_type varchar(60) NULL, -- Alarm Type
	alarm_start_time timestamp(6) NOT NULL, -- Alarm Start Time
	alarm_duration int4 NULL, -- Alarm Duration
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Load Time
	PRIMARY KEY (region_abbr, device_code, alarm_start_time)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_tmu_device_alarm_minf IS 'Real-time Device Alarm Table';

-- Column comments

COMMENT ON COLUMN coss_dm.dm_tmu_device_alarm_minf.region_abbr IS 'Regional Abbreviation';
COMMENT ON COLUMN coss_dm.dm_tmu_device_alarm_minf.device_code IS 'Device Name';
COMMENT ON COLUMN coss_dm.dm_tmu_device_alarm_minf.alarm_type IS 'Alarm Type';
COMMENT ON COLUMN coss_dm.dm_tmu_device_alarm_minf.alarm_start_time IS 'Alarm Start Time';
COMMENT ON COLUMN coss_dm.dm_tmu_device_alarm_minf.alarm_duration IS 'Alarm Duration';
COMMENT ON COLUMN coss_dm.dm_tmu_device_alarm_minf.dm_update_time IS 'Update Time';
COMMENT ON COLUMN coss_dm.dm_tmu_device_alarm_minf.dm_load_time IS 'Load Time';



DROP TABLE if exists  coss_dm.dm_tmu_device_abnormal_alarm_minf;

CREATE TABLE if not exists  coss_dm.dm_tmu_device_abnormal_alarm_minf (
	region_abbr varchar(20) NOT NULL, -- Regional Abbreviation
	normal_num int4 NULL DEFAULT 0, -- Normal Num
	abnormal_num int4 NULL DEFAULT 0, -- Abnormal Num
	alarm_time timestamp(6) NOT NULL, -- Alarm Time
	dm_update_time timestamp(6) NOT NULL DEFAULT pg_systimestamp(), -- Update Time
	dm_load_time timestamp(6) NOT NULL DEFAULT pg_systimestamp(), -- Load Time
	PRIMARY KEY (region_abbr, alarm_time)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_tmu_device_abnormal_alarm_minf IS 'Device Abnormal Alarm Table';

COMMENT ON COLUMN coss_dm.dm_tmu_device_abnormal_alarm_minf.region_abbr IS 'Regional Abbreviation';
COMMENT ON COLUMN coss_dm.dm_tmu_device_abnormal_alarm_minf.normal_num IS 'Normal Num';
COMMENT ON COLUMN coss_dm.dm_tmu_device_abnormal_alarm_minf.abnormal_num IS 'Abnormal Num';
COMMENT ON COLUMN coss_dm.dm_tmu_device_abnormal_alarm_minf.alarm_time IS 'Alarm Time';
COMMENT ON COLUMN coss_dm.dm_tmu_device_abnormal_alarm_minf.dm_update_time IS 'Update Time';
COMMENT ON COLUMN coss_dm.dm_tmu_device_abnormal_alarm_minf.dm_load_time IS 'Load Time';







Manipulation
WeakBattery
Leakage



DWO5_PC	Pass123456
DWO5_AD	Pass123456
http://10.66.168.83/COSS/sys/role/index



1. zoom会议

   ```
   加入 Zoom 会议
   https://us06web.zoom.us/j/81738943299?pwd=N1I2cWdFN3lhN3lPWlhoRThtYnVEQT09
   会议号: 817 3894 3299
   密码: 378822
   zoom 账号
   1582231073@qq.com
   368632_*Lq
   ```

2. 事件PEMSID

   | PEMSID                | 建筑           |
   | --------------------- | -------------- |
   | 202505178427287551519 | 太古城         |
   | 202505178427287554549 | 愉景灣醫療中心 |
   | 202505178427287554512 | 海堤居第１座   |

3. 太古城的水质案件的起止事件 25年11月15日到30日

   





-- coss_dm.dm_cus_annon_watersupplyinfo_di definition

-- Drop table

-- DROP TABLE coss_dm.dm_cus_annon_watersupplyinfo_di;

CREATE TABLE coss_dm.dm_cus_annon_watersupplyinfo_di (
	id int8 NOT NULL, -- Primary Key Id
	recid int8 NULL, -- Announcement Id
	updateid int8 NULL, -- Announcement Record Id
	watersupplytype int4 NULL, -- Temporary Water Supply Method
	watersupplytype_code varchar(20) NULL, -- Temporary Water Supply Code
	watersupplyaddressen varchar(1000) NULL, -- Temporary Water Supply Address (English)
	watersupplyaddresscn varchar(1000) NULL, -- Temporary Water Supply Address (Simplified Chinese)
	watersupplyaddressgn varchar(1000) NULL, -- Temporary Water Supply Address (Traditional Chinese)
	watersupplytime timestamp NULL, -- Temporary Water Supply Application Time
	opentime timestamp NULL, -- Opening Time
	endtime timestamp NULL, -- Closing Time
	quality int4 NULL, -- Quantity
	watersupplyremark varchar(4000) NULL, -- Remarks
	createtime timestamp NULL, -- Creation Time
	creator int4 NULL, -- Creator
	"location" varchar(100) NULL, -- Coordinates
	leavingtime timestamp NULL, -- Departure Time
	vechiclenumber varchar(100) NULL, -- License Plate Number
	drivername varchar(50) NULL, -- Driver Name
	driverphone varchar(50) NULL, -- Driver Contact Number
	workman1 varchar(50) NULL, -- Staff Member 1
	workman2 varchar(50) NULL, -- Staff Member 2
	workmanphone1 varchar(50) NULL, -- Staff Contact Number 1
	workmanphone2 varchar(50) NULL, -- Staff Contact Number 2
	locationx varchar(100) NULL, -- Coordinate X
	locationy varchar(100) NULL, -- Coordinate Y
	isvalid int4 NULL, -- Validity (0: Invalid, 1: Valid)
	lastupdatetime timestamp NULL, -- Last Update Time
	updater int4 NULL, -- Updater
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Load Time
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Update Time
	CONSTRAINT dm_cus_annon_watersupplyinfo_di_pkey PRIMARY KEY (id)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_cus_annon_watersupplyinfo_di IS 'Customer Announcement Temporary Water Supply Information Fact Table (DI: Incremental Update Table)';

-- Column comments

COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.id IS 'Primary Key Id';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.recid IS 'Announcement Id';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.updateid IS 'Announcement Record Id';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplytype IS 'Temporary Water Supply Method';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplytype_code IS 'Temporary Water Supply Code';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyaddressen IS 'Temporary Water Supply Address (English)';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyaddresscn IS 'Temporary Water Supply Address (Simplified Chinese)';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyaddressgn IS 'Temporary Water Supply Address (Traditional Chinese)';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplytime IS 'Temporary Water Supply Application Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.opentime IS 'Opening Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.endtime IS 'Closing Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.quality IS 'Quantity';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyremark IS 'Remarks';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.createtime IS 'Creation Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.creator IS 'Creator';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di."location" IS 'Coordinates';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.leavingtime IS 'Departure Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.vechiclenumber IS 'License Plate Number';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.drivername IS 'Driver Name';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.driverphone IS 'Driver Contact Number';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.workman1 IS 'Staff Member 1';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.workman2 IS 'Staff Member 2';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.workmanphone1 IS 'Staff Contact Number 1';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.workmanphone2 IS 'Staff Contact Number 2';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.locationx IS 'Coordinate X';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.locationy IS 'Coordinate Y';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.isvalid IS 'Validity (0: Invalid, 1: Valid)';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.lastupdatetime IS 'Last Update Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.updater IS 'Updater';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.dm_load_time IS 'Dm Load Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.dm_update_time IS 'Dm Update Time';







create table coss_tmp.dm_cus_water_quality_wo_details_mini_arch_260117 as  
select * from coss_dm.dm_cus_water_quality_wo_details_mini 
where ordernum = '202505161427283354720'

delete from coss_dm.dm_cus_water_quality_wo_details_mini 
where ordernum = '202505161427283354720'



























select 
ordernum
,region_abbr
,admin_division_code
,cpt_type_code
,biz_type_cn cpt_type_cn
,biz_type_tc cpt_type_tc
,biz_type_en cpt_type_en
,urgency_code
,t.water_type_code
,water_type_cn
,water_type_tc
,water_type_en
,t.wo_status_code
,wo_status_cn
,wo_status_tc
,wo_status_en
,org_type_code
,name_cn org_type_name_cn
,name_tc org_type_name_tc
,name_en org_type_name_en
,street
,wutun
,term
,village
,buildingno
,service_content
,post
,functionary
,phone
,coordinate_x
,coordinate_y
,create_time
,dm_update_time
,dm_load_time
from 
coss_dm.dm_cus_customer_service_wo_detail_info_di t
inner join (select 
wo_biz_type_code 
,biz_type_cn 
,biz_type_tc 
,biz_type_en 
from 
coss_dim.dim_wo_biz_type_info
where topic_type = 'COMPLAINTS') t1 on  t.cpt_type_code = wo_biz_type_code
inner join (select 
water_type_code
,water_type_cn
,water_type_tc
,water_type_en
from 
coss_dim.dim_water_type 
) t2 on t.water_type_code = t2.water_type_code 
inner join (select 
wo_status_code
,wo_status_cn
,wo_status_tc
,wo_status_en
from 
coss_dim.dim_wo_status_info) t3 on t.wo_status_code =t3.wo_status_code 
inner join (select 
code
,name_cn
,name_tc
,name_en
from 
coss_dim.dim_wo_dict_info) t4 on t.org_type_code = t4.code 








coss_dm.dm_cus_water_quality_wo_details_mini
coss_dm.dm_cus_water_quality_impact_build_mini
coss_dm.dm_cus_water_quality_accident_impact_mini
coss_dm.dm_wqm_accident_tag_monitored_day_mini
coss_dm.dm_cus_annon_watersupplyinfo_di
coss_dm.dm_pnw_sr_burst_tag_monitored_day_mini -- dm_pnw_service_reservoir_tag_monitored_day_mini
coss_dm.dm_wqm_accident_logger_info_mini
coss_dim.dim_water_quality_accident_sz_installation_info
coss_dim.dim_sz_info



12589
Asdfg.456

Lai Yeung House

<GEOJSON>{ "type": "Polygon", "coordinates": [[[834501.78300000, 822260.37360000], [834508.19400000, 822267.92590000], [834500.00000000, 822274.83640000], [834486.28670000, 822286.28660000], [834487.57610000, 822287.94130000], [834491.26660000, 822284.86520000], [834497.48760000, 822292.61300000], [834488.62890000, 822300.00000000], [834480.05070000, 822307.15320000], [834481.55670000, 822309.04120000], [834484.31860000, 822306.73390000], [834490.67530000, 822314.54290000], [834458.53070000, 822341.48630000], [834452.01440000, 822333.72210000], [834470.35420000, 822318.40030000], [834468.80960000, 822316.52690000], [834465.29320000, 822319.45920000], [834458.95080000, 822311.80060000], [834473.10850000, 822300.00000000], [834480.12630000, 822294.15070000], [834478.79560000, 822292.53680000], [834476.00460000, 822294.86550000], [834469.51180000, 822287.08300000], [834500.00000000, 822261.85960000], [834501.78300000, 822260.37360000]]] }</GEOJSON>

https://mgisweb.windm.wsd.gov/mgisweb/main.aspx


DWO4	Pass123456	test



select * from coss_dm.dm_cus_water_quality_wo_details_mini
select * from coss_dm.dm_cus_water_quality_impact_build_mini
select * from coss_dm.dm_cus_water_quality_accident_impact_mini
select * from coss_dm.dm_wqm_accident_tag_monitored_day_mini
select * from coss_dm.dm_cus_annon_watersupplyinfo_di
select * from coss_dim.dim_wo_biz_type_info 




SELECT
    n.nspname AS schema_name,
    c.relname AS table_name,
    a.attname AS column_name,
    format_type(a.atttypid, a.atttypmod) AS data_type  -- 自动处理 varchar(50), numeric(10,2) 等
FROM
    pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
JOIN pg_attribute a ON a.attrelid = c.oid
WHERE
    c.relkind = 'r'                     -- 只查普通表（relation）
    AND n.nspname = 'your_schema_name'  -- ← 替换为你的 schema 名，例如 'public'
    AND a.attnum > 0                    -- 排除系统列（如 ctid, xmin 等）
    AND NOT a.attisdropped              -- 排除已删除的列
ORDER BY
    c.relname,
    a.attnum;




delete from coss_dm.dm_cus_water_quality_wo_details_mini
delete from coss_dm.dm_cus_annon_watersupplyinfo_di 
delete from coss_dm.dm_cus_water_quality_accident_impact_mini
delete from coss_dm.dm_wqm_accident_tag_monitored_day_mini




账号：DWO1 密码：Pass123456
账号：DWO2密码：Pass123456
账号：DWO3 密码：Pass123456



DROP TABLE coss_dm.dm_cus_water_quality_wo_details_mini;

CREATE TABLE coss_dm.dm_cus_water_quality_wo_details_mini (
	ordernum varchar(150) NULL, -- The Ticket Number
	region_abbr varchar(200) NULL, -- Region
	admin_division_code varchar(100) NULL, -- Administrative Area Code
	cpt_type_code varchar(100) NULL, -- Complaint Code
	urgency_code varchar(100) NULL, -- Urgency Code
	water_type_code varchar(100) NULL, -- Water Supply Type Code
	wo_status_code varchar(100) NULL, -- Ticket Status Code
	org_type_code varchar(100) NULL, -- Channel Status Code
	wq_cpt_type_code varchar(100) NULL, -- Water Quality Type Code
	dma_code varchar(100) NULL, -- Dma Code
	street varchar(200) NULL, -- Street
	wutun varchar(200) NULL, -- Houses
	term varchar(200) NULL, -- Term
	village varchar(200) NULL, -- Village
	affect_building_no varchar(200) NULL, -- Number of Affect Building
	building_tc varchar(100) NULL, -- Building Tc
	building_en varchar(100) NULL, -- Building En
	floor varchar(200) NULL, -- Floor
	isrepeatedcomplaint int4 NULL, -- Is Repeated Complaint
	relateorder varchar(150) NULL, -- Relate Order
	service_content varchar(500) NULL, -- Service Content
	post varchar(100) NULL, -- Position Of Responsible Person
	functionary varchar(100) NULL, -- Functionary Of Responsible Person
	phone varchar(100) NULL, -- Phone Of Responsible Person
	coordinate_x numeric(20, 6) NULL, -- X-Axis Coordinate
	coordinate_y numeric(20, 6) NULL, -- Y-Axis Coordinate
	region_receiving_date timestamp(6) NULL, -- Region Receiving Date
	create_time timestamp(6) NULL, -- Create Time
	finishtime timestamp(6) NULL, -- Create Time
	dm_update_time timestamp(6) default pg_systimestamp(), -- Work Order Completion Time
	dm_load_time timestamp(6) default pg_systimestamp(), -- Data Loading Time
	primary key(ordernum)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_cus_water_quality_wo_details_mini IS 'Customer Service Water Quality Ticket Details';

-- Column comments

COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.ordernum IS 'The Ticket Number';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.region_abbr IS 'Region';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.admin_division_code IS 'Administrative Area Code';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.cpt_type_code IS 'Complaint Code';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.urgency_code IS 'Urgency Code';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.water_type_code IS 'Water Supply Type Code';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.wo_status_code IS 'Ticket Status Code';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.org_type_code IS 'Channel Status Code';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.wq_cpt_type_code IS 'Water Quality Type Code';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.dma_code IS 'Dma Code';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.street IS 'Street';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.wutun IS 'Houses';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.term IS 'Term';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.village IS 'Village';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.affect_building_no IS 'Number of Affect Building';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.building_tc IS 'Building Tc';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.building_en IS 'Building En';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.floor IS 'Floor';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.isrepeatedcomplaint IS 'Is Repeated Complaint';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.relateorder IS 'Relate Order';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.service_content IS 'Service Content';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.post IS 'Position Of Responsible Person';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.functionary IS 'Functionary Of Responsible Person';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.phone IS 'Phone Of Responsible Person';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.coordinate_x IS 'X-Axis Coordinate';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.coordinate_y IS 'Y-Axis Coordinate';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.region_receiving_date IS 'Region Receiving Date';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.create_time IS 'Create Time';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.finishtime IS 'Create Time';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.dm_update_time IS 'Work Order Completion Time';
COMMENT ON COLUMN coss_dm.dm_cus_water_quality_wo_details_mini.dm_load_time IS 'Data Loading Time';



delete from coss_dm.dm_cus_water_quality_wo_details_mini
;delete from coss_dm.dm_cus_water_quality_impact_build_mini
;delete from coss_dm.dm_cus_water_quality_accident_impact_mini
;delete from coss_dm.dm_wqm_accident_tag_monitored_day_mini
;delete from coss_dm.dm_cus_annon_watersupplyinfo_di



-- coss_dm.dm_wqm_accident_logger_info_mini definition

-- Drop table

-- DROP TABLE coss_dm.dm_wqm_accident_logger_info_mini;

CREATE TABLE coss_dm.dm_wqm_accident_logger_info_mini (
	ordernum varchar(60) NOT NULL, -- Order Num
	logger_id varchar(40) NOT NULL, -- Logger Id
	logger_ref varchar(64) NOT NULL, -- Logger Feference
	supply_zone varchar(64) NOT NULL, -- Supply Zone
	coordinate_x numeric(17, 10) NULL, -- X Coordinate
	coordinate_y numeric(17, 10) NULL, -- Y Coordinate
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	CONSTRAINT dm_wqm_accident_logger_info_mini_pkey PRIMARY KEY (ordernum, supply_zone, logger_id, logger_ref)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_wqm_accident_logger_info_mini IS 'Logger related to pipe burst incidents';

-- Column comments

COMMENT ON COLUMN coss_dm.dm_wqm_accident_logger_info_mini.ordernum IS 'Order Num';
COMMENT ON COLUMN coss_dm.dm_wqm_accident_logger_info_mini.logger_id IS 'Logger Id';
COMMENT ON COLUMN coss_dm.dm_wqm_accident_logger_info_mini.logger_ref IS 'Logger Feference';
COMMENT ON COLUMN coss_dm.dm_wqm_accident_logger_info_mini.supply_zone IS 'Supply Zone';
COMMENT ON COLUMN coss_dm.dm_wqm_accident_logger_info_mini.coordinate_x IS 'X Coordinate';
COMMENT ON COLUMN coss_dm.dm_wqm_accident_logger_info_mini.coordinate_y IS 'Y Coordinate';
COMMENT ON COLUMN coss_dm.dm_wqm_accident_logger_info_mini.dm_load_time IS 'Data Loading Time';
COMMENT ON COLUMN coss_dm.dm_wqm_accident_logger_info_mini.dm_update_time IS 'Data Update Time';

















SELECT ordernum,region_abbr,admin_division_code,cpt_type_code,urgency_code,water_type_code,wo_status_code,org_type_code,wq_cpt_type_code,dma_code,street,wutun,term,village,affect_building_no,building_tc,building_en AS buildingEc,floor,isrepeatedcomplaint,relateorder,service_content,post,functionary,phone,coordinate_x,coordinate_y,region_receiving_date,finishtime,create_time,dm_load_time,dm_update_time FROM coss_dm.dm_cus_water_quality_wo_details_mini WHERE (region_receiving_date BETWEEN '2025-01-01' AND '2025-12-31')



select count(*)  from coss_dim.dim_water_quality_accident_sz_installation_info
union all select count(*)  from coss_dim.dim_sz_info
union all select count(*)  from coss_dm.dm_cus_water_quality_wo_details_mini
union all select count(*)  from coss_dm.dm_cus_water_quality_impact_build_mini
union all select count(*)  from coss_dm.dm_cus_water_quality_accident_impact_mini
union all select count(*)  from coss_dm.dm_wqm_accident_tag_monitored_day_mini
union all select count(*)  from coss_dm.dm_cus_annon_watersupplyinfo_di

5
2
947
13
4
1536
10



太古城案件ID
202505178427287551519
愉景湾
202505178427287000000
<img width="264" height="97" alt="image" src="https://github.com/user-attachments/assets/8a4ba547-03b8-41dc-9ac6-ab5a43f3f5a2" />


DROP TABLE coss_dm.dm_cus_annon_watersupplyinfo_di;
CREATE TABLE coss_dm.dm_cus_annon_watersupplyinfo_di (
	id int8 NOT NULL, -- Primary Key Id
	recid int8 NULL, -- Announcement Id
	updateid int8 NULL, -- Announcement Record Id
	watersupplytype int4 NULL, -- Temporary Water Supply Method
	watersupplytype_code varchar(20) NULL, -- Temporary Water Supply Code
	watersupplyaddressen varchar(1000) NULL, -- Temporary Water Supply Address (English)
	watersupplyaddresscn varchar(1000) NULL, -- Temporary Water Supply Address (Simplified Chinese)
	watersupplyaddressgn varchar(1000) NULL, -- Temporary Water Supply Address (Traditional Chinese)
	watersupplytime timestamp NULL, -- Temporary Water Supply Application Time
	opentime timestamp NULL, -- Opening Time
	endtime timestamp NULL, -- Closing Time
	quality int4 NULL, -- Quantity
	watersupplyremark varchar(4000) NULL, -- Remarks
	createtime timestamp NULL, -- Creation Time
	creator int4 NULL, -- Creator
	"location" varchar(100) NULL, -- Coordinates
	leavingtime timestamp NULL, -- Departure Time
	vechiclenumber varchar(100) NULL, -- License Plate Number
	drivername varchar(50) NULL, -- Driver Name
	driverphone varchar(50) NULL, -- Driver Contact Number
	workman1 varchar(50) NULL, -- Staff Member 1
	workman2 varchar(50) NULL, -- Staff Member 2
	workmanphone1 varchar(50) NULL, -- Staff Contact Number 1
	workmanphone2 varchar(50) NULL, -- Staff Contact Number 2
	locationx varchar(100) NULL, -- Coordinate X
	locationy varchar(100) NULL, -- Coordinate Y
	isvalid int4 NULL, -- Validity (0: Invalid, 1: Valid)
	lastupdatetime timestamp NULL, -- Last Update Time
	updater int4 NULL, -- Updater
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Load Time
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Update Time
	CONSTRAINT dm_cus_annon_watersupplyinfo_di_pkey PRIMARY KEY (id)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_cus_annon_watersupplyinfo_di IS 'Customer Announcement Temporary Water Supply Information Fact Table (DI: Incremental Update Table)';

-- Column comments

COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.id IS 'Primary Key Id';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.recid IS 'Announcement Id';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.updateid IS 'Announcement Record Id';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplytype IS 'Temporary Water Supply Method';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplytype_code IS 'Temporary Water Supply Code';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyaddressen IS 'Temporary Water Supply Address (English)';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyaddresscn IS 'Temporary Water Supply Address (Simplified Chinese)';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyaddressgn IS 'Temporary Water Supply Address (Traditional Chinese)';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplytime IS 'Temporary Water Supply Application Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.opentime IS 'Opening Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.endtime IS 'Closing Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.quality IS 'Quantity';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyremark IS 'Remarks';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.createtime IS 'Creation Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.creator IS 'Creator';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di."location" IS 'Coordinates';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.leavingtime IS 'Departure Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.vechiclenumber IS 'License Plate Number';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.drivername IS 'Driver Name';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.driverphone IS 'Driver Contact Number';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.workman1 IS 'Staff Member 1';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.workman2 IS 'Staff Member 2';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.workmanphone1 IS 'Staff Contact Number 1';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.workmanphone2 IS 'Staff Contact Number 2';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.locationx IS 'Coordinate X';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.locationy IS 'Coordinate Y';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.isvalid IS 'Validity (0: Invalid, 1: Valid)';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.lastupdatetime IS 'Last Update Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.updater IS 'Updater';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.dm_load_time IS 'Dm Load Time';
COMMENT ON COLUMN coss_dm.dm_cus_annon_watersupplyinfo_di.dm_update_time IS 'Dm Update Time';

**id	namecn	nameen	namegn
3	消防栓	Fire hydrant	消防栓
4	水箱	Water tank	水箱
2	水车	Water wheel	水車**



Lai Huen House
Lai Yeung House
Vegetable Marketing Organization Cheung Sha Wan Wholesale Vegetable Market
  
  
  COSS Dev 环境的访问地址：http://10.66.169.199/COSS/login
正式账号：
  coss_wds
  CosS@wsd.123
测试账号：
  coss_wds_test
  CosS@wsd.123



  


wsd_coss_test_01	CosS@wsd.coss01



-- 260106 水质专题模拟水质监测数据代码
with t_a as (
select 
*
from 
(
select 
installation_id,
scada_tag tag_name,
comment,
cast(value as decimal(15,5)) value,
time,
unit,
water_biz_type,
current_timestamp dm_update_time,
current_timestamp dm_load_time
from coss_dm.dm_pnw_service_reservoir_tag_monitored_hst_mini_month dpsrtmhmm 
where installation_id = 'SR230' and water_biz_type = 'CHLORINE'
union all
select 
installation_id,
scada_tag tag_name,
comment,
cast(value as decimal(15,5)) value,
time,
unit,
water_biz_type,
current_timestamp dm_update_time,
current_timestamp dm_load_time
from coss_dm.dm_pnw_service_reservoir_tag_monitored_hst_mini_month dpsrtmhmm 
where installation_id = 'SR230' and water_biz_type = 'CHLORINE'
union all
select 
installation_id,
scada_tag tag_name,
comment,
cast(value as decimal(15,5)) value,
time,
unit,
water_biz_type,
current_timestamp dm_update_time,
current_timestamp dm_load_time
from coss_dm.dm_pnw_service_reservoir_tag_monitored_hst_mini_month dpsrtmhmm 
where installation_id = 'SR230' and water_biz_type = 'CHLORINE'
union all
select 
installation_id,
scada_tag tag_name,
comment,
cast(value as decimal(15,5)) value,
time,
unit,
water_biz_type,
current_timestamp dm_update_time,
current_timestamp dm_load_time
from coss_dm.dm_pnw_service_reservoir_tag_monitored_hst_mini_month dpsrtmhmm 
where installation_id = 'SR230' and water_biz_type = 'CHLORINE'
union all
select 
installation_id,
scada_tag tag_name,
comment,
cast(value as decimal(15,5)) value,
time,
unit,
water_biz_type,
current_timestamp dm_update_time,
current_timestamp dm_load_time
from coss_dm.dm_pnw_service_reservoir_tag_monitored_hst_mini_month dpsrtmhmm 
where installation_id = 'SR230' and water_biz_type = 'CHLORINE'
) limit 192
) ,t_b as 
(
select 
half_hour_time,
tag_name
from 
(
SELECT 
    
    generate_series AS half_hour_time
FROM generate_series(
    -- 起始时间：近3天的00:00:00（如今天是2025-12-24，则起始为2025-12-21 00:00:00）
    (CURRENT_DATE - INTERVAL '3 days')::timestamp,
    -- 结束时间：当天的23:30:00
    (CURRENT_DATE + INTERVAL '1 day - 30 minutes')::timestamp,
    -- 步长：30分钟
    INTERVAL '30 minutes'
)
) t 
join (select 'realflex6/KLN/BUTERFLYV_SR/A/AISR0LCH01' tag_name) t1 on 1=1
) 
select 
installation_id,
t.tag_name,
comment,
value,
half_hour_time as time,
unit,
water_biz_type,
current_timestamp dm_update_time,
current_timestamp dm_load_time
from t_a t inner join t_b t1 on t.tag_name = t1.tag_name 

、





with t_a as(
(select 
  t.i_code as installation_id                     -- install code
  ,t.tag_name                         -- tag name
  ,t.tag_name_tc as comment               -- tag traditional chinese name
  ,cast(t.tag_value as decimal(15,5)) as value               -- tag value
  ,t.tag_time as time                    -- tag time
  ,t.units  as unit                    -- tag units
  ,CASE 
        WHEN tag_name_cn LIKE '%余氯%' THEN 'CHLORINE'
        WHEN tag_name_cn LIKE '%PH%' THEN 'PH'
        WHEN tag_name_cn LIKE '%氟%' THEN 'FLUORIDE'
        WHEN tag_name_cn LIKE '%浊度%' THEN 'TURBIDITY'
        ELSE tag_name_cn
    END AS  water_biz_type
  ,current_timestamp dm_update_time
  ,current_timestamp dm_load_time
from coss_dm.dm_wtw_opc_data_mini_day t
where i_code = 'TW009' and tag_type ='water_quality'
and tag_name_cn = '出厂食水-余氯'
and  tag_value !=0
limit 1)
union all 

(select 
  t.i_code as installation_id                     -- install code
  ,t.tag_name                         -- tag name
  ,t.tag_name_tc as comment               -- tag traditional chinese name
  ,cast(t.tag_value as decimal(15,5)) as value               -- tag value
  ,t.tag_time as time                    -- tag time
  ,t.units  as unit                    -- tag units
  ,CASE 
        WHEN tag_name_cn LIKE '%余氯%' THEN 'CHLORINE'
        WHEN tag_name_cn LIKE '%PH%' THEN 'PH'
        WHEN tag_name_cn LIKE '%氟%' THEN 'FLUORIDE'
        WHEN tag_name_cn LIKE '%浊度%' THEN 'TURBIDITY'
        ELSE tag_name_cn
    END AS  water_biz_type
  ,current_timestamp dm_update_time
  ,current_timestamp dm_load_time
from coss_dm.dm_wtw_opc_data_mini_day t
where i_code = 'TW009' and tag_type ='water_quality'
and tag_name_cn = '出厂食水-PH'
and  tag_value !=0
limit 1)

union all 
(select 
  t.i_code as installation_id                     -- install code
  ,t.tag_name                         -- tag name
  ,t.tag_name_tc as comment               -- tag traditional chinese name
  ,cast(1.01 as decimal(15,5)) as value               -- tag value
  ,t.tag_time as time                    -- tag time
  ,t.units  as unit                    -- tag units
  ,CASE 
        WHEN tag_name_cn LIKE '%余氯%' THEN 'CHLORINE'
        WHEN tag_name_cn LIKE '%PH%' THEN 'PH'
        WHEN tag_name_cn LIKE '%氟%' THEN 'FLUORIDE'
        WHEN tag_name_cn LIKE '%浊度%' THEN 'TURBIDITY'
        ELSE tag_name_cn
    END AS  water_biz_type
  ,current_timestamp dm_update_time
  ,current_timestamp dm_load_time
from coss_dm.dm_wtw_opc_data_mini_day t
where i_code = 'TW009' and tag_type ='water_quality'
and tag_name_cn = '出厂食水-氟'
limit 1)
union all 
(
select 
  t.i_code as installation_id                     -- install code
  ,t.tag_name                         -- tag name
  ,t.tag_name_tc as comment               -- tag traditional chinese name
  ,cast(0.35 as decimal(15,5)) as value               -- tag value
  ,t.tag_time as time                    -- tag time
  ,t.units  as unit                    -- tag units
  ,CASE 
        WHEN tag_name_cn LIKE '%余氯%' THEN 'CHLORINE'
        WHEN tag_name_cn LIKE '%PH%' THEN 'PH'
        WHEN tag_name_cn LIKE '%氟%' THEN 'FLUORIDE'
        WHEN tag_name_cn LIKE '%浊度%' THEN 'TURBIDITY'
        ELSE tag_name_cn
    END AS  water_biz_type
  ,current_timestamp dm_update_time
  ,current_timestamp dm_load_time
from coss_dm.dm_wtw_opc_data_mini_day t
where i_code = 'TW009' and tag_type ='water_quality'
and tag_name_cn = '出厂食水-浊度'
limit 1)
), t_b as (
select 
half_hour_time,
tag_name
from 
(
SELECT 
    
    generate_series AS half_hour_time
FROM generate_series(
    -- 起始时间：近3天的00:00:00（如今天是2025-12-24，则起始为2025-12-21 00:00:00）
    (CURRENT_DATE - INTERVAL '3 days')::timestamp,
    -- 结束时间：当天的23:30:00
    (CURRENT_DATE + INTERVAL '1 day - 30 minutes')::timestamp,
    -- 步长：30分钟
    INTERVAL '30 minutes'
)
) t 
join (select 
  distinct t.tag_name_cn as comment               -- tag traditional chinese name
  ,tag_name
from coss_dm.dm_wtw_opc_data_mini_day t
where i_code = 'TW009' and tag_type ='water_quality'
and tag_name_cn like '出厂食水%') t1 on 1=1
)
select 
installation_id,
t.tag_name,
comment,
value,
half_hour_time as time,
unit,
water_biz_type,
current_timestamp dm_update_time,
current_timestamp dm_load_time
from t_a t inner join t_b t1 on t.tag_name = t1.tag_name 









select 
installation_id,
scada_tag,
comment,
value,
time,
unit,
water_biz_type,
current_timestamp dm_update_time,
current_timestamp dm_load_time
from coss_dm.dm_pnw_pipe_tag_monitored_rt_mini 







drop table if exists coss_dm.dm_cus_annon_watersupplyinfo_di;

create table if not exists coss_dm.dm_cus_annon_watersupplyinfo_di(
    id int8,
    recid int8,
    updateid int8,
    watersupplytype int4,
    watersupplyaddressen varchar(1000),
    watersupplyaddresscn varchar(1000),
    watersupplyaddressgn varchar(1000),
    watersupplytime timestamp,
    opentime timestamp,
    endtime timestamp,
    quality int4,
    watersupplyremark varchar(4000),
    createtime timestamp,
    creator int4,
    location varchar(100),
    leavingtime timestamp,
    vechiclenumber varchar(100),
    drivername varchar(50),
    driverphone varchar(50),
    workman1 varchar(50),
    workman2 varchar(50),
    workmanphone1 varchar(50),
    workmanphone2 varchar(50),
    locationx varchar(100),
    locationy varchar(100),
    isvalid int4,
    lastupdatetime timestamp,
    updater int4,
    dm_load_time timestamp(6) default current_timestamp,
    dm_update_time timestamp(6) default current_timestamp,
    primary key (id)
)
with (
    orientation = row,
    compression = no
);
comment on table coss_dm.dm_cus_annon_watersupplyinfo_di is 'Customer Announcement Temporary Water Supply Information Fact Table (DI: Incremental Update Table)';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.id is 'Primary Key Id';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.recid is 'Announcement Id';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.updateid is 'Announcement Record Id';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplytype is 'Temporary Water Supply Method';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyaddressen is 'Temporary Water Supply Address (English)';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyaddresscn is 'Temporary Water Supply Address (Simplified Chinese)';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyaddressgn is 'Temporary Water Supply Address (Traditional Chinese)';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplytime is 'Temporary Water Supply Application Time';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.opentime is 'Opening Time';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.endtime is 'Closing Time';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.quality is 'Quantity';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.watersupplyremark is 'Remarks';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.createtime is 'Creation Time';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.creator is 'Creator';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.location is 'Coordinates';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.leavingtime is 'Departure Time';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.vechiclenumber is 'License Plate Number';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.drivername is 'Driver Name';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.driverphone is 'Driver Contact Number';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.workman1 is 'Staff Member 1';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.workman2 is 'Staff Member 2';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.workmanphone1 is 'Staff Contact Number 1';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.workmanphone2 is 'Staff Contact Number 2';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.locationx is 'Coordinate X';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.locationy is 'Coordinate Y';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.isvalid is 'Validity (0: Invalid, 1: Valid)';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.lastupdatetime is 'Last Update Time';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.updater is 'Updater';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.dm_load_time is 'Dm Load Time';
comment on column coss_dm.dm_cus_annon_watersupplyinfo_di.dm_update_time is 'Dm Update Time';



10.66.169.140
lp.cups -d TASKaflfa5054ci wwol.pdf



create table coss_tmp.dim_ass_wtw_info_arch251223 as 
select * from coss_dim.dim_ass_wtw_info dawi 
where 
i_code in
('TW010',
'TW028',
'TW008',
'TW022');

delete  from coss_dim.dim_ass_wtw_info dawi 
where 
i_code in
('TW010',
'TW028',
'TW008',
'TW022')


















drop table if exists coss_dm.dm_wtw_opc_data_mini_month;

create table if not exists coss_dm.dm_wtw_opc_data_mini_month (
    id              bigserial       not null,
    i_code          varchar(50)     not null,
    region_abbr     varchar(50)     null, 
    wtw_name_en     varchar(128)    null,
    wtw_name_cn     varchar(128)    null,
    wtw_name_tc     varchar(128)    null,
    tag_name_cn     varchar(128)    null,
    tag_name_tc     varchar(128)    null,
    units           varchar(128)    null,
    tag_type        varchar(128)    null,  
    tag_name        varchar(128)    null,
    tag_value       varchar(128)    null,
    quality         int             null,
    tag_time        timestamp       not null,
    dm_update_time  timestamp       not null,
    dm_load_time    timestamp(6)    not null,
    primary key (i_code, tag_name, tag_time)
)
with (
    orientation = row,
    compression = no,
    storage_type = ustore,
    segment = off
)
partition by range (tag_time)
(
    -- 2025 Monthly Partitions
    partition mh_202501 values less than ('2025-02-01 00:00:00'),
    partition mh_202503 values less than ('2025-04-01 00:00:00'),
    partition mh_202505 values less than ('2025-06-01 00:00:00'),
    partition mh_202507 values less than ('2025-08-01 00:00:00'),
    partition mh_202509 values less than ('2025-10-01 00:00:00'),
    partition mh_202511 values less than ('2025-12-01 00:00:00'),
    
    -- 2026 Monthly Partitions
    partition mh_202601 values less than ('2026-02-01 00:00:00'),
    partition mh_202603 values less than ('2026-04-01 00:00:00'),
    partition mh_202605 values less than ('2026-06-01 00:00:00'),
    partition mh_202607 values less than ('2026-08-01 00:00:00'),
    partition mh_202609 values less than ('2026-10-01 00:00:00'),
    partition mh_202611 values less than ('2026-12-01 00:00:00'),
    
    -- 2027 Monthly Partitions
    partition mh_202701 values less than ('2027-02-01 00:00:00'),
    partition mh_202703 values less than ('2027-04-01 00:00:00'),
    partition mh_202705 values less than ('2027-06-01 00:00:00'),
    partition mh_202707 values less than ('2027-08-01 00:00:00'),
    partition mh_202709 values less than ('2027-10-01 00:00:00'),
    partition mh_202711 values less than ('2027-12-01 00:00:00'),
    
    -- 2028 Monthly Partitions（修正年份错误：2027-12-01改为2028-12-01）
    partition mh_202801 values less than ('2028-02-01 00:00:00'),
    partition mh_202803 values less than ('2028-04-01 00:00:00'),
    partition mh_202805 values less than ('2028-06-01 00:00:00'),
    partition mh_202807 values less than ('2028-08-01 00:00:00'),
    partition mh_202809 values less than ('2028-10-01 00:00:00'),
    partition mh_202811 values less than ('2028-12-01 00:00:00'),
    
    -- Future Partition
    partition mh_future values less than ('9999-01-01 00:00:00')
);

-- Comment on table
comment on table coss_dm.dm_wtw_opc_data_mini_month 
is 'Water Treatment Work Tag Poc Data Latest';

-- Comments on columns
comment on column coss_dm.dm_wtw_opc_data_mini_month.id 
is 'Id';
comment on column coss_dm.dm_wtw_opc_data_mini_month.i_code 
is 'Install Code';
comment on column coss_dm.dm_wtw_opc_data_mini_month.region_abbr 
is 'Region Abbreviation';
comment on column coss_dm.dm_wtw_opc_data_mini_month.wtw_name_en 
is 'Water Treatments Work English Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.wtw_name_cn 
is 'Water Treatments Work Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.wtw_name_tc 
is 'Water Treatments Work Traditional Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_name_cn 
is 'Tag Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_name_tc 
is 'Tag Traditional Chinese Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.units 
is 'Tag Units';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_type
is 'Tag Type';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_name 
is 'Tag Name';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_value 
is 'Tag Value';
comment on column coss_dm.dm_wtw_opc_data_mini_month.quality 
is 'Quality';
comment on column coss_dm.dm_wtw_opc_data_mini_month.tag_time 
is 'Tag Time';
comment on column coss_dm.dm_wtw_opc_data_mini_month.dm_update_time 
is 'Dm Update Time';
comment on column coss_dm.dm_wtw_opc_data_mini_month.dm_load_time 
is 'Dm Load Time';






























-- coss_dim.dim_sr_installation_info definition

-- Drop table

-- DROP TABLE coss_dim.dim_sr_installation_info;

CREATE TABLE coss_dim.dim_sr_installation_info (
	sr_id varchar(50) NOT NULL, -- Sr Id 
	i_code varchar(50) NULL, -- Installation Code 
	sr_name varchar(200) NULL, -- Sr Name 
	sr_cname varchar(300) NULL, -- Sr Name Tc
	rpt_label varchar(100) NULL, -- Report Label
	region_code varchar(50) NULL, -- Region Abbr(注：这张旧版本的数据表，region_code字段是关联dim_region_info.region_abbr字段，后续可能会修改字段名)
	sub_region varchar(50) NULL, -- Sub Region 
	region_name varchar(50) NULL, -- Region Name En
	region_cname varchar(50) NULL, -- Region Name Tc
	region_ind varchar(50) NULL, -- Region Index
	w_type varchar(50) NULL, -- Water_type
	w_type_desc varchar(50) NULL, -- Water Type Desc
	is_qty int4 NULL, -- Is Water Output Quantity 1 Is True 0 Is False
	dim_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dim Update Time
	dim_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dim Load Time 
	CONSTRAINT dim_sr_installation_info_pkey PRIMARY KEY (sr_id)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dim.dim_sr_installation_info IS 'Service Reservoir Installation Information';

-- Column comments

COMMENT ON COLUMN coss_dim.dim_sr_installation_info.sr_id IS 'Sr Id ';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.i_code IS 'Installation Code ';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.sr_name IS 'Sr Name ';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.sr_cname IS 'Sr Name Tc';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.rpt_label IS 'Report Label';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.region_code IS 'Region Abbr(注：这张旧版本的数据表，region_code字段是关联dim_region_info.region_abbr字段，后续可能会修改字段名)';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.sub_region IS 'Sub Region ';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.region_name IS 'Region Name En';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.region_cname IS 'Region Name Tc';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.region_ind IS 'Region Index';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.w_type IS 'Water_type';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.w_type_desc IS 'Water Type Desc';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.is_qty IS 'Is Water Output Quantity 1 Is True 0 Is False';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.dim_update_time IS 'Dim Update Time';
COMMENT ON COLUMN coss_dim.dim_sr_installation_info.dim_load_time IS 'Dim Load Time ';


















https://docs.qq.com/sheet/DUGdOTE9rdnJwb2xI?no_promotion=1&tab=959o1o

 



select count(*) from coss_dm.dm_cus_monthly_skill_hotline_item_di
union all select count(*) from coss_dm.dm_cus_monthly_water_quality_cpt_di
union all select count(*) from coss_dm.dm_cus_monthly_skill_hotline_wo_item_di
union all select count(*) from coss_dim.dim_cus_skill_info

352
160
352
11




amd
cmsdms
dip
imjrms
imwms

abpms
dwsams
isms
ohap
pems
wcdms
wmams

ods_sttss_extract_raw_water_supply_day
dwd_rws_etl_raw_water_supply_day
dim_rws_etl_raw_water_supply_day
dws_rws_etl_raw_water_supply_day
dm_rws_etl_raw_water_supply_day
<img width="346" height="111" alt="image" src="https://github.com/user-attachments/assets/73ae0a2b-5195-4555-ba71-3ee943a1198b" />









-- coss_dm.dm_srs_daily_sr_wl_qty_item_di
-- update subregion code 
update coss_dm.dm_srs_daily_sr_wl_qty_item_di set sub_region = concat(region_code,'(',sub_region,')') where sub_region is not null


-- update region code
update coss_dm.dm_srs_daily_sr_wl_qty_item_di set region_code = 'HKI' where region_code = 'HK'





-- coss_dim.dim_sr_installation_info
-- update subregion code 
update coss_dim.dim_sr_installation_info set sub_region = concat(region_code,'(',sub_region,')') where sub_region is not null


-- update region code
update coss_dim.dim_sr_installation_info set region_code = 'HKI' where region_code = 'HK'



drop table if exists coss_dm.dm_srs_daily_sr_wl_qty_item_di;

create table coss_dm.dm_srs_daily_sr_wl_qty_item_di (
    sr_id           varchar(50) null,
    i_code          varchar(50) null,
    sr_name         varchar(200) null,
    sr_cname        varchar(300) null,
    rpt_label       varchar(100) null,
    region_code     varchar(50) null,
    sub_region      varchar(50) null,
    region_name     varchar(50) null,
    region_cname    varchar(50) null,
    region_ind      varchar(50) null,
    w_type          varchar(50) null,
    w_type_desc     varchar(50) null,
    div_height      varchar(50) null,
    capacity        numeric(20, 5) null,
    w_lim           numeric(20, 5) null,
    num_of_storage  numeric(20, 2) null,
    a_wl            numeric(20, 5) null,
    b_wl            numeric(20, 5) null,
    qty_del         numeric(20, 5) null,
    rec_dt          timestamp(6) null,
    dm_update_time  timestamp(6) null default pg_systimestamp(),
    dm_load_time    timestamp(6) null default pg_systimestamp(),
    primary key (sr_id, rec_dt)
) with (
    orientation=row,
    compression=no
);

comment on table coss_dm.dm_srs_daily_sr_wl_qty_item_di 
is 'Service Reservoir Water Level And Qty_del Detail';

comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.sr_id           is 'Service Reservoir Id';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.i_code          is 'Installation Code';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.sr_name         is 'Service Reservoir Name En ';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.sr_cname        is 'Service Reservoir Name Tc ';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.rpt_label       is 'Report Label';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.region_code     is 'Region Code';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.sub_region      is 'Sub Region';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.region_name     is 'Region Name En';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.region_cname    is 'Region Name Tc';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.region_ind      is 'Region Ind';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.w_type          is 'Water Type';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.w_type_desc     is 'Water Type Describe';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.div_height      is 'Div Height';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.capacity        is 'Capacity';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.w_lim           is 'Water Limit';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.num_of_storage  is 'Num Of Storage';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.a_wl            is 'A Water Level';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.b_wl            is 'B Water Level ';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.qty_del         is 'Qty Del';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.rec_dt          is 'Rec Date';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.dm_update_time  is 'Dm Update Time';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.dm_load_time    is 'Dm Load Time';



insert into coss_dm.dm_srs_daily_sr_wl_qty_item_di
select 
sr_id
,i_code
,sr_name
,sr_cname
,rpt_label
,region_code
,sub_region
,region_name
,region_cname
,region_ind
,w_type
,w_type_desc
,div_height
,capacity
,w_lim
,num_of_storage
,a_wl
,b_wl
,qty_del
,rec_dt
from 
coss_tmp.dm_srs_daily_sr_wl_qty_item_di_arch_251127



create table coss_dim.dim_sr_installation_qty_info (
    sr_id            varchar(50) not null,
    i_code           varchar(50) null,
    sr_name_en       varchar(200) null,
    sr_name_tc       varchar(300) null,
    rpt_label        varchar(100) null,
    region_abbr      varchar(50) null,
    sub_region       varchar(50) null,
    region_ind       varchar(50) null,
    w_type           varchar(50) null,
    w_type_desc      varchar(50) null,
    dim_update_time  timestamp(6) null default pg_systimestamp(),
    dim_load_time    timestamp(6) null default pg_systimestamp(),
    primary key (sr_id)
) with (
    orientation=row,
    compression=no
);

comment on table coss_dim.dim_sr_installation_qty_info 
is 'Service Reservoir Installation Output Quantity Information';

comment on column coss_dim.dim_sr_installation_qty_info.sr_id           is 'Service Reservoir Id';
comment on column coss_dim.dim_sr_installation_qty_info.i_code          is 'Installation Code';
comment on column coss_dim.dim_sr_installation_qty_info.sr_name_en      is 'Service Reservoir Name';
comment on column coss_dim.dim_sr_installation_qty_info.sr_name_tc      is 'Service Reservoir Name Tc';
comment on column coss_dim.dim_sr_installation_qty_info.rpt_label       is 'Report Label';
comment on column coss_dim.dim_sr_installation_qty_info.region_abbr     is 'Region Abbr';
comment on column coss_dim.dim_sr_installation_qty_info.sub_region      is 'Sub Region ';
comment on column coss_dim.dim_sr_installation_qty_info.region_ind      is 'Region Index';
comment on column coss_dim.dim_sr_installation_qty_info.w_type          is 'Water_type';
comment on column coss_dim.dim_sr_installation_qty_info.w_type_desc     is 'Water Type Desc';
comment on column coss_dim.dim_sr_installation_qty_info.dim_update_time is 'Dim Update Time';
comment on column coss_dim.dim_sr_installation_qty_info.dim_load_time   is 'Dim Load Time ';



-- drop table if exists coss_dm.dm_rws_monthly_sr_qty_di;
create if not exists table coss_dm.dm_rws_monthly_sr_qty_di (
    statistical_month    varchar(7),
    sr_id                varchar(50),
    i_code               varchar(50),
    sr_name_en           varchar(200),
    sr_name_tc           varchar(300),
    rpt_label            varchar(100),
    region_abbr          varchar(50),
    sub_region           varchar(50),
    qty_del              decimal(20, 5),
    dm_update_time       timestamp(6) null default pg_systimestamp(),
    dm_load_time         timestamp(6) null default pg_systimestamp(),
    primary key (sr_id, statistical_month)
);

comment on table coss_dm.dm_rws_monthly_sr_qty_di is 'Service Reservoir Quantity Delivery';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.statistical_month  is 'Statistical Month';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.sr_id              is 'Service Reservoir Id';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.i_code             is 'Installation Code';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.sr_name_en         is 'Service Reservoir Name';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.sr_name_tc         is 'Service Reservoir Name Tc';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.rpt_label          is 'Report Label';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.region_abbr        is 'Region Abbr';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.sub_region         is 'Sub Region ';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.qty_del            is 'Quantity Deliver';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.dm_update_time     is 'Dm Update Time';
comment on column coss_dm.dm_rws_monthly_sr_qty_di.dm_load_time       is 'Dm Load Time ';


-- drop table if exists coss_dm.dm_rws_annual_sr_pool_stoped_di;

create table if not exists coss_dm.dm_rws_annual_sr_pool_stoped_di (
    statistical_year    varchar(7),
    sr_id               varchar(50),
    i_code              varchar(50),
    sr_name_en          varchar(200),
    sr_name_tc          varchar(300),
    rpt_label           varchar(100),
    region_abbr         varchar(50),
    sub_region          varchar(50),
    a_stoped            decimal(20, 5),
    b_stoped            decimal(20, 5),
    dm_update_time      timestamp(6) null default pg_systimestamp(),
    dm_load_time        timestamp(6) null default pg_systimestamp(),
    primary key (sr_id, statistical_year)
);

comment on table coss_dm.dm_rws_annual_sr_pool_stoped_di is 'Service Reservoir Annual Pool Stoped Situation';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.statistical_year  is 'Statistical Year';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.sr_id              is 'Service Reservoir Id';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.i_code             is 'Installation Code';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.sr_name_en         is 'Service Reservoir Name EN';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.sr_name_tc         is 'Service Reservoir Name Tc';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.rpt_label          is 'Report Label';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.region_abbr        is 'Region Abbr';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.sub_region         is 'Sub Region ';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.a_stoped           is 'Number of Days When Pool A Is Stopped';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.b_stoped           is 'Number of Days When Pool B Is Stopped';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.dm_update_time     is 'Dm Update Time';
comment on column coss_dm.dm_rws_annual_sr_pool_stoped_di.dm_load_time       is 'Dm Load Time ';



-- 按需启用：删除水库设施信息表（若存在）
-- drop table if exists coss_dim.dim_sr_installation_info;

-- 创建DIM层水库设施信息表
create table coss_dim.dim_sr_installation_info (
    sr_id            varchar(50) not null,
    i_code           varchar(50) null,
    sr_name          varchar(200) null,
    sr_cname         varchar(300) null,
    rpt_label        varchar(100) null,
    region_code      varchar(50) null,
    sub_region       varchar(50) null,
    region_name      varchar(50) null,
    region_cname     varchar(50) null,
    region_ind       varchar(50) null,
    w_type           varchar(50) null,
    w_type_desc      varchar(50) null,
    dim_update_time  timestamp(6) null default pg_systimestamp(),
    dim_load_time    timestamp(6) null default pg_systimestamp()
) with (
    orientation=row,
    compression=no
);

-- 表注释：明确表业务用途
comment on table coss_dim.dim_sr_installation_info is 'Service Reservoir Installation Information';

-- 字段注释：保留原始业务说明（含旧表关联备注），首字母大写
comment on column coss_dim.dim_sr_installation_info.sr_id           is 'Sr Id ';
comment on column coss_dim.dim_sr_installation_info.i_code          is 'Installation Code ';
comment on column coss_dim.dim_sr_installation_info.sr_name         is 'Sr Name ';
comment on column coss_dim.dim_sr_installation_info.sr_cname        is 'Sr Name Tc';
comment on column coss_dim.dim_sr_installation_info.rpt_label       is 'Report Label';
comment on column coss_dim.dim_sr_installation_info.region_code     is 'Region Abbr(注：这张旧版本的数据表，region_code字段是关联dim_region_info.region_abbr字段，后续可能会修改字段名)';
comment on column coss_dim.dim_sr_installation_info.sub_region      is 'Sub Region ';
comment on column coss_dim.dim_sr_installation_info.region_name     is 'Region Name En';
comment on column coss_dim.dim_sr_installation_info.region_cname    is 'Region Name Tc';
comment on column coss_dim.dim_sr_installation_info.region_ind      is 'Region Index';
comment on column coss_dim.dim_sr_installation_info.w_type          is 'Water_type';
comment on column coss_dim.dim_sr_installation_info.w_type_desc     is 'Water Type Desc';
comment on column coss_dim.dim_sr_installation_info.dim_update_time is 'Dim Update Time';
comment on column coss_dim.dim_sr_installation_info.dim_load_time   is 'Dim Load Time ';



