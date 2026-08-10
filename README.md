# -*- coding: utf-8 -*-
# File : point_in_shape.py
# Author : CDM
# Date : 2026/5/18 10:55

import pandas as pd
import json
from shapely.geometry import Point, Polygon
from shapely.strtree import STRtree
import warnings

warnings.filterwarnings('ignore')

def match_wq_complaint_sz(df_areas: pd.DataFrame, df_orders: pd.DataFrame) -> pd.DataFrame:
    """
    Spatial matching using R-tree index (point-by-point query, more stable)
    """
    if len(df_orders) == 0:
        return pd.DataFrame(columns=["ordernum", "supply_id", "supply_code", "water_type_code", "ordernum"])

    # Parse polygons
    geometry_list = []
    area_metadata = []

    for _, row in df_areas.iterrows():
        try:
            coords = [(p[0], p[1]) for p in json.loads(row["geometry"])[0]]
            polygon = Polygon(coords)
            geometry_list.append(polygon)
            area_metadata.append({
			    "supply_id": row["supply_id"],
                "supply_code": row["supply_code"],
                "water_type_code": row["water_type_code"]
            })
        except Exception as e:
            print(f"Error parsing geometry for area {row['supply_code']}: {e}")
            continue

    if not geometry_list:
        return pd.DataFrame(columns=["ordernum", "supply_id", "supply_code", "water_type_code", "ordernum"])

    # Build spatial index
    spatial_index = STRtree(geometry_list)

    # Preprocess order data
    df_orders = df_orders.copy()
    df_orders["coordinate_x"] = pd.to_numeric(df_orders["coordinate_x"], errors="coerce")
    df_orders["coordinate_y"] = pd.to_numeric(df_orders["coordinate_y"], errors="coerce")
    df_orders = df_orders.dropna(subset=["coordinate_x", "coordinate_y"])

    # Match point by point (accelerated with spatial index)
    match_results = []

    for _, order in df_orders.iterrows():
        point = Point(order.coordinate_x, order.coordinate_y)

        # Query candidate areas using spatial index (returns indices in geometry_list)
        candidate_indices = spatial_index.query(point)

        # Iterate candidates for precise judgment
        matched = False
        for area_idx in candidate_indices:
            # Ensure valid index
            if area_idx < len(geometry_list):
                if geometry_list[area_idx].contains(point):
                    match_results.append((
                        order.ordernum,
					    area_metadata[area_idx]["supply_id"],
                        area_metadata[area_idx]["supply_code"],
                        area_metadata[area_idx]["water_type_code"]
                    ))
                    matched = True
                    break

    print(f"Matched {len(match_results)} out of {len(df_orders)} order incidents")

    return pd.DataFrame(
        match_results,
        columns=["ordernum", "supply_id", "supply_code", "water_type_code"]
    )



	
























-- drop table if exists coss_dwd.dwd_cus_water_quality_accident_wo_mini;

drop table if exists coss_dwd.dwd_cus_water_quality_accident_wo_mini;

create table if not exists coss_dwd.dwd_cus_water_quality_accident_wo_mini (
    ordernum varchar(150) null, -- Ordernum
    buildingno varchar(150) null, -- Building NO
    relateorder varchar(150) null, -- Relate Order
    case_num int8 null, -- Case Num
    dwd_update_time timestamp(6) default current_timestamp, -- Dwd Update Time
    dwd_load_time timestamp(6) default current_timestamp, -- Dwd Load Time
    primary key (ordernum)
)
with (
    orientation=row,
    compression=no,
    storage_type=USTORE,
    segment=off
);

-- table comment
comment on table coss_dwd.dwd_cus_water_quality_accident_wo_mini is 'Customer Water Quality Accident Work Order Mini';

-- column comment
comment on column coss_dwd.dwd_cus_water_quality_accident_wo_mini.ordernum is 'Ordernum';
comment on column coss_dwd.dwd_cus_water_quality_accident_wo_mini.buildingno is 'Building NO';
comment on column coss_dwd.dwd_cus_water_quality_accident_wo_mini.relateorder is 'Relate Order';
comment on column coss_dwd.dwd_cus_water_quality_accident_wo_mini.case_num is 'Case Num';
comment on column coss_dwd.dwd_cus_water_quality_accident_wo_mini.dwd_update_time is 'Dwd Update Time';
comment on column coss_dwd.dwd_cus_water_quality_accident_wo_mini.dwd_load_time is 'Dwd Load Time';


