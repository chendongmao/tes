

jdbc:postgresql://192.168.130.137:8000,192.168.130.11:8000,192.168.130.213:8000,192.168.130.145:8000/wsd?autoBalance=true&refreshCNIpListTime=3









预生产	10.66.168.212	192.168.110.226
预生产	10.66.168.11	192.168.110.215
预生产	10.66.168.85	192.168.110.145
ISIT	10.66.168.7	192.168.102.75
ISIT	10.66.168.50	192.168.102.155
ISIT	10.66.168.121	192.168.102.84
IUAT	10.66.168.174	192.168.101.238
IUAT	10.66.168.41	192.168.101.138
IUAT	10.66.168.113	192.168.101.145
<img width="422" height="199" alt="image" src="https://github.com/user-attachments/assets/2a5c07aa-05b3-42e1-be27-4ef21e773bef" />



import requests

# 配置参数
BASE_URL = "http://10.66.110.106:8325"
APP_ID = "替换为你的真实appId"
HEADERS = {"appId": APP_ID, "Content-Type": "application/json"}

def get_permission_data(page_no=1, page_size=10, device_codes=None, business_type=None):
    url = f"{BASE_URL}/share/data/permission"
    payload = {"pageNo": page_no, "pageSize": page_size}
    if device_codes:
        payload["deviceCodes"] = device_codes
    if business_type:
        payload["businessType"] = business_type

    resp = requests.post(url, json=payload, headers=HEADERS)
    resp.raise_for_status()  # 抛出http异常
    res = resp.json()
    return res if res.get("success") else None

# 示例调用
if __name__ == "__main__":
    data = get_permission_data(page_no=1, page_size=10)
    if data:
        records = data["data"]["records"]
        print(f"总条数：{data['data']['total']}")
        for item in records:
            print("设备编码：", item["deviceCode"])




			

curl -X POST --url "http://10.66.110.106:8325/share/data/permission" \
-H "appId: none" \
-H "Content-Type: application/json" \
-d '{
  "deviceCodes": [],
  "pageSize": 10,
  "pageNo": 1
}'

{"success":true,"code":200,"message":"success","data":{"records":[],"total":0,"size":10,"current":1,"orders":[{"column":"sort_num","asc":true},{"column":"update_time","asc":false}],"optimizeCountSql":true,"searchCount":true,"optimizeJoinOfCountSql":true,"maxLimit":null,"countId":null,"pages":0},"timestamp":1783491271051,"requestId":"LZXAQC4TalMTa3hVVMc5","msg":"success"}





curl -X POST --url "http://10.66.110.106:8325/share/data/sensor/realtime" \
-H "Content-Type: application/json" \
-d  '{
    "sensorCodes": [
        "WLIS_1023_voltage_1",
        "WLIS_1023_voltage_2",
        "WLIS_1023_digital_in_1"
    ]
}'



{"success":true,"code":200,"message":"success",
"data":[{"snsCode":"WLIS_1023_voltage_1"}
,{"snsCode":"WLIS_1023_voltage_2"},
{"snsCode":"WLIS_1023_digital_in_1"}],"timestamp":1783482568080,"requestId":"xhQIsn4O1KyBbnZUekOe","msg":"success"}





![Uploading image.png…]()

 /share/data/sensor/realtime


{
    "sensorCodes": [
        "WLIS_1023_voltage_1",
        "WLIS_1023_voltage_2",
        "WLIS_1023_digital_in_1"
    ]
}




curl -X POST --url "http://10.66.110.106:8325/share/data/sensor/realtime" \
-H "Content-Type: application/json" \
-d {
    "sensorCodes": [
        "WLIS_1023_voltage_1",
        "WLIS_1023_voltage_2",
        "WLIS_1023_digital_in_1"
    ]
}






curl -X POST --url "http://10.66.110.106:8325/share/data/permission" \
-H "Content-Type: application/json" \
-d '{
  "deviceCodes": [],
  "pageSize": 10,
  "pageNo": 1
}'




<img width="3436" height="1594" alt="image" src="https://github.com/user-attachments/assets/38066cb6-0ceb-443b-9d83-4797fc1e6314" />




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


