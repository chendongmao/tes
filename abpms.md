



<center><h1>ABPMS System</h1></center>

> code version: Still missing the DM level
>
> job flow: The most authoritative code is DMZ
>
> note: The DP's ods_load_time filed is mistake

| ENV  | Depoly | Running |
| ---- | ------ | ------- |
| DEV  | YES    | YES     |
| DMZ  | YES    | YES     |
| SIT  | NO     | NO      |
| UAT  | NO     | NO      |

```tex
****************************************************************************************
1.IUAT 环境更新了 ods_abpms_tmu_premise_df 表结构
2.配置了ods_abpms_tmu_premise_df和ods_abpms_tmu_svc_dtl_df 两张表的增量数据同步
****************************************************************************************
```



# ods

## 1.ods_abpms_tmu_cfg_hsic_df

```sql

drop table if exists coss_ods.ods_abpms_tmu_cfg_hsic_df;
create table if not exists coss_ods.ods_abpms_tmu_cfg_hsic_df (
    hsic_code varchar(8) null,                    -- Industry Classification Code
    hsic_desc varchar(60) null,                   -- Classification Description
    hsic_desc_tc varchar(60) null,                -- Classification Description (Traditional Chinese)
    hsic_desc_sc varchar(60) null,                -- Classification Description (Simplified Chinese)
    obs_sw bpchar(1) null,                        -- Cancel Switch (Y/N)
    created_by varchar(8) null,                   -- Creator
    created_date timestamp(6) null,               -- Creation Time
    modified_by varchar(8) null,                  -- Modifier
    modified_date timestamp(0) null,              -- Modification Time
    "timestamp" timestamp(6) null,                -- Timestamp
    hsic_cat_code varchar(8) null,                -- HK Standard Industrial Classification Category Code
    domestic_debt_recovery_sw bpchar(1) null,     -- Debt Recovery Switch
    desc_on_bill varchar(60) null,                -- Description on Bill
    desc_on_bill_tc varchar(60) null,             -- Description on Bill (Traditional Chinese)
    desc_on_bill_sc varchar(60) null,             -- Description on Bill (Simplified Chinese)
    ods_load_time timestamp(6),                   -- Data Loading Time
    ods_update_time timestamp(6),                 -- Data Update Time
    primary key(hsic_code)
)
with (
    orientation=row,
    compression=no
);
comment on table  coss_ods.ods_abpms_tmu_cfg_hsic_df                             is 'Industry classification code configuration table';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.hsic_code                   is 'Industry Classification Code';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.hsic_desc                   is 'Classification Description';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.hsic_desc_tc                is 'Classification Description (Traditional Chinese)';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.hsic_desc_sc                is 'Classification Description (Simplified Chinese)';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.obs_sw                      is 'Cancel Switch (Y/N)';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.created_by                  is 'Creator';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.created_date                is 'Creation Time';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.modified_by                 is 'Modifier';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.modified_date               is 'Modification Time';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.timestamp                   is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.hsic_cat_code               is 'HK Standard Industrial Classification Category Code';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.domestic_debt_recovery_sw   is 'Debt Recovery Switch';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.desc_on_bill                is 'Description on Bill';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.desc_on_bill_tc             is 'Description on Bill (Traditional Chinese)';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.desc_on_bill_sc             is 'Description on Bill (Simplified Chinese)';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.ods_load_time               is 'Data Loading Time';
comment on column coss_ods.ods_abpms_tmu_cfg_hsic_df.ods_update_time             is 'Data Update Time';

```

```sql
-- ****************************************************************************************
-- Subject     Areas: ABPMS
-- Function Describe: Industry classification code configuration table
-- Create         By: dongmaochen
-- Create       Date: 2025-08-09
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- abpms.cfg_hsic
-- Target Table
-- coss_ods.ods_abpms_tmu_cfg_hsic_df
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_cfg_hsic_df
select
    hsic_code,                         -- Industry Classification Code
    hsic_desc,                        -- Classification Description
    hsic_desc_tc,                     -- Classification Description (Traditional Chinese)
    hsic_desc_sc,                     -- Classification Description (Simplified Chinese)
    obs_sw,                           -- Cancel Switch (Y/N)
    created_by,                       -- Creator
    created_date,                     -- Creation Time
    modified_by,                      -- Modifier
    modified_date,                    -- Modification Time
    timestamp,                        -- Timestamp
    hsic_cat_code,                    -- HK Standard Industrial Classification Category Code
    domestic_debt_recovery_sw,        -- Debt Recovery Switch
    desc_on_bill,                     -- Description on Bill
    desc_on_bill_tc,                  -- Description on Bill (Traditional Chinese)
    desc_on_bill_sc,                  -- Description on Bill (Simplified Chinese)
    current_timestamp ods_load_time,  -- Data load time
    current_timestamp ods_update_time -- Data Update time
from abpms.cfg_hsic;
```



## 2.ods_abpms_tmu_meter_df

```sql

drop table if exists coss_ods.ods_abpms_tmu_meter_df;
create table if not exists coss_ods.ods_abpms_tmu_meter_df (
    meter_id bpchar(10) null,              -- Meter ID
    meter_no bpchar(8) null,               -- Meter number
    meter_type_code varchar(15) null,      -- Meter type code
    meter_sts_ind bpchar(1) null,          -- Meter status
    serial_no varchar(16) null,            -- Serial number
    rcv_date timestamp(6) null,            -- Received date
    retire_date timestamp(6) null,         -- Retired date
    "comments" varchar(254) null,          -- Remarks
    retire_rsn_code varchar(10) null,      -- Retired reason code
    recond_date timestamp(6) null,         -- Registered date
    created_by varchar(8) null,            -- Created by
    created_date timestamp(6) null,        -- Created time
    modified_by varchar(8) null,           -- Modified by
    modified_date timestamp(6) null,       -- Modified time
    "timestamp" timestamp(6) null,         -- Timestamp
    ods_load_time timestamp(6),            -- Data Loading Time
    ods_update_time timestamp(6),          -- Data Update Time
    primary key(meter_id)
)
with (
    orientation=row,
    compression=no
);

comment on table coss_ods.ods_abpms_tmu_meter_df                       is 'Water meter main meter';
comment on column coss_ods.ods_abpms_tmu_meter_df.meter_id              is 'Meter ID';
comment on column coss_ods.ods_abpms_tmu_meter_df.meter_no              is 'Meter number';
comment on column coss_ods.ods_abpms_tmu_meter_df.meter_type_code       is 'Meter type code';
comment on column coss_ods.ods_abpms_tmu_meter_df.meter_sts_ind         is 'Meter status';
comment on column coss_ods.ods_abpms_tmu_meter_df.serial_no             is 'Serial number';
comment on column coss_ods.ods_abpms_tmu_meter_df.rcv_date              is 'Received date';
comment on column coss_ods.ods_abpms_tmu_meter_df.retire_date           is 'Retired date';
comment on column coss_ods.ods_abpms_tmu_meter_df.comments              is 'Remarks';
comment on column coss_ods.ods_abpms_tmu_meter_df.retire_rsn_code       is 'Retired reason code';
comment on column coss_ods.ods_abpms_tmu_meter_df.recond_date           is 'Registered date';
comment on column coss_ods.ods_abpms_tmu_meter_df.created_by            is 'Created by';
comment on column coss_ods.ods_abpms_tmu_meter_df.created_date          is 'Created time';
comment on column coss_ods.ods_abpms_tmu_meter_df.modified_by           is 'Modified by';
comment on column coss_ods.ods_abpms_tmu_meter_df.modified_date         is 'Modified time';
comment on column coss_ods.ods_abpms_tmu_meter_df.timestamp             is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_meter_df.ods_load_time         is 'Data loaded time';


```

```sql
-- ****************************************************************************************
-- subject     areas: ABPMS
-- function describe: Water meter main meter
-- create         by: dongmaochen
-- create       date: 2025-08-09
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- abpms.meter
-- target table
-- coss_ods.ods_abpms_tmu_meter_df
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_meter_df
select
    meter_id,                          -- Meter ID
    meter_no,                          -- Meter number
    meter_type_code,                   -- Meter type code
    meter_sts_ind,                     -- Meter status
    serial_no,                         -- Serial number
    rcv_date,                          -- Received date
    retire_date,                       -- Retired date
    comments,                          -- Remarks
    retire_rsn_code,                   -- Retired reason code
    recond_date,                       -- Registered date
    created_by,                        -- Created by
    created_date,                      -- Created time
    modified_by,                       -- Modified by
    modified_date,                     -- Modified time
    "timestamp",                       -- Timestamp
    current_timestamp ods_load_time,   -- Data load time
    current_timestamp ods_update_time  -- Data Update time
from abpms.meter;
```



## 3.ods_abpms_tmu_premise_df