-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Customer Service WO Details
-- Create         By:
-- Create       Date: 2026-07-07
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year
-- Target Table:  coss_dwd.dwd_cus_water_quality_accident_wo_mini
-- ****************************************************************************************

with t_a as (
    select distinct relateorder
    from coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year
    where relateorder is not null
      and relateorder != ''
      and ods_update_time >= '${dwd_update_time}'
),
t_b as (
    select
        ordernum,
        decode(relateorder, '', ordernum, relateorder) as relateorder
    from coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year t
    where exists (
        select 1
        from t_a s
        where s.relateorder = t.ordernum
    )
    or exists (
        select 1
        from t_a s
        where s.relateorder = t.relateorder
    )
),
t_c as (
    select
        ordernum,
        relateorder,
        case_num,
        current_timestamp as dwd_update_time,
        current_timestamp as dwd_load_time
    from (
        select
            ordernum,
            relateorder,
            count(1) over(partition by relateorder) as case_num
        from t_b
    ) sub
    where case_num > 1
)
insert into coss_dwd.dwd_cus_water_quality_accident_wo_stg_mini (
    ordernum,
    relateorder,
    case_num,
    dwd_update_time,
    dwd_load_time
)
select
    ordernum,
    relateorder,
    case_num,
    dwd_update_time,
    dwd_load_time
from t_c;


insert into coss_dwd.dwd_cus_water_quality_accident_wo_mini (
    ordernum,
    buildingno,
    relateorder,
    case_num,
    dwd_update_time,
    dwd_load_time
)
select
    ordernum,
    buildingno,
    relateorder,
    case_num,
    current_timestamp as dwd_update_time,
    current_timestamp as dwd_load_time
from coss_dwd.dwd_cus_water_quality_accident_wo_stg_mini
on duplicate key update
    relateorder = values(relateorder),
    buildingno = values(buildingno),
    case_num = values(case_num),
    dwd_update_time = values(dwd_update_time);