-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function Describe: Terminal User Monitoring For Water Quality
-- Create         By: dongmaochen
-- Create       Date: 2026-05-21
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table: coss_dwd.dwd_tmu_sensor_data_mini_month
-- Target Table: coss_dm.dm_tmu_sensor_data_minf
-- ****************************************************************************************
insert into coss_dm.dm_tmu_sensor_data_mini_month 
select 
    id,
    sensor_code,
    sensor_value,
    sensor_time,
    dm_update_time,
    dm_load_time
from (
    select 
        id,
        sensor_code,
        sensor_value,
        sensor_time,
        dm_update_time,
        dm_load_time,
        row_number() over (partition by sensor_code order by sensor_time desc) as rn
    from coss_dwd.dwd_tmu_sensor_data_mini_month
    where dwd_update_time >= '${dm_update_time}'
) t
where rn = 1
on duplicate key update nothing






https://10.66.110.21:6443/arcgis/rest/services/MSC/MSC/MapServer/0/query




https://10.66.168.83/dm/topic/waterQualityComplaint/waterQualityPoint/position



预生产DP
 http://10.66.168.212:12345/dolphinscheduler/ui/login

预生产GaussDB
jdbc:postgresql://10.66.169.52:8000,10.66.169.59:8000,10.66.169.76:8000,10.66.169.225:8000/wsd?loadBalanceHosts=true&refreshCNIpListTime=3
账号：coss
密码:WsdUat@MS30F



-- coss_dim.dim_wtw_installation_info definition

-- Drop table

-- DROP TABLE coss_dim.dim_wtw_installation_info;

