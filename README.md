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