```sql

drop table if exists coss_ods.ods_abpms_tmu_premise_df;
create table if not exists coss_ods.ods_abpms_tmu_premise_df (
    premise_id varchar(255) null,                           -- 'Property ID'
    premise_type_code varchar(255) null,                    -- 'Address Type'
    housing_id varchar(255) null,                           -- 'Property ID'
    ess_inst_sw varchar(255) null,                          -- 'Is a water meter required? (Essential)'
    ess_inst_desc varchar(255) null,                        -- 'ESS Installation Instructions'
    meter_read_warn_code varchar(255) null,                 -- 'Meter Reading Notes'
    meter_read_instr_dtl varchar(255) null,                 -- 'Meter Reading Details'
    mail_addr_sw varchar(255) null,                         -- 'Is the address mailable?'
    obs_sw varchar(200) null,                               -- 'Abandoned Switch'
    demolished_sw varchar(200) null,                        -- 'Removed Flag (used for bulk uploads, other information not related to business logic)'
    restricted_sw varchar(200) null,                        -- 'Restricted Flag (used for bulk uploads, other information not related to business logic)'
    addr_line1 varchar(255) null,                           -- 'Address Line 1'
    addr_line2 varchar(255) null,                           -- 'Address Line 2'
    addr_line3 varchar(255) null,                           -- 'Address Line 3'
    addr_line4 varchar(255) null,                           -- 'Address Line 4'
    region_code varchar(200) null,                           -- 'Administrative Region (Hong Kong, Kowloon, New Territories)'
    district_code varchar(200) null,                         -- 'Jurisdiction under an Administrative Region'
    sub_district_code varchar(200) null,                     -- 'Name of a specific area under a Jurisdiction'
    street_no varchar(200) null,                             -- 'Street Number'
    start_street_no varchar(200) null,                       -- 'Start Street Number'
    end_street_no varchar(200) null,                         -- 'End Street Number'
    street_no_add1 varchar(255) null,                       -- 'Multiple street numbers can be entered'
    street_no_add2 varchar(255) null,                       -- 'Multiple street numbers can be entered'
    street_no_add3 varchar(255) null,                       -- 'Multiple street numbers can be entered'
    street_name varchar(255) null,                          -- 'Street Name'
    street_name_add1 varchar(255) null,                     -- 'Multiple street names can be entered'
    street_name_add2 varchar(255) null,                     -- 'Multiple street names can be entered'
    street_name_add3 varchar(255) null,                     -- 'Multiple street names can be entered'
    estate_name varchar(255) null,                          -- 'Estate/Village'
    phase_name varchar(255) null,                           -- 'Phase (many developments are phased)'
    village_place_no varchar(200) null,                      -- 'Village Number'
    village_place_name varchar(255) null,                   -- 'Village Place Name'
    block_house_type varchar(200) null,                      -- 'Block Number Type'
    block_house_no varchar(200) null,                        -- 'Block Number'
    building_name varchar(255) null,                        -- 'Building Name'
    floor_type varchar(200) null,                            -- 'Store Type'
    floor_no varchar(200) null,                              -- 'Store Number'
    flat_unit_no varchar(400) null,                          -- 'Apartment Unit Number'
    flat_unit_type varchar(200) null,                        -- 'Apartment Unit Type'
    dd_no varchar(200) null,                                 -- 'Measurement Reduction (Interface Limiting Boundary)'
    lot_no varchar(128) null,                               -- 'Lot Number'
    incident_desc varchar(255) null,                        -- 'Location and Project Event Description'
    contract_no varchar(200) null,                           -- 'Contract Number'
    shortform_building varchar(200) null,                    -- 'Building Abbreviation'
    shortform_estate varchar(200) null,                      -- 'Land Abbreviation'
    created_by varchar(200) null,                            -- 'Created by'
    created_date timestamp(6) null,                         -- 'Created Time'
    modified_by varchar(200) null,                           -- 'Modified by'
    modified_date timestamp(6) null,                        -- 'Modified Time'
    "timestamp" timestamp(6) null,                          -- 'Timestamp'
    street_name_no_sw varchar(200) null,                     -- 'Street Name Number Entry Switch'
    block_house_no_sw varchar(200) null,                     -- 'Block Number Entry Switch'
    floor_no_sw varchar(200) null,                           -- 'Store Number Entry Switch'
    dd_lot_no_sw varchar(200) null,                          -- 'DD Lot Number Entry Switch'
    contract_no_sw varchar(200) null,                        -- 'Contract Number Entry Switch'
    incident_desc_sw varchar(200) null,                      -- 'Event Description Entry Switch'
    estate_sw varchar(200) null,                             -- 'Estate/Village Entry Switch'
    phase_sw varchar(200) null,                              -- 'Phase Number Entry Switch'
    village_place_sw varchar(200) null,                      -- 'Village Address Entry Switch'
    building_sw varchar(200) null,                           -- 'Building Name Entry Switch'
    flat_unit_no_sw varchar(200) null,                       -- 'Store Number Entry Switch'
    user_formatted_sw varchar(200) null,                     -- 'User-Formatted Entry Switch'
    full_addr varchar(256) null,                            -- 'Full Address'
    parent_premise_id varchar(255) null,                    -- 'Parent Premises ID'
    portable_meter_construction_site varchar(2) null,       -- 'Portable Meter/Construction Site'
    ods_load_time timestamp(6),                   -- Data Loading Time
    ods_update_time timestamp(6),                 -- Data Update Time
    primary key(premise_id)
)
with (
    orientation=row,
    compression=no
);
comment on table  coss_ods.ods_abpms_tmu_premise_df                                         is 'Address master table, records the main address information';
comment on column coss_ods.ods_abpms_tmu_premise_df.premise_id                              is 'Property ID';
comment on column coss_ods.ods_abpms_tmu_premise_df.premise_type_code                       is 'Address Type';
comment on column coss_ods.ods_abpms_tmu_premise_df.housing_id                              is 'Property ID';
comment on column coss_ods.ods_abpms_tmu_premise_df.ess_inst_sw                             is 'Is a water meter required? (Essential)';
comment on column coss_ods.ods_abpms_tmu_premise_df.ess_inst_desc                           is 'ESS Installation Instructions';
comment on column coss_ods.ods_abpms_tmu_premise_df.meter_read_warn_code                    is 'Meter Reading Notes';
comment on column coss_ods.ods_abpms_tmu_premise_df.meter_read_instr_dtl                    is 'Meter Reading Details';
comment on column coss_ods.ods_abpms_tmu_premise_df.mail_addr_sw                            is 'Is the address mailable?';
comment on column coss_ods.ods_abpms_tmu_premise_df.obs_sw                                  is 'Abandoned Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.demolished_sw                           is 'Removed Flag (used for bulk uploads, other information not related to business logic)';
comment on column coss_ods.ods_abpms_tmu_premise_df.restricted_sw                           is 'Restricted Flag (used for bulk uploads, other information not related to business logic)';
comment on column coss_ods.ods_abpms_tmu_premise_df.addr_line1                              is 'Address Line 1';
comment on column coss_ods.ods_abpms_tmu_premise_df.addr_line2                              is 'Address Line 2';
comment on column coss_ods.ods_abpms_tmu_premise_df.addr_line3                              is 'Address Line 3';
comment on column coss_ods.ods_abpms_tmu_premise_df.addr_line4                              is 'Address Line 4';
comment on column coss_ods.ods_abpms_tmu_premise_df.region_code                             is 'Administrative Region (Hong Kong, Kowloon, New Territories)';
comment on column coss_ods.ods_abpms_tmu_premise_df.district_code                           is 'Jurisdiction under an Administrative Region';
comment on column coss_ods.ods_abpms_tmu_premise_df.sub_district_code                       is 'Name of a specific area under a Jurisdiction';
comment on column coss_ods.ods_abpms_tmu_premise_df.street_no                               is 'Street Number';
comment on column coss_ods.ods_abpms_tmu_premise_df.start_street_no                         is 'Start Street Number';
comment on column coss_ods.ods_abpms_tmu_premise_df.end_street_no                           is 'End Street Number';
comment on column coss_ods.ods_abpms_tmu_premise_df.street_no_add1                          is 'Multiple street numbers can be entered';
comment on column coss_ods.ods_abpms_tmu_premise_df.street_no_add2                          is 'Multiple street numbers can be entered';
comment on column coss_ods.ods_abpms_tmu_premise_df.street_no_add3                          is 'Multiple street numbers can be entered';
comment on column coss_ods.ods_abpms_tmu_premise_df.street_name                             is 'Street Name';
comment on column coss_ods.ods_abpms_tmu_premise_df.street_name_add1                        is 'Multiple street names can be entered';
comment on column coss_ods.ods_abpms_tmu_premise_df.street_name_add2                        is 'Multiple street names can be entered';
comment on column coss_ods.ods_abpms_tmu_premise_df.street_name_add3                        is 'Multiple street names can be entered';
comment on column coss_ods.ods_abpms_tmu_premise_df.estate_name                             is 'Estate/Village';
comment on column coss_ods.ods_abpms_tmu_premise_df.phase_name                              is 'Phase (many developments are phased)';
comment on column coss_ods.ods_abpms_tmu_premise_df.village_place_no                        is 'Village Number';
comment on column coss_ods.ods_abpms_tmu_premise_df.village_place_name                      is 'Village Place Name';
comment on column coss_ods.ods_abpms_tmu_premise_df.block_house_type                        is 'Block Number Type';
comment on column coss_ods.ods_abpms_tmu_premise_df.block_house_no                          is 'Block Number';
comment on column coss_ods.ods_abpms_tmu_premise_df.building_name                           is 'Building Name';
comment on column coss_ods.ods_abpms_tmu_premise_df.floor_type                              is 'Store Type';
comment on column coss_ods.ods_abpms_tmu_premise_df.floor_no                                is 'Store Number';
comment on column coss_ods.ods_abpms_tmu_premise_df.flat_unit_no                            is 'Apartment Unit Number';
comment on column coss_ods.ods_abpms_tmu_premise_df.flat_unit_type                          is 'Apartment Unit Type';
comment on column coss_ods.ods_abpms_tmu_premise_df.dd_no                                   is 'Measurement Reduction (Interface Limiting Boundary)';
comment on column coss_ods.ods_abpms_tmu_premise_df.lot_no                                  is 'Lot Number';
comment on column coss_ods.ods_abpms_tmu_premise_df.incident_desc                           is 'Location and Project Event Description';
comment on column coss_ods.ods_abpms_tmu_premise_df.contract_no                             is 'Contract Number';
comment on column coss_ods.ods_abpms_tmu_premise_df.shortform_building                      is 'Building Abbreviation';
comment on column coss_ods.ods_abpms_tmu_premise_df.shortform_estate                        is 'Land Abbreviation';
comment on column coss_ods.ods_abpms_tmu_premise_df.created_by                              is 'Created by';
comment on column coss_ods.ods_abpms_tmu_premise_df.created_date                            is 'Created Time';
comment on column coss_ods.ods_abpms_tmu_premise_df.modified_by                             is 'Modified by';
comment on column coss_ods.ods_abpms_tmu_premise_df.modified_date                           is 'Modified Time';
comment on column coss_ods.ods_abpms_tmu_premise_df.timestamp                               is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_premise_df.street_name_no_sw                       is 'Street Name Number Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.block_house_no_sw                       is 'Block Number Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.floor_no_sw                             is 'Store Number Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.dd_lot_no_sw                            is 'DD Lot Number Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.contract_no_sw                          is 'Contract Number Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.incident_desc_sw                        is 'Event Description Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.estate_sw                               is 'Estate/Village Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.phase_sw                                is 'Phase Number Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.village_place_sw                        is 'Village Address Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.building_sw                             is 'Building Name Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.flat_unit_no_sw                         is 'Store Number Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.user_formatted_sw                       is 'User-Formatted Entry Switch';
comment on column coss_ods.ods_abpms_tmu_premise_df.full_addr                               is 'Full Address';
comment on column coss_ods.ods_abpms_tmu_premise_df.parent_premise_id                       is 'Parent Premises ID';
comment on column coss_ods.ods_abpms_tmu_premise_df.portable_meter_construction_site        is 'Portable Meter/Construction Site';
comment on column coss_ods.ods_abpms_tmu_premise_df.ods_load_time                           is 'Data Loading Time';
comment on column coss_ods.ods_abpms_tmu_premise_df.ods_update_time                         is 'Data Update Time';

```