CREATE TABLE coss_dim.dim_wtw_installation_info (
	asset_id numeric(11) NOT NULL, -- Asset Id 
	asset_name varchar(120) NULL, -- Asset Name
	asset_desc varchar(120) NULL, -- Asset Descrip
	installation_id varchar(36) NULL, -- Installation ID
	loca_code varchar(15) NULL, -- Local Code
	region_abbr varchar(150) NULL, -- Region
	i_type_id numeric(11) NULL, -- Installation Type Id 
	i_type_code varchar(150) NULL, -- Installation Code 
	i_type_desc varchar(150) NULL, -- Installation Type Descrip
	dim_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Update Time
	dim_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Load Time
	CONSTRAINT dim_wtw_installation_info_pkey PRIMARY KEY (asset_id)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dim.dim_wtw_installation_info IS 'The Water Treatment Works Items';

-- Column comments

COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.asset_id IS 'Asset Id ';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.asset_name IS 'Asset Name';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.asset_desc IS 'Asset Descrip';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.installation_id IS 'Installation ID';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.loca_code IS 'Local Code';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.region_abbr IS 'Region';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.i_type_id IS 'Installation Type Id ';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.i_type_code IS 'Installation Code ';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.i_type_desc IS 'Installation Type Descrip';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.dim_update_time IS 'Dm Update Time';
COMMENT ON COLUMN coss_dim.dim_wtw_installation_info.dim_load_time IS 'Dm Load Time';

-- Permissions

ALTER TABLE coss_dim.dim_wtw_installation_info OWNER TO gddst01;
GRANT ALL ON TABLE coss_dim.dim_wtw_installation_info TO gddst01;






-- coss_dm.dm_srs_daily_sr_wl_qty_item_di definition

-- Drop table

-- DROP TABLE coss_dm.dm_srs_daily_sr_wl_qty_item_di;

CREATE TABLE coss_dm.dm_srs_daily_sr_wl_qty_item_di (
	sr_id varchar(50) NOT NULL, -- Service Reservoir Id
	i_code varchar(50) NULL, -- Installation Code
	sr_name varchar(200) NULL, -- Service Reservoir Name En 
	sr_cname varchar(300) NULL, -- Service Reservoir Name Tc 
	rpt_label varchar(100) NULL, -- Report Label
	region_code varchar(50) NULL, -- Region Code
	sub_region varchar(50) NULL, -- Sub Region
	region_name varchar(50) NULL, -- Region Name En
	region_cname varchar(50) NULL, -- Region Name Tc
	region_ind varchar(50) NULL, -- Region Ind
	w_type varchar(50) NULL, -- Water Type
	w_type_desc varchar(50) NULL, -- Water Type Describe
	a_wl numeric(20, 5) NULL, -- A Water Level
	b_wl numeric(20, 5) NULL, -- B Water Level 
	a_storage numeric(20, 5) NULL,
	b_storage numeric(20, 5) NULL, -- B Water Storage 
	tot_storage numeric(20, 5) NULL, -- Total Volume Of Water In A+ B+..+R.  Unit Is In Cu M
	qty_del numeric(20, 5) NULL, -- Qty Del
	rec_dt timestamp(6) NOT NULL, -- Rec Date
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Load Time
	CONSTRAINT dm_srs_daily_sr_wl_qty_item_di_pkey PRIMARY KEY (sr_id, rec_dt)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_srs_daily_sr_wl_qty_item_di IS 'Service Reservoir Water Level And Qty_del Detail';

-- Column comments

COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.sr_id IS 'Service Reservoir Id';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.i_code IS 'Installation Code';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.sr_name IS 'Service Reservoir Name En ';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.sr_cname IS 'Service Reservoir Name Tc ';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.rpt_label IS 'Report Label';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.region_code IS 'Region Code';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.sub_region IS 'Sub Region';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.region_name IS 'Region Name En';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.region_cname IS 'Region Name Tc';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.region_ind IS 'Region Ind';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.w_type IS 'Water Type';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.w_type_desc IS 'Water Type Describe';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.a_wl IS 'A Water Level';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.b_wl IS 'B Water Level ';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.b_storage IS 'B Water Storage ';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.tot_storage IS 'Total Volume Of Water In A+ B+..+R.  Unit Is In Cu M';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.qty_del IS 'Qty Del';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.rec_dt IS 'Rec Date';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.dm_update_time IS 'Dm Update Time';
COMMENT ON COLUMN coss_dm.dm_srs_daily_sr_wl_qty_item_di.dm_load_time IS 'Dm Load Time';

-- Permissions

ALTER TABLE coss_dm.dm_srs_daily_sr_wl_qty_item_di OWNER TO gddst01;
GRANT ALL ON TABLE coss_dm.dm_srs_daily_sr_wl_qty_item_di TO gddst01;






ods_iot_extract_device_info_day
http://10.66.169.58:8001/iot3/rest/api/v1/realtime.json


drop table if exists coss_ods.ods_iot_tmu_device_info_df;

create table if not exists coss_ods.ods_iot_tmu_device_info_df (
    device_code      varchar(200),
    device_name      varchar(200),
    sensor_id        varchar(200),
    sensor_name      varchar(200),
    sensor_unit      varchar(120),
    ods_update_time  timestamp(6) null default pg_systimestamp(),
    ods_load_time    timestamp(6) null default pg_systimestamp(),
    primary key (device_code)
);

comment on table coss_ods.ods_iot_tmu_device_info_df is 'Device Info';
comment on column coss_ods.ods_iot_tmu_device_info_df.device_code is 'Device Code';
comment on column coss_ods.ods_iot_tmu_device_info_df.device_name is 'Device Name';
comment on column coss_ods.ods_iot_tmu_device_info_df.sensor_id is 'Sensorid';
comment on column coss_ods.ods_iot_tmu_device_info_df.sensor_name is 'Sensor Name';
comment on column coss_ods.ods_iot_tmu_device_info_df.sensor_unit is 'Sensor Unit';
comment on column coss_ods.ods_iot_tmu_device_info_df.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_iot_tmu_device_info_df.ods_load_time is 'Ods Load Time';













http://10.66.169.102:8330/share/data/sensor/moreDevRealtime

root@wsd-server02:~# telnet 10.66.169.102 8330
Trying 10.66.169.102...
telnet: Unable to connect to remote host: Connection refused











 





pems.t_dic_district   -- 关联运作区和行政区
pems.t_dic_sub_district   -- 关联运作区和行政区
pems.t_dic_bigclass   -- 关联投诉类型
-- 关联工单状态
pems.t_sys_dict  -- 关联渠道码表
pems.t_sys_dict  -- 水质类型编码




    
    
    
    
    
    COSS系统在预生产环境访问EMIS接口报错，需要您协助帮忙解决，五个接口报错内容如下：
1. 访问接口：https://wiki.sis2.wsd.gov/ems/webresources/reports?loc_id=24&from=2023-01-01&to=2023-02-28
报错内容：(conn=43276) Table 'mysql2.report_pump' doesn't exist Query: SELECT LEFT(Report_Id,LENGTH(Report_Id)-6) AS asset_id, RIGHT(Report_Id,6) as ym, Hours_Run_This_Month, Pump_Number, Water_Pumped_This_Month, pd.Name as drive, pc.Name as category, del.Name as destination, del.ID AS dest_id, Average_Head_Suct, Average_Head_Del FROM report_pump rp INNER JOIN pump_delivery_to del ON rp.Delivery_To_Id=del.ID INNER JOIN pump_category pc ON rp.Category_Id = pc.ID INNER JOIN pump_drive pd ON rp.Drive_Id = pd.ID HAVING asset_id = ? AND ym BETWEEN ? AND ? ORDER BY ym,Pump_Number Parameters: [24, 202301, 202302]

2. 访问接口：https://wiki.sis2.wsd.gov/ems/webresources/bills?from=2023-01-01&to=2023-01-31
报错内容：{"exception":{"class":"SQLException","message":"(conn=43276) Table 'mysql2.billing' doesn't exist Query: SELECT b.Date, a.Name, t.Name , b.kWh_On_Peak, b.kWh_Off_Peak, b.kVA_On_Peak, b.kVA_Off_Peak, b.Payout, t.Description, a.ID  FROM billing b INNER JOIN asset a ON b.Location_Code_Id=a.ID INNER JOIN tariff t ON b.Tariff_Id=t.ID WHERE b.Date >= ? AND b.Date<= ? ORDER BY a.Name, b.Date Parameters: [2023-01-01, 2023-01-31]"}}

3. 访问接口：https://wiki.sis2.wsd.gov/ems/webresources/assets
报错内容：[{"class":"SQLException","message":"(conn=43276) Table 'mysql2.asset' doesn't exist Query: SELECT a.ID, a.Name, a.Description, a.Location_Code, a.Account_No, a.Remarks, a.Active, a.Offical_Name as Official_Name, a.Station_Code, a.Billing_Active, a.Installation_number, r.Name as Region, r.Description as Region_Desc, t.Name as Type, t.Description as Type_Desc, ps_active, ecw_active, hkp_active, fy_active, 1 AS 1035_active, fw_portion, sw_portion, rw_portion, tw_portion FROM asset a INNER JOIN region r ON a.Region_Id=r.id INNER JOIN installation_type t ON a.Installation_Type_Id=t.ID   ORDER BY a.ID Parameters: []"}]

4. 访问接口：https://wiki.sis2.wsd.gov/ems/webresources/pumps
报错内容：[{"class":"SQLException","message":"(conn=43276) Table 'mysql2.pump_details' doesn't exist Query: SELECT p.Equipment_No, a.ID, a.Name, m.Name, p.Designed_Capacity, p.Designed_Stage, p.Running_Hour_Overhaul, p.LastOverhaulDate, p.Suspend FROM pump_details p INNER JOIN asset a ON a.ID=p.Asset_Id INNER JOIN pump_manufacturer m ON p.Manufacturer_Id=m.ID  ORDER BY p.Equipment_No Parameters: []"}]

5. 访问接口：https://wiki.sis2.wsd.gov/ems/webresources/tagnames
报错内容：HTTP Status 500 – Internal Server Error




Select count(*) from coss_ods.ods_sttss_rws_channel_flow_di_year where last_upd_dt >= ‘2025-07-16 00:00:00.00’;

Select count(*) from sttss.channel_flow where last_upd_dt >= ‘2025-07-16 00:00:00.00’;






https://wiki.sis2.wsd.gov/ems/webresources/reports?loc_id=24&from=2023-01-01&to=2023-02-28

https://wiki.sis2/wsd.gov/ems/webresources/bills?from=2023-01-01&to=2023-01-31


https://wiki.sis2.wsd.gov/ems/webresources/assets?id=1&id=2


https://wiki.sis2.wsd.gov/ems/webresources/pumps?equip-number=M503-10905&equip-number=M524-11325
https://wiki.sis2.wsd.gov/ems/webresources/tagnames?id=4&id=55


API_URL = 'http://10.66.169.58:8001/iot3/rest/api/v1/realtime.json'
