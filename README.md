
jdbc:postgresql://192.168.138.107:8000,192.168.138.98:8000,192.168.138.25:8000,192.168.138.120:8000/wsd_isit?autoBalance=true&refreshCNIpListTime=3

jdbc:postgresql://10.66.110.64:8000,10.66.110.151:8000,10.66.110.194:8000,10.66.110.235:8000/wsd_isit?loadBalanceHosts=true&refreshCNIpListTime=3

 



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