```sql
-- ****************************************************************************************
-- Subject     Areas: ABPMS
-- Function Describe: Address master table, records the main address information
-- Create         By: dongmaochen
-- Create       Date: 2025-08-09
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- abpms.premise
-- Target Table
-- coss_ods.ods_abpms_tmu_premise_df
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_premise_df
select
    premise_id,                               -- 'Property ID'
    premise_type_code,                       -- 'Address Type'
    housing_id,                              -- 'Property ID'
    ess_inst_sw,                             -- 'Is a water meter required? (Essential)'
    ess_inst_desc,                           -- 'ESS Installation Instructions'
    meter_read_warn_code,                    -- 'Meter Reading Notes'
    meter_read_instr_dtl,                    -- 'Meter Reading Details'
    mail_addr_sw,                            -- 'Is the address mailable?'
    obs_sw,                                  -- 'Abandoned Switch'
    demolished_sw,                           -- 'Removed Flag (used for bulk uploads, other information not related to business logic)'
    restricted_sw,                           -- 'Restricted Flag (used for bulk uploads, other information not related to business logic)'
    addr_line1,                              -- 'Address Line 1'
    addr_line2,                              -- 'Address Line 2'
    addr_line3,                              -- 'Address Line 3'
    addr_line4,                              -- 'Address Line 4'
    region_code,                             -- 'Administrative Region (Hong Kong, Kowloon, New Territories)'
    district_code,                           -- 'Jurisdiction under an Administrative Region'
    sub_district_code,                       -- 'Name of a specific area under a Jurisdiction'
    street_no,                               -- 'Street Number'
    start_street_no,                         -- 'Start Street Number'
    end_street_no,                           -- 'End Street Number'
    street_no_add1,                          -- 'Multiple street numbers can be entered'
    street_no_add2,                          -- 'Multiple street numbers can be entered'
    street_no_add3,                          -- 'Multiple street numbers can be entered'
    street_name,                             -- 'Street Name'
    street_name_add1,                        -- 'Multiple street names can be entered'
    street_name_add2,                        -- 'Multiple street names can be entered'
    street_name_add3,                        -- 'Multiple street names can be entered'
    estate_name,                             -- 'Estate/Village'
    phase_name,                              -- 'Phase (many developments are phased)'
    village_place_no,                        -- 'Village Number'
    village_place_name,                      -- 'Village Place Name'
    block_house_type,                        -- 'Block Number Type'
    block_house_no,                          -- 'Block Number'
    building_name,                           -- 'Building Name'
    floor_type,                              -- 'Store Type'
    floor_no,                                -- 'Store Number'
    flat_unit_no,                            -- 'Apartment Unit Number'
    flat_unit_type,                          -- 'Apartment Unit Type'
    dd_no,                                   -- 'Measurement Reduction (Interface Limiting Boundary)'
    lot_no,                                  -- 'Lot Number'
    incident_desc,                           -- 'Location and Project Event Description'
    contract_no,                             -- 'Contract Number'
    shortform_building,                      -- 'Building Abbreviation'
    shortform_estate,                        -- 'Land Abbreviation'
    created_by,                              -- 'Created by'
    created_date,                            -- 'Created Time'
    modified_by,                             -- 'Modified by'
    modified_date,                           -- 'Modified Time'
    timestamp,                               -- 'Timestamp'
    street_name_no_sw,                       -- 'Street Name Number Entry Switch'
    block_house_no_sw,                       -- 'Block Number Entry Switch'
    floor_no_sw,                             -- 'Store Number Entry Switch'
    dd_lot_no_sw,                            -- 'DD Lot Number Entry Switch'
    contract_no_sw,                          -- 'Contract Number Entry Switch'
    incident_desc_sw,                        -- 'Event Description Entry Switch'
    estate_sw,                               -- 'Estate/Village Entry Switch'
    phase_sw,                                -- 'Phase Number Entry Switch'
    village_place_sw,                        -- 'Village Address Entry Switch'
    building_sw,                             -- 'Building Name Entry Switch'
    flat_unit_no_sw,                         -- 'Store Number Entry Switch'
    user_formatted_sw,                       -- 'User-Formatted Entry Switch'
    full_addr,                               -- 'Full Address'
    parent_premise_id,                       -- 'Parent Premises ID'
    portable_meter_construction_site,        -- 'Portable Meter/Construction Site'
    current_timestamp ods_load_time,  -- Data load time
    current_timestamp ods_update_time   -- Data Update time
from abpms.premise
where modified_date >= to_date(${dt1},'yyyy-mm-dd')
  and modified_date < to_date(${dt1},'yyyy-mm-dd')+1;
```



## 4.ods_abpms_tmu_premise_meter_df

```sql

drop table if exists coss_ods.ods_abpms_tmu_premise_meter_df;
create table if not exists coss_ods.ods_abpms_tmu_premise_meter_df (
    premise_meter_id bpchar(10) null,             -- Meter ID at the address
    meter_id bpchar(10) null,                     -- Foreign key, MeterID
    premise_id bpchar(10) null,                   -- Foreign key, PREMISE
    install_meter_read_id bpchar(12) null,        -- Foreign key, Meter ID at installation
    install_date timestamp(6) null,               -- Meter installation date
    install_reading numeric(15, 6) null,          -- Meter reading at installation
    removal_meter_read_id bpchar(12) null,        -- Foreign key, Meter ID at removal
    removal_date timestamp(6) null,               -- Meter removal date
    removal_reading numeric(15, 6) null,          -- Meter reading at removal
    created_by varchar(8) null,                   -- Creator
    created_date timestamp(6) null,               -- Creation time
    modified_by varchar(8) null,                  -- Modifier
    modified_date timestamp(6) null,              -- Modification time
    "timestamp" timestamp(6) null,                -- Timestamp
    meter_no bpchar(8) null,                      -- Meter number
    serial_no varchar(16) null,                   -- Serial number
    ods_load_time timestamp(6),                   -- Data Loading Time
    ods_update_time timestamp(6),                 -- Data Update Time
    primary key(premise_meter_id)
)
with (
    orientation=row,
    compression=no
);

comment on table coss_ods.ods_abpms_tmu_premise_meter_df                          is 'Water meter address intermediate table';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.premise_meter_id         is 'Meter ID at the address';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.meter_id                 is 'Foreign key, MeterID';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.premise_id               is 'Foreign key, PREMISE';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.install_meter_read_id    is 'Foreign key, Meter ID at installation';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.install_date             is 'Meter installation date';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.install_reading          is 'Meter reading at installation';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.removal_meter_read_id    is 'Foreign key, Meter ID at removal';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.removal_date             is 'Meter removal date';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.removal_reading          is 'Meter reading at removal';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.created_by               is 'Creator';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.created_date             is 'Creation time';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.modified_by              is 'Modifier';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.modified_date            is 'Modification time';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.timestamp                is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.meter_no                 is 'Meter number';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.serial_no                is 'Serial number';
comment on column coss_ods.ods_abpms_tmu_premise_meter_df.ods_load_time            is 'Data load time';

```

```sql
-- ****************************************************************************************
-- subject     areas: ABPMS
-- function describe: Water meter address intermediate table
-- create         by: dongmaochen
-- create       date: 2025-08-09
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- abpms.premise_meter
-- target table
-- coss_ods.ods_abpms_tmu_premise_meter_df
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_premise_meter_df
select
    premise_meter_id,                     -- Meter ID at the address
    meter_id,                            -- Foreign key, MeterID
    premise_id,                          -- Foreign key, PREMISE
    install_meter_read_id,               -- Foreign key, Meter ID at installation
    install_date,                        -- Meter installation date
    install_reading,                     -- Meter reading at installation
    removal_meter_read_id,               -- Foreign key, Meter ID at removal
    removal_date,                        -- Meter removal date
    removal_reading,                     -- Meter reading at removal
    created_by,                          -- Creator
    created_date,                        -- Creation time
    modified_by,                         -- Modifier
    modified_date,                       -- Modification time
    "timestamp",                         -- Timestamp
    meter_no,                            -- Meter number
    serial_no,                           -- Serial number
    current_timestamp ods_load_time,     -- Data load time
    current_timestamp ods_update_time    -- Data Update time
from abpms.premise_meter;
```



## 5.ods_abpms_tmu_svc_dtl_df