create table if not exists coss_dwd.dwd_cus_water_quality_accident_impact_stg_mini (
    ordernum varchar(64) not null, -- Order Num
    incident_cpt_no numeric(15) null, -- Number Of Incident Complaints
    water_quality_no numeric(15) null, -- Number Of Water Quality Samples
    meter_clearance_no numeric(15) null, -- Number Of Water Meter Clearance Requests
    dwd_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    dwd_update_time timestamp(6) null default pg_systimestamp() -- Data Update Time
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

-- ****************************************************************************************
-- Subject Areas: Customer Service Water Quality Accident Statistics
-- Function Describe: Statistical water sampling and meter cleaning quantity by relateorder
-- Source Table 1: coss_dwd.dwd_cus_water_quality_accident_wo_mini
-- Source Table 2: coss_ods.ods_pems_cus_water_sample_number_di
-- Source Table 3: coss_ods.ods_pems_cus_meter_clean_number_di
-- Target Table: coss_dwd.dwd_cus_water_quality_accident_impact_mini
-- ****************************************************************************************


 where dwd_update_time >= '${dwd_update_time}'



with base_relate as (
    -- 1、基础维度：按relateorder统计投诉工单总数 incident_cpt_no
    select
        relateorder as ordernum,
        count(distinct ordernum) as incident_cpt_no
    from coss_dwd.dwd_cus_water_quality_accident_wo_mini
    where dwd_update_time >= '${dwd_update_time}'
    group by relateorder
),
sample_stat as (
    -- 2、按relateorder汇总水样数量 water_quality_no
    select
        a.relateorder,
        sum(b.sample_num) as water_quality_no
    from coss_dwd.dwd_cus_water_quality_accident_wo_mini a
    left join coss_ods.ods_pems_cus_water_sample_number_di b
        on a.ordernum = b.ordernum
    group by a.relateorder
),
clean_stat as (
    -- 3、按relateorder汇总水表清洗数量 meter_clearance_no
    select
        a.relateorder,
        sum(b.clean_num) as meter_clearance_no
    from coss_dwd.dwd_cus_water_quality_accident_wo_mini a
    left join coss_ods.ods_pems_cus_meter_clean_number_di b
        on a.ordernum = b.ordernum
    group by a.relateorder
)
insert into coss_dwd.dwd_cus_water_quality_accident_impact_stg_mini (
    ordernum,
    incident_cpt_no,
    water_quality_no,
    meter_clearance_no,
    dwd_load_time,
    dwd_update_time
)
select
    br.ordernum,
    br.incident_cpt_no,
    coalesce(ss.water_quality_no, 0) as water_quality_no,
    coalesce(cs.meter_clearance_no, 0) as meter_clearance_no,
    current_timestamp as dwd_load_time,
    current_timestamp as dwd_update_time
from base_relate br
left join sample_stat ss
    on br.ordernum = ss.relateorder
left join clean_stat cs
    on br.ordernum = cs.relateorder


-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Customer Service Accident Impact
-- Create         By:
-- Create       Date: 2026-06-30
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_dwd.dwd_cus_water_quality_accident_wo_mini
-- Source Table:  coss_ods.ods_pems_cus_meter_clean_number_di
-- Source Table:  coss_ods.ods_pems_cus_water_sample_number_di
-- Target Table:  coss_dwd.dwd_cus_water_quality_accident_impact_mini
-- ****************************************************************************************
insert into coss_dwd.dwd_cus_water_quality_accident_impact_mini (
    ordernum,
    incident_cpt_no,
    water_quality_no,
    meter_clearance_no,
    dwd_load_time,
    dwd_update_time
)
select
    ordernum,
    incident_cpt_no,
    water_quality_no,
    meter_clearance_no,
    dwd_load_time,
    dwd_update_time
from coss_dwd.dwd_cus_water_quality_accident_impact_stg_mini
on duplicate key update
    incident_cpt_no = values(incident_cpt_no),
    water_quality_no = values(water_quality_no),
    meter_clearance_no = values(meter_clearance_no),
    dwd_update_time = values(dwd_update_time);




with
-- 1. Water Quality Complains WO
t_work_a as (
    select
        ordernum,
        relateorder
    from coss_dwd.dwd_cus_water_quality_wo_details_mini
    where dwd_update_time >= '${dm_update_time}'
),
t_work_b as (
    select
        distinct coalesce(relateorder, ordernum) as relateorder,
        affect_building_code
    from coss_dwd.dwd_cus_water_quality_wo_details_mini t
    where exists (
        select 1 from t_work_a
        where t.ordernum = t_work_a.ordernum
           or (t.relateorder = t_work_a.relateorder and t_work_a.relateorder is not null)
    )
),
t_work_c as (
    select
        t.relateorder         as ordernum,
        count(t.affect_building_code) as affect_building_code,
        sum(t1.meter_num)     as affect_meter_no,
        sum(t1.population)    as affect_people_no
    from t_work_b t
    inner join coss_dws.dws_tmu_building_di t1
        on t.affect_building_code = t1.building_csu_id
    group by relateorder
)
insert into coss_dm.dm_cus_water_quality_accident_impact_stg_mini
(
    ordernum,
    affect_building_no,
    affect_meter_no,
    affect_people_no,
    incident_cpt_no,
    water_quality_no,
    meter_clearance_no,
    dm_load_time,
    dm_update_time
)
select
    ordernum,
    max(affect_building_code) as affect_building_no,
    max(affect_meter_no)      as affect_meter_no,
    max(affect_people_no)     as affect_people_no,
    max(incident_cpt_no)      as incident_cpt_no,
    max(water_quality_no)     as water_quality_no,
    max(meter_clearance_no)   as meter_clearance_no,
    current_timestamp         as dm_load_time,
    current_timestamp         as dm_update_time
from
(
    select
        ordernum,
        affect_building_code,
        affect_meter_no,
        affect_people_no,
        null as incident_cpt_no,
        null as water_quality_no,
        null as meter_clearance_no
    from t_work_c t

    union all

    select
        ordernum,
        null as affect_building_code,
        null as affect_meter_no,
        null as affect_people_no,
        incident_cpt_no,
        water_quality_no,
        meter_clearance_no
    from coss_dwd.dwd_cus_water_quality_accident_impact_mini
        where dwd_update_time >= '${dm_update_time}'
)
group by ordernum;







select * from  coss_ods.ods_pems_cus_t_order_workorder_mini_year;
select * from  coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year;
select * from  coss_dwd.dwd_cus_water_quality_wo_details_mini ;
select * from coss_dwd.dwd_cus_water_quality_accident_wo_mini ;
select * from coss_dwd.dwd_cus_water_quality_fa_details_mini;
select * from coss_dwd.dwd_cus_water_quality_accident_impact_mini ;
select * from coss_dm.dm_cus_water_quality_wo_details_mini;
select * from coss_dm.dm_cus_water_quality_impact_build_mini;
select * from coss_dm.dm_cus_water_quality_accident_impact_mini;













-- DROP TABLE coss_dim.dim_water_quality_accident_sz_installation_info_1;

CREATE TABLE coss_dim.dim_water_quality_accident_sz_installation_info_1 (
	ordernum varchar(200) NOT NULL, -- The Work Order Number
	supply_code varchar(100) NOT NULL, -- Supply Code
	supply_id varchar(100) NOT NULL, -- Supply ID
	dim_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading time
	dim_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update time
	CONSTRAINT dim_water_quality_accident_sz_installation_info_1_pkey PRIMARY KEY (ordernum, supply_code, supply_id)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dim.dim_water_quality_accident_sz_installation_info_1 IS 'Water Quality Accident Supply Zone Installation Information';

-- Column comments
COMMENT ON COLUMN coss_dim.dim_water_quality_accident_sz_installation_info_1.ordernum IS 'The Work Order Number';
COMMENT ON COLUMN coss_dim.dim_water_quality_accident_sz_installation_info_1.supply_code IS 'Supply Code';
COMMENT ON COLUMN coss_dim.dim_water_quality_accident_sz_installation_info_1.supply_id IS 'Supply ID';
COMMENT ON COLUMN coss_dim.dim_water_quality_accident_sz_installation_info_1.dim_load_time IS 'Data Loading time';
COMMENT ON COLUMN coss_dim.dim_water_quality_accident_sz_installation_info_1.dim_update_time IS 'Data Update time';






select distinct sr_id  from coss_dm.dm_srs_daily_sr_wl_qty_item_di
where 
sr_id not in(
select sr_id
from coss_dim.dim_sr_installation_info
where is_qty = 1)
and qty_del is not null 




DROP TABLE coss_dwd.dwd_tmu_meter_svc_dtl_di;

CREATE TABLE coss_dwd.dwd_tmu_meter_svc_dtl_di (
	meter_id bpchar(10) NULL, -- Meter ID
	meter_no bpchar(8) NULL, -- Meter number
	meter_type_code varchar(15) NULL, -- Meter type code
	meter_sts_ind bpchar(1) NULL, -- Meter status
	serial_no varchar(16) NULL, -- Serial number
	rcv_date timestamp(6) NULL, -- Received date
	retire_date timestamp(6) NULL, -- Retired date
	"comments" varchar(254) NULL, -- Remarks
	retire_rsn_code varchar(10) NULL, -- Retired reason code
	recond_date timestamp(6) NULL, -- Registered date
	created_date timestamp(6) NULL, -- Created time
	modified_date timestamp(6) NULL, -- Modified time
	premise_id bpchar(10) NULL, -- Foreign key, PREMISE
	hsic_code varchar(8) NULL, -- Industry classification HSIC code
	hsic_desc varchar(60) NULL, -- Classification Description
	hsic_desc_tc varchar(60) NULL, -- Classification Description (Traditional Chinese)
	desc_on_bill varchar(60) NULL, -- Description on Bill
	desc_on_bill_tc varchar(60) NULL, -- Description on Bill (Traditional Chinese)
	sic_bcode varchar(40) NULL, -- sic bcode
	mcategory_code varchar(40) NULL, -- mcategory code
	dwd_load_time timestamp(6) default current_timestamp, -- Data load time
	dwd_update_time timestamp(6) default current_timestamp,
	primary key(meter_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
);
COMMENT ON TABLE coss_dwd.dwd_tmu_meter_svc_dtl_di IS 'Meter info';

-- Column comments

COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.meter_id IS 'Meter ID';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.meter_no IS 'Meter number';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.meter_type_code IS 'Meter type code';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.meter_sts_ind IS 'Meter status';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.serial_no IS 'Serial number';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.rcv_date IS 'Received date';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.retire_date IS 'Retired date';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di."comments" IS 'Remarks';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.retire_rsn_code IS 'Retired reason code';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.recond_date IS 'Registered date';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.created_date IS 'Created time';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.modified_date IS 'Modified time';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.premise_id IS 'Foreign key, PREMISE';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.hsic_code IS 'Industry classification HSIC code';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.hsic_desc IS 'Classification Description';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.hsic_desc_tc IS 'Classification Description (Traditional Chinese)';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.desc_on_bill IS 'Description on Bill';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.desc_on_bill_tc IS 'Description on Bill (Traditional Chinese)';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.sic_bcode IS 'sic bcode';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.mcategory_code IS 'mcategory code';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.dwd_load_time IS 'Data load time';
COMMENT ON COLUMN coss_dwd.dwd_tmu_meter_svc_dtl_di.dwd_update_time IS 'Data Update time';






drop table if exists coss_dwd.dwd_tmu_premise_svc_dtl_di;

create table if not exists coss_dwd.dwd_tmu_premise_svc_dtl_di (
	premise_id bpchar(10) null,
	hsic_code varchar(8) null,
	hsic_desc varchar(60) null,
	hsic_desc_tc varchar(60) null,
	desc_on_bill varchar(60) null,
	desc_on_bill_tc varchar(60) null,
	dwd_load_time timestamp(6) default current_timestamp,
	dwd_update_time timestamp(6) default current_timestamp,
	primary key(premise_id)
)
with (
	orientation=row,
	compression=no,
	storage_type=USTORE,
	segment=off
);

-- table comment
comment on table coss_dwd.dwd_tmu_premise_svc_dtl_di is 'Premise Service Detail';

-- column comment
comment on column coss_dwd.dwd_tmu_premise_svc_dtl_di.premise_id is 'Premise Id';
comment on column coss_dwd.dwd_tmu_premise_svc_dtl_di.hsic_code is 'Hsic Code';
comment on column coss_dwd.dwd_tmu_premise_svc_dtl_di.hsic_desc is 'Hsic Description';
comment on column coss_dwd.dwd_tmu_premise_svc_dtl_di.hsic_desc_tc is 'Hsic Description Tc';
comment on column coss_dwd.dwd_tmu_premise_svc_dtl_di.desc_on_bill is 'Description On Bill';
comment on column coss_dwd.dwd_tmu_premise_svc_dtl_di.desc_on_bill_tc is 'Description On Bill Tc';
comment on column coss_dwd.dwd_tmu_premise_svc_dtl_di.dwd_load_time is 'Dwd Load Time';
comment on column coss_dwd.dwd_tmu_premise_svc_dtl_di.dwd_update_time is 'Dwd Update Time';





with t_a as (
    select
        premise_id,
        hsic_code,
        start_date
    from (
        select
            premise_id,
            hsic_code,
            start_date,
            row_number() over(partition by premise_id order by start_date desc) as rk
        from coss_ods.ods_abpms_tmu_svc_dtl_di
        where
          ods_update_time >= '${dwd_update_time}'
          and hsic_code is not null
          and premise_id is not null
    ) sub
    where rk = 1
),
t_b as (
    select
        t.hsic_code,
        t.hsic_desc,
        t.hsic_desc_tc,
        t.desc_on_bill,
        t.desc_on_bill_tc,
        t1.sic_bcode,
        t1.mcategory_code
    from (
        select
            hsic_code,
            hsic_desc,
            hsic_desc_tc,
            desc_on_bill,
            desc_on_bill_tc
        from coss_ods.ods_abpms_tmu_cfg_hsic_df
    ) t
    inner join (
        select
            sic_bcode,
            sic_ecode,
            mcategory_code
        from coss_ods.ods_inms_gdhk_dim_sic_mcategory_df
    ) t1
        on t.hsic_code = t1.sic_bcode
)
insert into coss_dwd.dwd_tmu_premise_svc_dtl_stg_di (
    premise_id,
    hsic_code,
    hsic_desc,
    hsic_desc_tc,
    desc_on_bill,
    desc_on_bill_tc,
    dwd_load_time,
    dwd_update_time
)
select
    t.premise_id,
    t.hsic_code,
    t1.hsic_desc,
    t1.hsic_desc_tc,
    t1.desc_on_bill,
    t1.desc_on_bill_tc,
    current_timestamp as dwd_load_time,
    current_timestamp as dwd_update_time
from t_a t
inner join t_b t1
    on t.hsic_code = t1.hsic_code;


-- ****************************************************************************************
-- subject     areas: TMU
-- function describe: Premise Service Detail Information
-- create         by:
-- create       date: 2026-08-09
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_ods.ods_inms_gdhk_dim_sic_mcategory_df
-- coss_ods.ods_abpms_tmu_cfg_hsic_df
-- coss_ods.ods_abpms_tmu_svc_dtl_di
-- target table
-- coss_dwd.dwd_tmu_premise_svc_dtl_di
-- ****************************************************************************************
insert into coss_dwd.dwd_tmu_premise_svc_dtl_di
select
    premise_id,
    hsic_code,
    hsic_desc,
    hsic_desc_tc,
    desc_on_bill,
    desc_on_bill_tc,
    current_timestamp dwd_load_time,
    current_timestamp dwd_update_time
from coss_dwd.dwd_tmu_premise_svc_dtl_stg_di
on duplicate key update
    hsic_code = values(hsic_code),
    hsic_desc = values(hsic_desc),
    hsic_desc_tc = values(hsic_desc_tc),
    desc_on_bill = values(desc_on_bill),
    desc_on_bill_tc = values(desc_on_bill_tc),
    dwd_update_time = values(dwd_update_time)






create table if not exists coss_dm.dm_tmu_annual_user_customer_item_stg_di (
    statistical_year varchar(50) not null, -- Statistical Year
    region_abbr varchar(120) not null, -- Regional Abbreviation
    inter_item_code varchar(120) not null, -- Index Code
    type_code varchar(120) not null, -- Type Code
    item_value numeric(20, 6) null, -- Index Value
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Dm Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Dm Load Time
    primary key (statistical_year, region_abbr, inter_item_code, type_code)
);

with t_a as (
    select
        meter_no,
        region_abbr,
        case
            when amr = 'Y' then 'ME_TY_000002'
            else 'ME_TY_000001'
        end as type_code
    from coss_dwd.dwd_ass_user_meter_di
    where meter_status = 'Active'
      and region_abbr is not null
)
insert into coss_dm.dm_tmu_annual_user_customer_item_stg_di
select
	statistical_year,
	region_abbr,
	inter_item_code,
	type_code,
	item_value,
	dm_update_time,
	dm_load_time
from
(
select
    to_char(current_timestamp, 'YYYY') as statistical_year,
    region_abbr,
    'US_CM_000001' as inter_item_code,
    type_code,
    count(distinct meter_no) as item_value,
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from t_a
group by
    region_abbr,
    type_code

union all

select
    to_char(current_timestamp, 'YYYY') as statistical_year,
    'HKSAR' as region_abbr,
    'US_CM_000001' as inter_item_code,
    type_code,
    count(distinct meter_no) as item_value,
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from t_a
group by
    type_code
)



-- ****************************************************************************************
-- subject     areas: TMU
-- function describe: User Customer Item
-- create         by:
-- create       date: 2026-08-09
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dwd_ass_user_meter_di
-- target table
-- coss_dm.dm_tmu_annual_user_customer_item_di
-- ****************************************************************************************
insert into coss_dm.dm_tmu_annual_user_customer_item_di (
    statistical_year,
    region_abbr,
    inter_item_code,
    type_code,
    item_value,
    dm_update_time,
    dm_load_time
)
select
    statistical_year,
    region_abbr,
    inter_item_code,
    type_code,
    item_value,
    dm_update_time,
    dm_load_time
from coss_dm.dm_tmu_annual_user_customer_item_stg_di
on duplicate key update
    item_value = values(item_value),
    dm_update_time = values(dm_update_time);















































delete from coss_dim.dim_ass_wtw_info
where i_code not in (
select distinct i_code from coss_dim.dim_wtw_tag_info dwti 
)

-- coss_dm.dm_tmu_annual_user_customer_item_di definition

-- Drop table

-- DROP TABLE coss_dm.dm_tmu_annual_user_customer_item_di;

CREATE TABLE coss_dm.dm_tmu_annual_user_customer_item_di (
	statistical_year varchar(50) NOT NULL, -- Statistical Year
	region_abbr varchar(120) NOT NULL, -- Regional Abbreviation
	inter_item_code varchar(120) NOT NULL, -- Index Code
	type_code varchar(120) NOT NULL, -- Type Code
	item_value numeric(20, 6) NULL, -- Index Value
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Dm Load Time
	CONSTRAINT dm_tmu_user_customer_item_di_pkey PRIMARY KEY (statistical_year, region_abbr, inter_item_code, type_code)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_tmu_annual_user_customer_item_di IS 'User Customer Item Table';

-- Column comments

COMMENT ON COLUMN coss_dm.dm_tmu_annual_user_customer_item_di.statistical_year IS 'Statistical Year';
COMMENT ON COLUMN coss_dm.dm_tmu_annual_user_customer_item_di.region_abbr IS 'Regional Abbreviation';
COMMENT ON COLUMN coss_dm.dm_tmu_annual_user_customer_item_di.inter_item_code IS 'Index Code';
COMMENT ON COLUMN coss_dm.dm_tmu_annual_user_customer_item_di.type_code IS 'Type Code';
COMMENT ON COLUMN coss_dm.dm_tmu_annual_user_customer_item_di.item_value IS 'Index Value';
COMMENT ON COLUMN coss_dm.dm_tmu_annual_user_customer_item_di.dm_update_time IS 'Dm Update Time';
COMMENT ON COLUMN coss_dm.dm_tmu_annual_user_customer_item_di.dm_load_time IS 'Dm Load Time';







10.66.168.220:8080/webroot/decision/login?

fanruan/Fr123




create table coss_tmp.dm_srs_daily_sr_wl_qty_item_di_arch260723 as 
select * from coss_dm.dm_srs_daily_sr_wl_qty_item_di 
where 
rec_dt >= '2025-12-13 00:00:00.000'
order by rec_dt asc 

delete  from coss_dm.dm_srs_daily_sr_wl_qty_item_di 
where 
rec_dt >= '2025-12-13 00:00:00.000'



		
		
		
		
		select
            asset_id,
            total_kwh/pump_qty as kwh_ml,
            mh
        from coss_dws.dws_psr_eng_cons_billing_details_di_year
        where pump_qty != 0
            and pump_qty is not null
            and mh >= ${mh1}
            
            
            
            
        select
            asset_id,
            sum(total_kwh)/sum(pump_qty) as kwh_ml,
            mh
        from coss_dws.dws_psr_eng_cons_billing_details_di_year
        where pump_qty != 0
            and pump_qty is not null
            and mh >= ${mh1}    
        group by
          asset_id,
          mh
            




核对其计算逻辑：
select *  from coss_dws.dws_psr_eng_cons_billing_details_di_year  
where asset_id = 71 and mh = 201503
71	201503
 
 
 
 
 https://10.66.168.83/COSS/login


drop table if exists coss_dm.dm_tmu_user_customer_item_di;

create table if not exists coss_dm.dm_tmu_user_customer_item_di (
    statistical_year  varchar(50),
    inter_item_code   varchar(120),
    hsic_code         varchar(120),
    item_value        numeric(20,6),
    dm_update_time    timestamp(6) null default current_timestamp,
    dm_load_time      timestamp(6) null default current_timestamp,
    primary key (statistical_year, inter_item_code, hsic_code)
);

comment on table coss_dm.dm_tmu_user_customer_item_di is 'User Customer Item Table';
comment on column coss_dm.dm_tmu_user_customer_item_di.statistical_year  is 'Statistical Year';
comment on column coss_dm.dm_tmu_user_customer_item_di.inter_item_code   is 'Index Code';
comment on column coss_dm.dm_tmu_user_customer_item_di.hsic_code         is 'Industry Classification Code';
comment on column coss_dm.dm_tmu_user_customer_item_di.item_value        is 'Index Value';
comment on column coss_dm.dm_tmu_user_customer_item_di.dm_update_time    is 'Dm Update Time';
comment on column coss_dm.dm_tmu_user_customer_item_di.dm_load_time      is 'Dm Load Time';




数仓建设文档：
https://docs.qq.com/sheet/DUGdOTE9rdnJwb2xI?no_promotion=1&tab=BB08J2

https://docs.qq.com/sheet/DUHdhaEZXRE1pZW1x?no_promotion=1&is_blank_or_template=blank&tab=BB08J2



t_order_workorder	ordernum
	bigregion
	classify2
	urgency
	orderstate
	channeltype
	isrepeatedcomplaint
t_order_workorder_entity	waterqualitycode
	street
	estate
	term
	village
	buildingno
	floor
	relateorder
	servicecontent
	locationx
	locationy
	regionreceivingdate
	createdat
	finishtime




-- coss_dcs.opc_data_tseungkwuno definition

-- Drop table

-- DROP TABLE coss_dcs.opc_data_tseungkwuno;

CREATE TABLE coss_dcs.opc_data_tseungkwuno (
	id bigserial NOT NULL,
	tag_name varchar(128) NULL,
	tag_value varchar(128) NULL,
	tag_value_avg numeric NULL,
	tag_value_min numeric NULL,
	tag_value_max numeric NULL,
	quality int4 NOT NULL,
	tag_time timestamp NOT NULL,
	ms_sql_time timestamp NOT NULL DEFAULT pg_systimestamp(),
	CONSTRAINT opc_data_tseungkwuno_unique UNIQUE (tag_name)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
);

-- Permissions

GRANT SELECT ON TABLE coss_dcs.opc_data_tseungkwuno TO coss;
GRANT ALL ON TABLE coss_dcs.opc_data_tseungkwuno TO coss_dcs_wtw;
GRANT SELECT ON TABLE coss_dcs.opc_data_tseungkwuno TO wqms_admin;






https://docs.qq.com/sheet/DUGdOTE9rdnJwb2xI?no_promotion=1&tab=fl8tx0



# 数开-IOT数据对接

## 数据清洗过程

1. 18个水质监测点的数据查询sql

   ```sql
    select * from iot.device where  "type" ='gw111'
   ```

2. 查询水质监测点的sensor数据，gps_position是经纬度，需要转换为HK80,对应数据表的表解构：dim_sz_device_info

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

3. 查询需要获取三个监测数据的sensor数据，获取相关的sensor_code值

   ```sql
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
   	and name in ('WSD Kowloon Bay Building (PI)',
   	'Fan Kam Road Kiosk (PI)',
   	'Tsuen Wan Park (S::can)')
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
   ```

4. 查询三个指定点位的sensor数据

   ```sql
   insert into coss_dm.dm_tmu_sensor_data_mini_month 
   select 
   	id,
   	code sensor_code,
   	value sensor_value,
   	to_timestamp(time / 1000) sensor_time,
   	current_timestamp dm_update_time,
   	current_timestamp dm_load_time
   from data_gw
   where 
   code in ('FWWMNW04001Q00101',
   'FWWMNW04001Q00105',
   'FWBDKN05002Q00101',
   'FWBDKN05002Q00103',
   'FWBDKN05002Q00104',
   'FWBDKN05002Q00105',
   'FWWMNW03001Q00101',
   'FWWMNW03001Q00103',
   'FWWMNW03001Q00102',
   'FWWMNW03001Q00105',
   'FWBDKN05002Q00102',
   'FWWMNW03001Q00104',
   'FWWMNW04001Q00103',
   'FWWMNW04001Q00104',
   'FWWMNW04001Q00102')
   and 
   to_timestamp(time / 1000) >= '2026-04-01 18:52:00.000 +0800'
   
   ```

   


1. 水质dev接口： http://10.66.169.58:8001/iot3/rest/api/v1/realtime.json
2. 与生产水位接口：http://10.66.110.106:8325
3. ISIT远传表接口：http://10.66.169.102:8330/share/data/sensor/moreDevRealtime

iuat dp
http://10.66.168.41:12345/dolphinscheduler/ui/login
iuat gaussdb
jdbc:postgresql://192.168.136.64:8000,192.168.136.61:8000,192.168.136.52:8000,192.168.136.206:8000/wsd?loadBalanceHosts=true&refreshCNIpListTime=3
coss/WsdUat@MS30F


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





<img width="158" height="23" alt="image" src="https://github.com/user-attachments/assets/489e8a17-49ce-4daa-838e-859e2c5e44bb" />

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
