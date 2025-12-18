version desc

```tex
1.修改dm层代码查询语句，用AI优化
```



> ods_labconnect_wtw_wqmm_analyzer_verification_di_year
> ods_labconnect_wtw_wqmm_analyzer_verification_item_df
> ods_labconnect_wtw_wqmm_config_df
> ods_labconnect_wtw_wqmm_location_df
> ods_labconnect_wtw_wqmm_parameter_limit_df
> ods_labconnect_wtw_wtw_unit_df

# ods

## 1.ods_labconnect_wtw_wqmm_analyzer_verification_di_year

```sql
-- Drop existing table if it exists
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year;

-- Create partitioned table for online analyzer verification results (yearly)
create table if not exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year (
    verification_id serial4 not null,
    wtw_id int4 not null,
    status int2 null,
    last_updated_date timestamp null,
    sample_date timestamp null,
    reported_by int4 null,
    reported_role int4 null,
    reported_date timestamp null,
    no_record_reason text null,
    approved_by int4 null,
    approved_role int4 null,
    approved_remarks text null,
    approved_date timestamp null,
    require_acknowledgement bool null,
    acknowledged_by int4 null,
    acknowledged_role int4 null,
    acknowledged_remarks text null,
    acknowledged_date timestamp null,
    reviewed_by int4 null,
    reviewed_role int4 null,
    reviewed_remarks text null,
    reviewed_date timestamp null,
    rejected_by int4 null,
    rejected_role int4 null,
    rejected_remarks text null,
    rejected_date timestamp null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    -- Primary key constraint: Unique identifier for verification records
    constraint ods_labconnect_wtw_wqmm_analyzer_verification_di_year_pkey primary key (verification_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
-- Partition by range of last update date
partition by range (last_updated_date)
(
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

comment on table coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year is 'Table To Store All The Online Analyzer Verification Results';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.verification_id is 'ID Of Each Online Analyzer Verification Record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.wtw_id is 'ID Of The Corresponding WTW';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.status is 'Status Of The Reminder:0: Reported And Not Yet Approved ;1: Approved And Require Acknowledged.;2: Approved/Acknowledged And Not Yet Reviewed;3: Reviewed;-1: Rejected';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.last_updated_date is 'Datetime When The Record Is Updated';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.sample_date is 'Datetime When The Sample Is Taken';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reported_by is 'User Who The Sample Record Is Created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reported_role is 'Role Of The Users Who The Sample Record Is Created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reported_date is 'Datetime When The Sample Record Is Created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.no_record_reason is 'Reason For Not Taking The Sample ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.approved_by is 'User Who Has Approved The Record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.approved_role is 'Role Of The Users Who The Sample Record Is Approved';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.approved_remarks is 'Remarks From The Approver';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.approved_date is 'Datetime When The Analyzer Is Checked';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.require_acknowledgement is 'True: The Records Need Acknowledged Instrument Colleague;False: No Need To Acknowledged Instrument Colleague';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.acknowledged_by is 'Instrument Colleague Who Has Acknowledged.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.acknowledged_role is 'Role Of The Users Who Has Acknowledged.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.acknowledged_remarks is 'Remarks From The Acknowledged Instrument Colleague';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.acknowledged_date is 'Datetime When The Sample Record Is Acknowledged';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reviewed_by is 'User Who Has Reviewed The Record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reviewed_role is 'Role Of The Users Who The Sample Record Is Reviewed';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reviewed_remarks is 'Remarks From The Reviewer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reviewed_date is 'Datetime When The Sample Record Is Reviewed';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.rejected_by is 'User Who Has Rejected The Record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.rejected_role is 'Role Of The Users Who The Sample Record Is Rejected';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.rejected_remarks is 'Remarks From The Rejecter';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.rejected_date is 'Datetime When The Sample Record Is Rejected';
```

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year
-- target table
-- labcon_hki.wqmm_analyzer_verification
-- ****************************************************************************************
insert into coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year
select
    verification_id,                   -- ID Of Each Online Analyzer Verification Record
    wtw_id,                            -- ID Of The Corresponding WTW
    status,                            -- Status Of The Reminder:0: Reported And Not Yet Approved ;1: Approved And Require Acknowledged.;2: Approved/Acknowledged And Not Yet Reviewed;3: Reviewed;-1: Rejected
    last_updated_date,                 -- Datetime When The Record Is Updated
    sample_date,                       -- Datetime When The Sample Is Taken
    reported_by,                       -- User Who The Sample Record Is Created
    reported_role,                     -- Role Of The Users Who The Sample Record Is Created
    reported_date,                     -- Datetime When The Sample Record Is Created
    no_record_reason,                  -- Reason For Not Taking The Sample
    approved_by,                       -- User Who Has Approved The Record
    approved_role,                     -- Role Of The Users Who The Sample Record Is Approved
    approved_remarks,                  -- Remarks From The Approver
    approved_date,                     -- Datetime When The Analyzer Is Checked
    require_acknowledgement,           -- True: The Records Need Acknowledged Instrument Colleague;False: No Need To Acknowledged Instrument Colleague
    acknowledged_by,                   -- Instrument Colleague Who Has Acknowledged.
    acknowledged_role,                 -- Role Of The Users Who Has Acknowledged.
    acknowledged_remarks,              -- Remarks From The Acknowledged Instrument Colleague
    acknowledged_date,                 -- Datetime When The Sample Record Is Acknowledged
    reviewed_by,                       -- User Who Has Reviewed The Record
    reviewed_role,                     -- Role Of The Users Who The Sample Record Is Reviewed
    reviewed_remarks,                  -- Remarks From The Reviewer
    reviewed_date,                     -- Datetime When The Sample Record Is Reviewed
    rejected_by,                       -- User Who Has Rejected The Record
    rejected_role,                     -- Role Of The Users Who The Sample Record Is Rejected
    rejected_remarks,                  -- Remarks From The Rejecter
    rejected_date,                     -- Datetime When The Sample Record Is Rejected
    current_timestamp ods_update_time,  -- Update Time Of ODS Layer Record
    current_timestamp ods_load_time     -- Load Time Of ODS Layer Record
from coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year_tmp -- Original Source Table: labcon_hki.wqmm_analyzer_verification
on duplicate key update
    wtw_id = values(wtw_id),
    status = values(status),
    last_updated_date = values(last_updated_date),
    sample_date = values(sample_date),
    reported_by = values(reported_by),
    reported_role = values(reported_role),
    reported_date = values(reported_date),
    no_record_reason = values(no_record_reason),
    approved_by = values(approved_by),
    approved_role = values(approved_role),
    approved_remarks = values(approved_remarks),
    approved_date = values(approved_date),
    require_acknowledgement = values(require_acknowledgement),
    acknowledged_by = values(acknowledged_by),
    acknowledged_role = values(acknowledged_role),
    acknowledged_remarks = values(acknowledged_remarks),
    acknowledged_date = values(acknowledged_date),
    reviewed_by = values(reviewed_by),
    reviewed_role = values(reviewed_role),
    reviewed_remarks = values(reviewed_remarks),
    reviewed_date = values(reviewed_date),
    rejected_by = values(rejected_by),
    rejected_role = values(rejected_role),
    rejected_remarks = values(rejected_remarks),
    rejected_date = values(rejected_date),
    ods_update_time = values(ods_update_time)