```sql

drop table if exists coss_ods.ods_abpms_tmu_svc_dtl_df;
create table if not exists coss_ods.ods_abpms_tmu_svc_dtl_df (
    svc_id bpchar(10) null,                        -- Service ID
    svc_type_code varchar(8) null,                 -- Service type code
    start_date timestamp(6) null,                  -- Start date
    svc_dtl_sts_ind bpchar(2) null,                -- SD status indicator
    account_id bpchar(10) null,                    -- Account ID
    end_date timestamp(6) null,                    -- End date
    wis_account_no varchar(15) null,               -- Wis account number
    cust_read_sw bpchar(1) null,                   -- Whether to support customer self-uploaded meter readings
    hsic_code varchar(8) null,                     -- Industry classification HSIC code
    request_deposit_amt numeric(15, 2) null,       -- Deposit amount
    svc_dtl_relation_id varchar(10) null,          -- Service detail relationship ID
    start_req_by varchar(50) null,                 -- If the SD status is 20 (active), fill in CC Create_by to this field.
    stop_req_by varchar(50) null,                  -- If the SD status is 40 (discontinued), fill in CC Create_by to this field.
    high_bill_amt numeric(15, 2) null,             -- Used for generating some reports.
    exp_date timestamp(6) null,                    -- When CC creates a locksmith SD, check if this field is expired. If the SD status is expired, change it to 40 and fill in EndDate.
    created_by varchar(8) null,                    -- Creator
    created_date timestamp(6) null,                -- Creation time
    modified_by varchar(8) null,                   -- Updater
    modified_date timestamp(6) null,               -- Update time
    "timestamp" timestamp(6) null,                 -- Timestamp
    premise_id bpchar(10) null,                    -- Building ID
    svc_dtl_start_date timestamp(6) null,          -- When the first meter reading is done, record the StartDate in Bitem to calculate water usage.
    start_meter_read_id bpchar(12) null,           -- When opening a bill for the first time, use this to retrieve the first meter reading form.
    svc_dtl_stop_date timestamp(6) null,           -- Service detail end date
    usage_ind varchar(2) null,                     -- Only one value, '+' When creating a Bitem account, this field is synchronized to Bitem.
    stop_meter_read_id bpchar(12) null,            -- Stop meter reading ID
    rmk varchar(500) null,                         -- Notes
    workflow_id bpchar(50) null,                   -- Work order ID
    instal_svc_dtl_for_deposit_sw bpchar(1) null,  -- Deposit download service details switch
    start_rsn_ind varchar(4) null,                 -- Start reason indicator
    stop_rsn_ind varchar(4) null,                  -- End reason indicator
    no_payment_periods numeric null,               -- Non-payment deadline
    cust_comm_id bpchar(12) null,                  -- CCid
    special_usage_ind varchar(4) null,             -- PROP and null
    ods_load_time timestamp(6),                    -- Data Loading Time
    ods_update_time timestamp(6),                  -- Data Update Time
    primary key(svc_id)
)
with (
    orientation=row,
    compression=no
);

comment on table  coss_ods.ods_abpms_tmu_svc_dtl_df                                    is 'Service details, user account billing intermediate table, through which prices and some switches required for billing can be obtained';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.svc_id                             is 'Service ID';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.svc_type_code                      is 'Service type code';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.start_date                         is 'Start date';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.svc_dtl_sts_ind                    is 'SD status indicator';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.account_id                         is 'Account ID';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.end_date                           is 'End date';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.wis_account_no                     is 'Wis account number';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.cust_read_sw                       is 'Whether to support customer self-uploaded meter readings';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.hsic_code                          is 'Industry classification HSIC code';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.request_deposit_amt                is 'Deposit amount';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.svc_dtl_relation_id                is 'Service detail relationship ID';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.start_req_by                       is 'If the SD status is 20 (active), fill in CC Create_by to this field.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.stop_req_by                        is 'If the SD status is 40 (discontinued), fill in CC Create_by to this field.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.high_bill_amt                      is 'Used for generating some reports.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.exp_date                           is 'When CC creates a locksmith SD, check if this field is expired. If the SD status is expired, change it to 40 and fill in EndDate.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.created_by                         is 'Creator';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.created_date                       is 'Creation time';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.modified_by                        is 'Updater';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.modified_date                      is 'Update time';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.timestamp                          is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.premise_id                         is 'Building ID';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.svc_dtl_start_date                 is 'When the first meter reading is done, record the StartDate in Bitem to calculate water usage.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.start_meter_read_id                is 'When opening a bill for the first time, use this to retrieve the first meter reading form.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.svc_dtl_stop_date                  is 'Service detail end date';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.usage_ind                          is 'Only one value, + When creating a Bitem account, this field is synchronized to Bitem.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.stop_meter_read_id                 is 'Stop meter reading ID';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.rmk                                is 'Notes';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.workflow_id                        is 'Work order ID';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.instal_svc_dtl_for_deposit_sw      is 'Deposit download service details switch';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.start_rsn_ind                      is 'Start reason indicator';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.stop_rsn_ind                       is 'End reason indicator';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.no_payment_periods                 is 'Non-payment deadline';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.cust_comm_id                       is 'CCid';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.special_usage_ind                  is 'PROP and null';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.ods_load_time                      is 'Data load time';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_df.ods_update_time                    is 'Data Update time';




```

```sql
-- ****************************************************************************************
-- Subject     Areas: ABPMS
-- Function Describe: Service details, user account billing intermediate table, through which prices and some switches required for billing can be obtained
-- Create         By: dongmaochen
-- Create       Date: 2025-08-09
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- abpms.svc_dtl
-- Target Table
-- coss_ods.ods_abpms_tmu_svc_dtl_df
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_svc_dtl_df
select
    svc_id,                            -- Service ID
    svc_type_code,                    -- Service type code
    start_date,                       -- Start date
    svc_dtl_sts_ind,                  -- SD status indicator
    account_id,                       -- Account ID
    end_date,                         -- End date
    wis_account_no,                   -- Wis account number
    cust_read_sw,                     -- Whether to support customer self-uploaded meter readings
    hsic_code,                        -- Industry classification HSIC code
    request_deposit_amt,              -- Deposit amount
    svc_dtl_relation_id,              -- Service detail relationship ID
    start_req_by,                     -- If the SD status is 20 (active), fill in CC Create_by to this field.
    stop_req_by,                      -- If the SD status is 40 (discontinued), fill in CC Create_by to this field.
    high_bill_amt,                    -- Used for generating some reports.
    exp_date,                         -- When CC creates a locksmith SD, check if this field is expired. If the SD status is expired, change it to 40 and fill in EndDate.
    created_by,                       -- Creator
    created_date,                     -- Creation time
    modified_by,                      -- Updater
    modified_date,                    -- Update time
    timestamp,                        -- Timestamp
    premise_id,                       -- Building ID
    svc_dtl_start_date,               -- When the first meter reading is done, record the StartDate in Bitem to calculate water usage.
    start_meter_read_id,              -- When opening a bill for the first time, use this to retrieve the first meter reading form.
    svc_dtl_stop_date,                -- Service detail end date
    usage_ind,                        -- Only one value, '+' When creating a Bitem account, this field is synchronized to Bitem.
    stop_meter_read_id,               -- Stop meter reading ID
    rmk,                              -- Notes
    workflow_id,                      -- Work order ID
    instal_svc_dtl_for_deposit_sw,    -- Deposit download service details switch
    start_rsn_ind,                    -- Start reason indicator
    stop_rsn_ind,                     -- End reason indicator
    no_payment_periods,               -- Non-payment deadline
    cust_comm_id,                     -- CCid
    special_usage_ind,                -- PROP and null
    current_timestamp ods_load_time,  -- Data load time
    current_timestamp ods_update_time  -- Data Update time
from abpms.svc_dtl
where modified_date >= to_date(${dt1},'yyyy-mm-dd')
  and modified_date < to_date(${dt1},'yyyy-mm-dd')+1;
```



## 6.ods_abpms_tmu_meter_read_di_year

```sql

drop table if exists coss_ods.ods_abpms_tmu_meter_read_di_year;
create table if not exists coss_ods.ods_abpms_tmu_meter_read_di_year (
    meter_read_id bpchar(12),              -- 'Meter reading record Id (primary key)'
    read_date timestamp(6),                -- 'Meter reading date'
    billable_sw bpchar(1),                 -- 'Billing switch'
    meter_read_src_code varchar(12),       -- 'Meter reading source code'
    meter_reader_id varchar(20),           -- 'Meter reader Id'
    read_type_ind varchar(2),              -- 'Meter reading type indicator'
    reading numeric(15, 6),                -- 'Reading'
    lo_limit numeric(15, 6),               -- 'Lower limit'
    hi_limit numeric(15, 6),               -- 'Upper limit'
    rev_hilo_sw bpchar(1),                 -- 'Review HiLo switch'
    trended_sw bpchar(1),                  -- 'Trend switch'
    meter_id bpchar(10),                   -- 'Water meter Id'
    created_by varchar(8),                 -- 'Creator'
    created_date timestamp(6),             -- 'Creation date'
    modified_by varchar(8),                -- 'Modifier'
    modified_date timestamp(6),            -- 'Modification date'
    timestamp timestamp(6),                -- 'Timestamp'
    fld_act_id bpchar(10),                 -- 'Field activity Id'
    est_basis varchar(250),                -- 'Estimated reading basis'
    sec_userid varchar(15),                -- 'Security user Id'
    sec_grp varchar(20),                   -- 'Security group'
    ods_load_time timestamp(6),            -- Data Loading Time
    ods_update_time timestamp(6),          -- Data Update Time
    primary key(meter_read_id)
)
with (
    orientation=row,
    compression=no
);

comment on table coss_ods.ods_abpms_tmu_meter_read_di_year                          is 'Meter reading record';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.meter_read_id            is 'Meter reading record ID (primary key)';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.read_date                is 'Meter reading date';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.billable_sw              is 'Billing switch';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.meter_read_src_code      is 'Meter reading source code';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.meter_reader_id          is 'Meter reader ID';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.read_type_ind            is 'Meter reading type indicator';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.reading                  is 'Reading value';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.lo_limit                 is 'Lower limit';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.hi_limit                 is 'Upper limit';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.rev_hilo_sw              is 'Review HiLo switch';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.trended_sw               is 'Trend switch';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.meter_id                 is 'Water meter ID';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.created_by               is 'Creator';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.created_date             is 'Creation date';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.modified_by              is 'Modifier';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.modified_date            is 'Modification date';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.timestamp                is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.fld_act_id               is 'Field activity ID';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.est_basis                is 'Estimated reading basis';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.sec_userid               is 'Security user ID';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.sec_grp                  is 'Security group';
comment on column coss_ods.ods_abpms_tmu_meter_read_di_year.ods_load_time            is 'Data load time';


```

```sql
-- ****************************************************************************************
-- subject     areas: ABPMS
-- function describe: Meter reading record
-- create         by: dongmaochen
-- create       date: 2025-08-09
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- abpms.meter_read
-- target table
-- coss_ods.ods_abpms_tmu_meter_read_di_year
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_meter_read_di_year
select
    meter_read_id,           -- 'Meter reading record Id (primary key)'
    read_date,               -- 'Meter reading date'
    billable_sw,             -- 'Billing switch'
    meter_read_src_code,     -- 'Meter reading source code'
    meter_reader_id,         -- 'Meter reader Id'
    read_type_ind,           -- 'Meter reading type indicator'
    reading,                 -- 'Reading'
    lo_limit,                -- 'Lower limit'
    hi_limit,                -- 'Upper limit'
    rev_hilo_sw,             -- 'Review HiLo switch'
    trended_sw,              -- 'Trend switch'
    meter_id,                -- 'Water meter Id'
    created_by,              -- 'Creator'
    created_date,            -- 'Creation date'
    modified_by,             -- 'Modifier'
    modified_date,           -- 'Modification date'
    timestamp,               -- 'Timestamp'
    fld_act_id,              -- 'Field activity Id'
    est_basis,               -- 'Estimated reading basis'
    sec_userid,              -- 'Security user Id'
    sec_grp,                 -- 'Security group'
    current_timestamp ods_load_time,  -- Data load time
    current_timestamp ods_update_time  -- Data Update time
from abpms.meter_read;
```



