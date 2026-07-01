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