```



## 2.ods_labconnect_wtw_wqmm_analyzer_verification_item_df

```sql
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df;
create table if not exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df (
    verification_item_id int4 null,
    verification_id int4 null,
    loc_id int4 null,
    ph_manual numeric(8, 5) null,
    ph_manual_dp int2 null,
    ph_analyzer numeric(8, 5) null,
    ph_analyzer_dp int2 null,
    ph_remarks text null,
    turb_manual numeric(8, 5) null,
    turb_manual_dp int2 null,
    turb_analyzer numeric(8, 5) null,
    turb_analyzer_dp int2 null,
    turb_remarks text null,
    rcl2_manual numeric(8, 5) null,
    rcl2_manual_dp int2 null,
    rcl2_analyzer numeric(8, 5) null,
    rcl2_analyzer_dp int2 null,
    rcl2_remarks text null,
    fluoride_manual numeric(8, 5) null,
    fluoride_manual_dp int2 null,
    fluoride_analyzer numeric(8, 5) null,
    fluoride_analyzer_dp int2 null,
    fluoride_remarks text null,
    mn_manual numeric(8, 5) null,
    mn_manual_dp int2 null,
    mn_analyzer numeric(8, 5) null,
    mn_analyzer_dp int2 null,
    mn_remarks text null,
    nh3_manual numeric(8, 5) null,
    nh3_manual_dp int2 null,
    nh3_analyzer int4 null,
    nh3_analyzer_dp int2 null,
    nh3_remarks text null,
    uv_manual numeric(8, 5) null,
    uv_manual_dp int2 null,
    uv_analyzer int4 null,
    uv_analyzer_dp int2 null,
    uv_remarks text null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    constraint ods_labconnect_wtw_wqmm_analyzer_verification_item_df_pkey primary key (verification_item_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df is 'Table To Store The Sample Items In The Online Analyzer Verification Results';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.verification_item_id is 'ID Of Each Record Item';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.verification_id is 'ID Of The Corresponding Record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.loc_id is 'ID Of The Sampling Location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_manual is 'Sample Value Of pH From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_analyzer is 'Sample Value Of pH From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_remarks is 'Remarks On The pH Sample';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_manual is 'Sample Value Of Turbidity From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_analyzer is 'Sample Value Of Turbidity From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_remarks is 'Remarks On The Turbidity Sample';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_manual is 'Sample Value Of Residual Chlorine From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_analyzer is 'Sample Value Of Residual Chlorine From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_remarks is 'Remarks On The Sample Of Residual Chlorine';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_manual is 'Sample Value Of Fluoride From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_analyzer is 'Sample Value Of Fluoride From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_remarks is 'Remarks On The Sample Of Fluoride';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_manual is 'Sample Value Of Mangenese From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_analyzer is 'Sample Value Of Mangenese From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_remarks is 'Remarks On The Sample Of Mangenese';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_manual is 'Sample Value Of Ammonia From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_analyzer is 'Sample Value Of Ammonia From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_remarks is 'Remarks On The Sample Of Ammonia';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_manual is 'Sample Value Of UV Light From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_analyzer is 'Sample Value Of UV Light From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_remarks is 'Remarks On The Sample Of UV Light';
```

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- labcon_hki.wqmm_analyzer_verification_item
-- target table
-- coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df
-- ****************************************************************************************
insert into coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df
select
    verification_item_id,         -- ID Of Each Record Item
    verification_id,              -- ID Of The Corresponding Record
    loc_id,                       -- ID Of The Sampling Location
    ph_manual,                    -- Sample Value Of pH From Manual Test
    ph_analyzer,                  -- Sample Value Of pH From Online Analyzer
    ph_manual_dp,                 -- No. Of Decimal Places Required For The Value From Manual Test
    ph_analyzer_dp,               -- No. Of Decimal Places Required For The Value From Online Analyzer
    ph_remarks,                   -- Remarks On The pH Sample
    turb_manual,                  -- Sample Value Of Turbidity From Manual Test
    turb_analyzer,                -- Sample Value Of Turbidity From Online Analyzer
    turb_manual_dp,               -- No. Of Decimal Places Required For The Value From Manual Test
    turb_analyzer_dp,             -- No. Of Decimal Places Required For The Value From Online Analyzer
    turb_remarks,                 -- Remarks On The Turbidity Sample
    rcl2_manual,                  -- Sample Value Of Residual Chlorine From Manual Test
    rcl2_analyzer,                -- Sample Value Of Residual Chlorine From Online Analyzer
    rcl2_manual_dp,               -- No. Of Decimal Places Required For The Value From Manual Test
    rcl2_analyzer_dp,             -- No. Of Decimal Places Required For The Value From Online Analyzer
    rcl2_remarks,                 -- Remarks On The Sample Of Residual Chlorine
    fluoride_manual,              -- Sample Value Of Fluoride From Manual Test
    fluoride_analyzer,            -- Sample Value Of Fluoride From Online Analyzer
    fluoride_manual_dp,           -- No. Of Decimal Places Required For The Value From Manual Test
    fluoride_analyzer_dp,         -- No. Of Decimal Places Required For The Value From Online Analyzer
    fluoride_remarks,             -- Remarks On The Sample Of Fluoride
    mn_manual,                    -- Sample Value Of Mangenese From Manual Test
    mn_analyzer,                  -- Sample Value Of Mangenese From Online Analyzer
    mn_manual_dp,                 -- No. Of Decimal Places Required For The Value From Manual Test
    mn_analyzer_dp,               -- No. Of Decimal Places Required For The Value From Online Analyzer
    mn_remarks,                   -- Remarks On The Sample Of Mangenese
    nh3_manual,                   -- Sample Value Of Ammonia From Manual Test
    nh3_analyzer,                 -- Sample Value Of Ammonia From Online Analyzer
    nh3_manual_dp,                -- No. Of Decimal Places Required For The Value From Manual Test
    nh3_analyzer_dp,              -- No. Of Decimal Places Required For The Value From Online Analyzer
    nh3_remarks,                  -- Remarks On The Sample Of Ammonia
    uv_manual,                    -- Sample Value Of UV Light From Manual Test
    uv_analyzer,                  -- Sample Value Of UV Light From Online Analyzer
    uv_manual_dp,                 -- No. Of Decimal Places Required For The Value From Manual Test
    uv_analyzer_dp,               -- No. Of Decimal Places Required For The Value From Online Analyzer
    uv_remarks,                   -- Remarks On The Sample Of UV Light
    current_timestamp ods_update_time,  -- ODS Layer Record Update Time
    current_timestamp ods_load_time     -- ODS Layer Record Load Time
from coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df_tmp  -- Original Source Table: labcon_hki.wqmm_analyzer_verification_item
on duplicate key update
    verification_id = values(verification_id),
    loc_id = values(loc_id),
    ph_manual = values(ph_manual),
    ph_analyzer = values(ph_analyzer),
    ph_manual_dp = values(ph_manual_dp),
    ph_analyzer_dp = values(ph_analyzer_dp),
    ph_remarks = values(ph_remarks),
    turb_manual = values(turb_manual),
    turb_analyzer = values(turb_analyzer),
    turb_manual_dp = values(turb_manual_dp),
    turb_analyzer_dp = values(turb_analyzer_dp),
    turb_remarks = values(turb_remarks),
    rcl2_manual = values(rcl2_manual),
    rcl2_analyzer = values(rcl2_analyzer),
    rcl2_manual_dp = values(rcl2_manual_dp),
    rcl2_analyzer_dp = values(rcl2_analyzer_dp),
    rcl2_remarks = values(rcl2_remarks),
    fluoride_manual = values(fluoride_manual),
    fluoride_analyzer = values(fluoride_analyzer),
    fluoride_manual_dp = values(fluoride_manual_dp),
    fluoride_analyzer_dp = values(fluoride_analyzer_dp),
    fluoride_remarks = values(fluoride_remarks),
    mn_manual = values(mn_manual),
    mn_analyzer = values(mn_analyzer),
    mn_manual_dp = values(mn_manual_dp),
    mn_analyzer_dp = values(mn_analyzer_dp),
    mn_remarks = values(mn_remarks),
    nh3_manual = values(nh3_manual),
    nh3_analyzer = values(nh3_analyzer),
    nh3_manual_dp = values(nh3_manual_dp),
    nh3_analyzer_dp = values(nh3_analyzer_dp),
    nh3_remarks = values(nh3_remarks),
    uv_manual = values(uv_manual),
    uv_analyzer = values(uv_analyzer),
    uv_manual_dp = values(uv_manual_dp),
    uv_analyzer_dp = values(uv_analyzer_dp),
    uv_remarks = values(uv_remarks),
    ods_update_time = values(ods_update_time)
```





## 3.ods_labconnect_wtw_wqmm_config_df

```sql
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_config_df;
create table if not exists coss_ods.ods_labconnect_wtw_wqmm_config_df (
    config_id serial4 not null,
    wtw_id int4 not null,
    config_type int2 null,
    created_date timestamp null,
    created_by int4 null,
    created_role int4 null,
    effective_date timestamp null,
    verification_interval_hr int2 null,
    jar_test_interval_hr int2 null,
    jar_measure_type int2 null,
    require_to_test bool null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    constraint ods_labconnect_wtw_wqmm_config_df_pkey primary key (config_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_ods.ods_labconnect_wtw_wqmm_config_df is 'Table To Store All The Configuration Records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.config_id is 'ID Of Each Parameter Set';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.wtw_id is 'ID Of The Corresponding WTW';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.config_type is 'Configuration Type 0: Parameters For Water Quality Monitoring; 1: Parameters For Online Analyzer Verification; 2: Sampling Frequency';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.created_date is 'Datetime When The Record Is Created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.created_by is 'User Who Creates The Records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.created_role is 'User Role Who Creates The Records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.effective_date is 'Datetime When The Parameter Set Is Effective. The Parameter Set Is Effective On Or After The Effective_Date. If There Are Multiple Effective Records, Choose The One With The Latest Effective Date, Tie-Break By Latest Created_Date';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.verification_interval_hr is 'This Field Only Has Meaning If Config_Type = 2.The Interval (Hrs) In Which The Online Analyzer Verification Test Is Performed. If This Field Is Empty, No Online Analyzer Verification Test Is Required For The Specific WTW.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.jar_test_interval_hr is 'This Field Only Has Meaning If Config_Type = 2.The Interval (Hrs) In Which The Jar Test Is Performed. If This Field Is Empty, No Jar Test Is Required For The Specific WTW.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.jar_measure_type is '(If Config_Type <> 2, Use Default Value 0) 0: The Jar Test Measurement Is "絮凝大小"; 1: The Jar Test Measurement Is "沉澱速度"';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.require_to_test is '(If Config_Type <> 2, Use Default Value False)True: Perform Taste & Odour Test;False: No Need To Perform Taste & Odour Test';
```

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- labcon_hki.wqmm_config
-- target table
-- coss_ods.ods_labconnect_wtw_wqmm_config_df
-- ****************************************************************************************
insert into coss_ods.ods_labconnect_wtw_wqmm_config_df
select
    config_id,                          -- ID Of Each Parameter Set
    wtw_id,                             -- ID Of The Corresponding WTW
    config_type,                        -- Configuration Type 0: Parameters For Water Quality Monitoring; 1: Parameters For Online Analyzer Verification; 2: Sampling Frequency
    created_date,                       -- Datetime When The Record Is Created
    created_by,                         -- User Who Creates The Records
    created_role,                       -- User Role Who Creates The Records
    effective_date,                     -- Datetime When The Parameter Set Is Effective. The Parameter Set Is Effective On Or After The Effective_Date. If There Are Multiple Effective Records, Choose The One With The Latest Effective Date, Tie-Break By Latest Created_Date
    verification_interval_hr,           -- This Field Only Has Meaning If Config_Type = 2.The Interval (Hrs) In Which The Online Analyzer Verification Test Is Performed. If This Field Is Empty, No Online Analyzer Verification Test Is Required For The Specific WTW.
    jar_test_interval_hr,               -- This Field Only Has Meaning If Config_Type = 2.The Interval (Hrs) In Which The Jar Test Is Performed. If This Field Is Empty, No Jar Test Is Required For The Specific WTW.
    jar_measure_type,                   -- (If Config_Type <> 2, Use Default Value 0) 0: The Jar Test Measurement Is "絮凝大小"; 1: The Jar Test Measurement Is "沉澱速度"
    require_to_test,                    -- (If Config_Type <> 2, Use Default Value False)True: Perform Taste & Odour Test;False: No Need To Perform Taste & Odour Test
    current_timestamp ods_update_time,  -- ODS Layer Record Update Time
    current_timestamp ods_load_time     -- ODS Layer Record Load Time
from coss_ods.ods_labconnect_wtw_wqmm_config_df_tmp -- Source Table: labcon_hki.wqmm_config
on duplicate key update
    wtw_id = values(wtw_id),
    config_type = values(config_type),
    created_date = values(created_date),
    created_by = values(created_by),
    created_role = values(created_role),
    effective_date = values(effective_date),
    verification_interval_hr = values(verification_interval_hr),
    jar_test_interval_hr = values(jar_test_interval_hr),
    jar_measure_type = values(jar_measure_type),
    require_to_test = values(require_to_test),
    ods_update_time = values(ods_update_time)
```

## 4.ods_labconnect_wtw_wqmm_location_df

```sql
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_location_df;
create table if not exists coss_ods.ods_labconnect_wtw_wqmm_location_df (
    loc_id serial4 not null,
    loc_full_name text null,
    loc_name text null,
    loc_suffix text null,
    loc_name_chi text null,
    loc_color_pri text null,
    loc_color_sec text null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    constraint ods_labconnect_wtw_wqmm_location_df_pkey primary key (loc_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_ods.ods_labconnect_wtw_wqmm_location_df is 'Table To Store The Sample Location. Note That Some WTW May Need To Take Two Different Samples At The Same Location. (e.g. Clarified (A) And Clarified (B) For SHW, But Only Clarified For Others)';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_id is 'ID Of The Location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_full_name is 'Location Full Name (Including Suffices). This Field Can Also Be Used For Translation In UI And Labeling In Reports.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_name is 'Name Of The Location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_suffix is 'Suffix Of The Location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_name_chi is 'Name Of The Location In Chinese (For Reporting)';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_color_pri is 'Primary Display Color (In RGBA),Primary Color Is Used For Text And Section Border';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_color_sec is 'Secondary Display Color (In RGBA),Secondary Color Is Used For Highlight And Section Shading';
```

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- labcon_hki.wqmm_location
-- target table
-- coss_ods.ods_labconnect_wtw_wqmm_location_df
-- ****************************************************************************************
insert into coss_ods.ods_labconnect_wtw_wqmm_location_df
select
    loc_id,              -- ID Of The Location
    loc_full_name,       -- Location Full Name (Including Suffices). This Field Can Also Be Used For Translation In UI And Labeling In Reports.
    loc_name,            -- Name Of The Location
    loc_suffix,          -- Suffix Of The Location
    loc_name_chi,        -- Name Of The Location In Chinese (For Reporting)
    loc_color_pri,       -- Primary Display Color (In RGBA),Primary Color Is Used For Text And Section Border
    loc_color_sec,       -- Secondary Display Color (In RGBA),Secondary Color Is Used For Highlight And Section Shading
    current_timestamp ods_update_time,
    current_timestamp ods_load_time
from coss_ods.ods_labconnect_wtw_wqmm_location_df_tmp -- labcon_hki.wqmm_location
on duplicate key update
    loc_full_name = values(loc_full_name),
    loc_name = values(loc_name),
    loc_suffix = values(loc_suffix),
    loc_name_chi = values(loc_name_chi),
    loc_color_pri = values(loc_color_pri),
    loc_color_sec = values(loc_color_sec),
    ods_update_time = values(ods_update_time)
```



## 5.ods_labconnect_wtw_wqmm_parameter_limit_df

```sql
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df;
create table if not exists coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df (
    parameter_limit_id serial4 not null,
    config_id int4 null,
    loc_id int4 null,
    target_type int2 null,
    ph_compare text null,
    ph_min_value numeric(8, 5) null,
    ph_min_val_dp int4 null,
    ph_max_value numeric(8, 5) null,
    ph_max_val_dp int4 null,
    turb_compare text null,
    turb_min_value numeric(8, 5) null,
    turb_min_val_dp int4 null,
    turb_max_value numeric(8, 5) null,
    turb_max_val_dp int4 null,
    rcl2_compare text null,
    rcl2_min_value numeric(8, 5) null,
    rcl2_min_val_dp int4 null,
    rcl2_max_value numeric(8, 5) null,
    rcl2_max_val_dp int4 null,
    uv_compare text null,
    uv_min_value numeric(8, 5) null,
    uv_min_val_dp int4 null,
    uv_max_value numeric(8, 5) null,
    uv_max_val_dp int4 null,
    fluoride_compare text null,
    fluoride_min_value numeric(8, 5) null,
    fluoride_min_val_dp int4 null,
    fluoride_max_value numeric(8, 5) null,
    fluoride_max_val_dp int4 null,
    mn_compare text null,
    mn_min_value numeric(8, 5) null,
    mn_min_val_dp int4 null,
    mn_max_value numeric(8, 5) null,
    mn_max_val_dp int4 null,
    nh3_compare text null,
    nh3_min_value numeric(8, 5) null,
    nh3_min_val_dp int4 null,
    nh3_max_value numeric(8, 5) null,
    nh3_max_val_dp int4 null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    constraint ods_labconnect_wtw_wqmm_parameter_limit_df_pkey primary key (parameter_limit_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df is 'Table To Store All The Operational Targets And Critical Limits For Water Quality Monitoring';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.parameter_limit_id is 'ID Of Each Item In The Parameters';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.config_id is 'Configuration ID';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.loc_id is 'ID Of The Corresponding Sampling Location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.target_type is 'Target Type: 0: Operational Target; 1: Critical Limit';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_compare is 'Define Whether pH Value Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_min_value is 'Define Whether pH Value Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_max_value is 'Define Whether pH Value Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_compare is 'Define Whether Turbidity Value Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_min_value is 'Define Whether Turbidity Value Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_max_value is 'Define Whether Turbidity Value Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_compare is 'Define Whether Residual Chlorine Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_min_value is 'Define Whether Residual Chlorine Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_max_value is 'Define Whether Residual Chlorine Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_compare is 'Define Whether Fluoride Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_min_value is 'Define Whether Fluoride Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_max_value is 'Define Whether Fluoride Is Acceptable Or Not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_compare is 'Define Whether Manganese Is Acceptable Or Not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_min_value is 'Define Whether Manganese Is Acceptable Or Not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_max_value is 'Define Whether Manganese Is Acceptable Or Not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_compare is 'Define Whether Ammonia Is Acceptable Or Not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_min_value is 'Define Whether Ammonia Is Acceptable Or Not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_max_value is 'Define Whether Ammonia Is Acceptable Or Not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_compare is 'Define Whether UV Light Is Acceptable Or Not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_min_value is 'Define Whether UV Light Is Acceptable Or Not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_max_value is 'Define Whether UV Light Is Acceptable Or Not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
```

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- labcon_hki.wqmm_parameter_limit
-- target table
-- coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df
-- ****************************************************************************************
insert into coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df
select 
    parameter_limit_id,        -- ID Of Each Item In The Parameters
    config_id,                 -- Configuration ID
    loc_id,                    -- ID Of The Corresponding Sampling Location
    target_type,               -- Target Type: 0: Operational Target; 1: Critical Limit
    ph_compare,                -- Define Whether pH Value Is Acceptable Or Not
    ph_min_value,              -- Define Whether pH Value Is Acceptable Or Not
    ph_max_value,              -- Define Whether pH Value Is Acceptable Or Not
    ph_min_val_dp,             -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    ph_max_val_dp,             -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    turb_compare,              -- Define Whether Turbidity Value Is Acceptable Or Not
    turb_min_value,            -- Define Whether Turbidity Value Is Acceptable Or Not
    turb_max_value,            -- Define Whether Turbidity Value Is Acceptable Or Not
    turb_min_val_dp,           -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    turb_max_val_dp,           -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    rcl2_compare,              -- Define Whether Residual Chlorine Is Acceptable Or Not
    rcl2_min_value,            -- Define Whether Residual Chlorine Is Acceptable Or Not
    rcl2_max_value,            -- Define Whether Residual Chlorine Is Acceptable Or Not
    rcl2_min_val_dp,           -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    rcl2_max_val_dp,           -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    fluoride_compare,          -- Define Whether Fluoride Is Acceptable Or Not
    fluoride_min_value,        -- Define Whether Fluoride Is Acceptable Or Not
    fluoride_max_value,        -- Define Whether Fluoride Is Acceptable Or Not
    fluoride_min_val_dp,       -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    fluoride_max_val_dp,       -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    mn_compare,                -- Define Whether Manganese Is Acceptable Or Not
    mn_min_value,              -- Define Whether Manganese Is Acceptable Or Not
    mn_max_value,              -- Define Whether Manganese Is Acceptable Or Not
    mn_min_val_dp,             -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    mn_max_val_dp,             -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    nh3_compare,               -- Define Whether Ammonia Is Acceptable Or Not
    nh3_min_value,             -- Define Whether Ammonia Is Acceptable Or Not
    nh3_max_value,             -- Define Whether Ammonia Is Acceptable Or Not
    nh3_min_val_dp,            -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    nh3_max_val_dp,            -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    uv_compare,                -- Define Whether UV Light Is Acceptable Or Not
    uv_min_value,              -- Define Whether UV Light Is Acceptable Or Not
    uv_max_value,              -- Define Whether UV Light Is Acceptable Or Not
    uv_min_val_dp,             -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    uv_max_val_dp,             -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    current_timestamp ods_update_time,
    current_timestamp ods_load_time
from coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df_tmp -- labcon_hki.wqmm_parameter_limit
on duplicate key update
    config_id = values(config_id),
    loc_id = values(loc_id),
    target_type = values(target_type),
    ph_compare = values(ph_compare),
    ph_min_value = values(ph_min_value),
    ph_max_value = values(ph_max_value),
    ph_min_val_dp = values(ph_min_val_dp),
    ph_max_val_dp = values(ph_max_val_dp),
    turb_compare = values(turb_compare),
    turb_min_value = values(turb_min_value),
    turb_max_value = values(turb_max_value),
    turb_min_val_dp = values(turb_min_val_dp),
    turb_max_val_dp = values(turb_max_val_dp),
    rcl2_compare = values(rcl2_compare),
    rcl2_min_value = values(rcl2_min_value),
    rcl2_max_value = values(rcl2_max_value),
    rcl2_min_val_dp = values(rcl2_min_val_dp),
    rcl2_max_val_dp = values(rcl2_max_val_dp),
    fluoride_compare = values(fluoride_compare),
    fluoride_min_value = values(fluoride_min_value),
    fluoride_max_value = values(fluoride_max_value),
    fluoride_min_val_dp = values(fluoride_min_val_dp),
    fluoride_max_val_dp = values(fluoride_max_val_dp),
    mn_compare = values(mn_compare),
    mn_min_value = values(mn_min_value),
    mn_max_value = values(mn_max_value),
    mn_min_val_dp = values(mn_min_val_dp),
    mn_max_val_dp = values(mn_max_val_dp),
    nh3_compare = values(nh3_compare),
    nh3_min_value = values(nh3_min_value),
    nh3_max_value = values(nh3_max_value),
    nh3_min_val_dp = values(nh3_min_val_dp),
    nh3_max_val_dp = values(nh3_max_val_dp),
    uv_compare = values(uv_compare),
    uv_min_value = values(uv_min_value),
    uv_max_value = values(uv_max_value),
    uv_min_val_dp = values(uv_min_val_dp),
    uv_max_val_dp = values(uv_max_val_dp),
    ods_update_time = values(ods_update_time)
```

## 6.ods_labconnect_wtw_wtw_unit_df

```sql
drop table if exists coss_ods.ods_labconnect_wtw_wtw_unit_df;
create table if not exists coss_ods.ods_labconnect_wtw_wtw_unit_df (
    wtw_id serial4 not null,
    wtw_code text not null,
    wtw_name text not null,
    wtw_name_chi text not null,
    phase_1 bool not null,
    phase_2 bool not null,
    phase_3 bool not null,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    constraint ods_labconnect_wtw_wtw_unit_pkey primary key (wtw_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_ods.ods_labconnect_wtw_wtw_unit_df is 'A List Of WTW Units';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_id is 'ID Of The WTW';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_code is 'WTW Code ';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_name is 'WTW English Name (For Phase 1 & 3 Reporting)';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_name_chi is 'WTW Chinese Name (For Phase 2 Reporting)';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.phase_1 is 'True: WTW Has Joined Phase 1, Which Should Show Up In Phase 1 Site.False: WTW Should Not Show Up In Phase 1 Site';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.phase_2 is 'True: WTW Has Joined Phase 2, Which Should Show Up In Phase 2 Site.False: WTW Should Not Show Up In Phase 2 Site';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.phase_3 is 'True: WTW Has Joined Phase 3, Which Should Show Up In Phase 3 Site.False: WTW Should Not Show Up In Phase 3 Site';
```

```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- labcon_hki.wtw_unit
-- target table
-- coss_ods.ods_labconnect_wtw_wtw_unit_df
-- ****************************************************************************************
insert into coss_ods.ods_labconnect_wtw_wtw_unit_df
select
  wtw_id,                          -- ID Of The WTW
  wtw_code,                        -- WTW Code
  wtw_name,                        -- WTW English Name (For Phase 1 & 3 Reporting)
  wtw_name_chi,                    -- WTW Chinese Name (For Phase 2 Reporting)
  phase_1,                         -- True: WTW Has Joined Phase 1, Which Should Show Up In Phase 1 Site.False: WTW Should Not Show Up In Phase 1 Site
  phase_2,                         -- True: WTW Has Joined Phase 2, Which Should Show Up In Phase 2 Site.False: WTW Should Not Show Up In Phase 2 Site
  phase_3,                         -- True: WTW Has Joined Phase 3, Which Should Show Up In Phase 3 Site.False: WTW Should Not Show Up In Phase 3 Site
  current_timestamp ods_update_time,  -- ODS Layer Record Update Time
  current_timestamp ods_load_time     -- ODS Layer Record Load Time
from coss_ods.ods_labconnect_wtw_wtw_unit_df_tmp -- Source Table: labcon_hki.wtw_unit
on duplicate key update
    wtw_code = values(wtw_code),
    wtw_name = values(wtw_name),
    wtw_name_chi = values(wtw_name_chi),
    phase_1 = values(phase_1),
    phase_2 = values(phase_2),
    phase_3 = values(phase_3),
    ods_update_time = values(ods_update_time)
```





# dwd

## 1.coss_dwd.dwd_wtw_verification_di_year

```sql
drop table if exists coss_dwd.dwd_wtw_verification_di_year;
create table if not exists coss_dwd.dwd_wtw_verification_di_year(
    verification_id    int4,
    wtw_id             int4,
    status             int2,
    last_updated_date  timestamp,
    sample_date        timestamp,
    reviewed_date      timestamp,
    wtw_code           text,
    wtw_name           text,
    wtw_name_chi       text,
    phase_1            bool,
    phase_2            bool,
    phase_3            bool,
    dwd_update_time timestamp(6) default current_timestamp,
    dwd_load_time timestamp(6) default current_timestamp,
    constraint dwd_wtw_verification_di_year_pkey primary key (verification_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
partition by range (sample_date)
(
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

comment on table coss_dwd.dwd_wtw_verification_di_year is 'Table To Store All The Online Analyzer Verification Results';
comment on column coss_dwd.dwd_wtw_verification_di_year.verification_id is 'ID Of Each Online Analyzer Verification Record';
comment on column coss_dwd.dwd_wtw_verification_di_year.wtw_id is 'ID Of The Corresponding WTW';
comment on column coss_dwd.dwd_wtw_verification_di_year.status is 'Status Of The Reminder:0: Reported And Not Yet Approved ;1: Approved And Require Acknowledged.;2: Approved/Acknowledged And Not Yet Reviewed;3: Reviewed;-1: Rejected';
comment on column coss_dwd.dwd_wtw_verification_di_year.last_updated_date is 'Datetime When The Record Is Updated';
comment on column coss_dwd.dwd_wtw_verification_di_year.sample_date is 'Datetime When The Sample Is Taken';
comment on column coss_dwd.dwd_wtw_verification_di_year.reviewed_date is 'Datetime When The Sample Record Is Reviewed';
comment on column coss_dwd.dwd_wtw_verification_di_year.wtw_code is 'WTW Code';
comment on column coss_dwd.dwd_wtw_verification_di_year.wtw_name is 'WTW English Name (For Phase 1 & 3 Reporting)';
comment on column coss_dwd.dwd_wtw_verification_di_year.wtw_name_chi is 'WTW Chinese Name (For Phase 2 Reporting)';
comment on column coss_dwd.dwd_wtw_verification_di_year.phase_1 is 'True: WTW Has Joined Phase 1, Which Should Show Up In Phase 1 Site.False: WTW Should Not Show Up In Phase 1 Site';
comment on column coss_dwd.dwd_wtw_verification_di_year.phase_2 is 'True: WTW Has Joined Phase 2, Which Should Show Up In Phase 2 Site.False: WTW Should Not Show Up In Phase 2 Site';
comment on column coss_dwd.dwd_wtw_verification_di_year.phase_3 is 'True: WTW Has Joined Phase 3, Which Should Show Up In Phase 3 Site.False: WTW Should Not Show Up In Phase 3 Site';
```



```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year
-- coss_ods.ods_labconnect_wtw_wtw_unit_df
-- target table
-- coss_dwd.dwd_wtw_verification_di_year
-- ****************************************************************************************
insert into coss_dwd.dwd_wtw_verification_di_year
select
    t.verification_id,       -- ID Of Each Online Analyzer Verification Record
    t.wtw_id,               -- ID Of The Corresponding WTW
    t.status,               -- Status Of The Reminder:0: Reported And Not Yet Approved ;1: Approved And Require Acknowledged.;2: Approved/Acknowledged And Not Yet Reviewed;3: Reviewed;-1: Rejected
    t.last_updated_date,    -- Datetime When The Record Is Updated
    t.sample_date,          -- Datetime When The Sample Is Taken
    t.reviewed_date,        -- Datetime When The Sample Record Is Reviewed
    t1.wtw_code,            -- WTW Code
    t1.wtw_name,            -- WTW English Name (For Phase 1 & 3 Reporting)
    t1.wtw_name_chi,        -- WTW Chinese Name (For Phase 2 Reporting)
    t1.phase_1,             -- True: WTW Has Joined Phase 1, Which Should Show Up In Phase 1 Site.False: WTW Should Not Show Up In Phase 1 Site
    t1.phase_2,             -- True: WTW Has Joined Phase 2, Which Should Show Up In Phase 2 Site.False: WTW Should Not Show Up In Phase 2 Site
    t1.phase_3,             -- True: WTW Has Joined Phase 3, Which Should Show Up In Phase 3 Site.False: WTW Should Not Show Up In Phase 3 Site
    current_timestamp as dwd_update_time,
    current_timestamp as dwd_load_time
from
    coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year t
    inner join coss_ods.ods_labconnect_wtw_wtw_unit_df t1 on t.wtw_id = t1.wtw_id
where t.ods_update_time >= '${dwd_update_time}' and t1.ods_update_time >= '${dwd_update_time}'
on duplicate key update
    wtw_id = values(wtw_id),
    status = values(status),
    last_updated_date = values(last_updated_date),
    sample_date = values(sample_date),
    reviewed_date = values(reviewed_date),
    wtw_code = values(wtw_code),
    wtw_name = values(wtw_name),
    wtw_name_chi = values(wtw_name_chi),
    phase_1 = values(phase_1),
    phase_2 = values(phase_2),
    phase_3 = values(phase_3),
    dwd_update_time = values(dwd_update_time)
```



## 2.coss_dwd.dwd_wtw_verification_item_di_year

```sql
drop table if exists coss_dwd.dwd_wtw_verification_item_di_year;
create table if not exists coss_dwd.dwd_wtw_verification_item_di_year(
    verification_item_id  int4,
    verification_id       int4,
    loc_id                int4,
    loc_full_name         text,
    loc_name              text,
    loc_suffix            text,
    loc_name_chi          text,
    sample_date           timestamp,
    ph_manual             numeric(8, 5),
    ph_manual_dp          int2,
    ph_analyzer           numeric(8, 5),
    ph_analyzer_dp        int2,
    ph_remarks            text,
    turb_manual           numeric(8, 5),
    turb_manual_dp        int2,
    turb_analyzer         numeric(8, 5),
    turb_analyzer_dp      int2,
    turb_remarks          text,
    rcl2_manual           numeric(8, 5),
    rcl2_manual_dp        int2,
    rcl2_analyzer         numeric(8, 5),
    rcl2_analyzer_dp      int2,
    rcl2_remarks          text,
    fluoride_manual       numeric(8, 5),
    fluoride_manual_dp    int2,
    fluoride_analyzer     numeric(8, 5),
    fluoride_analyzer_dp  int2,
    fluoride_remarks      text,
    mn_manual             numeric(8, 5),
    mn_manual_dp          int2,
    mn_analyzer           numeric(8, 5),
    mn_analyzer_dp        int2,
    mn_remarks            text,
    nh3_manual            numeric(8, 5),
    nh3_manual_dp         int2,
    nh3_analyzer          int4,
    nh3_analyzer_dp       int2,
    nh3_remarks           text,
    uv_manual             numeric(8, 5),
    uv_manual_dp          int2,
    uv_analyzer           int4,
    uv_analyzer_dp        int2,
    uv_remarks            text,
    dwd_update_time timestamp(6) default current_timestamp,
    dwd_load_time timestamp(6) default current_timestamp,
    constraint dwd_wtw_verification_item_di_year_pkey primary key (verification_item_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
partition by range (sample_date)
(
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

comment on table coss_dwd.dwd_wtw_verification_item_di_year is 'Table To Store The Sample Items In The Online Analyzer Verification Results';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.verification_item_id is 'ID Of Each Record Item';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.verification_id is 'ID Of The Corresponding Record';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_id is 'ID Of The Sampling Location';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_full_name is 'Location Full Name (Including Suffices). This Field Can Also Be Used For Translation In UI And Labeling In Reports.';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_name is 'Name Of The Location';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_suffix is 'Suffix Of The Location';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_name_chi is 'Name Of The Location In Chinese (For Reporting)';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.sample_date is 'Datetime When The Sample Is Taken';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_manual is 'Sample Value Of pH From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_analyzer is 'Sample Value Of pH From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_remarks is 'Remarks On The pH Sample';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_manual is 'Sample Value Of Turbidity From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_analyzer is 'Sample Value Of Turbidity From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_remarks is 'Remarks On The Turbidity Sample';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_manual is 'Sample Value Of Residual Chlorine From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_analyzer is 'Sample Value Of Residual Chlorine From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_remarks is 'Remarks On The Sample Of Residual Chlorine';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_manual is 'Sample Value Of Fluoride From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_analyzer is 'Sample Value Of Fluoride From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_remarks is 'Remarks On The Sample Of Fluoride';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_manual is 'Sample Value Of Mangenese From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_analyzer is 'Sample Value Of Mangenese From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_remarks is 'Remarks On The Sample Of Mangenese';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_manual is 'Sample Value Of Ammonia From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_analyzer is 'Sample Value Of Ammonia From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_remarks is 'Remarks On The Sample Of Ammonia';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_manual is 'Sample Value Of UV Light From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_analyzer is 'Sample Value Of UV Light From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_remarks is 'Remarks On The Sample Of UV Light';
```



```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year
-- coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df
-- coss_ods.ods_labconnect_wtw_wqmm_location_df
-- target table
-- coss_dwd.dwd_wtw_verification_item_di_year
-- ****************************************************************************************
insert into coss_dwd.dwd_wtw_verification_item_di_year
select
    t1.verification_item_id,      -- ID Of Each Record Item
    t1.verification_id,           -- ID Of The Corresponding Record
    t1.loc_id,                    -- ID Of The Sampling Location
    t2.loc_full_name,             -- Location Full Name (Including Suffices). This Field Can Also Be Used For Translation In UI And Labeling In Reports.
    t2.loc_name,                  -- Name Of The Location
    t2.loc_suffix,                -- Suffix Of The Location
    t2.loc_name_chi,              -- Name Of The Location In Chinese (For Reporting)
    t.sample_date,                -- Datetime When The Sample Is Taken
    t1.ph_manual,                 -- Sample Value Of pH From Manual Test
    t1.ph_manual_dp,              -- No. Of Decimal Places Required For The Value From Manual Test
    t1.ph_analyzer,               -- Sample Value Of pH From Online Analyzer
    t1.ph_analyzer_dp,            -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.ph_remarks,                -- Remarks On The pH Sample
    t1.turb_manual,               -- Sample Value Of Turbidity From Manual Test
    t1.turb_manual_dp,            -- No. Of Decimal Places Required For The Value From Manual Test
    t1.turb_analyzer,             -- Sample Value Of Turbidity From Online Analyzer
    t1.turb_analyzer_dp,          -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.turb_remarks,              -- Remarks On The Turbidity Sample
    t1.rcl2_manual,               -- Sample Value Of Residual Chlorine From Manual Test
    t1.rcl2_manual_dp,            -- No. Of Decimal Places Required For The Value From Manual Test
    t1.rcl2_analyzer,             -- Sample Value Of Residual Chlorine From Online Analyzer
    t1.rcl2_analyzer_dp,          -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.rcl2_remarks,              -- Remarks On The Sample Of Residual Chlorine
    t1.fluoride_manual,           -- Sample Value Of Fluoride From Manual Test
    t1.fluoride_manual_dp,        -- No. Of Decimal Places Required For The Value From Manual Test
    t1.fluoride_analyzer,         -- Sample Value Of Fluoride From Online Analyzer
    t1.fluoride_analyzer_dp,      -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.fluoride_remarks,          -- Remarks On The Sample Of Fluoride
    t1.mn_manual,                 -- Sample Value Of Mangenese From Manual Test
    t1.mn_manual_dp,              -- No. Of Decimal Places Required For The Value From Manual Test
    t1.mn_analyzer,               -- Sample Value Of Mangenese From Online Analyzer
    t1.mn_analyzer_dp,            -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.mn_remarks,                -- Remarks On The Sample Of Mangenese
    t1.nh3_manual,                -- Sample Value Of Ammonia From Manual Test
    t1.nh3_manual_dp,             -- No. Of Decimal Places Required For The Value From Manual Test
    t1.nh3_analyzer,              -- Sample Value Of Ammonia From Online Analyzer
    t1.nh3_analyzer_dp,           -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.nh3_remarks,               -- Remarks On The Sample Of Ammonia
    t1.uv_manual,                 -- Sample Value Of UV Light From Manual Test
    t1.uv_manual_dp,              -- No. Of Decimal Places Required For The Value From Manual Test
    t1.uv_analyzer,               -- Sample Value Of UV Light From Online Analyzer
    t1.uv_analyzer_dp,            -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.uv_remarks,                -- Remarks On The Sample Of UV Light
    current_timestamp as dwd_update_time,  -- DWD Layer Record Update Time
    current_timestamp as dwd_load_time     -- DWD Layer Record Load Time
from
    coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year t
    inner join coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df t1 
        on t.verification_id = t1.verification_id
    inner join coss_ods.ods_labconnect_wtw_wqmm_location_df t2 
        on t1.loc_id = t2.loc_id
where t.ods_update_time >= '${dwd_update_time}' 
  and t1.ods_update_time >= '${dwd_update_time}'
on duplicate key update
    verification_id = values(verification_id),
    loc_id = values(loc_id),
    loc_full_name = values(loc_full_name),
    loc_name = values(loc_name),
    loc_suffix = values(loc_suffix),
    loc_name_chi = values(loc_name_chi),
    sample_date = values(sample_date),
    ph_manual = values(ph_manual),
    ph_manual_dp = values(ph_manual_dp),
    ph_analyzer = values(ph_analyzer),
    ph_analyzer_dp = values(ph_analyzer_dp),
    ph_remarks = values(ph_remarks),
    turb_manual = values(turb_manual),
    turb_manual_dp = values(turb_manual_dp),
    turb_analyzer = values(turb_analyzer),
    turb_analyzer_dp = values(turb_analyzer_dp),
    turb_remarks = values(turb_remarks),
    rcl2_manual = values(rcl2_manual),
    rcl2_manual_dp = values(rcl2_manual_dp),
    rcl2_analyzer = values(rcl2_analyzer),
    rcl2_analyzer_dp = values(rcl2_analyzer_dp),
    rcl2_remarks = values(rcl2_remarks),
    fluoride_manual = values(fluoride_manual),
    fluoride_manual_dp = values(fluoride_manual_dp),
    fluoride_analyzer = values(fluoride_analyzer),
    fluoride_analyzer_dp = values(fluoride_analyzer_dp),
    fluoride_remarks = values(fluoride_remarks),
    mn_manual = values(mn_manual),
    mn_manual_dp = values(mn_manual_dp),
    mn_analyzer = values(mn_analyzer),
    mn_analyzer_dp = values(mn_analyzer_dp),
    mn_remarks = values(mn_remarks),
    nh3_manual = values(nh3_manual),
    nh3_manual_dp = values(nh3_manual_dp),
    nh3_analyzer = values(nh3_analyzer),
    nh3_analyzer_dp = values(nh3_analyzer_dp),
    nh3_remarks = values(nh3_remarks),
    uv_manual = values(uv_manual),
    uv_manual_dp = values(uv_manual_dp),
    uv_analyzer = values(uv_analyzer),
    uv_analyzer_dp = values(uv_analyzer_dp),
    uv_remarks = values(uv_remarks),
    dwd_update_time = values(dwd_update_time)
```

# dws

## 1.coss_dws.dws_wtw_verification_item_di_year

```sql
drop table if exists coss_dws.dws_wtw_verification_item_di_year;
create table if not exists coss_dws.dws_wtw_verification_item_di_year(
    verification_id          int4,
    wtw_id                   int4,
    status                   int2,
    last_updated_date        timestamp,
    sample_date              timestamp,
    reviewed_date            timestamp,
    wtw_code                 text,
    wtw_name                 text,
    wtw_name_chi             text,
    phase_1                  bool,
    phase_2                  bool,
    phase_3                  bool,
    verification_item_id     int4,
    loc_id                   int4,
    loc_full_name            text,
    loc_name                 text,
    loc_suffix               text,
    loc_name_chi             text,
    ph_manual                numeric(8, 5),
    ph_manual_dp             int2,
    ph_analyzer              numeric(8, 5),
    ph_analyzer_dp           int2,
    ph_remarks               text,
    turb_manual              numeric(8, 5),
    turb_manual_dp           int2,
    turb_analyzer            numeric(8, 5),
    turb_analyzer_dp         int2,
    turb_remarks             text,
    rcl2_manual              numeric(8, 5),
    rcl2_manual_dp           int2,
    rcl2_analyzer            numeric(8, 5),
    rcl2_analyzer_dp         int2,
    rcl2_remarks             text,
    fluoride_manual          numeric(8, 5),
    fluoride_manual_dp       int2,
    fluoride_analyzer        numeric(8, 5),
    fluoride_analyzer_dp     int2,
    fluoride_remarks         text,
    mn_manual                numeric(8, 5),
    mn_manual_dp             int2,
    mn_analyzer              numeric(8, 5),
    mn_analyzer_dp           int2,
    mn_remarks               text,
    nh3_manual               numeric(8, 5),
    nh3_manual_dp            int2,
    nh3_analyzer             int4,
    nh3_analyzer_dp          int2,
    nh3_remarks              text,
    uv_manual                numeric(8, 5),
    uv_manual_dp             int2,
    uv_analyzer              int4,
    uv_analyzer_dp           int2,
    uv_remarks               text,
    dws_update_time timestamp(6) default current_timestamp,
    dws_load_time timestamp(6) default current_timestamp,
    constraint dws_wtw_verification_item_di_year_pkey primary key (verification_item_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
partition by range (sample_date)
(
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

comment on table coss_dws.dws_wtw_verification_item_di_year is 'Table To Store The Sample Items In The Online Analyzer Verification Results';
comment on column coss_dws.dws_wtw_verification_item_di_year.verification_id is 'ID Of Each Online Analyzer Verification Record';
comment on column coss_dws.dws_wtw_verification_item_di_year.wtw_id is 'ID Of The Corresponding WTW';
comment on column coss_dws.dws_wtw_verification_item_di_year.status is 'Status Of The Reminder:0: Reported And Not Yet Approved ;1: Approved And Require Acknowledged.;2: Approved/Acknowledged And Not Yet Reviewed;3: Reviewed;-1: Rejected';
comment on column coss_dws.dws_wtw_verification_item_di_year.last_updated_date is 'Datetime When The Record Is Updated';
comment on column coss_dws.dws_wtw_verification_item_di_year.sample_date is 'Datetime When The Sample Is Taken';
comment on column coss_dws.dws_wtw_verification_item_di_year.reviewed_date is 'Datetime When The Sample Record Is Reviewed';
comment on column coss_dws.dws_wtw_verification_item_di_year.wtw_code is 'WTW Code';
comment on column coss_dws.dws_wtw_verification_item_di_year.wtw_name is 'WTW English Name (For Phase 1 & 3 Reporting)';
comment on column coss_dws.dws_wtw_verification_item_di_year.wtw_name_chi is 'WTW Chinese Name (For Phase 2 Reporting)';
comment on column coss_dws.dws_wtw_verification_item_di_year.phase_1 is 'True: WTW Has Joined Phase 1, Which Should Show Up In Phase 1 Site.False: WTW Should Not Show Up In Phase 1 Site';
comment on column coss_dws.dws_wtw_verification_item_di_year.phase_2 is 'True: WTW Has Joined Phase 2, Which Should Show Up In Phase 2 Site.False: WTW Should Not Show Up In Phase 2 Site';
comment on column coss_dws.dws_wtw_verification_item_di_year.phase_3 is 'True: WTW Has Joined Phase 3, Which Should Show Up In Phase 3 Site.False: WTW Should Not Show Up In Phase 3 Site';
comment on column coss_dws.dws_wtw_verification_item_di_year.verification_item_id is 'ID Of Each Record Item';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_id is 'ID Of The Sampling Location';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_full_name is 'Location Full Name (Including Suffices). This Field Can Also Be Used For Translation In UI And Labeling In Reports.';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_name is 'Name Of The Location';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_suffix is 'Suffix Of The Location';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_name_chi is 'Name Of The Location In Chinese (For Reporting)';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_manual is 'Sample Value Of pH From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_analyzer is 'Sample Value Of pH From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_remarks is 'Remarks On The pH Sample';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_manual is 'Sample Value Of Turbidity From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_analyzer is 'Sample Value Of Turbidity From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_remarks is 'Remarks On The Turbidity Sample';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_manual is 'Sample Value Of Residual Chlorine From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_analyzer is 'Sample Value Of Residual Chlorine From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_remarks is 'Remarks On The Sample Of Residual Chlorine';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_manual is 'Sample Value Of Fluoride From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_analyzer is 'Sample Value Of Fluoride From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_remarks is 'Remarks On The Sample Of Fluoride';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_manual is 'Sample Value Of Mangenese From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_analyzer is 'Sample Value Of Mangenese From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_remarks is 'Remarks On The Sample Of Mangenese';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_manual is 'Sample Value Of Ammonia From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_analyzer is 'Sample Value Of Ammonia From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_remarks is 'Remarks On The Sample Of Ammonia';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_manual is 'Sample Value Of UV Light From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_manual_dp is 'No. Of Decimal Places Required For The Value From Manual Test';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_analyzer is 'Sample Value Of UV Light From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_analyzer_dp is 'No. Of Decimal Places Required For The Value From Online Analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_remarks is 'Remarks On The Sample Of UV Light';
```



```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dwd_wtw_verification_di_year
-- coss_dwd.dwd_wtw_verification_item_di_year
-- target table
-- coss_dws.dws_wtw_verification_item_di_year
-- ****************************************************************************************
insert into coss_dws.dws_wtw_verification_item_di_year
select
    t.verification_id,               -- ID Of Each Online Analyzer Verification Record
    t.wtw_id,                        -- ID Of The Corresponding WTW
    t.status,                        -- Status Of The Reminder:0: Reported And Not Yet Approved ;1: Approved And Require Acknowledged.;2: Approved/Acknowledged And Not Yet Reviewed;3: Reviewed;-1: Rejected
    t.last_updated_date,             -- Datetime When The Record Is Updated
    t.sample_date,                   -- Datetime When The Sample Is Taken
    t.reviewed_date,                 -- Datetime When The Sample Record Is Reviewed
    t.wtw_code,                      -- WTW Code
    t.wtw_name,                      -- WTW English Name (For Phase 1 & 3 Reporting)
    t.wtw_name_chi,                  -- WTW Chinese Name (For Phase 2 Reporting)
    t.phase_1,                       -- True: WTW Has Joined Phase 1, Which Should Show Up In Phase 1 Site.False: WTW Should Not Show Up In Phase 1 Site
    t.phase_2,                       -- True: WTW Has Joined Phase 2, Which Should Show Up In Phase 2 Site.False: WTW Should Not Show Up In Phase 2 Site
    t.phase_3,                       -- True: WTW Has Joined Phase 3, Which Should Show Up In Phase 3 Site.False: WTW Should Not Show Up In Phase 3 Site
    t1.verification_item_id,         -- ID Of Each Record Item
    t1.loc_id,                       -- ID Of The Sampling Location
    t1.loc_full_name,                -- Location Full Name (Including Suffices). This Field Can Also Be Used For Translation In UI And Labeling In Reports.
    t1.loc_name,                     -- Name Of The Location
    t1.loc_suffix,                   -- Suffix Of The Location
    t1.loc_name_chi,                 -- Name Of The Location In Chinese (For Reporting)
    t1.ph_manual,                    -- Sample Value Of pH From Manual Test
    t1.ph_manual_dp,                 -- No. Of Decimal Places Required For The Value From Manual Test
    t1.ph_analyzer,                  -- Sample Value Of pH From Online Analyzer
    t1.ph_analyzer_dp,               -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.ph_remarks,                   -- Remarks On The pH Sample
    t1.turb_manual,                  -- Sample Value Of Turbidity From Manual Test
    t1.turb_manual_dp,               -- No. Of Decimal Places Required For The Value From Manual Test
    t1.turb_analyzer,                -- Sample Value Of Turbidity From Online Analyzer
    t1.turb_analyzer_dp,             -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.turb_remarks,                 -- Remarks On The Turbidity Sample
    t1.rcl2_manual,                  -- Sample Value Of Residual Chlorine From Manual Test
    t1.rcl2_manual_dp,               -- No. Of Decimal Places Required For The Value From Manual Test
    t1.rcl2_analyzer,                -- Sample Value Of Residual Chlorine From Online Analyzer
    t1.rcl2_analyzer_dp,             -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.rcl2_remarks,                 -- Remarks On The Sample Of Residual Chlorine
    t1.fluoride_manual,              -- Sample Value Of Fluoride From Manual Test
    t1.fluoride_manual_dp,           -- No. Of Decimal Places Required For The Value From Manual Test
    t1.fluoride_analyzer,            -- Sample Value Of Fluoride From Online Analyzer
    t1.fluoride_analyzer_dp,         -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.fluoride_remarks,             -- Remarks On The Sample Of Fluoride
    t1.mn_manual,                    -- Sample Value Of Mangenese From Manual Test
    t1.mn_manual_dp,                 -- No. Of Decimal Places Required For The Value From Manual Test
    t1.mn_analyzer,                  -- Sample Value Of Mangenese From Online Analyzer
    t1.mn_analyzer_dp,               -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.mn_remarks,                   -- Remarks On The Sample Of Mangenese
    t1.nh3_manual,                   -- Sample Value Of Ammonia From Manual Test
    t1.nh3_manual_dp,                -- No. Of Decimal Places Required For The Value From Manual Test
    t1.nh3_analyzer,                 -- Sample Value Of Ammonia From Online Analyzer
    t1.nh3_analyzer_dp,              -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.nh3_remarks,                  -- Remarks On The Sample Of Ammonia
    t1.uv_manual,                    -- Sample Value Of UV Light From Manual Test
    t1.uv_manual_dp,                 -- No. Of Decimal Places Required For The Value From Manual Test
    t1.uv_analyzer,                  -- Sample Value Of UV Light From Online Analyzer
    t1.uv_analyzer_dp,               -- No. Of Decimal Places Required For The Value From Online Analyzer
    t1.uv_remarks,                   -- Remarks On The Sample Of UV Light
    current_timestamp as dws_update_time,
    current_timestamp as dws_load_time
from 
    coss_dwd.dwd_wtw_verification_di_year t
    inner join coss_dwd.dwd_wtw_verification_item_di_year t1 
        on t.verification_id = t1.verification_id
where t.dwd_update_time >= '${dws_update_time}' 
  and t1.dwd_update_time >= '${dws_update_time}'
on duplicate key update
    verification_id = values(verification_id),
    wtw_id = values(wtw_id),
    status = values(status),
    last_updated_date = values(last_updated_date),
    sample_date = values(sample_date),
    reviewed_date = values(reviewed_date),
    wtw_code = values(wtw_code),
    wtw_name = values(wtw_name),
    wtw_name_chi = values(wtw_name_chi),
    phase_1 = values(phase_1),
    phase_2 = values(phase_2),
    phase_3 = values(phase_3),
    loc_id = values(loc_id),
    loc_full_name = values(loc_full_name),
    loc_name = values(loc_name),
    loc_suffix = values(loc_suffix),
    loc_name_chi = values(loc_name_chi),
    ph_manual = values(ph_manual),
    ph_manual_dp = values(ph_manual_dp),
    ph_analyzer = values(ph_analyzer),
    ph_analyzer_dp = values(ph_analyzer_dp),
    ph_remarks = values(ph_remarks),
    turb_manual = values(turb_manual),
    turb_manual_dp = values(turb_manual_dp),
    turb_analyzer = values(turb_analyzer),
    turb_analyzer_dp = values(turb_analyzer_dp),
    turb_remarks = values(turb_remarks),
    rcl2_manual = values(rcl2_manual),
    rcl2_manual_dp = values(rcl2_manual_dp),
    rcl2_analyzer = values(rcl2_analyzer),
    rcl2_analyzer_dp = values(rcl2_analyzer_dp),
    rcl2_remarks = values(rcl2_remarks),
    fluoride_manual = values(fluoride_manual),
    fluoride_manual_dp = values(fluoride_manual_dp),
    fluoride_analyzer = values(fluoride_analyzer),
    fluoride_analyzer_dp = values(fluoride_analyzer_dp),
    fluoride_remarks = values(fluoride_remarks),
    mn_manual = values(mn_manual),
    mn_manual_dp = values(mn_manual_dp),
    mn_analyzer = values(mn_analyzer),
    mn_analyzer_dp = values(mn_analyzer_dp),
    mn_remarks = values(mn_remarks),
    nh3_manual = values(nh3_manual),
    nh3_manual_dp = values(nh3_manual_dp),
    nh3_analyzer = values(nh3_analyzer),
    nh3_analyzer_dp = values(nh3_analyzer_dp),
    nh3_remarks = values(nh3_remarks),
    uv_manual = values(uv_manual),
    uv_manual_dp = values(uv_manual_dp),
    uv_analyzer = values(uv_analyzer),
    uv_analyzer_dp = values(uv_analyzer_dp),
    uv_remarks = values(uv_remarks),
    dws_update_time = values(dws_update_time)
```



# dim

## coss_dim.dim_wtw_water_quality_parameters

```sql
drop table if exists coss_dim.dim_wtw_water_quality_parameters;
create table if not exists coss_dim.dim_wtw_water_quality_parameters(
    config_id                     serial4,
    wtw_id                        int4,
    i_code                        varchar(255),
    config_type                   int2,
    created_date                  timestamp,
    verification_interval_hr      int2,
    jar_test_interval_hr          int2,
    jar_measure_type              int2,
    require_to_test               bool,
    parameter_limit_id            int4,
    loc_id                        int4,
    target_type                   int2,
    ph_compare                    text,
    ph_min_value                  numeric(8, 5),
    ph_min_val_dp                 int4,
    ph_max_value                  numeric(8, 5),
    ph_max_val_dp                 int4,
    turb_compare                  text,
    turb_min_value                numeric(8, 5),
    turb_min_val_dp               int4,
    turb_max_value                numeric(8, 5),
    turb_max_val_dp               int4,
    rcl2_compare                  text,
    rcl2_min_value                numeric(8, 5),
    rcl2_min_val_dp               int4,
    rcl2_max_value                numeric(8, 5),
    rcl2_max_val_dp               int4,
    uv_compare                    text,
    uv_min_value                  numeric(8, 5),
    uv_min_val_dp                 int4,
    uv_max_value                  numeric(8, 5),
    uv_max_val_dp                 int4,
    fluoride_compare              text,
    fluoride_min_value            numeric(8, 5),
    fluoride_min_val_dp           int4,
    fluoride_max_value            numeric(8, 5),
    fluoride_max_val_dp           int4,
    mn_compare                    text,
    mn_min_value                  numeric(8, 5),
    mn_min_val_dp                 int4,
    mn_max_value                  numeric(8, 5),
    mn_max_val_dp                 int4,
    nh3_compare                   text,
    nh3_min_value                 numeric(8, 5),
    nh3_min_val_dp                int4,
    nh3_max_value                 numeric(8, 5),
    nh3_max_val_dp                int4,
    loc_full_name                 text,
    loc_name                      text,
    loc_suffix                    text,
    loc_name_chi                  text,
    dim_update_time timestamp(6) default current_timestamp,
    dim_load_time timestamp(6) default current_timestamp,
    primary key (parameter_limit_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);
comment on table coss_dim.dim_wtw_water_quality_parameters is 'Table To Store All The Operational Targets And Critical Limits For Water Quality Monitoring';
comment on column coss_dim.dim_wtw_water_quality_parameters.config_id is 'ID Of Each Parameter Set';
comment on column coss_dim.dim_wtw_water_quality_parameters.wtw_id is 'ID Of The Corresponding WTW';
comment on column coss_dim.dim_wtw_water_quality_parameters.i_code is 'Installations Code';
comment on column coss_dim.dim_wtw_water_quality_parameters.config_type is 'Configuration Type 0: Parameters For Water Quality Monitoring; 1: Parameters For Online Analyzer Verification; 2: Sampling Frequency';
comment on column coss_dim.dim_wtw_water_quality_parameters.created_date is 'Datetime When The Record Is Created';
comment on column coss_dim.dim_wtw_water_quality_parameters.verification_interval_hr is 'This Field Only Has Meaning If Config_Type = 2.The Interval (Hrs) In Which The Online Analyzer Verification Test Is Performed. If This Field Is Empty, No Online Analyzer Verification Test Is Required For The Specific WTW.';
comment on column coss_dim.dim_wtw_water_quality_parameters.jar_test_interval_hr is 'This Field Only Has Meaning If Config_Type = 2.The Interval (Hrs) In Which The Jar Test Is Performed. If This Field Is Empty, No Jar Test Is Required For The Specific WTW.';
comment on column coss_dim.dim_wtw_water_quality_parameters.jar_measure_type is '(If Config_Type <> 2, Use Default Value 0) 0: The Jar Test Measurement Is "絮凝大小"; 1: The Jar Test Measurement Is "沉澱速度"';
comment on column coss_dim.dim_wtw_water_quality_parameters.require_to_test is '(If Config_Type <> 2, Use Default Value False)True: Perform Taste & Odour Test;False: No Need To Perform Taste & Odour Test';
comment on column coss_dim.dim_wtw_water_quality_parameters.parameter_limit_id is 'ID Of Each Item In The Parameters';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_id is 'ID Of The Corresponding Sampling Location';
comment on column coss_dim.dim_wtw_water_quality_parameters.target_type is 'Target Type: 0: Operational Target; 1: Critical Limit';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_compare is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_min_value is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_max_value is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_compare is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_min_value is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_max_value is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_compare is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_min_value is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_max_value is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_compare is 'Define Whether UV Light Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_min_value is 'Define Whether UV Light Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_max_value is 'Define Whether UV Light Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_compare is 'Define Whether Fluoride Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_min_value is 'Define Whether Fluoride Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_max_value is 'Define Whether Fluoride Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_compare is 'Define Whether Manganese Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_min_value is 'Define Whether Manganese Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_max_value is 'Define Whether Manganese Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_compare is 'Define Whether Ammonia Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_min_value is 'Define Whether Ammonia Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_min_val_dp is 'No. Of Decimal Places For Min Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_max_value is 'Define Whether Ammonia Is Acceptable Or Not';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_max_val_dp is 'No. Of Decimal Places For Max Value,-1: If The Value Is Null';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_full_name is 'Location Full Name (Including Suffices). This Field Can Also Be Used For Translation In UI And Labeling In Reports.';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_name is 'Name Of The Location';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_suffix is 'Suffix Of The Location';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_name_chi is 'Name Of The Location In Chinese (For Reporting)';
```



```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_ods.ods_labconnect_wtw_wqmm_config_df
-- coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df
-- coss_ods.ods_labconnect_wtw_wqmm_location_df
-- target table
-- coss_dim.dim_wtw_water_quality_parameters
-- ****************************************************************************************
insert into coss_dim.dim_wtw_water_quality_parameters
select
    t.config_id,                              -- ID Of Each Parameter Set
    t.wtw_id,                                 -- ID Of The Corresponding WTW
    case
        when wtw_id = 1 then 'TW025'
        when wtw_id = 2 then 'TW009'
        when wtw_id = 3 then 'TW015'
        when wtw_id = 4 then 'TW019'
        when wtw_id = 5 then 'TW011'
        else '10000'
    end as i_code,                            -- Installations Code
    t.config_type,                            -- Configuration Type 0: Parameters For Water Quality Monitoring; 1: Parameters For Online Analyzer Verification; 2: Sampling Frequency
    t.effective_date,                         -- Datetime When The Record Is Created
    t.verification_interval_hr,               -- This Field Only Has Meaning If Config_Type = 2.The Interval (Hrs) In Which The Online Analyzer Verification Test Is Performed. If This Field Is Empty, No Online Analyzer Verification Test Is Required For The Specific WTW.
    t.jar_test_interval_hr,                   -- This Field Only Has Meaning If Config_Type = 2.The Interval (Hrs) In Which The Jar Test Is Performed. If This Field Is Empty, No Jar Test Is Required For The Specific WTW.
    t.jar_measure_type,                       -- (If Config_Type <> 2, Use Default Value 0) 0: The Jar Test Measurement Is "絮凝大小"; 1: The Jar Test Measurement Is "沉澱速度"
    t.require_to_test,                        -- (If Config_Type <> 2, Use Default Value False)True: Perform Taste & Odour Test;False: No Need To Perform Taste & Odour Test
    t1.parameter_limit_id,                    -- ID Of Each Item In The Parameters
    t1.loc_id,                                -- ID Of The Corresponding Sampling Location
    t1.target_type,                           -- Target Type: 0: Operational Target; 1: Critical Limit
    t1.ph_compare,                            -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value,                          -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_val_dp,                         -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    t1.ph_max_value,                          -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_val_dp,                         -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    t1.turb_compare,                          -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value,                        -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_val_dp,                       -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    t1.turb_max_value,                        -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_val_dp,                       -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    t1.rcl2_compare,                          -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value,                        -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_val_dp,                       -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    t1.rcl2_max_value,                        -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_val_dp,                       -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    t1.uv_compare,                            -- Define Whether UV Light Is Acceptable Or Not
    t1.uv_min_value,                          -- Define Whether UV Light Is Acceptable Or Not
    t1.uv_min_val_dp,                         -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    t1.uv_max_value,                          -- Define Whether UV Light Is Acceptable Or Not
    t1.uv_max_val_dp,                         -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    t1.fluoride_compare,                      -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_min_value,                    -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_min_val_dp,                   -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    t1.fluoride_max_value,                    -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_max_val_dp,                   -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    t1.mn_compare,                            -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_min_value,                          -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_min_val_dp,                         -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    t1.mn_max_value,                          -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_max_val_dp,                         -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    t1.nh3_compare,                           -- Define Whether Ammonia Is Acceptable Or Not
    t1.nh3_min_value,                         -- Define Whether Ammonia Is Acceptable Or Not
    t1.nh3_min_val_dp,                        -- No. Of Decimal Places For Min Value,-1: If The Value Is Null
    t1.nh3_max_value,                         -- Define Whether Ammonia Is Acceptable Or Not
    t1.nh3_max_val_dp,                        -- No. Of Decimal Places For Max Value,-1: If The Value Is Null
    t2.loc_full_name,                         -- Location Full Name (Including Suffices). This Field Can Also Be Used For Translation In UI And Labeling In Reports.
    t2.loc_name,                              -- Name Of The Location
    t2.loc_suffix,                            -- Suffix Of The Location
    t2.loc_name_chi,                          -- Name Of The Location In Chinese (For Reporting)
    current_timestamp as dim_update_time,
    current_timestamp as dim_load_time
from
    coss_ods.ods_labconnect_wtw_wqmm_config_df t
    inner join coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df t1 
        on t.config_id = t1.config_id
    inner join coss_ods.ods_labconnect_wtw_wqmm_location_df t2 
        on t1.loc_id = t2.loc_id
on duplicate key update
    config_id = values(config_id),
    wtw_id = values(wtw_id),
    i_code = values(i_code),
    config_type = values(config_type),
    created_date = values(created_date),
    verification_interval_hr = values(verification_interval_hr),
    jar_test_interval_hr = values(jar_test_interval_hr),
    jar_measure_type = values(jar_measure_type),
    require_to_test = values(require_to_test),
    loc_id = values(loc_id),
    target_type = values(target_type),
    ph_compare = values(ph_compare),
    ph_min_value = values(ph_min_value),
    ph_min_val_dp = values(ph_min_val_dp),
    ph_max_value = values(ph_max_value),
    ph_max_val_dp = values(ph_max_val_dp),
    turb_compare = values(turb_compare),
    turb_min_value = values(turb_min_value),
    turb_min_val_dp = values(turb_min_val_dp),
    turb_max_value = values(turb_max_value),
    turb_max_val_dp = values(turb_max_val_dp),
    rcl2_compare = values(rcl2_compare),
    rcl2_min_value = values(rcl2_min_value),
    rcl2_min_val_dp = values(rcl2_min_val_dp),
    rcl2_max_value = values(rcl2_max_value),
    rcl2_max_val_dp = values(rcl2_max_val_dp),
    uv_compare = values(uv_compare),
    uv_min_value = values(uv_min_value),
    uv_min_val_dp = values(uv_min_val_dp),
    uv_max_value = values(uv_max_value),
    uv_max_val_dp = values(uv_max_val_dp),
    fluoride_compare = values(fluoride_compare),
    fluoride_min_value = values(fluoride_min_value),
    fluoride_min_val_dp = values(fluoride_min_val_dp),
    fluoride_max_value = values(fluoride_max_value),
    fluoride_max_val_dp = values(fluoride_max_val_dp),
    mn_compare = values(mn_compare),
    mn_min_value = values(mn_min_value),
    mn_min_val_dp = values(mn_min_val_dp),
    mn_max_value = values(mn_max_value),
    mn_max_val_dp = values(mn_max_val_dp),
    nh3_compare = values(nh3_compare),
    nh3_min_value = values(nh3_min_value),
    nh3_min_val_dp = values(nh3_min_val_dp),
    nh3_max_value = values(nh3_max_value),
    nh3_max_val_dp = values(nh3_max_val_dp),
    loc_full_name = values(loc_full_name),
    loc_name = values(loc_name),
    loc_suffix = values(loc_suffix),
    loc_name_chi = values(loc_name_chi),
    dim_update_time = values(dim_update_time)
```

## coss_dim.dim_ass_wtw_info[unbelong to]

```sql
DROP TABLE if exists  coss_dim.dim_ass_wtw_info;
CREATE TABLE if not exists  coss_dim.dim_ass_wtw_info (
	tw_id varchar(20) NOT NULL, -- Water Treatment Woks ID with format TWNNNNNNNN
	i_code varchar(10) NULL, -- Installation Code of Water Treatment Works
	tw_name_en varchar(200) NULL, -- Water Treatment Works Name
	tw_name_tc varchar(300) NULL, -- Water Treatment Works Chinese Name
	tw_name_cn varchar(300) NULL, -- Water Treatment Works Traditional Chinese Name
	rpt_label varchar(400) NULL, -- Labels used in reports
	region_code varchar NULL, -- Region
	region_ind varchar(2) NULL, -- Possible Values: {"I" - HK Island, "M" - Mainland}
	capacity numeric(12, 4) NULL, -- Capacity of WTW.  Unit is in Mld
	dim_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	dim_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time
	CONSTRAINT dim_ass_wtw_info_pkey PRIMARY KEY (tw_id)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dim.dim_ass_wtw_info IS 'Water Treatment Works Information';

-- Column comments

COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.tw_id IS 'Water Treatment Woks ID with format TWNNNNNNNN';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.i_code IS 'Installation Code of Water Treatment Works';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.tw_name_en IS 'Water Treatment Works Name';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.tw_name_tc IS 'Water Treatment Works Chinese Name';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.tw_name_cn IS 'Water Treatment Works Traditional Chinese Name';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.rpt_label IS 'Labels used in reports';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.region_code IS 'Region';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.region_ind IS 'Possible Values: {"I" - HK Island, "M" - Mainland}';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.capacity IS 'Capacity of WTW.  Unit is in Mld';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.dim_update_time IS 'Data Update Time';
COMMENT ON COLUMN coss_dim.dim_ass_wtw_info.dim_load_time IS 'Data Loading Time';


```



# dm

## 原水水质

### wtw_id = 1

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,if((if(t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0))=2, 1, 0) raw_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value 
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =1
    and loc_id = 0
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 1 and loc_id =0
    and parameter_limit_id = 19
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```



### wtw_id=2

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,if((if(t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0))=2, 1, 0) raw_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value 
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =2
    and loc_id = 0
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 2 
    and loc_id =0
    and parameter_limit_id = 35
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id

```

### wtw_id=3

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,if((if(t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0))=2, 1, 0) raw_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value 	
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =3
    and loc_id = 0
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 3 
    and loc_id =0
    and parameter_limit_id = 9
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id

```

### wtw_id=4

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,if((if(t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0))=2, 1, 0) raw_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value 
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =4
    and loc_id = 0
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 4 
    and loc_id =0
    and parameter_limit_id = 1
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id


```

### wtw_id=5

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,if((if(t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0))=2, 1, 0) raw_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value 	
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,0 as loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =5
    and loc_id in(1,2)
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 5
    and loc_id  = 0
    and parameter_limit_id = 45
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```

### coss_dm.dm_wtw_raw_water_quality_di

```sql
drop table if exists coss_dm.dm_wtw_raw_water_quality_di;

create table if not exists coss_dm.dm_wtw_raw_water_quality_di(
    wtw_id           int4,               -- ID Of The Corresponding WTW
    loc_id           int4,               -- ID Of The Sampling Location
    i_code           varchar(255),       -- Installations Code
    sample_date      timestamp,          -- Datetime When The Sample Is Taken
    ph_manual        numeric(8, 5),      -- Sample Value Of pH From Manual Test
    ph_analyzer      numeric(8, 5),      -- Sample Value Of pH From Online Analyzer
    ph_is_pass       int4,               -- pH Is Pass
    turb_manual      numeric(8, 5),      -- Sample Value Of Turbidity From Manual Test
    turb_analyzer    numeric(8, 5),      -- Sample Value Of Turbidity From Online Analyzer
    turb_is_pass     int4,               -- Turb Is Pass
    raw_is_pass      int4,               -- Raw Water Is Pass
    ph_compare       text,               -- Define Whether pH Value Is Acceptable Or Not
    ph_min_value     numeric(8, 5),      -- Define Whether pH Value Is Acceptable Or Not
    ph_max_value     numeric(8, 5),      -- Define Whether pH Value Is Acceptable Or Not
    turb_compare     text,               -- Define Whether Turbidity Value Is Acceptable Or Not
    turb_min_value   numeric(8, 5),      -- Define Whether Turbidity Value Is Acceptable Or Not
    turb_max_value   numeric(8, 5),      -- Define Whether Turbidity Value Is Acceptable Or Not
    dm_update_time timestamp(6) default current_timestamp,
    dm_load_time timestamp(6) default current_timestamp,
    constraint dm_wtw_raw_water_quality_di_pkey primary key (i_code, loc_id, sample_date)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_dm.dm_wtw_raw_water_quality_di is 'WTW Raw Water Quality';
comment on column coss_dm.dm_wtw_raw_water_quality_di.wtw_id is 'ID Of The Corresponding WTW';
comment on column coss_dm.dm_wtw_raw_water_quality_di.loc_id is 'ID Of The Sampling Location';
comment on column coss_dm.dm_wtw_raw_water_quality_di.i_code is 'Installations Code';
comment on column coss_dm.dm_wtw_raw_water_quality_di.sample_date is 'Datetime When The Sample Is Taken';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_manual is 'Sample Value Of pH From Manual Test';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_analyzer is 'Sample Value Of pH From Online Analyzer';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_is_pass is 'pH Is Pass';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_manual is 'Sample Value Of Turbidity From Manual Test';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_analyzer is 'Sample Value Of Turbidity From Online Analyzer';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_is_pass is 'Turb Is Pass';
comment on column coss_dm.dm_wtw_raw_water_quality_di.raw_is_pass is 'Raw Water Is Pass';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_compare is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_min_value is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_max_value is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_compare is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_min_value is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_max_value is 'Define Whether Turbidity Value Is Acceptable Or Not';
```



```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dws.dws_wtw_verification_item_di_year
-- coss_dim.dim_wtw_water_quality_parameters
-- target table
-- coss_dm.dm_wtw_raw_water_quality_di
-- ****************************************************************************************
insert into coss_dm.dm_wtw_raw_water_quality_di (
    wtw_id,
    loc_id,
    i_code,
    sample_date,
    ph_manual,
    ph_analyzer,
    ph_is_pass,
    turb_manual,
    turb_analyzer,
    turb_is_pass,
    raw_is_pass,
    ph_compare,
    ph_min_value,
    ph_max_value,
    turb_compare,
    turb_min_value,
    turb_max_value,
    dm_update_time,
    dm_load_time
)
select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.turb_manual, -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer, -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass, -- Turb Is Pass
    if((if(t.ph_manual <= t1.ph_max_value, 1, 0) + if(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) as raw_is_pass, -- Raw Water Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 1
      and loc_id = 0
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 1
      and loc_id = 0
      and parameter_limit_id = 19
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.turb_manual, -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer, -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass, -- Turb Is Pass
    if((if(t.ph_manual <= t1.ph_max_value, 1, 0) + if(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) as raw_is_pass, -- Raw Water Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 2
      and loc_id = 0
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 2
      and loc_id = 0
      and parameter_limit_id = 35
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.turb_manual, -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer, -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass, -- Turb Is Pass
    if((if(t.ph_manual <= t1.ph_max_value, 1, 0) + if(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) as raw_is_pass, -- Raw Water Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 3
      and loc_id = 0
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 3
      and loc_id = 0
      and parameter_limit_id = 9
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.turb_manual, -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer, -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass, -- Turb Is Pass
    if((if(t.ph_manual <= t1.ph_max_value, 1, 0) + if(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) as raw_is_pass, -- Raw Water Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 4
      and loc_id = 0
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 4
      and loc_id = 0
      and parameter_limit_id = 1
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.turb_manual, -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer, -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass, -- Turb Is Pass
    if((if(t.ph_manual <= t1.ph_max_value, 1, 0) + if(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) as raw_is_pass, -- Raw Water Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        0 as loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 5
      and loc_id in (1, 2)
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 5
      and loc_id = 0
      and parameter_limit_id = 45
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

on duplicate key update
    wtw_id = values(wtw_id),
    ph_manual = values(ph_manual),
    ph_analyzer = values(ph_analyzer),
    ph_is_pass = values(ph_is_pass),
    turb_manual = values(turb_manual),
    turb_analyzer = values(turb_analyzer),
    turb_is_pass = values(turb_is_pass),
    raw_is_pass = values(raw_is_pass),
    ph_compare = values(ph_compare),
    ph_min_value = values(ph_min_value),
    ph_max_value = values(ph_max_value),
    turb_compare = values(turb_compare),
    turb_min_value = values(turb_min_value),
    turb_max_value = values(turb_max_value),
    dm_update_time = values(dm_update_time);
```



## 投药水质

### wtw_id=1

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(true ,1,0) rcl2_is_pass
    ,if((if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0))+if(true ,1,0)=2, 1, 0) dosed_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 	
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =1
    and loc_id = 20
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code  
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 1
    and loc_id =20
    and parameter_limit_id = 21
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```

### wtw_id=2

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(true ,1,0) rcl2_is_pass
    ,if((if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0))+if(true ,1,0)=2, 1, 0) dosed_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 	
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =2
    and loc_id = 20
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 2
    and loc_id =20
    and parameter_limit_id = 37
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```

### wtw_id=3

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,if((if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0))+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)=2, 1, 0) dosed_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 	
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =3
    and loc_id = 20
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 3
    and loc_id =20
    and parameter_limit_id = 11
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id

```

### wtw_id=4

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,if((if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0))+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)=2, 1, 0) dosed_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 	
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =4
    and loc_id = 20
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 4
    and loc_id =20
    and parameter_limit_id = 3
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```

### wtw_id=5

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(true ,1,0) rcl2_is_pass
    ,if((if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0))+if(true ,1,0)=2, 1, 0) dosed_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 	
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =5
    and loc_id = 20
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 5
    and loc_id =20
    and parameter_limit_id = 47
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```

### coss_dm.dm_wtw_dosed_water_quality_di

```sql
drop table if exists coss_dm.dm_wtw_dosed_water_quality_di;

create table if not exists coss_dm.dm_wtw_dosed_water_quality_di(
    wtw_id         int4,
    loc_id         int4,
    i_code         varchar(255),
    sample_date    timestamp,
    ph_manual      numeric(8, 5),
    ph_analyzer    numeric(8, 5),
    ph_is_pass     int4,
    rcl2_manual    numeric(8, 5),
    rcl2_analyzer  numeric(8, 5),
    rcl2_is_pass   int4,
    dosed_is_pass  int4,
    ph_compare     text,
    ph_min_value   numeric(8, 5),
    ph_max_value   numeric(8, 5),
    rcl2_compare   text,
    rcl2_min_value numeric(8, 5),
    rcl2_max_value numeric(8, 5),
    dm_update_time timestamp(6) default current_timestamp,
    dm_load_time timestamp(6) default current_timestamp,
    constraint dm_wtw_dosed_water_quality_di_pkey primary key (i_code, loc_id, sample_date)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_dm.dm_wtw_dosed_water_quality_di is 'WTW Dosed Water Quality';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.wtw_id is 'ID Of The Corresponding WTW';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.loc_id is 'ID Of The Sampling Location';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.i_code is 'Installations Code';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.sample_date is 'Datetime When The Sample Is Taken';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_manual is 'Sample Value Of pH From Manual Test';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_analyzer is 'Sample Value Of pH From Online Analyzer';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_is_pass is 'pH Is Pass';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_manual is 'Sample Value Of Residual Chlorine From Manual Test';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_analyzer is 'Sample Value Of Residual Chlorine From Online Analyzer';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_is_pass is 'Rcl2 Is Pass';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.dosed_is_pass is 'Dosed Is Pass';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_compare is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_min_value is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_max_value is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_compare is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_min_value is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_max_value is 'Define Whether Residual Chlorine Is Acceptable Or Not';
```



```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dws.dws_wtw_verification_item_di_year
-- coss_dim.dim_wtw_water_quality_parameters
-- target table
-- coss_dm.dm_wtw_dosed_water_quality_di
-- ****************************************************************************************
insert into coss_dm.dm_wtw_dosed_water_quality_di (
    wtw_id,
    loc_id,
    i_code,
    sample_date,
    ph_manual,
    ph_analyzer,
    ph_is_pass,
    rcl2_manual,
    rcl2_analyzer,
    rcl2_is_pass,
    dosed_is_pass,
    ph_compare,
    ph_min_value,
    ph_max_value,
    rcl2_compare,
    rcl2_min_value,
    rcl2_max_value,
    dm_update_time,
    dm_load_time
)
select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.rcl2_manual, -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer, -- Sample Value Of Residual Chlorine From Online Analyzer
    if(true, 1, 0) as rcl2_is_pass, -- Rcl2 Is Pass
    if((if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0)) + if(true, 1, 0) = 2, 1, 0) as dosed_is_pass, -- Dosed Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.rcl2_compare, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 1
      and loc_id = 20
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 1
      and loc_id = 20
      and parameter_limit_id = 21
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.rcl2_manual, -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer, -- Sample Value Of Residual Chlorine From Online Analyzer
    if(true, 1, 0) as rcl2_is_pass, -- Rcl2 Is Pass
    if((if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0)) + if(true, 1, 0) = 2, 1, 0) as dosed_is_pass, -- Dosed Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.rcl2_compare, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 2
      and loc_id = 20
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 2
      and loc_id = 20
      and parameter_limit_id = 37
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.rcl2_manual, -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer, -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass, -- Rcl2 Is Pass
    if(
        (if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0)) + 
        (if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) as dosed_is_pass, -- Dosed Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.rcl2_compare, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 3
      and loc_id = 20
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 3
      and loc_id = 20
      and parameter_limit_id = 11
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.rcl2_manual, -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer, -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass, -- Rcl2 Is Pass
    if(
        (if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0)) + 
        (if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) as dosed_is_pass, -- Dosed Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.rcl2_compare, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 4
      and loc_id = 20
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 4
      and loc_id = 20
      and parameter_limit_id = 3
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.ph_manual, -- Sample Value Of pH From Manual Test
    t.ph_analyzer, -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass, -- pH Is Pass
    t.rcl2_manual, -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer, -- Sample Value Of Residual Chlorine From Online Analyzer
    if(true, 1, 0) as rcl2_is_pass, -- Rcl2 Is Pass
    if((if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0)) + if(true, 1, 0) = 2, 1, 0) as dosed_is_pass, -- Dosed Is Pass
    t1.ph_compare, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value, -- Define Whether pH Value Is Acceptable Or Not
    t1.rcl2_compare, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 5
      and loc_id = 20
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 5
      and loc_id = 20
      and parameter_limit_id = 47
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

on duplicate key update
    wtw_id = values(wtw_id),
    ph_manual = values(ph_manual),
    ph_analyzer = values(ph_analyzer),
    ph_is_pass = values(ph_is_pass),
    rcl2_manual = values(rcl2_manual),
    rcl2_analyzer = values(rcl2_analyzer),
    rcl2_is_pass = values(rcl2_is_pass),
    dosed_is_pass = values(dosed_is_pass),
    ph_compare = values(ph_compare),
    ph_min_value = values(ph_min_value),
    ph_max_value = values(ph_max_value),
    rcl2_compare = values(rcl2_compare),
    rcl2_min_value = values(rcl2_min_value),
    rcl2_max_value = values(rcl2_max_value),
    dm_update_time = values(dm_update_time);
```



## 过滤水水质

### wtw_id = 1

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,if(if(t.turb_manual<= t1.turb_max_value,1,0)+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)=2, 1, 0) filtered_is_pass
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 	
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,turb_manual
    ,turb_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =1
    and loc_id = 40
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,turb_compare
    ,turb_min_value
    ,turb_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 1
    and loc_id =40
    and parameter_limit_id = 27
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```



### wtw_id = 2

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,if(if(t.turb_manual<= t1.turb_max_value,1,0)+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)=2, 1, 0) filtered_is_pass
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 	
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,turb_manual
    ,turb_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =2
    and loc_id = 40
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,turb_compare
    ,turb_min_value
    ,turb_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 2
    and loc_id =40
    and parameter_limit_id = 41
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```



### wtw_id = 3

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,if(if(t.turb_manual<= t1.turb_max_value,1,0)+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)=2, 1, 0) filtered_is_pass
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,turb_manual
    ,turb_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =3
    and loc_id in (44, 45)
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,turb_compare
    ,turb_min_value
    ,turb_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 3
    and loc_id in (44, 45)
    and parameter_limit_id in(13, 15)
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```



### wtw_id = 4

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,if(if(t.turb_manual<= t1.turb_max_value,1,0)+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)=2, 1, 0) filtered_is_pass
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,turb_manual
    ,turb_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =4
    and loc_id = 40
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,turb_compare
    ,turb_min_value
    ,turb_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 4
    and loc_id =40
    and parameter_limit_id = 5
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```



### wtw_id = 5

```sql
no data
```

### coss_dm.dm_wtw_filtered_water_quality_di

```sql
drop table if exists coss_dm.dm_wtw_filtered_water_quality_di;

create table if not exists coss_dm.dm_wtw_filtered_water_quality_di(
    wtw_id             int4,
    loc_id             int4,
    i_code             varchar(255),
    sample_date        timestamp,
    turb_manual        numeric(8, 5),
    turb_analyzer      numeric(8, 5),
    turb_is_pass       int4,
    rcl2_manual        numeric(8, 5),
    rcl2_analyzer      numeric(8, 5),
    rcl2_is_pass       int4,
    filtered_is_pass   int4,
    turb_compare       text,
    turb_min_value     numeric(8, 5),
    turb_max_value     numeric(8, 5),
    rcl2_compare       text,
    rcl2_min_value     numeric(8, 5),
    rcl2_max_value     numeric(8, 5),
    dm_update_time timestamp(6) default current_timestamp,
    dm_load_time timestamp(6) default current_timestamp,
    constraint dm_wtw_filtered_water_quality_di_pkey primary key (i_code, loc_id, sample_date)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_dm.dm_wtw_filtered_water_quality_di is 'WTW Filtered Water Quality';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.wtw_id is 'ID Of The Corresponding WTW';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.loc_id is 'ID Of The Sampling Location';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.i_code is 'Installations Code';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.sample_date is 'Datetime When The Sample Is Taken';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_manual is 'Sample Value Of Turbidity From Manual Test';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_analyzer is 'Sample Value Of Turbidity From Online Analyzer';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_is_pass is 'Turb Is Pass';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_manual is 'Sample Value Of Residual Chlorine From Manual Test';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_analyzer is 'Sample Value Of Residual Chlorine From Online Analyzer';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_is_pass is 'Rcl2 Is Pass';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.filtered_is_pass is 'Filtered Is Pass';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_compare is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_min_value is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_max_value is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_compare is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_min_value is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_max_value is 'Define Whether Residual Chlorine Is Acceptable Or Not';
```



```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dws.dws_wtw_verification_item_di_year
-- coss_dim.dim_wtw_water_quality_parameters
-- target table
-- coss_dm.dm_wtw_filtered_water_quality_di
-- ****************************************************************************************
insert into coss_dm.dm_wtw_filtered_water_quality_di (
    wtw_id,
    loc_id,
    i_code,
    sample_date,
    turb_manual,
    turb_analyzer,
    turb_is_pass,
    rcl2_manual,
    rcl2_analyzer,
    rcl2_is_pass,
    filtered_is_pass,
    turb_compare,
    turb_min_value,
    turb_max_value,
    rcl2_compare,
    rcl2_min_value,
    rcl2_max_value,
    dm_update_time,
    dm_load_time
)
select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.turb_manual, -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer, -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass, -- Turb Is Pass
    t.rcl2_manual, -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer, -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass, -- Rcl2 Is Pass
    if(
        (if(t.turb_manual <= t1.turb_max_value, 1, 0)) + 
        (if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) as filtered_is_pass, -- Filtered Is Pass
    t1.turb_compare, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.rcl2_compare, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 1
      and loc_id = 40
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 1
      and loc_id = 40
      and parameter_limit_id = 27
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.turb_manual, -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer, -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass, -- Turb Is Pass
    t.rcl2_manual, -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer, -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass, -- Rcl2 Is Pass
    if(
        (if(t.turb_manual <= t1.turb_max_value, 1, 0)) + 
        (if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) as filtered_is_pass, -- Filtered Is Pass
    t1.turb_compare, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.rcl2_compare, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 2
      and loc_id = 40
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 2
      and loc_id = 40
      and parameter_limit_id = 41
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.turb_manual, -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer, -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass, -- Turb Is Pass
    t.rcl2_manual, -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer, -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass, -- Rcl2 Is Pass
    if(
        (if(t.turb_manual <= t1.turb_max_value, 1, 0)) + 
        (if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) as filtered_is_pass, -- Filtered Is Pass
    t1.turb_compare, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.rcl2_compare, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 3
      and loc_id in (44, 45)
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 3
      and loc_id in (44, 45)
      and parameter_limit_id in (13, 15)
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

union all

select
    t.wtw_id, -- ID Of The Corresponding WTW
    t.loc_id, -- ID Of The Sampling Location
    t1.i_code, -- Installations Code
    t.sample_date, -- Datetime When The Sample Is Taken
    t.turb_manual, -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer, -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass, -- Turb Is Pass
    t.rcl2_manual, -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer, -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass, -- Rcl2 Is Pass
    if(
        (if(t.turb_manual <= t1.turb_max_value, 1, 0)) + 
        (if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) as filtered_is_pass, -- Filtered Is Pass
    t1.turb_compare, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value, -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.rcl2_compare, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value, -- Define Whether Residual Chlorine Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 4
      and loc_id = 40
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 4
      and loc_id = 40
      and parameter_limit_id = 5
) t1 on t.wtw_id = t1.wtw_id 
    and t.loc_id = t1.loc_id

on duplicate key update
    wtw_id = values(wtw_id),
    turb_manual = values(turb_manual),
    turb_analyzer = values(turb_analyzer),
    turb_is_pass = values(turb_is_pass),
    rcl2_manual = values(rcl2_manual),
    rcl2_analyzer = values(rcl2_analyzer),
    rcl2_is_pass = values(rcl2_is_pass),
    filtered_is_pass = values(filtered_is_pass),
    turb_compare = values(turb_compare),
    turb_min_value = values(turb_min_value),
    turb_max_value = values(turb_max_value),
    rcl2_compare = values(rcl2_compare),
    rcl2_min_value = values(rcl2_min_value),
    rcl2_max_value = values(rcl2_max_value),
    dm_update_time = values(dm_update_time);
```



##   出厂水质

### wtw_id = 1

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,t.fluoride_manual
    ,t.fluoride_analyzer
    ,if(t.fluoride_manual<= t1.fluoride_max_value,1,0) fluoride_is_pass
    ,t.mn_manual
    ,t.mn_analyzer
    ,1 as mn_is_pass
    ,if(if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0)+if(t.rcl2_manual<= t1.rcl2_max_value,1,0)+if(t.fluoride_manual<= t1.fluoride_max_value,1,0)+ 1=5, 1, 0) final_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 
    ,t1.fluoride_compare
    ,t1.fluoride_min_value
    ,t1.fluoride_max_value 
    ,t1.mn_compare
    ,t1.mn_min_value
    ,t1.mn_max_value
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
    ,fluoride_manual
    ,fluoride_analyzer 
    ,mn_manual
    ,mn_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =1
    and loc_id = 100
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
    ,fluoride_compare
    ,fluoride_min_value
    ,fluoride_max_value 
    ,mn_compare
    ,mn_min_value
    ,mn_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 1
    and loc_id = 100
    and parameter_limit_id = 34
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```

### wtw_id = 2

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,t.fluoride_manual
    ,t.fluoride_analyzer
    ,if(t.fluoride_manual>= t1.fluoride_min_value and t.fluoride_manual<= t1.fluoride_max_value,1,0) fluoride_is_pass
    ,t.mn_manual
    ,t.mn_analyzer
    ,1 as mn_is_pass
    ,if(if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0)+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)+if(t.fluoride_manual>= t1.fluoride_min_value and t.fluoride_manual<= t1.fluoride_max_value,1,0)+ 1=5, 1, 0) final_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 
    ,t1.fluoride_compare
    ,t1.fluoride_min_value
    ,t1.fluoride_max_value 
    ,t1.mn_compare
    ,t1.mn_min_value
    ,t1.mn_max_value 
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
    ,fluoride_manual
    ,fluoride_analyzer 
    ,mn_manual
    ,mn_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =2
    and loc_id = 100
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
    ,fluoride_compare
    ,fluoride_min_value
    ,fluoride_max_value 
    ,mn_compare
    ,mn_min_value
    ,mn_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 2
    and loc_id = 100
    and parameter_limit_id = 43
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```



### wtw_id = 3

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,t.fluoride_manual
    ,t.fluoride_analyzer
    ,if(t.fluoride_manual>= t1.fluoride_min_value and t.fluoride_manual<= t1.fluoride_max_value,1,0) fluoride_is_pass
    ,t.mn_manual
    ,t.mn_analyzer
    ,1 as mn_is_pass
    ,if(if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0)+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)+if(t.fluoride_manual>= t1.fluoride_min_value and t.fluoride_manual<= t1.fluoride_max_value,1,0)+ 1=5, 1, 0) final_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 
    ,t1.fluoride_compare
    ,t1.fluoride_min_value
    ,t1.fluoride_max_value 
    ,t1.mn_compare
    ,t1.mn_min_value
    ,t1.mn_max_value 
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
    ,fluoride_manual
    ,fluoride_analyzer 
    ,mn_manual
    ,mn_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =3
    and loc_id = 100
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
    ,fluoride_compare
    ,fluoride_min_value
    ,fluoride_max_value 
    ,mn_compare
    ,mn_min_value
    ,mn_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 3
    and loc_id = 100
    and parameter_limit_id = 17
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```



### wtw_id = 4

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,t.fluoride_manual
    ,t.fluoride_analyzer
    ,if(t.fluoride_manual>= t1.fluoride_min_value and t.fluoride_manual<= t1.fluoride_max_value,1,0) fluoride_is_pass
    ,t.mn_manual
    ,t.mn_analyzer
    ,1 as mn_is_pass
    ,if(if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0)+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)+if(t.fluoride_manual>= t1.fluoride_min_value and t.fluoride_manual<= t1.fluoride_max_value,1,0)+ 1=5, 1, 0) final_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 
    ,t1.fluoride_compare
    ,t1.fluoride_min_value
    ,t1.fluoride_max_value 
    ,t1.mn_compare
    ,t1.mn_min_value
    ,t1.mn_max_value 
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
    ,fluoride_manual
    ,fluoride_analyzer 
    ,mn_manual
    ,mn_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =4
    and loc_id = 100
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
    ,fluoride_compare
    ,fluoride_min_value
    ,fluoride_max_value 
    ,mn_compare
    ,mn_min_value
    ,mn_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 4
    and loc_id = 100
    and parameter_limit_id = 7
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```



### wtw_id = 5

```sql
select 
    t.wtw_id
    ,t.loc_id
    ,t1.i_code
    ,t.sample_date
    ,t.ph_manual
    ,t.ph_analyzer
    ,if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0) ph_is_pass
    ,t.turb_manual
    ,t.turb_analyzer
    ,if(t.turb_manual<= t1.turb_max_value,1,0) turb_is_pass
    ,t.rcl2_manual
    ,t.rcl2_analyzer
    ,if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0) rcl2_is_pass
    ,t.fluoride_manual
    ,t.fluoride_analyzer
    ,if(t.fluoride_manual>= t1.fluoride_min_value and t.fluoride_manual<= t1.fluoride_max_value,1,0) fluoride_is_pass
    ,t.mn_manual
    ,t.mn_analyzer
    ,1 as mn_is_pass
    ,if(if(t.ph_manual>= t1.ph_min_value and t.ph_manual<= t1.ph_max_value,1,0)+if(t.turb_manual<= t1.turb_max_value,1,0)+if(t.rcl2_manual>= t1.rcl2_min_value and t.rcl2_manual<= t1.rcl2_max_value,1,0)+if(t.fluoride_manual>= t1.fluoride_min_value and t.fluoride_manual<= t1.fluoride_max_value,1,0)+ 1=5, 1, 0) final_is_pass
    ,t1.ph_compare
    ,t1.ph_min_value
    ,t1.ph_max_value
    ,t1.turb_compare
    ,t1.turb_min_value
    ,t1.turb_max_value
    ,t1.rcl2_compare
    ,t1.rcl2_min_value
    ,t1.rcl2_max_value 
    ,t1.fluoride_compare
    ,t1.fluoride_min_value
    ,t1.fluoride_max_value 
    ,t1.mn_compare
    ,t1.mn_min_value
    ,t1.mn_max_value 
    ,now() as dm_update_time
    ,now() as dm_load_time
from 
(
select 
    wtw_id
    ,loc_id
    ,sample_date
    ,ph_manual
    ,ph_analyzer
    ,turb_manual
    ,turb_analyzer
    ,rcl2_manual
    ,rcl2_analyzer 
    ,fluoride_manual
    ,fluoride_analyzer 
    ,mn_manual
    ,mn_analyzer 
from 
    coss_dws.dws_wtw_verification_item_di_year 
	where wtw_id =5
    and loc_id = 100
)t 
	inner join 
(
select 
    wtw_id
    ,loc_id
    ,i_code
    ,ph_compare
    ,ph_min_value
    ,ph_max_value
    ,turb_compare
    ,turb_min_value
    ,turb_max_value
    ,rcl2_compare
    ,rcl2_min_value
    ,rcl2_max_value 
    ,fluoride_compare
    ,fluoride_min_value
    ,fluoride_max_value 
    ,mn_compare
    ,mn_min_value
    ,mn_max_value 
from coss_dim.dim_wtw_water_quality_parameters 
    where wtw_id = 5
    and loc_id = 100
    and parameter_limit_id = 51
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```

### coss_dm.dm_wtw_final_water_quality_di

```sql
drop table if exists coss_dm.dm_wtw_final_water_quality_di;

create table if not exists coss_dm.dm_wtw_final_water_quality_di(
    wtw_id               int4,
    loc_id               int4,
    i_code               varchar(255),
    sample_date          timestamp,
    ph_manual            numeric(8, 5),
    ph_analyzer          numeric(8, 5),
    ph_is_pass           int4,
    turb_manual          numeric(8, 5),
    turb_analyzer        numeric(8, 5),
    turb_is_pass         int4,
    rcl2_manual          numeric(8, 5),
    rcl2_analyzer        numeric(8, 5),
    rcl2_is_pass         int4,
    fluoride_manual      numeric(8, 5),
    fluoride_analyzer    numeric(8, 5),
    fluoride_is_pass     int4,
    mn_manual            numeric(8, 5),
    mn_analyzer          numeric(8, 5),
    mn_is_pass           int4,
    final_is_pass        int4,
    ph_compare           text,
    ph_min_value         numeric(8, 5),
    ph_max_value         numeric(8, 5),
    turb_compare         text,
    turb_min_value       numeric(8, 5),
    turb_max_value       numeric(8, 5),
    rcl2_compare         text,
    rcl2_min_value       numeric(8, 5),
    rcl2_max_value       numeric(8, 5),
    fluoride_compare     text,
    fluoride_min_value   numeric(8, 5),
    fluoride_max_value   numeric(8, 5),
    mn_compare           text,
    mn_min_value         numeric(8, 5),
    mn_max_value         numeric(8, 5),
    dm_update_time timestamp(6) default current_timestamp,
    dm_load_time timestamp(6) default current_timestamp,
    constraint dm_wtw_final_water_quality_di_pkey primary key (i_code, loc_id, sample_date)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_dm.dm_wtw_final_water_quality_di is 'WTW Final Water Quality';
comment on column coss_dm.dm_wtw_final_water_quality_di.wtw_id is 'ID Of The Corresponding WTW';
comment on column coss_dm.dm_wtw_final_water_quality_di.loc_id is 'ID Of The Sampling Location';
comment on column coss_dm.dm_wtw_final_water_quality_di.i_code is 'Installations Code';
comment on column coss_dm.dm_wtw_final_water_quality_di.sample_date is 'Datetime When The Sample Is Taken';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_manual is 'Sample Value Of pH From Manual Test';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_analyzer is 'Sample Value Of pH From Online Analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_is_pass is 'pH Is Pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_manual is 'Sample Value Of Turbidity From Manual Test';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_analyzer is 'Sample Value Of Turbidity From Online Analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_is_pass is 'Turb Is Pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_manual is 'Sample Value Of Residual Chlorine From Manual Test';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_analyzer is 'Sample Value Of Residual Chlorine From Online Analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_is_pass is 'Rcl2 Is Pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_manual is 'Sample Value Of Fluoride From Manual Test';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_analyzer is 'Sample Value Of Fluoride From Online Analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_is_pass is 'Fluoride Is Pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_manual is 'Sample Value Of Mangenese From Manual Test';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_analyzer is 'Sample Value Of Mangenese From Online Analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_is_pass is 'Mn Is Pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.final_is_pass is 'Final Is Pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_compare is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_min_value is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_max_value is 'Define Whether pH Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_compare is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_min_value is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_max_value is 'Define Whether Turbidity Value Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_compare is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_min_value is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_max_value is 'Define Whether Residual Chlorine Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_compare is 'Define Whether Fluoride Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_min_value is 'Define Whether Fluoride Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_max_value is 'Define Whether Fluoride Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_compare is 'Define Whether Manganese Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_min_value is 'Define Whether Manganese Is Acceptable Or Not';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_max_value is 'Define Whether Manganese Is Acceptable Or Not';
```



```sql
-- ****************************************************************************************
-- subject     areas: Water Treatment Works
-- function describe: Water Treatment Works Water Quality
-- create         by: dongmaochen
-- create       date: 2025-11-17
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dws.dws_wtw_verification_item_di_year
-- coss_dim.dim_wtw_water_quality_parameters
-- target table
-- coss_dm.dm_wtw_final_water_quality_di
-- ****************************************************************************************
insert into coss_dm.dm_wtw_final_water_quality_di (
    wtw_id,
    loc_id,
    i_code,
    sample_date,
    ph_manual,
    ph_analyzer,
    ph_is_pass,
    turb_manual,
    turb_analyzer,
    turb_is_pass,
    rcl2_manual,
    rcl2_analyzer,
    rcl2_is_pass,
    fluoride_manual,
    fluoride_analyzer,
    fluoride_is_pass,
    mn_manual,
    mn_analyzer,
    mn_is_pass,
    final_is_pass,
    ph_compare,
    ph_min_value,
    ph_max_value,
    turb_compare,
    turb_min_value,
    turb_max_value,
    rcl2_compare,
    rcl2_min_value,
    rcl2_max_value,
    fluoride_compare,
    fluoride_min_value,
    fluoride_max_value,
    mn_compare,
    mn_min_value,
    mn_max_value,
    dm_update_time,
    dm_load_time
)
select
    t.wtw_id,                                                                             -- ID Of The Corresponding WTW
    t.loc_id,                                                                              -- ID Of The Sampling Location
    t1.i_code,                                                                            -- Installations Code
    t.sample_date,                                                                         -- Datetime When The Sample Is Taken
    t.ph_manual,                                                                           -- Sample Value Of pH From Manual Test
    t.ph_analyzer,                                                                         -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass,  -- pH Is Pass
    t.turb_manual,                                                                         -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer,                                                                       -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass,                          -- Turb Is Pass
    t.rcl2_manual,                                                                         -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer,                                                                       -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass,                          -- Rcl2 Is Pass
    t.fluoride_manual,                                                                     -- Sample Value Of Fluoride From Manual Test
    t.fluoride_analyzer,                                                                   -- Sample Value Of Fluoride From Online Analyzer
    if(t.fluoride_manual <= t1.fluoride_max_value, 1, 0) as fluoride_is_pass,              -- Fluoride Is Pass
    t.mn_manual,                                                                           -- Sample Value Of Mangenese From Manual Test
    t.mn_analyzer,                                                                         -- Sample Value Of Mangenese From Online Analyzer
    1 as mn_is_pass,                                                                       -- Mn Is Pass
    if(
        if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) + 
        if(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        if(t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        if(t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) as final_is_pass,                                                                    -- Final Is Pass
    t1.ph_compare,                                                                         -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare,                                                                       -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.rcl2_compare,                                                                       -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.fluoride_compare,                                                                   -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_min_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_max_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.mn_compare,                                                                         -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_min_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_max_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer,
        fluoride_manual,
        fluoride_analyzer,
        mn_manual,
        mn_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 1
      and loc_id = 100
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value,
        fluoride_compare,
        fluoride_min_value,
        fluoride_max_value,
        mn_compare,
        mn_min_value,
        mn_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 1
      and loc_id = 100
      and parameter_limit_id = 34
) t1 on t.wtw_id = t1.wtw_id 
   and t.loc_id = t1.loc_id

union all

select
    t.wtw_id,                                                                             -- ID Of The Corresponding WTW
    t.loc_id,                                                                              -- ID Of The Sampling Location
    t1.i_code,                                                                            -- Installations Code
    t.sample_date,                                                                         -- Datetime When The Sample Is Taken
    t.ph_manual,                                                                           -- Sample Value Of pH From Manual Test
    t.ph_analyzer,                                                                         -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass,  -- pH Is Pass
    t.turb_manual,                                                                         -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer,                                                                       -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass,                          -- Turb Is Pass
    t.rcl2_manual,                                                                         -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer,                                                                       -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass,  -- Rcl2 Is Pass
    t.fluoride_manual,                                                                     -- Sample Value Of Fluoride From Manual Test
    t.fluoride_analyzer,                                                                   -- Sample Value Of Fluoride From Online Analyzer
    if(t.fluoride_manual >= t1.fluoride_min_value and t.fluoride_manual <= t1.fluoride_max_value, 1, 0) as fluoride_is_pass,  -- Fluoride Is Pass
    t.mn_manual,                                                                           -- Sample Value Of Mangenese From Manual Test
    t.mn_analyzer,                                                                         -- Sample Value Of Mangenese From Online Analyzer
    1 as mn_is_pass,                                                                       -- Mn Is Pass
    if(
        if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) + 
        if(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        if(t.fluoride_manual >= t1.fluoride_min_value and t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) as final_is_pass,                                                                    -- Final Is Pass
    t1.ph_compare,                                                                         -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare,                                                                       -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.rcl2_compare,                                                                       -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.fluoride_compare,                                                                   -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_min_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_max_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.mn_compare,                                                                         -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_min_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_max_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer,
        fluoride_manual,
        fluoride_analyzer,
        mn_manual,
        mn_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 2
      and loc_id = 100
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value,
        fluoride_compare,
        fluoride_min_value,
        fluoride_max_value,
        mn_compare,
        mn_min_value,
        mn_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 2
      and loc_id = 100
      and parameter_limit_id = 43
) t1 on t.wtw_id = t1.wtw_id 
   and t.loc_id = t1.loc_id

union all

select
    t.wtw_id,                                                                             -- ID Of The Corresponding WTW
    t.loc_id,                                                                              -- ID Of The Sampling Location
    t1.i_code,                                                                            -- Installations Code
    t.sample_date,                                                                         -- Datetime When The Sample Is Taken
    t.ph_manual,                                                                           -- Sample Value Of pH From Manual Test
    t.ph_analyzer,                                                                         -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass,  -- pH Is Pass
    t.turb_manual,                                                                         -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer,                                                                       -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass,                          -- Turb Is Pass
    t.rcl2_manual,                                                                         -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer,                                                                       -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass,  -- Rcl2 Is Pass
    t.fluoride_manual,                                                                     -- Sample Value Of Fluoride From Manual Test
    t.fluoride_analyzer,                                                                   -- Sample Value Of Fluoride From Online Analyzer
    if(t.fluoride_manual >= t1.fluoride_min_value and t.fluoride_manual <= t1.fluoride_max_value, 1, 0) as fluoride_is_pass,  -- Fluoride Is Pass
    t.mn_manual,                                                                           -- Sample Value Of Mangenese From Manual Test
    t.mn_analyzer,                                                                         -- Sample Value Of Mangenese From Online Analyzer
    1 as mn_is_pass,                                                                       -- Mn Is Pass
    if(
        if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) + 
        if(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        if(t.fluoride_manual >= t1.fluoride_min_value and t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) as final_is_pass,                                                                    -- Final Is Pass
    t1.ph_compare,                                                                         -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare,                                                                       -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.rcl2_compare,                                                                       -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.fluoride_compare,                                                                   -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_min_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_max_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.mn_compare,                                                                         -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_min_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_max_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer,
        fluoride_manual,
        fluoride_analyzer,
        mn_manual,
        mn_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 3
      and loc_id = 100
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value,
        fluoride_compare,
        fluoride_min_value,
        fluoride_max_value,
        mn_compare,
        mn_min_value,
        mn_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 3
      and loc_id = 100
      and parameter_limit_id = 17
) t1 on t.wtw_id = t1.wtw_id 
   and t.loc_id = t1.loc_id

union all

select
    t.wtw_id,                                                                             -- ID Of The Corresponding WTW
    t.loc_id,                                                                              -- ID Of The Sampling Location
    t1.i_code,                                                                            -- Installations Code
    t.sample_date,                                                                         -- Datetime When The Sample Is Taken
    t.ph_manual,                                                                           -- Sample Value Of pH From Manual Test
    t.ph_analyzer,                                                                         -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass,  -- pH Is Pass
    t.turb_manual,                                                                         -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer,                                                                       -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass,                          -- Turb Is Pass
    t.rcl2_manual,                                                                         -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer,                                                                       -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass,  -- Rcl2 Is Pass
    t.fluoride_manual,                                                                     -- Sample Value Of Fluoride From Manual Test
    t.fluoride_analyzer,                                                                   -- Sample Value Of Fluoride From Online Analyzer
    if(t.fluoride_manual >= t1.fluoride_min_value and t.fluoride_manual <= t1.fluoride_max_value, 1, 0) as fluoride_is_pass,  -- Fluoride Is Pass
    t.mn_manual,                                                                           -- Sample Value Of Mangenese From Manual Test
    t.mn_analyzer,                                                                         -- Sample Value Of Mangenese From Online Analyzer
    1 as mn_is_pass,                                                                       -- Mn Is Pass
    if(
        if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) + 
        if(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        if(t.fluoride_manual >= t1.fluoride_min_value and t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) as final_is_pass,                                                                    -- Final Is Pass
    t1.ph_compare,                                                                         -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare,                                                                       -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.rcl2_compare,                                                                       -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.fluoride_compare,                                                                   -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_min_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_max_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.mn_compare,                                                                         -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_min_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_max_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer,
        fluoride_manual,
        fluoride_analyzer,
        mn_manual,
        mn_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 4
      and loc_id = 100
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value,
        fluoride_compare,
        fluoride_min_value,
        fluoride_max_value,
        mn_compare,
        mn_min_value,
        mn_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 4
      and loc_id = 100
      and parameter_limit_id = 7
) t1 on t.wtw_id = t1.wtw_id 
   and t.loc_id = t1.loc_id

union all

select
    t.wtw_id,                                                                             -- ID Of The Corresponding WTW
    t.loc_id,                                                                              -- ID Of The Sampling Location
    t1.i_code,                                                                            -- Installations Code
    t.sample_date,                                                                         -- Datetime When The Sample Is Taken
    t.ph_manual,                                                                           -- Sample Value Of pH From Manual Test
    t.ph_analyzer,                                                                         -- Sample Value Of pH From Online Analyzer
    if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) as ph_is_pass,  -- pH Is Pass
    t.turb_manual,                                                                         -- Sample Value Of Turbidity From Manual Test
    t.turb_analyzer,                                                                       -- Sample Value Of Turbidity From Online Analyzer
    if(t.turb_manual <= t1.turb_max_value, 1, 0) as turb_is_pass,                          -- Turb Is Pass
    t.rcl2_manual,                                                                         -- Sample Value Of Residual Chlorine From Manual Test
    t.rcl2_analyzer,                                                                       -- Sample Value Of Residual Chlorine From Online Analyzer
    if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) as rcl2_is_pass,  -- Rcl2 Is Pass
    t.fluoride_manual,                                                                     -- Sample Value Of Fluoride From Manual Test
    t.fluoride_analyzer,                                                                   -- Sample Value Of Fluoride From Online Analyzer
    if(t.fluoride_manual >= t1.fluoride_min_value and t.fluoride_manual <= t1.fluoride_max_value, 1, 0) as fluoride_is_pass,  -- Fluoride Is Pass
    t.mn_manual,                                                                           -- Sample Value Of Mangenese From Manual Test
    t.mn_analyzer,                                                                         -- Sample Value Of Mangenese From Online Analyzer
    1 as mn_is_pass,                                                                       -- Mn Is Pass
    if(
        if(t.ph_manual >= t1.ph_min_value and t.ph_manual <= t1.ph_max_value, 1, 0) + 
        if(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        if(t.rcl2_manual >= t1.rcl2_min_value and t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        if(t.fluoride_manual >= t1.fluoride_min_value and t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) as final_is_pass,                                                                    -- Final Is Pass
    t1.ph_compare,                                                                         -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_min_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.ph_max_value,                                                                       -- Define Whether pH Value Is Acceptable Or Not
    t1.turb_compare,                                                                       -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_min_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.turb_max_value,                                                                     -- Define Whether Turbidity Value Is Acceptable Or Not
    t1.rcl2_compare,                                                                       -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_min_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.rcl2_max_value,                                                                     -- Define Whether Residual Chlorine Is Acceptable Or Not
    t1.fluoride_compare,                                                                   -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_min_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.fluoride_max_value,                                                                 -- Define Whether Fluoride Is Acceptable Or Not
    t1.mn_compare,                                                                         -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_min_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    t1.mn_max_value,                                                                       -- Define Whether Manganese Is Acceptable Or Not
    current_timestamp as dm_update_time,
    current_timestamp as dm_load_time
from (
    select
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer,
        fluoride_manual,
        fluoride_analyzer,
        mn_manual,
        mn_analyzer
    from coss_dws.dws_wtw_verification_item_di_year
    where wtw_id = 5
      and loc_id = 100
      and dws_update_time >= '${dm_update_time}'
) t
inner join (
    select
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value,
        fluoride_compare,
        fluoride_min_value,
        fluoride_max_value,
        mn_compare,
        mn_min_value,
        mn_max_value
    from coss_dim.dim_wtw_water_quality_parameters
    where wtw_id = 5
      and loc_id = 100
      and parameter_limit_id = 51
) t1 on t.wtw_id = t1.wtw_id 
   and t.loc_id = t1.loc_id

on duplicate key update
    wtw_id = values(wtw_id),
    ph_manual = values(ph_manual),
    ph_analyzer = values(ph_analyzer),
    ph_is_pass = values(ph_is_pass),
    turb_manual = values(turb_manual),
    turb_analyzer = values(turb_analyzer),
    turb_is_pass = values(turb_is_pass),
    rcl2_manual = values(rcl2_manual),
    rcl2_analyzer = values(rcl2_analyzer),
    rcl2_is_pass = values(rcl2_is_pass),
    fluoride_manual = values(fluoride_manual),
    fluoride_analyzer = values(fluoride_analyzer),
    fluoride_is_pass = values(fluoride_is_pass),
    mn_manual = values(mn_manual),
    mn_analyzer = values(mn_analyzer),
    mn_is_pass = values(mn_is_pass),
    final_is_pass = values(final_is_pass),
    ph_compare = values(ph_compare),
    ph_min_value = values(ph_min_value),
    ph_max_value = values(ph_max_value),
    turb_compare = values(turb_compare),
    turb_min_value = values(turb_min_value),
    turb_max_value = values(turb_max_value),
    rcl2_compare = values(rcl2_compare),
    rcl2_min_value = values(rcl2_min_value),
    rcl2_max_value = values(rcl2_max_value),
    fluoride_compare = values(fluoride_compare),
    fluoride_min_value = values(fluoride_min_value),
    fluoride_max_value = values(fluoride_max_value),
    mn_compare = values(mn_compare),
    mn_min_value = values(mn_min_value),
    mn_max_value = values(mn_max_value),
    dm_update_time = values(dm_update_time)
```

### coss_dm.dm_wtw_water_quality_verification_item_di

```sql
drop table if exists coss_dm.dm_wtw_water_quality_verification_item_di;

create table if not exists coss_dm.dm_wtw_water_quality_verification_item_di (
    verification_id numeric(15) null, -- Verification Item Id
    i_code varchar(255) null, -- Local Id
    sample_date timestamp(6) null, -- Sample Date
    verification_item_id numeric(15) not null, -- Verification Item Id
    loc_id numeric(15) null, -- Loc Id
    loc_full_name varchar(255) null, -- Local Full Name
    water_type_code varchar(255) null, -- Water Type Code
    water_type_en varchar(255) null, -- Water Type En
    water_type_tc varchar(255) null, -- Water Type Tc
    water_type_cn varchar(255) null, -- Water Type Cn
    ph_manual numeric(15, 5) null, -- Ph Manual
    turb_manual numeric(15, 5) null, -- Turbidity Manual
    rcl2_manual numeric(15, 5) null, -- Residual Chlorine Manual
    fluoride_manual numeric(15, 5) null, -- Fluoride Manual
    mn_manual numeric(15, 5) null, -- Manganese Ions Manual
    nh3_manual numeric(15, 5) null, -- NH₃ Manual
    uv_manual numeric(15, 5) null, -- Organic Matter Manual
    dm_update_time timestamp(6) null, -- Dm Update Time
    dm_load_time timestamp(6) null, -- Dm Load Time
    constraint dm_wtw_water_quality_verification_item_di_pkey primary key (verification_item_id)
)
with (
    orientation=row,
    compression=no
);

comment on table coss_dm.dm_wtw_water_quality_verification_item_di is 'Water Treatment Works Of Water Quality Verification Item';

-- Column Comments
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.verification_id is 'Verification Item Id';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.i_code is 'Local Id';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.sample_date is 'Sample Date';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.verification_item_id is 'Verification Item Id';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.loc_id is 'Loc Id';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.loc_full_name is 'Local Full Name';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.water_type_code is 'Water Type Code';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.water_type_en is 'Water Type En';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.water_type_tc is 'Water Type Tc';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.water_type_cn is 'Water Type Cn';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.ph_manual is 'Ph Manual';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.turb_manual is 'Turbidity Manual';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.rcl2_manual is 'Residual Chlorine Manual';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.fluoride_manual is 'Fluoride Manual';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.mn_manual is 'Manganese Ions Manual';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.nh3_manual is 'NH₃ Manual';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.uv_manual is 'Organic Matter Manual';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.dm_update_time is 'Dm Update Time';
comment on column coss_dm.dm_wtw_water_quality_verification_item_di.dm_load_time is 'Dm Load Time';
```

### coss_dm.dm_wtw_water_quality_qualification_rate_di

```sql
drop table if exists coss_dm.dm_wtw_water_quality_qualification_rate_di;
create table coss_dm.dm_wtw_water_quality_qualification_rate_di (
    statistical_month   varchar(8),
    i_code              varchar(255),
    tw_name_en          varchar(200),
    tw_name_tc          varchar(300),
    tw_name_cn          varchar(300),
    region_code         varchar(20),
    water_type_code     varchar(255),
    water_type_en       varchar(255),
    water_type_tc       varchar(255),
    water_type_cn       varchar(255),
    qualification_rate  decimal(15,5),
    dm_update_time  timestamp(6) null default pg_systimestamp(),
    dm_load_time    timestamp(6) null default pg_systimestamp(),
    primary key (statistical_month, i_code, water_type_code)
);

comment on table coss_dm.dm_wtw_water_quality_qualification_rate_di 
is 'Water Treatment Works Water Quality Qualification Rate';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.statistical_month  is 'Statistical Month';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.i_code             is 'Local Id';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.tw_name_en         is 'Water Treatment Works Name';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.tw_name_tc         is 'Water Treatment Works Chinese Name';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.tw_name_cn         is 'Water Treatment Works Traditional Chinese Name';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.region_code        is 'Region';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.water_type_code    is 'Water Type Code';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.water_type_en      is 'Water Type En';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.water_type_tc      is 'Water Type Tc';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.water_type_cn      is 'Water Type Cn';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.qualification_rate is 'Qualification_rate';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.dm_update_time     is 'Dm Update Time';
comment on column coss_dm.dm_wtw_water_quality_qualification_rate_di.dm_load_time       is 'Dm Load Time';

```

Load Data

```sql
-- 模拟数据：
insert into coss_dm.dm_wtw_water_quality_qualification_rate_di
select 
t.statistical_month,
t.i_code,
t1.tw_name_en,
t1.tw_name_tc,
t1.tw_name_cn,
t1.region_code,
t.water_type_code,
t.water_type_en,
t.water_type_tc,
t.water_type_cn,
t.qualification_rate
from 
(select
to_char(sample_date,'yyyyMM') statistical_month,
i_code,
water_type_code,
water_type_en,
water_type_tc,
water_type_cn,
case
	when water_type_code = 'WT_TW_000004' then 99+(sum(verification_id) %10)/10 
	else 90+(sum(verification_id) %100)/10 
end qualification_rate,
now() dm_update_time,
now() dm_load_time
from 
coss_dm.dm_wtw_water_quality_verification_item_di
group by 
statistical_month,
i_code,
water_type_code,
water_type_en,
water_type_tc,
water_type_cn) t 
inner join coss_dim.dim_ass_wtw_info t1 on t.i_code =t1.i_code 
```





# 水厂水质参数

| 指标     | 核心检测对象                     | 对水厂的关键作用                               | 国标（GB 5749-2022）控制目标                |
| -------- | -------------------------------- | ---------------------------------------------- | ------------------------------------------- |
| ABS      | 有机污染物总量                   | 评估污染、监控有机物去除、预警消毒副产物       | 出厂水（254nm）＜0.05                       |
| pH       | 水体酸碱度                       | 防管网腐蚀 / 结垢、保障混凝 / 消毒效率         | 6.5~8.5                                     |
| Turb     | 悬浮 / 胶体颗粒                  | 保障感官合规、消除微生物包裹风险、监控过滤效果 | 出厂水≤1 NTU，末梢水≤2 NTU                  |
| UV       | 有机物（UV254）/ 消毒（UV 工艺） | 快速测有机物、无氯消毒控微生物                 | UV254＜0.03 cm⁻¹；消毒后微生物达标          |
| RCl₂     | 余氯                             | 管网持续杀菌、验证消毒效果                     | 出厂水≥0.3 mg/L，末梢水≥0.05 mg/L           |
| Mn       | 锰离子                           | 防感官污染（染色、水垢）、保护管网设备         | ≤0.1 mg/L                                   |
| NH₃      | 氨氮                             | 避免消耗余氯、防藻类滋生、减少管网腐蚀         | ≤0.5 mg/L（以 N 计）                        |
| Fluoride | 氟离子                           | 平衡防龋齿与氟中毒风险（分区控制）             | 0.5~1.0 mg/L（低氟区）；≤1.0 mg/L（高氟区） |
| Taste    | 味觉特性                         | 保障用户接受度、排查金属 / 氯污染              | 无异臭、异味                                |
| Odour    | 嗅觉特性                         | 快速发现藻类 / 微生物污染、响应用户反馈        | 无异臭、异味                                |