## 7.ods_abpms_tmu_bill_di_year

```sql
drop table if exists coss_ods.ods_abpms_tmu_bill_di_year;
create table if not exists coss_ods.ods_abpms_tmu_bill_di_year (
    bill_id                      bpchar(12) null,          -- Primary Key
    bill_cyc_code               varchar(4) null,          -- Billing Cycle
    win_start_date              timestamp(6) null,        -- Start Time of Scheduled Billing
    account_id                  bpchar(10) null,          -- Account ID, Associated Account
    bill_sts_ind                varchar(2) null,          -- Billing Status
    bill_date                   timestamp(6) null,        -- Billing Date
    due_date                    timestamp(6) null,        -- Overdue Date, configured by customer type, CFG_CUST_CLS
    created_date                timestamp(6) null,        -- Creation Date
    comp_date                   timestamp(6) null,        -- Completion Date
    late_payment_chg_sw         bpchar(1) null,           -- Surcharge On/Off
    late_payment_chg_date       timestamp(6) null,        -- Surcharge Date
    allow_reopen_sw             bpchar(1) null,           -- Reopen Allowed On/Off
    next_cr_rev_date            timestamp(6) null,        -- Next Credit Review Date
    auto_pay_created_date       timestamp(6) null,        -- Auto Payment Creation Date
    auto_pay_amt                numeric(15, 2) null,      -- Auto Payment Amount
    auto_pay_stop_userid        varchar(8) null,          -- ID of the Person Who Stopped the Auto Payment
    auto_pay_stop_date          timestamp(6) null,        -- Date the Auto Payment Stopped
    auto_pay_stop_amt           numeric(15, 2) null,      -- Amount of the Auto Payment Stopped
    auto_pay_stop_created_date  timestamp(6) null,        -- Date the Auto Payment Stopped
    created_by                  varchar(8) null,          -- Create by
    modified_by                 varchar(8) null,          -- Modified by
    modified_date               timestamp(6) null,        -- Modified date
    "timestamp"                 timestamp(6) null,        -- Timestamp
    account_days                varchar(255) null,        -- Number of Billing Days, Total Number of Days
    ods_load_time               timestamp(6) null,        -- Data Loading Time
    ods_update_time             timestamp(6) null,        -- Data Update Time
    primary key(bill_id)
)
with (
    orientation=row,
    compression=no
);
comment on table  coss_ods.ods_abpms_tmu_bill_di_year                            is 'Bill record';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.bill_id                    is 'Primary Key';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.bill_cyc_code              is 'Billing Cycle';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.win_start_date             is 'Start Time of Scheduled Billing';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.account_id                 is 'Account ID, Associated Account';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.bill_sts_ind               is 'Billing Status';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.bill_date                  is 'Billing Date';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.due_date                   is 'Overdue Date, configured by customer type, CFG_CUST_CLS';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.created_date               is 'Creation Date';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.comp_date                  is 'Completion Date';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.late_payment_chg_sw        is 'Surcharge On/Off';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.late_payment_chg_date      is 'Surcharge Date';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.allow_reopen_sw            is 'Reopen Allowed On/Off';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.next_cr_rev_date           is 'Next Credit Review Date';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.auto_pay_created_date      is 'Auto Payment Creation Date';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.auto_pay_amt               is 'Auto Payment Amount';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.auto_pay_stop_userid       is 'ID of the Person Who Stopped the Auto Payment';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.auto_pay_stop_date         is 'Date the Auto Payment Stopped';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.auto_pay_stop_amt          is 'Amount of the Auto Payment Stopped';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.auto_pay_stop_created_date is 'Date the Auto Payment Stopped';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.created_by                 is 'Create by';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.modified_by                is 'Modified by';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.modified_date              is 'Modified date';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.timestamp                  is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.account_days               is 'Number of Billing Days, Total Number of Days';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.ods_load_time              is 'Data Loading Time';
comment on column coss_ods.ods_abpms_tmu_bill_di_year.ods_update_time            is 'Data Update Time';

```

```sql
-- ****************************************************************************************
-- Subject     Areas: ABPMS
-- Function Describe: Bill record
-- Create         By: dongmaochen
-- Create       Date: 2025-08-09
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- abpms.bill
-- Target Table
-- coss_ods.ods_abpms_tmu_bill_di_year
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_bill_di_year
select
    bill_id,                        -- Primary Key
    bill_cyc_code,                 -- Billing Cycle
    win_start_date,                -- Start Time of Scheduled Billing
    account_id,                    -- Account ID, Associated Account
    bill_sts_ind,                  -- Billing Status
    bill_date,                     -- Billing Date
    due_date,                      -- Overdue Date, configured by customer type, CFG_CUST_CLS
    created_date,                  -- Creation Date
    comp_date,                     -- Completion Date
    late_payment_chg_sw,           -- Surcharge On/Off
    late_payment_chg_date,         -- Surcharge Date
    allow_reopen_sw,               -- Reopen Allowed On/Off
    next_cr_rev_date,              -- Next Credit Review Date
    auto_pay_created_date,         -- Auto Payment Creation Date
    auto_pay_amt,                  -- Auto Payment Amount
    auto_pay_stop_userid,          -- ID of the Person Who Stopped the Auto Payment
    auto_pay_stop_date,            -- Date the Auto Payment Stopped
    auto_pay_stop_amt,             -- Amount of the Auto Payment Stopped
    auto_pay_stop_created_date,    -- Date the Auto Payment Stopped
    created_by,                    -- Create by
    modified_by,                   -- Modified by
    modified_date,                 -- Modified date
    "timestamp",                   -- Timestamp
    account_days,                  -- Number of Billing Days, Total Number of Days
    current_timestamp ods_load_time,  -- Data load time
    current_timestamp ods_update_time  -- Data Update time
from abpms.bill;
```



## 8.ods_inms_gdhk_dim_sic_mcategory_df

```sql
-- ****************************************************************************************
-- subject     areas: INMS
-- function describe: Sic mcategory
-- create         by: dongmaochen
-- create       date: 2025-08-09
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- inms_gdhk_dim_sic_mcategory
-- target table
-- coss_ods.ods_inms_gdhk_dim_sic_mcategory_df
-- ****************************************************************************************
drop table if exists coss_ods.ods_inms_gdhk_dim_sic_mcategory_df;
create table if not exists coss_ods.ods_inms_gdhk_dim_sic_mcategory_df(
    id varchar(50),                      -- id
    mcategory_code varchar(40),          -- mcategory code
    sic_bcode varchar(40),               -- sic bcode
    sic_ecode varchar(40),               -- sic ecode
    create_time timestamp(6),            -- create time
    update_time timestamp(6),            -- update time
    create_account varchar(100),         -- create account
    update_account varchar(100),         -- update account
    ods_load_time timestamp(6),          -- Data Loading Time
    ods_update_time timestamp(6),        -- Data Update Time
    primary key(id)
);

comment on table coss_ods.ods_inms_gdhk_dim_sic_mcategory_df                   is 'sic mcategory';
comment on column coss_ods.ods_inms_gdhk_dim_sic_mcategory_df.id                is 'id';
comment on column coss_ods.ods_inms_gdhk_dim_sic_mcategory_df.mcategory_code    is 'mcategory code';
comment on column coss_ods.ods_inms_gdhk_dim_sic_mcategory_df.sic_bcode         is 'sic bcode';
comment on column coss_ods.ods_inms_gdhk_dim_sic_mcategory_df.sic_ecode         is 'sic ecode';
comment on column coss_ods.ods_inms_gdhk_dim_sic_mcategory_df.create_time       is 'create time';
comment on column coss_ods.ods_inms_gdhk_dim_sic_mcategory_df.update_time       is 'update time';
comment on column coss_ods.ods_inms_gdhk_dim_sic_mcategory_df.create_account    is 'create account';
comment on column coss_ods.ods_inms_gdhk_dim_sic_mcategory_df.update_account    is 'update account';
comment on column coss_ods.ods_inms_gdhk_dim_sic_mcategory_df.ods_load_time     is 'Data load time';


insert into coss_ods.ods_inms_gdhk_dim_sic_mcategory_df
select
    id,                                  -- id
    mcategory_code,                      -- mcategory code
    sic_bcode,                           -- sic bcode
    sic_ecode,                           -- sic ecode
    create_time,                         -- create time
    update_time,                         -- update time
    create_account,                      -- create account
    update_account,                      -- update account
    current_timestamp ods_load_time,     -- Data load time
    current_timestamp ods_update_time    -- Data Update time
from inms_gdhk_dim_sic_mcategory;
```

> coss_ods.ods_inms_gdhk_dim_sic_mcategory_df table from inms 
>
> 添加了ods_update_time

```python
spark.read.csv(r'C:\Users\Administrator\Desktop\abc\GDHK_DIM_SIC_MCATEGORY.csv',header=True).createOrReplaceTempView('GDHK_DIM_SIC_MCATEGORY')
sql = """
select 
  ID
  ,MCATEGORY_CODE
  ,SIC_BCODE
  ,SIC_ECODE
  ,now() CREATE_TIME
  ,now() UPDATE_TIME
  ,'' CREATE_ACCOUNT
  ,'' UPDATE_ACCOUNT 
  ,now() ods_load_time  from GDHK_DIM_SIC_MCATEGORY
"""
df = spark.sql(sql)
write_gaussbd_tbls(df, 'coss_ods.ods_inms_gdhk_dim_sic_mcategory_df')
```

# dim

## dim_tmu_meter_info

