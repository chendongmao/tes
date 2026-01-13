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