```sql
-- ****************************************************************************************
-- Subject     Areas: TMU
-- Function Describe: Meter info
-- Create         By: dongmaochen
-- Create       Date: 2025-08-09
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_ods.ods_abpms_tmu_meter_df
-- coss_ods.ods_abpms_tmu_premise_meter_df
-- coss_ods.ods_abpms_tmu_svc_dtl_df
-- coss_ods.ods_abpms_tmu_cfg_hsic_df
-- Target Table
-- coss_dim.dim_tmu_meter_info
-- ****************************************************************************************
drop table if exists coss_dim.dim_tmu_meter_info;
create table if not exists coss_dim.dim_tmu_meter_info(
    meter_id              bpchar(10) null,    -- Meter ID
    meter_no             bpchar(8) null,     -- Meter number
    meter_type_code      varchar(15) null,   -- Meter type code
    meter_sts_ind        bpchar(1) null,     -- Meter status
    serial_no            varchar(16) null,   -- Serial number
    rcv_date             timestamp(6) null,  -- Received date
    retire_date          timestamp(6) null,  -- Retired date
    comments             varchar(254) null,  -- Remarks
    retire_rsn_code      varchar(10) null,   -- Retired reason code
    recond_date          timestamp(6) null,  -- Registered date
    created_date         timestamp(6) null,  -- Created time
    modified_date        timestamp(6) null,  -- Modified time
    premise_id           bpchar(10) null,    -- Foreign key, PREMISE
    hsic_code            varchar(8) null,    -- Industry classification HSIC code
    hsic_desc            varchar(60) null,   -- Classification Description
    hsic_desc_tc         varchar(60) null,   -- Classification Description (Traditional Chinese)
    desc_on_bill         varchar(60) null,   -- Description on Bill
    desc_on_bill_tc      varchar(60) null,   -- Description on Bill (Traditional Chinese)
    sic_bcode            varchar(40) null,   -- sic bcode
    mcategory_code       varchar(40) null,   -- mcategory code
    dim_load_time        timestamp(6) null,  -- Data load time
    dim_update_time      timestamp(6) null,  -- Data update time
    -- primary key(meter_id)
);
comment on table  coss_dim.dim_tmu_meter_info                  is 'Meter info';
comment on column coss_dim.dim_tmu_meter_info.meter_id         is 'Meter ID';
comment on column coss_dim.dim_tmu_meter_info.meter_no         is 'Meter number';
comment on column coss_dim.dim_tmu_meter_info.meter_type_code  is 'Meter type code';
comment on column coss_dim.dim_tmu_meter_info.meter_sts_ind    is 'Meter status';
comment on column coss_dim.dim_tmu_meter_info.serial_no        is 'Serial number';
comment on column coss_dim.dim_tmu_meter_info.rcv_date         is 'Received date';
comment on column coss_dim.dim_tmu_meter_info.retire_date      is 'Retired date';
comment on column coss_dim.dim_tmu_meter_info.comments         is 'Remarks';
comment on column coss_dim.dim_tmu_meter_info.retire_rsn_code  is 'Retired reason code';
comment on column coss_dim.dim_tmu_meter_info.recond_date      is 'Registered date';
comment on column coss_dim.dim_tmu_meter_info.created_date     is 'Created time';
comment on column coss_dim.dim_tmu_meter_info.modified_date    is 'Modified time';
comment on column coss_dim.dim_tmu_meter_info.premise_id       is 'Foreign key, PREMISE';
comment on column coss_dim.dim_tmu_meter_info.hsic_code        is 'Industry classification HSIC code';
comment on column coss_dim.dim_tmu_meter_info.hsic_desc        is 'Classification Description';
comment on column coss_dim.dim_tmu_meter_info.hsic_desc_tc     is 'Classification Description (Traditional Chinese)';
comment on column coss_dim.dim_tmu_meter_info.desc_on_bill     is 'Description on Bill';
comment on column coss_dim.dim_tmu_meter_info.desc_on_bill_tc  is 'Description on Bill (Traditional Chinese)';
comment on column coss_dim.dim_tmu_meter_info.sic_bcode        is 'sic bcode';
comment on column coss_dim.dim_tmu_meter_info.mcategory_code   is 'mcategory code';
comment on column coss_dim.dim_tmu_meter_info.dim_load_time    is 'Data load time';
comment on column coss_dim.dim_tmu_meter_info.dim_update_time  is 'Data update time';

-- Create temporary table 1: Associate meter info with premise ID
drop table if exists coss_tmp.tmp_tmu_meter_info_01;
create table if not exists coss_tmp.tmp_tmu_meter_info_01 as
select
    t.meter_id,
    t.meter_no,
    t.meter_type_code,
    t.meter_sts_ind,
    t.serial_no,
    t.rcv_date,
    t.retire_date,
    t.comments,
    t.retire_rsn_code,
    t.recond_date,
    t.created_date,
    t.modified_date,
    t1.premise_id
from
(
    select
        meter_id,
        meter_no,
        meter_type_code,
        meter_sts_ind,
        serial_no,
        rcv_date,
        retire_date,
        comments,
        retire_rsn_code,
        recond_date,
        created_date,
        modified_date
    from coss_ods.ods_abpms_tmu_meter_df
) t
left join
(
    select
        meter_id,
        premise_id
    from coss_ods.ods_abpms_tmu_premise_meter_df
) t1
on t.meter_id = t1.meter_id;

-- Create temporary table 2: Associate with HSIC code via premise ID
drop table if exists coss_tmp.tmp_tmu_meter_info_02;
create table if not exists coss_tmp.tmp_tmu_meter_info_02 as
select
    t.meter_id,
    t.meter_no,
    t.meter_type_code,
    t.meter_sts_ind,
    t.serial_no,
    t.rcv_date,
    t.retire_date,
    t.comments,
    t.retire_rsn_code,
    t.recond_date,
    t.created_date,
    t.modified_date,
    t.premise_id,
    t1.hsic_code
from
(
    select
        meter_id,
        meter_no,
        meter_type_code,
        meter_sts_ind,
        serial_no,
        rcv_date,
        retire_date,
        comments,
        retire_rsn_code,
        recond_date,
        created_date,
        modified_date,
        premise_id
    from coss_tmp.tmp_tmu_meter_info_01
) t
left join
(
    select
        premise_id,
        hsic_code
    from coss_ods.ods_abpms_tmu_svc_dtl_df
) t1
on t.premise_id = t1.premise_id;

-- Create temporary table 3: Associate HSIC info with SIC and mcategory code
drop table if exists coss_tmp.tmp_tmu_meter_info_03;
create table if not exists coss_tmp.tmp_tmu_meter_info_03 as
select
    t.hsic_code,
    t.hsic_desc,
    t.hsic_desc_tc,
    t.desc_on_bill,
    t.desc_on_bill_tc,
    t1.sic_bcode,
    t1.mcategory_code
from
(
    select
        hsic_code,
        hsic_desc,
        hsic_desc_tc,
        desc_on_bill,
        desc_on_bill_tc
    from coss_ods.ods_abpms_tmu_cfg_hsic_df
) t
inner join
(
    select
        sic_bcode,
        sic_ecode,
        mcategory_code
    from coss_ods.ods_inms_gdhk_dim_sic_mcategory_df
) t1
on t.hsic_code = t1.sic_bcode;

-- Clear target table data before insertion
delete from coss_dim.dim_tmu_meter_info;

-- Insert data into target dimension table
insert into coss_dim.dim_tmu_meter_info
select
    t.meter_id,                     -- Meter ID
    t.meter_no,                     -- Meter number
    t.meter_type_code,              -- Meter type code
    t.meter_sts_ind,                -- Meter status
    t.serial_no,                    -- Serial number
    t.rcv_date,                     -- Received date
    t.retire_date,                  -- Retired date
    t.comments,                     -- Remarks
    t.retire_rsn_code,              -- Retired reason code
    t.recond_date,                  -- Registered date
    t.created_date,                 -- Created time
    t.modified_date,                -- Modified time
    t.premise_id,                   -- Foreign key, PREMISE
    t.hsic_code,                    -- Industry classification HSIC code
    t1.hsic_desc,                   -- Classification Description
    t1.hsic_desc_tc,                -- Classification Description (Traditional Chinese)
    t1.desc_on_bill,                -- Description on Bill
    t1.desc_on_bill_tc,             -- Description on Bill (Traditional Chinese)
    t1.sic_bcode,                   -- sic bcode
    t1.mcategory_code,              -- mcategory code
    current_timestamp dim_load_time,-- Data load time
    current_timestamp dim_update_time -- Data update time
from coss_tmp.tmp_tmu_meter_info_02 t
left join coss_tmp.tmp_tmu_meter_info_03 t1
on t.hsic_code = t1.hsic_code;
```





```sql
ods_abpms_tmu_extract_user_bill_day_datax_{}_all


dwd_tmu_etl_user_meter_day_sql_dwd_tmu_bill_di_year_all



```



# dwd

## dwd_tmu_meter_read_di_year

```sql
drop table if exists coss_dwd.dwd_tmu_meter_read_di_year;
create table if not exists coss_dwd.dwd_tmu_meter_read_di_year (
    meter_read_id bpchar(12),              -- 'Meter reading record Id (primary key)'
    read_date timestamp(6),                -- 'Meter reading date'
    billable_sw bpchar(1),                 -- 'Billing switch'
    meter_read_src_code varchar(12),       -- 'Meter reading source code'
    meter_reader_id varchar(20),           -- 'Meter reader Id'
    read_type_ind varchar(2),              -- 'Meter reading type indicator'
    reading numeric(15, 6),                -- 'Reading'
    lo_limit numeric(15, 6),               -- 'Lower limit'
    hi_limit numeric(15, 6),               -- 'Upper limit'
    rev_hilo_sw bpchar(1),                 -- 'Review HiLo switch'
    trended_sw bpchar(1),                  -- 'Trend switch'
    meter_id bpchar(10),                   -- 'Water meter Id'
    created_date timestamp(6),             -- 'Creation date'
    modified_date timestamp(6),            -- 'Modification date'
    timestamp timestamp(6),                -- 'Timestamp'
    fld_act_id bpchar(10),                 -- 'Field activity Id'
    est_basis varchar(250),                -- 'Estimated reading basis'
    sec_userid varchar(15),                -- 'Security user Id'
    sec_grp varchar(20),                   -- 'Security group'
    dwd_load_time timestamp(6),            -- 'dwd load time '
    dwd_update_time timestamp(6),          -- 'dwd update time '
    primary key(meter_read_id)
)
with (
    orientation=row,
    compression=no
);

comment on table coss_dwd.dwd_tmu_meter_read_di_year                          is 'Meter reading record';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_read_id            is 'Meter reading record ID (primary key)';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.read_date                is 'Meter reading date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.billable_sw              is 'Billing switch';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_read_src_code      is 'Meter reading source code';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_reader_id          is 'Meter reader ID';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.read_type_ind            is 'Meter reading type indicator';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.reading                  is 'Reading value';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.lo_limit                 is 'Lower limit';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.hi_limit                 is 'Upper limit';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.rev_hilo_sw              is 'Review HiLo switch';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.trended_sw               is 'Trend switch';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_id                 is 'Water meter ID';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.created_date             is 'Creation date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.modified_date            is 'Modification date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.timestamp                is 'Timestamp';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.fld_act_id               is 'Field activity ID';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.est_basis                is 'Estimated reading basis';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.sec_userid               is 'Security user ID';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.sec_grp                  is 'Security group';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.dwd_load_time            is 'Data load time';


```

```sql
-- ****************************************************************************************
-- subject     areas: TMU
-- function describe: Meter reading record
-- create         by: dongmaochen
-- create       date: 2025-08-09
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_ods.ods_abpms_tmu_meter_read_di_year
-- target table
-- coss_dwd.dwd_tmu_meter_read_di_year
-- ****************************************************************************************
delete from coss_dwd.dwd_tmu_meter_read_di_year;
insert into coss_dwd.dwd_tmu_meter_read_di_year
select
    meter_read_id,           -- 'Meter reading record Id (primary key)'
    read_date,               -- 'Meter reading date'
    billable_sw,             -- 'Billing switch'
    meter_read_src_code,     -- 'Meter reading source code'
    meter_reader_id,         -- 'Meter reader Id'
    read_type_ind,           -- 'Meter reading type indicator'
    reading,                 -- 'Reading'
    lo_limit,                -- 'Lower limit'
    hi_limit,                -- 'Upper limit'
    rev_hilo_sw,             -- 'Review HiLo switch'
    trended_sw,              -- 'Trend switch'
    meter_id,                -- 'Water meter Id'
    created_date,            -- 'Creation date'
    modified_date,           -- 'Modification date'
    timestamp,               -- 'Timestamp'
    fld_act_id,              -- 'Field activity Id'
    est_basis,               -- 'Estimated reading basis'
    sec_userid,              -- 'Security user Id'
    sec_grp,                 -- 'Security group'
    current_timestamp dwd_load_time,  -- 'dwd load time '
    current_timestamp dwd_update_time  -- 'dwd update time '（补充与dwd_load_time一致的时间逻辑，确保字段赋值完整）
from coss_ods.ods_abpms_tmu_meter_read_di_year;
```



## dwd_tmu_bill_di_year

```sql

drop table if exists coss_dwd.dwd_tmu_bill_di_year;
create table if not exists coss_dwd.dwd_tmu_bill_di_year (
    bill_id                      bpchar(12) null,          -- Primary Key
    bill_cyc_code               varchar(4) null,          -- Billing Cycle
    win_start_date              timestamp(6) null,        -- Start Time of Scheduled Billing
    account_id                  bpchar(10) null,          -- Account ID, Associated Account
    bill_sts_ind                varchar(2) null,          -- Billing Status
    bill_date                   timestamp(6) null,        -- Billing Date
    due_date                    timestamp(6) null,        -- Overdue Date, configured by customer type, CFG_CUST_CLS
    created_date                timestamp(6) null,        -- Creation Date
    comp_date                   timestamp(6) null,        -- Completion Date
    late_payment_chg_sw         bpchar(1) null,           -- Surcharge On/Off
    late_payment_chg_date       timestamp(6) null,        -- Surcharge Date
    allow_reopen_sw             bpchar(1) null,           -- Reopen Allowed On/Off
    next_cr_rev_date            timestamp(6) null,        -- Next Credit Review Date
    auto_pay_created_date       timestamp(6) null,        -- Auto Payment Creation Date
    auto_pay_amt                numeric(15, 2) null,      -- Auto Payment Amount
    auto_pay_stop_userid        varchar(8) null,          -- ID of the Person Who Stopped the Auto Payment
    auto_pay_stop_date          timestamp(6) null,        -- Date the Auto Payment Stopped
    auto_pay_stop_amt           numeric(15, 2) null,      -- Amount of the Auto Payment Stopped
    auto_pay_stop_created_date  timestamp(6) null,        -- Date the Auto Payment Stopped
    modified_date               timestamp(6) null,        -- modified date
    "timestamp"                 timestamp(6) null,        -- timestamp
    account_days                varchar(255) null,        -- Number of Billing Days, Total Number of Days
    dwd_load_time               timestamp(6) null,        -- 'dwd load time '
    dwd_update_time             timestamp(6) null,        -- 'dwd update time '
    primary key(bill_id)
)
with (
    orientation=row,
    compression=no
);
comment on table  coss_dwd.dwd_tmu_bill_di_year                            is 'Bill record';
comment on column coss_dwd.dwd_tmu_bill_di_year.bill_id                    is 'Primary Key';
comment on column coss_dwd.dwd_tmu_bill_di_year.bill_cyc_code              is 'Billing Cycle';
comment on column coss_dwd.dwd_tmu_bill_di_year.win_start_date             is 'Start Time of Scheduled Billing';
comment on column coss_dwd.dwd_tmu_bill_di_year.account_id                 is 'Account ID, Associated Account';
comment on column coss_dwd.dwd_tmu_bill_di_year.bill_sts_ind               is 'Billing Status';
comment on column coss_dwd.dwd_tmu_bill_di_year.bill_date                  is 'Billing Date';
comment on column coss_dwd.dwd_tmu_bill_di_year.due_date                   is 'Overdue Date, configured by customer type, CFG_CUST_CLS';
comment on column coss_dwd.dwd_tmu_bill_di_year.created_date               is 'Creation Date';
comment on column coss_dwd.dwd_tmu_bill_di_year.comp_date                  is 'Completion Date';
comment on column coss_dwd.dwd_tmu_bill_di_year.late_payment_chg_sw        is 'Surcharge On/Off';
comment on column coss_dwd.dwd_tmu_bill_di_year.late_payment_chg_date      is 'Surcharge Date';
comment on column coss_dwd.dwd_tmu_bill_di_year.allow_reopen_sw            is 'Reopen Allowed On/Off';
comment on column coss_dwd.dwd_tmu_bill_di_year.next_cr_rev_date           is 'Next Credit Review Date';
comment on column coss_dwd.dwd_tmu_bill_di_year.auto_pay_created_date      is 'Auto Payment Creation Date';
comment on column coss_dwd.dwd_tmu_bill_di_year.auto_pay_amt               is 'Auto Payment Amount';
comment on column coss_dwd.dwd_tmu_bill_di_year.auto_pay_stop_userid       is 'ID of the Person Who Stopped the Auto Payment';
comment on column coss_dwd.dwd_tmu_bill_di_year.auto_pay_stop_date         is 'Date the Auto Payment Stopped';
comment on column coss_dwd.dwd_tmu_bill_di_year.auto_pay_stop_amt          is 'Amount of the Auto Payment Stopped';
comment on column coss_dwd.dwd_tmu_bill_di_year.auto_pay_stop_created_date is 'Date the Auto Payment Stopped';
comment on column coss_dwd.dwd_tmu_bill_di_year.modified_date              is 'modified date';
comment on column coss_dwd.dwd_tmu_bill_di_year.timestamp                  is 'timestamp';
comment on column coss_dwd.dwd_tmu_bill_di_year.account_days               is 'Number of Billing Days, Total Number of Days';
comment on column coss_dwd.dwd_tmu_bill_di_year.dwd_load_time              is 'dwd load time ';
comment on column coss_dwd.dwd_tmu_bill_di_year.dwd_update_time            is 'dwd update time ';

```

```sql
-- ****************************************************************************************
-- Subject     Areas: TMU
-- Function Describe: Bill record
-- Create         By: dongmaochen
-- Create       Date: 2025-08-09
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- coss_ods.ods_abpms_tmu_bill_di_year
-- Target Table
-- coss_dwd.dwd_tmu_bill_di_year
-- ****************************************************************************************
-- Clear target table data before insertion
delete from coss_dwd.dwd_tmu_bill_di_year;

-- Insert data into target DWD table
insert into coss_dwd.dwd_tmu_bill_di_year
select
    bill_id,                        -- Primary Key
    bill_cyc_code,                 -- Billing Cycle
    win_start_date,                -- Start Time of Scheduled Billing
    account_id,                    -- Account ID, Associated Account
    bill_sts_ind,                  -- Billing Status
    bill_date,                     -- Billing Date
    due_date,                      -- Overdue Date, configured by customer type, CFG_CUST_CLS
    created_date,                  -- Creation Date
    comp_date,                     -- Completion Date
    late_payment_chg_sw,           -- Surcharge On/Off
    late_payment_chg_date,         -- Surcharge Date
    allow_reopen_sw,               -- Reopen Allowed On/Off
    next_cr_rev_date,              -- Next Credit Review Date
    auto_pay_created_date,         -- Auto Payment Creation Date
    auto_pay_amt,                  -- Auto Payment Amount
    auto_pay_stop_userid,          -- ID of the Person Who Stopped the Auto Payment
    auto_pay_stop_date,            -- Date the Auto Payment Stopped
    auto_pay_stop_amt,             -- Amount of the Auto Payment Stopped
    auto_pay_stop_created_date,    -- Date the Auto Payment Stopped
    modified_date,                 -- modified date
    "timestamp",                   -- timestamp
    account_days,                  -- Number of Billing Days, Total Number of Days
    current_timestamp dwd_load_time,  -- Data load time
    current_timestamp dwd_update_time  -- Data update time
from coss_ods.ods_abpms_tmu_bill_di_year;
```



# dm

## 1.coss_dm.dm_tmu_customer_meter_number_di

### create table 

```sql
;drop table if exists coss_dm.dm_tmu_customer_meter_number_di
;create table if not exists coss_dm.dm_tmu_customer_meter_number_di(
  id                   varchar(50)
  ,statistical_year     decimal(10)
  ,region_abbr          varchar(20)
  ,cmn_sum              decimal(15,0)
  ,ctg_dom              decimal(15,0)
  ,ctg_ser              decimal(15,0)
  ,ctg_ind              decimal(15,0)
  ,ctg_flu              decimal(15,0)
  ,ctg_coc              decimal(15,0)
  ,ctg_gov              decimal(15,0)
  ,ctg_con              decimal(15,0)
  ,ctg_fre              decimal(15,0)
  ,ctg_che              decimal(15,0)
  ,ctg_shi              decimal(15,0)
  ,cos_bill             decimal(15,0)
  ,cos_bill_t           decimal(15,0)
  ,cos_bill_h           decimal(15,0)
  ,cos_bill_tr          decimal(15,5)
  ,cos_bill_hr          decimal(15,5)
  ,cos_ubill            decimal(15,0)
  ,cos_ubill_t          decimal(15,0)
  ,cos_ubill_h          decimal(15,0)
  ,cos_ubill_tr         decimal(15,5)
  ,cos_ubill_hr         decimal(15,5)
  ,cos_tbill            decimal(15,0)
  ,cos_tbill_t          decimal(15,0)
  ,cos_tbill_h          decimal(15,0)
  ,cos_tbill_tr         decimal(15,5)
  ,cos_tbill_hr         decimal(15,5)
  ,ord_cm               decimal(15,0)
  ,tel_cm               decimal(15,0)
  ,dm_load_time         timestamp(6)
)
```

### simulation data

```python
# simulatin data from inms system's GDHK_MART_REGION_KPI_MONTH table
df = spark.read.csv('./inms/GDHK_MART_REGION_KPI_MONTH_202401221422.csv',header=True)
df.createOrReplaceTempView('dma_month')
sql = """
with t_a(select 
  cast(month_id/100 as int) year
  ,max(month_id) month_id
from dma_month where item_code = 'NOCM'
group by 
  year
order by
month_id),
t_b as (
select
  t.month_id
,'HKSAR' region_no
,sum(t.item_value) as ITEM_VALUE
from dma_month t 
  inner join (select 
  cast(month_id/100 as int) year
  ,max(month_id) month_id
from dma_month where item_code = 'NOCM'
group by 
  year
order by
month_id) t1 on t.month_id = t1.month_id
where 
  item_code = 'NOCM'
group by 
  t.month_id
)
select 
  uuid()                                       as id
  ,cast(t.month_id/100 as int)                 as statistical_year
  ,t.region_no                                 as region_abbr
  ,t.item_value                                as cmn_sum
  ,cast(t.item_value * 89.92880061/100 as int) as ctg_dom
  ,cast(t.item_value * 5.657027892/100 as int) as ctg_ser
  ,cast(t.item_value * 1.961490760/100 as int) as ctg_ind
  ,cast(t.item_value * 1.322269527/100 as int) as ctg_flu
  ,cast(t.item_value * 0.625054912/100 as int) as ctg_coc
  ,cast(t.item_value * 0.380311264/100 as int) as ctg_gov
  ,cast(t.item_value * 0.094635118/100 as int) as ctg_con
  ,cast(t.item_value * 0.020330034/100 as int) as ctg_fre
  ,cast(t.item_value * 0.006810732/100 as int) as ctg_che
  ,cast(t.item_value * 0.003166990/100 as int) as ctg_shi
  ,cast(t.item_value * 99.6/100 as int)        as cos_bill
  ,cast(t.item_value * 99.6/100*0.002 as int)  as cos_bill_t
  ,cast(t.item_value * 99.6/100*0.001 as int)  as cos_bill_h
  ,0.2                                         as cos_bill_tr
  ,0.1                                         as cos_bill_hr
  ,cast(t.item_value * 0.4/100  as int)        as cos_ubill
  ,cast(t.item_value * 0.4/100*0.002  as int)  as cos_ubill_t
  ,cast(t.item_value * 0.4/100*0.001  as int)  as cos_ubill_h
  ,0.2                                         as cos_ubill_tr
  ,0.1                                         as cos_ubill_hr
  ,cast(t.item_value   as int)                 as cos_tbill
  ,cast(t.item_value *0.002  as int)           as cos_tbill_t
  ,cast(t.item_value *0.001  as int)           as cos_tbill_h
  ,0.2                                         as cos_tbill_tr
  ,0.1                                         as cos_tbill_hr
  ,t.item_value*0.9981                         as ord_cm
  ,t.item_value*0.0019                         as tel_cm
  ,now()                                       as dm_load_time
 from dma_month t 
  inner join t_a t1 on t.month_id = t1.month_id
where 
item_code = 'NOCM' 
union all 
select 
  uuid()                                       as id
  ,cast(t.month_id/100 as int)                 as statistical_year
  ,t.region_no                                 as region_abbr
  ,t.item_value                                as cmn_sum
  ,cast(t.item_value * 89.92880061/100 as int) as ctg_dom
  ,cast(t.item_value * 5.657027892/100 as int) as ctg_ser
  ,cast(t.item_value * 1.961490760/100 as int) as ctg_ind
  ,cast(t.item_value * 1.322269527/100 as int) as ctg_flu
  ,cast(t.item_value * 0.625054912/100 as int) as ctg_coc
  ,cast(t.item_value * 0.380311264/100 as int) as ctg_gov
  ,cast(t.item_value * 0.094635118/100 as int) as ctg_con
  ,cast(t.item_value * 0.020330034/100 as int) as ctg_fre
  ,cast(t.item_value * 0.006810732/100 as int) as ctg_che
  ,cast(t.item_value * 0.003166990/100 as int) as ctg_shi
  ,cast(t.item_value * 99.6/100 as int)        as cos_bill
  ,cast(t.item_value * 99.6/100*0.002 as int)  as cos_bill_t
  ,cast(t.item_value * 99.6/100*0.001 as int)  as cos_bill_h
  ,0.2                                         as cos_bill_tr
  ,0.1                                         as cos_bill_hr
  ,cast(t.item_value * 0.4/100  as int)        as cos_ubill
  ,cast(t.item_value * 0.4/100*0.002  as int)  as cos_ubill_t
  ,cast(t.item_value * 0.4/100*0.001  as int)  as cos_ubill_h
  ,0.2                                         as cos_ubill_tr
  ,0.1                                         as cos_ubill_hr
  ,cast(t.item_value   as int)                 as cos_tbill
  ,cast(t.item_value *0.002  as int)           as cos_tbill_t
  ,cast(t.item_value *0.001  as int)           as cos_tbill_h
  ,0.2                                         as cos_tbill_tr
  ,0.1                                         as cos_tbill_hr
  ,t.item_value*0.9981                         as ord_cm
  ,t.item_value*0.0019                         as tel_cm
  ,now()                                       as dm_load_time
 from t_b t
"""
df = spark.sql(sql)
writeToPostgresql(df,'coss_dm.dm_tmu_customer_meter_number_di')
```

## 2.coss_dm.dm_tmu_water_consumption_di

### create table 

```sql
;drop table if exists coss_dm.dm_tmu_water_consumption_di
;create table if not exists coss_dm.dm_tmu_water_consumption_di(
  id                  varchar(50)
  ,statistical_year   decimal(10)
  ,region_abbr        varchar(20)
  ,bmc                decimal(15,5)
  ,umc                decimal(15,5)
  ,mc                 decimal(15,5)
  ,tbmc               decimal(15,5)
  ,fbmc               decimal(15,5)
  ,dm_load_time       timestamp(6)
)
```

### simulation data

```python
# simulatin data from inms system's GDHK_MART_REGION_KPI_MONTH table
df = spark.read.csv('./inms/GDHK_MART_REGION_KPI_MONTH_202401221422.csv',header=True)
df.createOrReplaceTempView('dma_month')
sql = """
with t_a as (select
  cast(month_id/100 as int) year
  ,region_no
  ,cast(sum(item_value)/10000 as decimal(15,5)) item_value
from dma_month 
where
  item_code = 'BMC'
group by 
   year
  ,region_no),
t_b as (select
  cast(month_id/100 as int) year
  ,region_no
  ,cast(sum(item_value)/10000 as decimal(15,5)) item_value
from dma_month 
where
  item_code = 'UMC'
group by 
   year
  ,region_no),
t_c as (select
  cast(month_id/100 as int) year
  ,region_no
  ,cast(sum(item_value)/10000 as decimal(15,5)) item_value
from dma_month 
where
  item_code = 'MC'
group by 
   year
  ,region_no)
select
  uuid() id
  ,t.year        as statistical_year
  ,t.region_no   as region_abbr
  ,t.item_value  as bmc
  ,t1.item_value as umc
  ,t2.item_value as mc
  ,t.item_value/10      as tbmc
  ,t.item_value/10*0.9  as fbmc
  ,now()              as dm_load_time
from t_a t
inner join t_b t1 on t.region_no = t1.region_no and t.year = t1.year
inner join t_c t2 on t.region_no = t2.region_no and t.year = t2.year
union all
select
  uuid()              as id
  ,t.year             as statistical_year
  ,'HKSAR'            as region_abbr
  ,sum(t.item_value)  as bmc
  ,sum(t1.item_value) as umc
  ,sum(t2.item_value) as mc
  ,sum(t.item_value)/10      as tbmc
  ,sum(t.item_value)/10*0.9  as fbmc
  ,now()              as dm_load_time
from t_a t
inner join t_b t1 on t.region_no = t1.region_no and t.year = t1.year
inner join t_c t2 on t.region_no = t2.region_no and t.year = t2.year
group by
  t.year

"""
df = spark.sql(sql)
writeToPostgresql(df,'coss_dm.dm_tmu_water_consumption_di')

#  item_code in('BMC', 'MC', 'UMC')
```

# appendix

## 1.python function

```sql
# ref https://zhuanlan.zhihu.com/p/596323405
# https://github.com/steveloughran/winutils
# spark https://spark.apache.org/docs/3.1.1/api/python/getting_started/quickstart.html
# 数仓设计教程： https://zhuanlan.zhihu.com/p/497979535
"""
日期字符串  '18-Jul-2018' 转换为日期函数：FROM_UNIXTIME(unix_timestamp('18-Jul-2018', 'dd-MMM-yyyy'))

"""
import os
os.environ["JAVA_HOME"] = r"F:\devtool\tool\jdk1.8.0_251"
os.environ["SPARK_HOME"] = r"F:\devtool\tool\spark-3.1.1-bin-hadoop2.7"
import findspark
findspark.init()
from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
pd.set_option('display.max_columns', None)
from pyspark.sql import Row

spark = SparkSession.builder.master("local[*]").config('driver-memory', '12g').config('spark.executor.memory','12g').getOrCreate()  
# spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
# spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled", "true")
def writeToPostgresql(df, tableName):
    df.write.format('jdbc')\
    .option("url", r"jdbc:postgresql://172.16.201.8:5432/dws" ) \
    .option("dbtable", tableName ) \
    .option("user", "gddst01" ) \
    .option("password", "Gddst_89225300" ) \
    .option("driver", "org.postgresql.Driver") \
    .option("numPartitions", 10 ) \
    .mode("append").save()
```

