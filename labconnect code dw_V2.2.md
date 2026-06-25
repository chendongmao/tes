version desc

```tex
1.修改dm层代码查询语句，用AI优化
2.AI优化提示词：接下来会话中的所有的代码关键字要改为小写，字段注释的英文首字母要改为大写
```

# 修改临时表代码

## 删除不规范表：

```sql
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_acceptable_diff_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_analyzer_verification_di_yea;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_analyzer_verification_item_d;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_chem_parameter_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_config_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_frequency_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_jar_test_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_jar_test_item_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_location_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_parameter_limit_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_process_handling_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_reminder_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_taste_odour_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_water_quality_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wqmm_water_quality_item_df;
drop table if exists coss_ods.ods_labconnect_labcon_hki_wtw_wtw_unit_df;
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year_tmp;
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df_tmp;
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_config_df_tmp;
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_location_df_tmp;
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df_tmp;
drop table if exists coss_ods.ods_labconnect_wtw_wtw_unit_df_tmp;
```

## 创建中间表

```sql
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di;
create table if not exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di (
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
	constraint primary key (verification_id)
)
with (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (verification_id)
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

comment on table  coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di                         is 'Table to store all store the online analyzer verification results';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.verification_id         is 'Id of each online analyzer verification record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.wtw_id                  is 'Id of the corresponding WTW';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.status                  is 'Status of the reminder:0: Reported and not yet approved ;1: Approved and require acknowledged.;2: Approved/acknowledged and not yet reviewed;3: Reviewed;-1: Rejected';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.last_updated_date       is 'Datetime when the record is updated';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.sample_date             is 'Datetime when the sample is taken';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reported_by             is 'User who the sample record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reported_role           is 'Role of the users who the sample record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reported_date           is 'Datetime when the sample record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.no_record_reason        is 'Reason for not taking the sample ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.approved_by             is 'User who has approved the record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.approved_role           is 'Role of the users who the sample record is approved';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.approved_remarks        is 'Remarks from the approver';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.approved_date           is 'Datetime when the analyzer is checked';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.require_acknowledgement is 'True: The records need acknowledged instrument colleague;False: No need to acknowledged instrument colleague';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.acknowledged_by         is 'Instrument colleague who has acknowledged.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.acknowledged_role       is 'Role of the users who has acknowledged.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.acknowledged_date       is 'Remarks from the acknowledged instrument colleague';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.acknowledged_remarks    is 'Datetime when the sample record is acknowledged';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reviewed_by             is 'User who has reviewed the record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reviewed_role           is 'Role of the users who the sample record is reviewed';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reviewed_remarks        is 'Remarks from the reviewer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reviewed_date           is 'Datetime when the sample record is reviewed';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.rejected_by             is 'User who has rejected the record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.rejected_role           is 'Role of the users who the sample record is rejected';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.rejected_remarks        is 'Remarks from the rejecter';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.rejected_date           is 'Datetime when the sample record is rejected';



drop table if exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df;
create table if not exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df (
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
	constraint primary key (verification_item_id)
)
with (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (verification_item_id);

comment on table  coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df                       is 'Table to store the sample items in the online analyzer verification results';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.verification_item_id   is 'Id of each record item';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.verification_id        is 'Id of the corresponding record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.loc_id                 is 'Id of the sampling location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_manual              is 'Sample value of Ph from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_analyzer            is 'Sample value of Ph from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_manual_dp           is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_analyzer_dp         is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_remarks             is 'Remarks on the Ph sample';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_manual            is 'Sample value of Turbidity from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_analyzer          is 'Sample value of Turbidity from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_manual_dp         is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_analyzer_dp       is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_remarks           is 'Remarks on the Turbidity sample';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_manual            is 'Sample value of Residual Chlorine from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_analyzer          is 'Sample value of Residual Chlorine from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_manual_dp         is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_analyzer_dp       is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_remarks           is 'Remarks on the sample of Residual Chlorine';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_manual        is 'Sample value of Fluoride from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_analyzer      is 'Sample value of Fluoride from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_manual_dp     is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_analyzer_dp   is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_remarks       is 'Remarks on the sample of Fluoride';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_manual              is 'Sample value of Mangenese from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_analyzer            is 'Sample value of Mangenese from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_manual_dp           is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_analyzer_dp         is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_remarks             is 'Remarks on the sample of Mangenese';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_manual             is 'Sample value of Ammonia from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_analyzer           is 'Sample value of Ammonia from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_manual_dp          is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_analyzer_dp        is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_remarks            is 'Remarks on the sample of Ammonia';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_manual              is 'Sample value of Uv light from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_analyzer            is 'Sample value of Uv light from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_manual_dp           is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_analyzer_dp         is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_remarks             is 'Remarks on the sample of Uv light';



DROP TABLE if exists coss_ods.ods_labconnect_wtw_wqmm_config_stg_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wqmm_config_stg_df (
	config_id serial4 NOT NULL,
	wtw_id int4 NOT NULL,
	config_type int2 NULL,
	created_date timestamp NULL,
	created_by int4 NULL,
	created_role int4 NULL,
	effective_date timestamp NULL,
	verification_interval_hr int2 NULL,
	jar_test_interval_hr int2 NULL,
	jar_measure_type int2 NULL,
	require_to_test bool NULL,
	ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
	CONSTRAINT PRIMARY KEY (config_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (config_id);
comment on table  coss_ods.ods_labconnect_wtw_wqmm_config_stg_df                          is 'Table to store all the configuration records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.config_id                is 'ID of each parameter set';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.wtw_id                   is 'ID of the corresponding WTW';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.config_type              is 'Configuration Type 0: parameters for water quality monitoring; 1: parameters for online analyzer verification; 2: sampling frequency';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.created_date             is 'Datetime when the record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.created_by               is 'User who creates the records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.created_role             is 'User role who creates the records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.effective_date           is 'Datetime when the parameter set is effective. The parameter set is effective on or after the effective_date. If there are multiple effective records, choose the one with the latest effective date, tie-break by latest created_date';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.verification_interval_hr is 'This field only has meaning if config_type = 2.The interval (hrs) in which the online analyzer verification test is performed. If this field is empty, no online analyzer verification test is required for the specific WTW.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.jar_test_interval_hr     is 'This field only has meaning if config_type = 2.The interval (hrs) in which the jar test is performed. If this field is empty, no jar test is required for the specific WTW.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.jar_measure_type         is '(if config_type <> 2, use default value 0) 0: the jar test measurement is "絮凝大小"; 1: the jar test measurement is "沉澱速度"';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.require_to_test          is '(if config_type <> 2, use default value false)True: perform taste & odour test;False: no need to perform taste & odour test';



DROP TABLE if exists coss_ods.ods_labconnect_wtw_wqmm_location_stg_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wqmm_location_stg_df (
    loc_id serial4 NOT NULL,
    loc_full_name text NULL,
    loc_name text NULL,
    loc_suffix text NULL,
    loc_name_chi text NULL,
    loc_color_pri text NULL,
    loc_color_sec text NULL,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    CONSTRAINT PRIMARY KEY (loc_id)
)
WITH (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
distribute by hash (loc_id);
comment on table  coss_ods.ods_labconnect_wtw_wqmm_location_stg_df                  is 'Table to store the sample location. Note that some WTW may need to take two different samples at the same location. (e.g. Clarified (A) and Clarified (B) for SHW, but only Clarified for others)';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_id           is 'ID of the location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_full_name    is 'Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_name         is 'Name of the location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_suffix       is 'Suffix of the location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_name_chi     is 'Name of the location in Chinese (for reporting)';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_color_pri    is 'Primary Display color (in RGBA),Primary color is used for text and section border';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_color_sec    is 'Secondary Display color (in RGBA),Secondary color is used for highlight and section shading';



DROP TABLE if exists coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df (
    parameter_limit_id serial4 NOT NULL,
    config_id int4 NULL,
    loc_id int4 NULL,
    target_type int2 NULL,
    ph_compare text NULL,
    ph_min_value numeric(8, 5) NULL,
    ph_min_val_dp int4 NULL,
    ph_max_value numeric(8, 5) NULL,
    ph_max_val_dp int4 NULL,
    turb_compare text NULL,
    turb_min_value numeric(8, 5) NULL,
    turb_min_val_dp int4 NULL,
    turb_max_value numeric(8, 5) NULL,
    turb_max_val_dp int4 NULL,
    rcl2_compare text NULL,
    rcl2_min_value numeric(8, 5) NULL,
    rcl2_min_val_dp int4 NULL,
    rcl2_max_value numeric(8, 5) NULL,
    rcl2_max_val_dp int4 NULL,
    uv_compare text NULL,
    uv_min_value numeric(8, 5) NULL,
    uv_min_val_dp int4 NULL,
    uv_max_value numeric(8, 5) NULL,
    uv_max_val_dp int4 NULL,
    fluoride_compare text NULL,
    fluoride_min_value numeric(8, 5) NULL,
    fluoride_min_val_dp int4 NULL,
    fluoride_max_value numeric(8, 5) NULL,
    fluoride_max_val_dp int4 NULL,
    mn_compare text NULL,
    mn_min_value numeric(8, 5) NULL,
    mn_min_val_dp int4 NULL,
    mn_max_value numeric(8, 5) NULL,
    mn_max_val_dp int4 NULL,
    nh3_compare text NULL,
    nh3_min_value numeric(8, 5) NULL,
    nh3_min_val_dp int4 NULL,
    nh3_max_value numeric(8, 5) NULL,
    nh3_max_val_dp int4 NULL,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    CONSTRAINT PRIMARY KEY (parameter_limit_id)
)
WITH (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
distribute by hash (parameter_limit_id);
comment on table  coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df                       is 'Table to store all the operational targets and critical limits for water quality monitoring';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.parameter_limit_id     is 'ID of each item in the parameters';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.config_id              is 'Configuration ID';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.loc_id                 is 'ID of the corresponding sampling location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.target_type            is 'Target type: 0: operational target; 1: critical limit';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_compare             is 'Define whether pH value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_min_value           is 'Define whether pH value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_max_value           is 'Define whether pH value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_min_val_dp          is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_max_val_dp          is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_compare           is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_min_value         is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_max_value         is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_min_val_dp        is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_max_val_dp        is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_compare           is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_min_value         is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_max_value         is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_min_val_dp        is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_max_val_dp        is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_compare       is 'Define whether Fluoride is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_min_value     is 'Define whether Fluoride is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_max_value     is 'Define whether Fluoride is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_min_val_dp    is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_max_val_dp    is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_compare             is 'Define whether Manganese is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_min_value           is 'Define whether Manganese is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_max_value           is 'Define whether Manganese is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_min_val_dp          is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_max_val_dp          is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_compare            is 'Define whether Ammonia is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_min_value          is 'Define whether Ammonia is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_max_value          is 'Define whether Ammonia is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_min_val_dp         is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_max_val_dp         is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_compare             is 'Define whether UV light is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_min_value           is 'Define whether UV light is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_max_value           is 'Define whether UV light is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_min_val_dp          is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_max_val_dp          is 'No. of decimal places for max value,-1: if the value is null';


DROP TABLE if exists coss_ods.ods_labconnect_wtw_wtw_unit_stg_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wtw_unit_stg_df (
    wtw_id serial4 NOT NULL,
    wtw_code text NOT NULL,
    wtw_name text NOT NULL,
    wtw_name_chi text NOT NULL,
    phase_1 bool NOT NULL,
    phase_2 bool NOT NULL,
    phase_3 bool NOT NULL,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    CONSTRAINT PRIMARY KEY (wtw_id)
)
WITH (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
distribute by hash (wtw_id);
comment on table  coss_ods.ods_labconnect_wtw_wtw_unit_stg_df                     is 'A list of WTW units';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_id              is 'ID of the WTW';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_code            is 'WTW Code ';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_name            is 'WTW English Name (for Phase 1 & 3 Reporting)';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_name_chi        is 'WTW Chinese Name (for Phase 2 Reporting)';
-- comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_transfer_order  is 'Display order of the wtw in the transfer display';
-- comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_lab             is 'Laboratory of the WTW.For CS, SHW, SMB, TO: Siu Ho Wan WTW Laboratory,For RH: Hong Kong Island Regional Laboratory,Others: null';
-- comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtcc_report_cus     is 'Json to record the customization of the Weekly Treatment Chemical Consumption Report';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.phase_1             is 'True: WTW has joined Phase 1, which should show up in Phase 1 site.False: WTW should not show up in Phase 1 site';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.phase_2             is 'True: WTW has joined Phase 2, which should show up in Phase 2 site.False: WTW should not show up in Phase 2 site';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.phase_3             is 'True: WTW has joined Phase 3, which should show up in Phase 3 site.False: WTW should not show up in Phase 3 site';
```



# ods

## ods_labconnect_extract_water_quality_day（调度任务）

### ods_labconnect_wtw_wqmm_analyzer_verification_di_year

#### create table

```sql
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year;
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
	constraint primary key (verification_id)
)
with (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (verification_id)
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

comment on table  coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year                         is 'Table to store all store the online analyzer verification results';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.verification_id         is 'Id of each online analyzer verification record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.wtw_id                  is 'Id of the corresponding WTW';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.status                  is 'Status of the reminder:0: Reported and not yet approved ;1: Approved and require acknowledged.;2: Approved/acknowledged and not yet reviewed;3: Reviewed;-1: Rejected';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.last_updated_date       is 'Datetime when the record is updated';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.sample_date             is 'Datetime when the sample is taken';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reported_by             is 'User who the sample record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reported_role           is 'Role of the users who the sample record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reported_date           is 'Datetime when the sample record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.no_record_reason        is 'Reason for not taking the sample ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.approved_by             is 'User who has approved the record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.approved_role           is 'Role of the users who the sample record is approved';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.approved_remarks        is 'Remarks from the approver';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.approved_date           is 'Datetime when the analyzer is checked';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.require_acknowledgement is 'True: The records need acknowledged instrument colleague;False: No need to acknowledged instrument colleague';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.acknowledged_by         is 'Instrument colleague who has acknowledged.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.acknowledged_role       is 'Role of the users who has acknowledged.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.acknowledged_date       is 'Remarks from the acknowledged instrument colleague';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.acknowledged_remarks    is 'Datetime when the sample record is acknowledged';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reviewed_by             is 'User who has reviewed the record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reviewed_role           is 'Role of the users who the sample record is reviewed';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reviewed_remarks        is 'Remarks from the reviewer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.reviewed_date           is 'Datetime when the sample record is reviewed';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.rejected_by             is 'User who has rejected the record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.rejected_role           is 'Role of the users who the sample record is rejected';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.rejected_remarks        is 'Remarks from the rejecter';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year.rejected_date           is 'Datetime when the sample record is rejected';
```



```sql
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di;
create table if not exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di (
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
	constraint primary key (verification_id)
)
with (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (verification_id)
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

comment on table  coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di                         is 'Table to store all store the online analyzer verification results';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.verification_id         is 'Id of each online analyzer verification record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.wtw_id                  is 'Id of the corresponding WTW';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.status                  is 'Status of the reminder:0: Reported and not yet approved ;1: Approved and require acknowledged.;2: Approved/acknowledged and not yet reviewed;3: Reviewed;-1: Rejected';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.last_updated_date       is 'Datetime when the record is updated';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.sample_date             is 'Datetime when the sample is taken';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reported_by             is 'User who the sample record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reported_role           is 'Role of the users who the sample record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reported_date           is 'Datetime when the sample record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.no_record_reason        is 'Reason for not taking the sample ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.approved_by             is 'User who has approved the record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.approved_role           is 'Role of the users who the sample record is approved';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.approved_remarks        is 'Remarks from the approver';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.approved_date           is 'Datetime when the analyzer is checked';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.require_acknowledgement is 'True: The records need acknowledged instrument colleague;False: No need to acknowledged instrument colleague';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.acknowledged_by         is 'Instrument colleague who has acknowledged.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.acknowledged_role       is 'Role of the users who has acknowledged.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.acknowledged_date       is 'Remarks from the acknowledged instrument colleague';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.acknowledged_remarks    is 'Datetime when the sample record is acknowledged';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reviewed_by             is 'User who has reviewed the record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reviewed_role           is 'Role of the users who the sample record is reviewed';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reviewed_remarks        is 'Remarks from the reviewer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.reviewed_date           is 'Datetime when the sample record is reviewed';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.rejected_by             is 'User who has rejected the record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.rejected_role           is 'Role of the users who the sample record is rejected';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.rejected_remarks        is 'Remarks from the rejecter';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_stg_di.rejected_date           is 'Datetime when the sample record is rejected';
```



#### select sql

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
    verification_id,                   -- ID of each online analyzer verification record
    wtw_id,                            -- ID of the corresponding WTW
    status,                            -- Status of the reminder:0: reported and not yet approved ;1: approved and require acknowledged.;2: approved/acknowledged and not yet reviewed;3: reviewed;-1: rejected
    last_updated_date,                 -- Datetime when the record is updated
    sample_date,                       -- Datetime when the sample is taken
    reported_by,                       -- User who the sample record is created
    reported_role,                     -- Role of the users who the sample record is created
    reported_date,                     -- Datetime when the sample record is created
    no_record_reason,                  -- Reason for not taking the sample
    approved_by,                       -- User who has approved the record
    approved_role,                     -- Role of the users who the sample record is approved
    approved_remarks,                  -- Remarks from the approver
    approved_date,                     -- Datetime when the analyzer is checked
    require_acknowledgement,           -- True: the records need acknowledged instrument colleague;False: no need to acknowledged instrument colleague
    acknowledged_by,                   -- Instrument colleague who has acknowledged.
    acknowledged_role,                 -- Role of the users who has acknowledged.
    acknowledged_remarks,              -- Remarks from the acknowledged instrument colleague
    acknowledged_date,                 -- Datetime when the sample record is acknowledged
    reviewed_by,                       -- User who has reviewed the record
    reviewed_role,                     -- Role of the users who the sample record is reviewed
    reviewed_remarks,                  -- Remarks from the reviewer
    reviewed_date,                     -- Datetime when the sample record is reviewed
    rejected_by,                       -- User who has rejected the record
    rejected_role,                     -- Role of the users who the sample record is rejected
    rejected_remarks,                  -- Remarks from the rejecter
    rejected_date,                     -- Datetime when the sample record is rejected
    localtimestamp ods_update_time,                                 
    localtimestamp ods_load_time                                 
from coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year_tmp 
ON DUPLICATE KEY update
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
    approved_date   = values(approved_date),
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



### ods_labconnect_wtw_wqmm_analyzer_verification_item_df

#### create tabel

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
	constraint primary key (verification_item_id)
)
with (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (verification_item_id);

comment on table  coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df                       is 'Table to store the sample items in the online analyzer verification results';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.verification_item_id   is 'Id of each record item';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.verification_id        is 'Id of the corresponding record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.loc_id                 is 'Id of the sampling location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_manual              is 'Sample value of Ph from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_analyzer            is 'Sample value of Ph from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_manual_dp           is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_analyzer_dp         is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.ph_remarks             is 'Remarks on the Ph sample';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_manual            is 'Sample value of Turbidity from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_analyzer          is 'Sample value of Turbidity from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_manual_dp         is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_analyzer_dp       is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.turb_remarks           is 'Remarks on the Turbidity sample';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_manual            is 'Sample value of Residual Chlorine from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_analyzer          is 'Sample value of Residual Chlorine from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_manual_dp         is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_analyzer_dp       is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.rcl2_remarks           is 'Remarks on the sample of Residual Chlorine';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_manual        is 'Sample value of Fluoride from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_analyzer      is 'Sample value of Fluoride from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_manual_dp     is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_analyzer_dp   is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.fluoride_remarks       is 'Remarks on the sample of Fluoride';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_manual              is 'Sample value of Mangenese from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_analyzer            is 'Sample value of Mangenese from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_manual_dp           is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_analyzer_dp         is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.mn_remarks             is 'Remarks on the sample of Mangenese';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_manual             is 'Sample value of Ammonia from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_analyzer           is 'Sample value of Ammonia from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_manual_dp          is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_analyzer_dp        is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.nh3_remarks            is 'Remarks on the sample of Ammonia';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_manual              is 'Sample value of Uv light from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_analyzer            is 'Sample value of Uv light from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_manual_dp           is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_analyzer_dp         is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df.uv_remarks             is 'Remarks on the sample of Uv light';
```



```sql
drop table if exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df;
create table if not exists coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df (
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
	constraint primary key (verification_item_id)
)
with (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (verification_item_id);

comment on table  coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df                       is 'Table to store the sample items in the online analyzer verification results';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.verification_item_id   is 'Id of each record item';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.verification_id        is 'Id of the corresponding record';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.loc_id                 is 'Id of the sampling location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_manual              is 'Sample value of Ph from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_analyzer            is 'Sample value of Ph from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_manual_dp           is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_analyzer_dp         is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.ph_remarks             is 'Remarks on the Ph sample';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_manual            is 'Sample value of Turbidity from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_analyzer          is 'Sample value of Turbidity from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_manual_dp         is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_analyzer_dp       is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.turb_remarks           is 'Remarks on the Turbidity sample';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_manual            is 'Sample value of Residual Chlorine from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_analyzer          is 'Sample value of Residual Chlorine from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_manual_dp         is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_analyzer_dp       is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.rcl2_remarks           is 'Remarks on the sample of Residual Chlorine';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_manual        is 'Sample value of Fluoride from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_analyzer      is 'Sample value of Fluoride from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_manual_dp     is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_analyzer_dp   is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.fluoride_remarks       is 'Remarks on the sample of Fluoride';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_manual              is 'Sample value of Mangenese from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_analyzer            is 'Sample value of Mangenese from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_manual_dp           is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_analyzer_dp         is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.mn_remarks             is 'Remarks on the sample of Mangenese';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_manual             is 'Sample value of Ammonia from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_analyzer           is 'Sample value of Ammonia from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_manual_dp          is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_analyzer_dp        is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.nh3_remarks            is 'Remarks on the sample of Ammonia';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_manual              is 'Sample value of Uv light from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_analyzer            is 'Sample value of Uv light from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_manual_dp           is 'No. of Decimal places required for the value from manual test';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_analyzer_dp         is 'No. of Decimal places required for the value from online analyzer';
comment on column coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_stg_df.uv_remarks             is 'Remarks on the sample of Uv light';
```

#### select sql

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
    verification_item_id,         -- ID of each record item
    verification_id,              -- ID of the corresponding record
    loc_id,                       -- ID of the sampling location
    ph_manual,                    -- Sample value of pH from manual test
    ph_analyzer,                  -- Sample value of pH from online analyzer
    ph_manual_dp,                 -- No. of decimal places required for the value from manual test
    ph_analyzer_dp,               -- No. of decimal places required for the value from online analyzer
    ph_remarks,                   -- Remarks on the pH sample
    turb_manual,                  -- Sample value of Turbidity from manual test
    turb_analyzer,                -- Sample value of Turbidity from online analyzer
    turb_manual_dp,               -- No. of decimal places required for the value from manual test
    turb_analyzer_dp,             -- No. of decimal places required for the value from online analyzer
    turb_remarks,                 -- Remarks on the Turbidity sample
    rcl2_manual,                  -- Sample value of Residual Chlorine from manual test
    rcl2_analyzer,                -- Sample value of Residual Chlorine from online analyzer
    rcl2_manual_dp,               -- No. of decimal places required for the value from manual test
    rcl2_analyzer_dp,             -- No. of decimal places required for the value from online analyzer
    rcl2_remarks,                 -- Remarks on the sample of Residual Chlorine
    fluoride_manual,              -- Sample value of Fluoride from manual test
    fluoride_analyzer,            -- Sample value of Fluoride from online analyzer
    fluoride_manual_dp,           -- No. of decimal places required for the value from manual test
    fluoride_analyzer_dp,         -- No. of decimal places required for the value from online analyzer
    fluoride_remarks,             -- Remarks on the sample of Fluoride
    mn_manual,                    -- Sample value of Mangenese from manual test
    mn_analyzer,                  -- Sample value of Mangenese from online analyzer
    mn_manual_dp,                 -- No. of decimal places required for the value from manual test
    mn_analyzer_dp,               -- No. of decimal places required for the value from online analyzer
    mn_remarks,                   -- Remarks on the sample of Mangenese
    nh3_manual,                   -- Sample value of Ammonia from manual test
    nh3_analyzer,                 -- Sample value of Ammonia from online analyzer
    nh3_manual_dp,                -- No. of decimal places required for the value from manual test
    nh3_analyzer_dp,              -- No. of decimal places required for the value from online analyzer
    nh3_remarks,                  -- Remarks on the sample of Ammonia
    uv_manual,                    -- Sample value of UV light from manual test
    uv_analyzer,                  -- Sample value of UV light from online analyzer
    uv_manual_dp,                 -- No. of decimal places required for the value from manual test
    uv_analyzer_dp,               -- No. of decimal places required for the value from online analyzer
    uv_remarks,                   -- Remarks on the sample of UV light
    localtimestamp ods_update_time,                                 
    localtimestamp ods_load_time      
from coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df_tmp  --labcon_hki.wqmm_analyzer_verification_item
ON DUPLICATE KEY update
    verification_id =values(verification_id),
    loc_id =values(loc_id),
    ph_manual =values(ph_manual),
    ph_analyzer =values(ph_analyzer),
    ph_manual_dp =values(ph_manual_dp),
    ph_analyzer_dp =values(ph_analyzer_dp),
    ph_remarks =values(ph_remarks),
    turb_manual =values(turb_manual),
    turb_analyzer =values(turb_analyzer),
    turb_manual_dp =values(turb_manual_dp),
    turb_analyzer_dp =values(turb_analyzer_dp),
    turb_remarks =values(turb_remarks),
    rcl2_manual =values(rcl2_manual),
    rcl2_analyzer =values(rcl2_analyzer),
    rcl2_manual_dp =values(rcl2_manual_dp),
    rcl2_analyzer_dp =values(rcl2_analyzer_dp),
    rcl2_remarks =values(rcl2_remarks),
    fluoride_manual =values(fluoride_manual),
    fluoride_analyzer =values(fluoride_analyzer),
    fluoride_manual_dp =values(fluoride_manual_dp),
    fluoride_analyzer_dp =values(fluoride_analyzer_dp),
    fluoride_remarks =values(fluoride_remarks),
    mn_manual =values(mn_manual),
    mn_analyzer =values(mn_analyzer),
    mn_manual_dp =values(mn_manual_dp),
    mn_analyzer_dp =values(mn_analyzer_dp),
    mn_remarks =values(mn_remarks),
    nh3_manual =values(nh3_manual),
    nh3_analyzer =values(nh3_analyzer),
    nh3_manual_dp =values(nh3_manual_dp),
    nh3_analyzer_dp =values(nh3_analyzer_dp),
    nh3_remarks =values(nh3_remarks),
    uv_manual =values(uv_manual),
    uv_analyzer =values(uv_analyzer),
    uv_manual_dp =values(uv_manual_dp),
    uv_analyzer_dp =values(uv_analyzer_dp),
    uv_remarks =values(uv_remarks),
    ods_update_time =values(ods_update_time)
```



### ods_labconnect_wtw_wqmm_config_df

#### create table

```sql
DROP TABLE if exists coss_ods.ods_labconnect_wtw_wqmm_config_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wqmm_config_df (
	config_id serial4 NOT NULL,
	wtw_id int4 NOT NULL,
	config_type int2 NULL,
	created_date timestamp NULL,
	created_by int4 NULL,
	created_role int4 NULL,
	effective_date timestamp NULL,
	verification_interval_hr int2 NULL,
	jar_test_interval_hr int2 NULL,
	jar_measure_type int2 NULL,
	require_to_test bool NULL,
	ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
	CONSTRAINT PRIMARY KEY (config_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (config_id);
comment on table  coss_ods.ods_labconnect_wtw_wqmm_config_df                          is 'Table to store all the configuration records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.config_id                is 'ID of each parameter set';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.wtw_id                   is 'ID of the corresponding WTW';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.config_type              is 'Configuration Type 0: parameters for water quality monitoring; 1: parameters for online analyzer verification; 2: sampling frequency';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.created_date             is 'Datetime when the record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.created_by               is 'User who creates the records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.created_role             is 'User role who creates the records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.effective_date           is 'Datetime when the parameter set is effective. The parameter set is effective on or after the effective_date. If there are multiple effective records, choose the one with the latest effective date, tie-break by latest created_date';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.verification_interval_hr is 'This field only has meaning if config_type = 2.The interval (hrs) in which the online analyzer verification test is performed. If this field is empty, no online analyzer verification test is required for the specific WTW.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.jar_test_interval_hr     is 'This field only has meaning if config_type = 2.The interval (hrs) in which the jar test is performed. If this field is empty, no jar test is required for the specific WTW.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.jar_measure_type         is '(if config_type <> 2, use default value 0) 0: the jar test measurement is "絮凝大小"; 1: the jar test measurement is "沉澱速度"';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_df.require_to_test          is '(if config_type <> 2, use default value false)True: perform taste & odour test;False: no need to perform taste & odour test';
```



```sql
DROP TABLE if exists coss_ods.ods_labconnect_wtw_wqmm_config_stg_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wqmm_config_stg_df (
	config_id serial4 NOT NULL,
	wtw_id int4 NOT NULL,
	config_type int2 NULL,
	created_date timestamp NULL,
	created_by int4 NULL,
	created_role int4 NULL,
	effective_date timestamp NULL,
	verification_interval_hr int2 NULL,
	jar_test_interval_hr int2 NULL,
	jar_measure_type int2 NULL,
	require_to_test bool NULL,
	ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
	CONSTRAINT PRIMARY KEY (config_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (config_id);
comment on table  coss_ods.ods_labconnect_wtw_wqmm_config_stg_df                          is 'Table to store all the configuration records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.config_id                is 'ID of each parameter set';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.wtw_id                   is 'ID of the corresponding WTW';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.config_type              is 'Configuration Type 0: parameters for water quality monitoring; 1: parameters for online analyzer verification; 2: sampling frequency';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.created_date             is 'Datetime when the record is created';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.created_by               is 'User who creates the records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.created_role             is 'User role who creates the records';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.effective_date           is 'Datetime when the parameter set is effective. The parameter set is effective on or after the effective_date. If there are multiple effective records, choose the one with the latest effective date, tie-break by latest created_date';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.verification_interval_hr is 'This field only has meaning if config_type = 2.The interval (hrs) in which the online analyzer verification test is performed. If this field is empty, no online analyzer verification test is required for the specific WTW.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.jar_test_interval_hr     is 'This field only has meaning if config_type = 2.The interval (hrs) in which the jar test is performed. If this field is empty, no jar test is required for the specific WTW.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.jar_measure_type         is '(if config_type <> 2, use default value 0) 0: the jar test measurement is "絮凝大小"; 1: the jar test measurement is "沉澱速度"';
comment on column coss_ods.ods_labconnect_wtw_wqmm_config_stg_df.require_to_test          is '(if config_type <> 2, use default value false)True: perform taste & odour test;False: no need to perform taste & odour test';
```

#### select sql

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
    config_id,                          -- ID of each parameter set
    wtw_id,                             -- ID of the corresponding WTW
    config_type,                        -- Configuration Type 0: parameters for water quality monitoring; 1: parameters for online analyzer verification; 2: sampling frequency
    created_date,                       -- Datetime when the record is created
    created_by,                         -- User who creates the records
    created_role,                       -- User role who creates the records
    effective_date,                     -- Datetime when the parameter set is effective. The parameter set is effective on or after the effective_date. If there are multiple effective records, choose the one with the latest effective date, tie-break by latest created_date
    verification_interval_hr,           -- This field only has meaning if config_type = 2.The interval (hrs) in which the online analyzer verification test is performed. If this field is empty, no online analyzer verification test is required for the specific WTW.
    jar_test_interval_hr,               -- This field only has meaning if config_type = 2.The interval (hrs) in which the jar test is performed. If this field is empty, no jar test is required for the specific WTW.
    jar_measure_type,                   -- (if config_type <> 2, use default value 0) 0: the jar test measurement is "絮凝大小"; 1: the jar test measurement is "沉澱速度"
    require_to_test,                    -- (if config_type <> 2, use default value false)True: perform taste & odour test;False: no need to perform taste & odour test
    localtimestamp ods_update_time,                                    
    localtimestamp ods_load_time                                    
from coss_ods.ods_labconnect_wtw_wqmm_config_df_tmp --labcon_hki.wqmm_config
ON DUPLICATE KEY update
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

### ods_labconnect_wtw_wqmm_location_df

#### create table 

```sql
DROP TABLE if exists coss_ods.ods_labconnect_wtw_wqmm_location_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wqmm_location_df (
	loc_id serial4 NOT NULL,
	loc_full_name text NULL,
	loc_name text NULL,
	loc_suffix text NULL,
	loc_name_chi text NULL,
	loc_color_pri text NULL,
	loc_color_sec text NULL,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
	CONSTRAINT PRIMARY KEY (loc_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (loc_id);
comment on table  coss_ods.ods_labconnect_wtw_wqmm_location_df                  is 'Table to store the sample location. Note that some WTW may need to take two different samples at the same location. (e.g. Clarified (A) and Clarified (B) for SHW, but only Clarified for others)';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_id           is 'ID of the location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_full_name    is 'Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_name         is 'Name of the location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_suffix       is 'Suffix of the location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_name_chi     is 'Name of the location in Chinese (for reporting)';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_color_pri    is 'Primary Display color (in RGBA),Primary color is used for text and section border';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_df.loc_color_sec    is 'Secondary Display color (in RGBA),Secondary color is used for highlight and section shading';

```



```sql
DROP TABLE if exists coss_ods.ods_labconnect_wtw_wqmm_location_stg_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wqmm_location_stg_df (
    loc_id serial4 NOT NULL,
    loc_full_name text NULL,
    loc_name text NULL,
    loc_suffix text NULL,
    loc_name_chi text NULL,
    loc_color_pri text NULL,
    loc_color_sec text NULL,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    CONSTRAINT PRIMARY KEY (loc_id)
)
WITH (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
distribute by hash (loc_id);
comment on table  coss_ods.ods_labconnect_wtw_wqmm_location_stg_df                  is 'Table to store the sample location. Note that some WTW may need to take two different samples at the same location. (e.g. Clarified (A) and Clarified (B) for SHW, but only Clarified for others)';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_id           is 'ID of the location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_full_name    is 'Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_name         is 'Name of the location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_suffix       is 'Suffix of the location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_name_chi     is 'Name of the location in Chinese (for reporting)';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_color_pri    is 'Primary Display color (in RGBA),Primary color is used for text and section border';
comment on column coss_ods.ods_labconnect_wtw_wqmm_location_stg_df.loc_color_sec    is 'Secondary Display color (in RGBA),Secondary color is used for highlight and section shading';
```

#### select sql

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
    loc_id,              -- ID of the location
    loc_full_name,       -- Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.
    loc_name,            -- Name of the location
    loc_suffix,          -- Suffix of the location
    loc_name_chi,        -- Name of the location in Chinese (for reporting)
    loc_color_pri,       -- Primary Display color (in RGBA),Primary color is used for text and section border
    loc_color_sec,       -- Secondary Display color (in RGBA),Secondary color is used for highlight and section shading
    localtimestamp ods_update_time,
    localtimestamp ods_load_time
from coss_ods.ods_labconnect_wtw_wqmm_location_df_tmp -- labcon_hki.wqmm_location
ON DUPLICATE KEY update
    loc_full_name = values(loc_full_name),
    loc_name = values(loc_name),
    loc_suffix = values(loc_suffix),
    loc_name_chi = values(loc_name_chi),
    loc_color_pri = values(loc_color_pri),
    loc_color_sec = values(loc_color_sec),
    ods_update_time = values(ods_update_time)
```



### ods_labconnect_wtw_wqmm_parameter_limit_df

#### create table

```sql

DROP TABLE if exists coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df (
	parameter_limit_id serial4 NOT NULL,
	config_id int4 NULL,
	loc_id int4 NULL,
	target_type int2 NULL,
	ph_compare text NULL,
	ph_min_value numeric(8, 5) NULL,
	ph_min_val_dp int4 NULL,
	ph_max_value numeric(8, 5) NULL,
	ph_max_val_dp int4 NULL,
	turb_compare text NULL,
	turb_min_value numeric(8, 5) NULL,
	turb_min_val_dp int4 NULL,
	turb_max_value numeric(8, 5) NULL,
	turb_max_val_dp int4 NULL,
	rcl2_compare text NULL,
	rcl2_min_value numeric(8, 5) NULL,
	rcl2_min_val_dp int4 NULL,
	rcl2_max_value numeric(8, 5) NULL,
	rcl2_max_val_dp int4 NULL,
	uv_compare text NULL,
	uv_min_value numeric(8, 5) NULL,
	uv_min_val_dp int4 NULL,
	uv_max_value numeric(8, 5) NULL,
	uv_max_val_dp int4 NULL,
	fluoride_compare text NULL,
	fluoride_min_value numeric(8, 5) NULL,
	fluoride_min_val_dp int4 NULL,
	fluoride_max_value numeric(8, 5) NULL,
	fluoride_max_val_dp int4 NULL,
	mn_compare text NULL,
	mn_min_value numeric(8, 5) NULL,
	mn_min_val_dp int4 NULL,
	mn_max_value numeric(8, 5) NULL,
	mn_max_val_dp int4 NULL,
	nh3_compare text NULL,
	nh3_min_value numeric(8, 5) NULL,
	nh3_min_val_dp int4 NULL,
	nh3_max_value numeric(8, 5) NULL,
	nh3_max_val_dp int4 NULL,
	ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
	CONSTRAINT PRIMARY KEY (parameter_limit_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (parameter_limit_id);
comment on table  coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df                       is 'Table to store all the operational targets and critical limits for water quality monitoring';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.parameter_limit_id     is 'ID of each item in the parameters';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.config_id              is 'Configuration ID';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.loc_id                 is 'ID of the corresponding sampling location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.target_type            is 'Target type: 0: operational target; 1: critical limit';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_compare             is 'Define whether pH value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_min_value           is 'Define whether pH value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_max_value           is 'Define whether pH value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_min_val_dp          is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.ph_max_val_dp          is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_compare           is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_min_value         is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_max_value         is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_min_val_dp        is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.turb_max_val_dp        is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_compare           is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_min_value         is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_max_value         is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_min_val_dp        is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.rcl2_max_val_dp        is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_compare       is 'Define whether Fluoride is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_min_value     is 'Define whether Fluoride is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_max_value     is 'Define whether Fluoride is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_min_val_dp    is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.fluoride_max_val_dp    is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_compare             is 'Define whether Manganese is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_min_value           is 'Define whether Manganese is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_max_value           is 'Define whether Manganese is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_min_val_dp          is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.mn_max_val_dp          is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_compare            is 'Define whether Ammonia is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_min_value          is 'Define whether Ammonia is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_max_value          is 'Define whether Ammonia is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_min_val_dp         is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.nh3_max_val_dp         is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_compare             is 'Define whether UV light is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_min_value           is 'Define whether UV light is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_max_value           is 'Define whether UV light is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_min_val_dp          is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df.uv_max_val_dp          is 'No. of decimal places for max value,-1: if the value is null';

```

```sql
DROP TABLE if exists coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df (
    parameter_limit_id serial4 NOT NULL,
    config_id int4 NULL,
    loc_id int4 NULL,
    target_type int2 NULL,
    ph_compare text NULL,
    ph_min_value numeric(8, 5) NULL,
    ph_min_val_dp int4 NULL,
    ph_max_value numeric(8, 5) NULL,
    ph_max_val_dp int4 NULL,
    turb_compare text NULL,
    turb_min_value numeric(8, 5) NULL,
    turb_min_val_dp int4 NULL,
    turb_max_value numeric(8, 5) NULL,
    turb_max_val_dp int4 NULL,
    rcl2_compare text NULL,
    rcl2_min_value numeric(8, 5) NULL,
    rcl2_min_val_dp int4 NULL,
    rcl2_max_value numeric(8, 5) NULL,
    rcl2_max_val_dp int4 NULL,
    uv_compare text NULL,
    uv_min_value numeric(8, 5) NULL,
    uv_min_val_dp int4 NULL,
    uv_max_value numeric(8, 5) NULL,
    uv_max_val_dp int4 NULL,
    fluoride_compare text NULL,
    fluoride_min_value numeric(8, 5) NULL,
    fluoride_min_val_dp int4 NULL,
    fluoride_max_value numeric(8, 5) NULL,
    fluoride_max_val_dp int4 NULL,
    mn_compare text NULL,
    mn_min_value numeric(8, 5) NULL,
    mn_min_val_dp int4 NULL,
    mn_max_value numeric(8, 5) NULL,
    mn_max_val_dp int4 NULL,
    nh3_compare text NULL,
    nh3_min_value numeric(8, 5) NULL,
    nh3_min_val_dp int4 NULL,
    nh3_max_value numeric(8, 5) NULL,
    nh3_max_val_dp int4 NULL,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    CONSTRAINT PRIMARY KEY (parameter_limit_id)
)
WITH (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
distribute by hash (parameter_limit_id);
comment on table  coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df                       is 'Table to store all the operational targets and critical limits for water quality monitoring';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.parameter_limit_id     is 'ID of each item in the parameters';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.config_id              is 'Configuration ID';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.loc_id                 is 'ID of the corresponding sampling location';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.target_type            is 'Target type: 0: operational target; 1: critical limit';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_compare             is 'Define whether pH value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_min_value           is 'Define whether pH value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_max_value           is 'Define whether pH value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_min_val_dp          is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.ph_max_val_dp          is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_compare           is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_min_value         is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_max_value         is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_min_val_dp        is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.turb_max_val_dp        is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_compare           is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_min_value         is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_max_value         is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_min_val_dp        is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.rcl2_max_val_dp        is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_compare       is 'Define whether Fluoride is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_min_value     is 'Define whether Fluoride is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_max_value     is 'Define whether Fluoride is acceptable or not ';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_min_val_dp    is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.fluoride_max_val_dp    is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_compare             is 'Define whether Manganese is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_min_value           is 'Define whether Manganese is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_max_value           is 'Define whether Manganese is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_min_val_dp          is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.mn_max_val_dp          is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_compare            is 'Define whether Ammonia is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_min_value          is 'Define whether Ammonia is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_max_value          is 'Define whether Ammonia is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_min_val_dp         is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.nh3_max_val_dp         is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_compare             is 'Define whether UV light is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_min_value           is 'Define whether UV light is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_max_value           is 'Define whether UV light is acceptable or not';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_min_val_dp          is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_stg_df.uv_max_val_dp          is 'No. of decimal places for max value,-1: if the value is null';
```

#### select sql

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
    parameter_limit_id,        -- ID of each item in the parameters
    config_id,                 -- Configuration ID
    loc_id,                    -- ID of the corresponding sampling location
    target_type,               -- Target type: 0: operational target; 1: critical limit
    ph_compare,                -- Define whether pH value is acceptable or not
    ph_min_value,              -- Define whether pH value is acceptable or not
    ph_max_value,              -- Define whether pH value is acceptable or not
    ph_min_val_dp,             -- No. of decimal places for min value,-1: if the value is null
    ph_max_val_dp,             -- No. of decimal places for max value,-1: if the value is null
    turb_compare,              -- Define whether Turbidity value is acceptable or not
    turb_min_value,            -- Define whether Turbidity value is acceptable or not
    turb_max_value,            -- Define whether Turbidity value is acceptable or not
    turb_min_val_dp,           -- No. of decimal places for min value,-1: if the value is null
    turb_max_val_dp,           -- No. of decimal places for max value,-1: if the value is null
    rcl2_compare,              -- Define whether Residual Chlorine is acceptable or not
    rcl2_min_value,            -- Define whether Residual Chlorine is acceptable or not
    rcl2_max_value,            -- Define whether Residual Chlorine is acceptable or not
    rcl2_min_val_dp,           -- No. of decimal places for min value,-1: if the value is null
    rcl2_max_val_dp,           -- No. of decimal places for max value,-1: if the value is null
    fluoride_compare,          -- Define whether Fluoride is acceptable or not
    fluoride_min_value,        -- Define whether Fluoride is acceptable or not
    fluoride_max_value,        -- Define whether Fluoride is acceptable or not
    fluoride_min_val_dp,       -- No. of decimal places for min value,-1: if the value is null
    fluoride_max_val_dp,       -- No. of decimal places for max value,-1: if the value is null
    mn_compare,                -- Define whether Manganese is acceptable or not
    mn_min_value,              -- Define whether Manganese is acceptable or not
    mn_max_value,              -- Define whether Manganese is acceptable or not
    mn_min_val_dp,             -- No. of decimal places for min value,-1: if the value is null
    mn_max_val_dp,             -- No. of decimal places for max value,-1: if the value is null
    nh3_compare,               -- Define whether Ammonia is acceptable or not
    nh3_min_value,             -- Define whether Ammonia is acceptable or not
    nh3_max_value,             -- Define whether Ammonia is acceptable or not
    nh3_min_val_dp,            -- No. of decimal places for min value,-1: if the value is null
    nh3_max_val_dp,            -- No. of decimal places for max value,-1: if the value is null
    uv_compare,                -- Define whether UV light is acceptable or not
    uv_min_value,              -- Define whether UV light is acceptable or not
    uv_max_value,              -- Define whether UV light is acceptable or not
    uv_min_val_dp,             -- No. of decimal places for min value,-1: if the value is null
    uv_max_val_dp,             -- No. of decimal places for max value,-1: if the value is null
    localtimestamp ods_update_time,
    localtimestamp ods_load_time
from coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df_tmp -- labcon_hki.wqmm_parameter_limit
ON DUPLICATE KEY update
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

### ods_labconnect_wtw_wtw_unit_df

#### create table

```sql
DROP TABLE if exists coss_ods.ods_labconnect_wtw_wtw_unit_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wtw_unit_df (
	wtw_id serial4 NOT NULL,
	wtw_code text NOT NULL,
	wtw_name text NOT NULL,
	wtw_name_chi text NOT NULL,
	phase_1 bool NOT NULL,
	phase_2 bool NOT NULL,
	phase_3 bool NOT NULL,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
	CONSTRAINT PRIMARY KEY (wtw_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (wtw_id);
comment on table  coss_ods.ods_labconnect_wtw_wtw_unit_df                     is 'A list of WTW units';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_id              is 'ID of the WTW';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_code            is 'WTW Code ';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_name            is 'WTW English Name (for Phase 1 & 3 Reporting)';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_name_chi        is 'WTW Chinese Name (for Phase 2 Reporting)';
-- comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_transfer_order  is 'Display order of the wtw in the transfer display';
-- comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtw_lab             is 'Laboratory of the WTW.For CS, SHW, SMB, TO: Siu Ho Wan WTW Laboratory,For RH: Hong Kong Island Regional Laboratory,Others: null';
-- comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.wtcc_report_cus     is 'Json to record the customization of the Weekly Treatment Chemical Consumption Report';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.phase_1             is 'True: WTW has joined Phase 1, which should show up in Phase 1 site.False: WTW should not show up in Phase 1 site';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.phase_2             is 'True: WTW has joined Phase 2, which should show up in Phase 2 site.False: WTW should not show up in Phase 2 site';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_df.phase_3             is 'True: WTW has joined Phase 3, which should show up in Phase 3 site.False: WTW should not show up in Phase 3 site';
```



```sql
DROP TABLE if exists coss_ods.ods_labconnect_wtw_wtw_unit_stg_df;
CREATE TABLE if not exists coss_ods.ods_labconnect_wtw_wtw_unit_stg_df (
    wtw_id serial4 NOT NULL,
    wtw_code text NOT NULL,
    wtw_name text NOT NULL,
    wtw_name_chi text NOT NULL,
    phase_1 bool NOT NULL,
    phase_2 bool NOT NULL,
    phase_3 bool NOT NULL,
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    CONSTRAINT PRIMARY KEY (wtw_id)
)
WITH (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
distribute by hash (wtw_id);
comment on table  coss_ods.ods_labconnect_wtw_wtw_unit_stg_df                     is 'A list of WTW units';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_id              is 'ID of the WTW';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_code            is 'WTW Code ';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_name            is 'WTW English Name (for Phase 1 & 3 Reporting)';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_name_chi        is 'WTW Chinese Name (for Phase 2 Reporting)';
-- comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_transfer_order  is 'Display order of the wtw in the transfer display';
-- comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtw_lab             is 'Laboratory of the WTW.For CS, SHW, SMB, TO: Siu Ho Wan WTW Laboratory,For RH: Hong Kong Island Regional Laboratory,Others: null';
-- comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.wtcc_report_cus     is 'Json to record the customization of the Weekly Treatment Chemical Consumption Report';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.phase_1             is 'True: WTW has joined Phase 1, which should show up in Phase 1 site.False: WTW should not show up in Phase 1 site';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.phase_2             is 'True: WTW has joined Phase 2, which should show up in Phase 2 site.False: WTW should not show up in Phase 2 site';
comment on column coss_ods.ods_labconnect_wtw_wtw_unit_stg_df.phase_3             is 'True: WTW has joined Phase 3, which should show up in Phase 3 site.False: WTW should not show up in Phase 3 site';
```

#### select sql

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
  wtw_id,
  wtw_code,
  wtw_name,
  wtw_name_chi,
--  wtw_transfer_order,
--  wtw_lab,
--  wtcc_report_cus,
  phase_1,
  phase_2,
  phase_3,
  localtimestamp ods_update_time,
  localtimestamp ods_load_time
from coss_ods.ods_labconnect_wtw_wtw_unit_df_tmp --labcon_hki.wtw_unit
ON DUPLICATE KEY update
    wtw_code = values(wtw_code),
    wtw_name = values(wtw_name),
    wtw_name_chi = values(wtw_name_chi),
--    wtw_transfer_order = values(wtw_transfer_order),
--    wtw_lab = values(wtw_lab),
--    wtcc_report_cus = values(wtcc_report_cus),
    phase_1 = values(phase_1),
    phase_2 = values(phase_2),
    phase_3 = values(phase_3),
    ods_update_time = values(ods_update_time)

```



# dwd

## dwd_wtw_etl_water_quality_day（调度任务）

### coss_dwd.dwd_wtw_verification_di_year

#### create table

```sql
drop table if exists  coss_dwd.dwd_wtw_verification_di_year;
create table if not exists coss_dwd.dwd_wtw_verification_di_year(
    verification_id    int4,         -- ID of each online analyzer verification record
    wtw_id             int4,         -- ID of the corresponding WTW
    status             int2,         -- Status of the reminder:0: reported and not yet approved ;1: approved and require acknowledged.;2: approved/acknowledged and not yet reviewed;3: reviewed;-1: rejected
    last_updated_date  timestamp,    -- Datetime when the record is updated
    sample_date        timestamp,    -- Datetime when the sample is taken
    reviewed_date      timestamp,    -- Datetime when the sample record is reviewed
    wtw_code           text,         -- WTW Code
    wtw_name           text,         -- WTW English Name (for Phase 1 & 3 Reporting)
    wtw_name_chi       text,         -- WTW Chinese Name (for Phase 2 Reporting)
    phase_1            bool,         -- True: WTW has joined Phase 1, which should show up in Phase 1 site.False: WTW should not show up in Phase 1 site
    phase_2            bool,         -- True: WTW has joined Phase 2, which should show up in Phase 2 site.False: WTW should not show up in Phase 2 site
    phase_3            bool,         -- True: WTW has joined Phase 3, which should show up in Phase 3 site.False: WTW should not show up in Phase 3 site
    dwd_update_time timestamp(6) default current_timestamp,
    dwd_load_time timestamp(6) default current_timestamp,
	CONSTRAINT dwd_wtw_verification_di_year_pkey PRIMARY KEY (verification_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (verification_id)
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
comment on table  coss_dwd.dwd_wtw_verification_di_year                         is 'Table to store all store the online analyzer verification results';
comment on column coss_dwd.dwd_wtw_verification_di_year.verification_id         is 'ID of each online analyzer verification record';
comment on column coss_dwd.dwd_wtw_verification_di_year.wtw_id                  is 'ID of the corresponding WTW';
comment on column coss_dwd.dwd_wtw_verification_di_year.status                  is 'Status of the reminder:0: reported and not yet approved ;1: approved and require acknowledged.;2: approved/acknowledged and not yet reviewed;3: reviewed;-1: rejected';
comment on column coss_dwd.dwd_wtw_verification_di_year.last_updated_date       is 'Datetime when the record is updated';
comment on column coss_dwd.dwd_wtw_verification_di_year.sample_date             is 'Datetime when the sample is taken';
comment on column coss_dwd.dwd_wtw_verification_di_year.reviewed_date           is 'Datetime when the sample record is reviewed';
comment on column coss_dwd.dwd_wtw_verification_di_year.wtw_code                is 'WTW Code';
comment on column coss_dwd.dwd_wtw_verification_di_year.wtw_name                is 'WTW English Name (for Phase 1 & 3 Reporting)';
comment on column coss_dwd.dwd_wtw_verification_di_year.wtw_name_chi            is 'WTW Chinese Name (for Phase 2 Reporting)';
comment on column coss_dwd.dwd_wtw_verification_di_year.phase_1                 is 'True: WTW has joined Phase 1, which should show up in Phase 1 site.False: WTW should not show up in Phase 1 site';
comment on column coss_dwd.dwd_wtw_verification_di_year.phase_2                 is 'True: WTW has joined Phase 2, which should show up in Phase 2 site.False: WTW should not show up in Phase 2 site';
comment on column coss_dwd.dwd_wtw_verification_di_year.phase_3                 is 'True: WTW has joined Phase 3, which should show up in Phase 3 site.False: WTW should not show up in Phase 3 site';
```

#### select sql

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
    t.verification_id,       -- ID of each online analyzer verification record
    t.wtw_id,               -- ID of the corresponding WTW
    t.status,               -- Status of the reminder:0: reported and not yet approved ;1: approved and require acknowledged.;2: approved/acknowledged and not yet reviewed;3: reviewed;-1: rejected
    t.last_updated_date,    -- Datetime when the record is updated
    t.sample_date,          -- Datetime when the sample is taken
    t.reviewed_date,        -- Datetime when the sample record is reviewed
    t1.wtw_code,            -- WTW Code
    t1.wtw_name,            -- WTW English Name (for Phase 1 & 3 Reporting)
    t1.wtw_name_chi,        -- WTW Chinese Name (for Phase 2 Reporting)
    t1.phase_1,             -- True: WTW has joined Phase 1, which should show up in Phase 1 site.False: WTW should not show up in Phase 1 site
    t1.phase_2,             -- True: WTW has joined Phase 2, which should show up in Phase 2 site.False: WTW should not show up in Phase 2 site
    t1.phase_3,             -- True: WTW has joined Phase 3, which should show up in Phase 3 site.False: WTW should not show up in Phase 3 site
    now() as dwd_update_time,
    now() as dwd_load_time
from
    coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year t
    inner join coss_ods.ods_labconnect_wtw_wtw_unit_df   t1 on t.wtw_id = t1.wtw_id
where t.ods_update_time >= '${dwd_update_time}' and t1.ods_update_time >= '${dwd_update_time}'
ON DUPLICATE KEY update
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



### coss_dwd.dwd_wtw_verification_item_di_year

#### create table

```sql
  
drop table if exists  coss_dwd.dwd_wtw_verification_item_di_year;
create table if not exists coss_dwd.dwd_wtw_verification_item_di_year(
    verification_item_id  int4,                     -- ID of each record item
    verification_id       int4,                     -- ID of the corresponding record
    loc_id                int4,                     -- ID of the sampling location
    loc_full_name         text,                     -- Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.
    loc_name              text,                     -- Name of the location
    loc_suffix            text,                     -- Suffix of the location
    loc_name_chi          text,                     -- Name of the location in Chinese (for reporting)
    sample_date           timestamp,                -- Datetime when the sample is taken
    ph_manual             numeric(8, 5),            -- Sample value of pH from manual test
    ph_manual_dp          int2,                     -- No. of decimal places required for the value from manual test
    ph_analyzer           numeric(8, 5),            -- Sample value of pH from online analyzer
    ph_analyzer_dp        int2,                     -- No. of decimal places required for the value from online analyzer
    ph_remarks            text,                     -- Remarks on the pH sample
    turb_manual           numeric(8, 5),            -- Sample value of Turbidity from manual test
    turb_manual_dp        int2,                     -- No. of decimal places required for the value from manual test
    turb_analyzer         numeric(8, 5),            -- Sample value of Turbidity from online analyzer
    turb_analyzer_dp      int2,                     -- No. of decimal places required for the value from online analyzer
    turb_remarks          text,                     -- Remarks on the Turbidity sample
    rcl2_manual           numeric(8, 5),            -- Sample value of Residual Chlorine from manual test
    rcl2_manual_dp        int2,                     -- No. of decimal places required for the value from manual test
    rcl2_analyzer         numeric(8, 5),            -- Sample value of Residual Chlorine from online analyzer
    rcl2_analyzer_dp      int2,                     -- No. of decimal places required for the value from online analyzer
    rcl2_remarks          text,                     -- Remarks on the sample of Residual Chlorine
    fluoride_manual       numeric(8, 5),            -- Sample value of Fluoride from manual test
    fluoride_manual_dp    int2,                     -- No. of decimal places required for the value from manual test
    fluoride_analyzer     numeric(8, 5),            -- Sample value of Fluoride from online analyzer
    fluoride_analyzer_dp  int2,                     -- No. of decimal places required for the value from online analyzer
    fluoride_remarks      text,                     -- Remarks on the sample of Fluoride
    mn_manual             numeric(8, 5),            -- Sample value of Mangenese from manual test
    mn_manual_dp          int2,                     -- No. of decimal places required for the value from manual test
    mn_analyzer           numeric(8, 5),            -- Sample value of Mangenese from online analyzer
    mn_analyzer_dp        int2,                     -- No. of decimal places required for the value from online analyzer
    mn_remarks            text,                     -- Remarks on the sample of Mangenese
    nh3_manual            numeric(8, 5),            -- Sample value of Ammonia from manual test
    nh3_manual_dp         int2,                     -- No. of decimal places required for the value from manual test
    nh3_analyzer          int4,                     -- Sample value of Ammonia from online analyzer
    nh3_analyzer_dp       int2,                     -- No. of decimal places required for the value from online analyzer
    nh3_remarks           text,                     -- Remarks on the sample of Ammonia
    uv_manual             numeric(8, 5),            -- Sample value of UV light from manual test
    uv_manual_dp          int2,                     -- No. of decimal places required for the value from manual test
    uv_analyzer           int4,                     -- Sample value of UV light from online analyzer
    uv_analyzer_dp        int2,                     -- No. of decimal places required for the value from online analyzer
    uv_remarks            text,                     -- Remarks on the sample of UV light
    dwd_update_time timestamp(6) default current_timestamp,
    dwd_load_time timestamp(6) default current_timestamp,
	CONSTRAINT dwd_wtw_verification_item_di_year_pkey PRIMARY KEY (verification_item_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (verification_item_id)
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
comment on table  coss_dwd.dwd_wtw_verification_item_di_year                         is 'Table to store the sample items in the online analyzer verification results';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.verification_item_id    is 'ID of each record item';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.verification_id         is 'ID of the corresponding record';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_id                  is 'ID of the sampling location';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_full_name           is 'Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_name                is 'Name of the location';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_suffix              is 'Suffix of the location';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.loc_name_chi            is 'Name of the location in Chinese (for reporting)';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.sample_date             is 'Datetime when the sample is taken';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_manual               is 'Sample value of pH from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_manual_dp            is 'No. of decimal places required for the value from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_analyzer             is 'Sample value of pH from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_analyzer_dp          is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.ph_remarks              is 'Remarks on the pH sample';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_manual             is 'Sample value of Turbidity from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_manual_dp          is 'No. of decimal places required for the value from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_analyzer           is 'Sample value of Turbidity from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_analyzer_dp        is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.turb_remarks            is 'Remarks on the Turbidity sample';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_manual             is 'Sample value of Residual Chlorine from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_manual_dp          is 'No. of decimal places required for the value from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_analyzer           is 'Sample value of Residual Chlorine from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_analyzer_dp        is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.rcl2_remarks            is 'Remarks on the sample of Residual Chlorine';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_manual         is 'Sample value of Fluoride from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_manual_dp      is 'No. of decimal places required for the value from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_analyzer       is 'Sample value of Fluoride from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_analyzer_dp    is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.fluoride_remarks        is 'Remarks on the sample of Fluoride';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_manual               is 'Sample value of Mangenese from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_manual_dp            is 'No. of decimal places required for the value from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_analyzer             is 'Sample value of Mangenese from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_analyzer_dp          is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.mn_remarks              is 'Remarks on the sample of Mangenese';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_manual              is 'Sample value of Ammonia from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_manual_dp           is 'No. of decimal places required for the value from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_analyzer            is 'Sample value of Ammonia from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_analyzer_dp         is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.nh3_remarks             is 'Remarks on the sample of Ammonia';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_manual               is 'Sample value of UV light from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_manual_dp            is 'No. of decimal places required for the value from manual test';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_analyzer             is 'Sample value of UV light from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_analyzer_dp          is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dwd.dwd_wtw_verification_item_di_year.uv_remarks              is 'Remarks on the sample of UV light';
```

#### select sql

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
    t1.verification_item_id,      -- ID of each record item
    t1.verification_id,           -- ID of the corresponding record
    t1.loc_id,                    -- ID of the sampling location
    t2.loc_full_name,             -- Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.
    t2.loc_name,                  -- Name of the location
    t2.loc_suffix,                -- Suffix of the location
    t2.loc_name_chi,              -- Name of the location in Chinese (for reporting)
    t.sample_date,                -- Datetime when the sample is taken
    t1.ph_manual,                 -- Sample value of pH from manual test
    t1.ph_manual_dp,              -- No. of decimal places required for the value from manual test
    t1.ph_analyzer,               -- Sample value of pH from online analyzer
    t1.ph_analyzer_dp,            -- No. of decimal places required for the value from online analyzer
    t1.ph_remarks,                -- Remarks on the pH sample
    t1.turb_manual,               -- Sample value of Turbidity from manual test
    t1.turb_manual_dp,            -- No. of decimal places required for the value from manual test
    t1.turb_analyzer,             -- Sample value of Turbidity from online analyzer
    t1.turb_analyzer_dp,          -- No. of decimal places required for the value from online analyzer
    t1.turb_remarks,              -- Remarks on the Turbidity sample
    t1.rcl2_manual,               -- Sample value of Residual Chlorine from manual test
    t1.rcl2_manual_dp,            -- No. of decimal places required for the value from manual test
    t1.rcl2_analyzer,             -- Sample value of Residual Chlorine from online analyzer
    t1.rcl2_analyzer_dp,          -- No. of decimal places required for the value from online analyzer
    t1.rcl2_remarks,              -- Remarks on the sample of Residual Chlorine
    t1.fluoride_manual,           -- Sample value of Fluoride from manual test
    t1.fluoride_manual_dp,        -- No. of decimal places required for the value from manual test
    t1.fluoride_analyzer,         -- Sample value of Fluoride from online analyzer
    t1.fluoride_analyzer_dp,      -- No. of decimal places required for the value from online analyzer
    t1.fluoride_remarks,          -- Remarks on the sample of Fluoride
    t1.mn_manual,                 -- Sample value of Mangenese from manual test
    t1.mn_manual_dp,              -- No. of decimal places required for the value from manual test
    t1.mn_analyzer,               -- Sample value of Mangenese from online analyzer
    t1.mn_analyzer_dp,            -- No. of decimal places required for the value from online analyzer
    t1.mn_remarks,                -- Remarks on the sample of Mangenese
    t1.nh3_manual,                -- Sample value of Ammonia from manual test
    t1.nh3_manual_dp,             -- No. of decimal places required for the value from manual test
    t1.nh3_analyzer,              -- Sample value of Ammonia from online analyzer
    t1.nh3_analyzer_dp,           -- No. of decimal places required for the value from online analyzer
    t1.nh3_remarks,               -- Remarks on the sample of Ammonia
    t1.uv_manual,                 -- Sample value of UV light from manual test
    t1.uv_manual_dp,              -- No. of decimal places required for the value from manual test
    t1.uv_analyzer,               -- Sample value of UV light from online analyzer
    t1.uv_analyzer_dp,            -- No. of decimal places required for the value from online analyzer
    t1.uv_remarks,                -- Remarks on the sample of UV light
    now() as dwd_update_time,
    now() as dwd_load_time
from
    coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_di_year  t
    inner join coss_ods.ods_labconnect_wtw_wqmm_analyzer_verification_item_df  t1 on t.verification_id = t1.verification_id
    inner join coss_ods.ods_labconnect_wtw_wqmm_location_df t2 on t1.loc_id = t2.loc_id
where t.ods_update_time >= '${dwd_update_time}' and t1.ods_update_time >= '${dwd_update_time}'
ON DUPLICATE KEY update
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



# dim

## dim_wtw_etl_water_quality_day（调度任务）

### coss_dim.dim_wtw_water_quality_paramaters

#### create table

```sql
drop table if exists coss_dim.dim_wtw_water_quality_parameters;
create table if not exists coss_dim.dim_wtw_water_quality_parameters(
    config_id                     serial4,          -- ID of each parameter set
    wtw_id                        int4,             -- ID of the corresponding WTW
    i_code                        varchar(255),     -- installations code
    config_type                   int2,             -- Configuration Type 0: parameters for water quality monitoring; 1: parameters for online analyzer verification; 2: sampling frequency
    created_date                  timestamp,        -- Datetime when the record is created
    verification_interval_hr      int2,             -- This field only has meaning if config_type = 2.The interval (hrs) in which the online analyzer verification test is performed. If this field is empty, no online analyzer verification test is required for the specific WTW.
    jar_test_interval_hr          int2,             -- This field only has meaning if config_type = 2.The interval (hrs) in which the jar test is performed. If this field is empty, no jar test is required for the specific WTW.
    jar_measure_type              int2,             -- (if config_type <> 2, use default value 0) 0: the jar test measurement is "絮凝大小"; 1: the jar test measurement is "沉澱速度"
    require_to_test               bool,             -- (if config_type <> 2, use default value false)True: perform taste & odour test;False: no need to perform taste & odour test
    parameter_limit_id            int4,             -- ID of each item in the parameters
    loc_id                        int4,             -- ID of the corresponding sampling location
    target_type                   int2,             -- Target type: 0: operational target; 1: critical limit
    ph_compare                    text,             -- Define whether pH value is acceptable or not
    ph_min_value                  numeric(8, 5),    -- Define whether pH value is acceptable or not
    ph_min_val_dp                 int4,             -- No. of decimal places for min value,-1: if the value is null
    ph_max_value                  numeric(8, 5),    -- Define whether pH value is acceptable or not
    ph_max_val_dp                 int4,             -- No. of decimal places for max value,-1: if the value is null
    turb_compare                  text,             -- Define whether Turbidity value is acceptable or not
    turb_min_value                numeric(8, 5),    -- Define whether Turbidity value is acceptable or not
    turb_min_val_dp               int4,             -- No. of decimal places for min value,-1: if the value is null
    turb_max_value                numeric(8, 5),    -- Define whether Turbidity value is acceptable or not
    turb_max_val_dp               int4,             -- No. of decimal places for max value,-1: if the value is null
    rcl2_compare                  text,             -- Define whether Residual Chlorine is acceptable or not
    rcl2_min_value                numeric(8, 5),    -- Define whether Residual Chlorine is acceptable or not
    rcl2_min_val_dp               int4,             -- No. of decimal places for min value,-1: if the value is null
    rcl2_max_value                numeric(8, 5),    -- Define whether Residual Chlorine is acceptable or not
    rcl2_max_val_dp               int4,             -- No. of decimal places for max value,-1: if the value is null
    uv_compare                    text,             -- Define whether UV light is acceptable or not
    uv_min_value                  numeric(8, 5),    -- Define whether UV light is acceptable or not
    uv_min_val_dp                 int4,             -- No. of decimal places for min value,-1: if the value is null
    uv_max_value                  numeric(8, 5),    -- Define whether UV light is acceptable or not
    uv_max_val_dp                 int4,             -- No. of decimal places for max value,-1: if the value is null
    fluoride_compare              text,             -- Define whether Fluoride is acceptable or not
    fluoride_min_value            numeric(8, 5),    -- Define whether Fluoride is acceptable or not
    fluoride_min_val_dp           int4,             -- No. of decimal places for min value,-1: if the value is null
    fluoride_max_value            numeric(8, 5),    -- Define whether Fluoride is acceptable or not
    fluoride_max_val_dp           int4,             -- No. of decimal places for max value,-1: if the value is null
    mn_compare                    text,             -- Define whether Manganese is acceptable or not
    mn_min_value                  numeric(8, 5),    -- Define whether Manganese is acceptable or not
    mn_min_val_dp                 int4,             -- No. of decimal places for min value,-1: if the value is null
    mn_max_value                  numeric(8, 5),    -- Define whether Manganese is acceptable or not
    mn_max_val_dp                 int4,             -- No. of decimal places for max value,-1: if the value is null
    nh3_compare                   text,             -- Define whether Ammonia is acceptable or not
    nh3_min_value                 numeric(8, 5),    -- Define whether Ammonia is acceptable or not
    nh3_min_val_dp                int4,             -- No. of decimal places for min value,-1: if the value is null
    nh3_max_value                 numeric(8, 5),    -- Define whether Ammonia is acceptable or not
    nh3_max_val_dp                int4,             -- No. of decimal places for max value,-1: if the value is null
    loc_full_name                 text,             -- Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.
    loc_name                      text,             -- Name of the location
    loc_suffix                    text,             -- Suffix of the location
    loc_name_chi                  text,             -- Name of the location in Chinese (for reporting)
    dim_update_time timestamp(6) default current_timestamp,
    dim_load_time timestamp(6) default current_timestamp,
	CONSTRAINT dim_wtw_water_quality_parameters_pkey PRIMARY KEY (parameter_limit_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (parameter_limit_id);
comment on table  coss_dim.dim_wtw_water_quality_parameters                         is 'Table to store all the operational targets and critical limits for water quality monitoring';
comment on column coss_dim.dim_wtw_water_quality_parameters.config_id                 is 'ID of each parameter set';
comment on column coss_dim.dim_wtw_water_quality_parameters.wtw_id                    is 'ID of the corresponding WTW';
comment on column coss_dim.dim_wtw_water_quality_parameters.i_code                    is 'installations code';
comment on column coss_dim.dim_wtw_water_quality_parameters.config_type               is 'Configuration Type 0: parameters for water quality monitoring; 1: parameters for online analyzer verification; 2: sampling frequency';
comment on column coss_dim.dim_wtw_water_quality_parameters.created_date              is 'Datetime when the record is created';
comment on column coss_dim.dim_wtw_water_quality_parameters.verification_interval_hr  is 'This field only has meaning if config_type = 2.The interval (hrs) in which the online analyzer verification test is performed. If this field is empty, no online analyzer verification test is required for the specific WTW.';
comment on column coss_dim.dim_wtw_water_quality_parameters.jar_test_interval_hr      is 'This field only has meaning if config_type = 2.The interval (hrs) in which the jar test is performed. If this field is empty, no jar test is required for the specific WTW.';
comment on column coss_dim.dim_wtw_water_quality_parameters.jar_measure_type          is '(if config_type <> 2, use default value 0) 0: the jar test measurement is "絮凝大小"; 1: the jar test measurement is "沉澱速度"';
comment on column coss_dim.dim_wtw_water_quality_parameters.require_to_test           is '(if config_type <> 2, use default value false)True: perform taste & odour test;False: no need to perform taste & odour test';
comment on column coss_dim.dim_wtw_water_quality_parameters.parameter_limit_id        is 'ID of each item in the parameters';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_id                    is 'ID of the corresponding sampling location';
comment on column coss_dim.dim_wtw_water_quality_parameters.target_type               is 'Target type: 0: operational target; 1: critical limit';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_compare                is 'Define whether pH value is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_min_value              is 'Define whether pH value is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_min_val_dp             is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_max_value              is 'Define whether pH value is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.ph_max_val_dp             is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_compare              is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_min_value            is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_min_val_dp           is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_max_value            is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.turb_max_val_dp           is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_compare              is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_min_value            is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_min_val_dp           is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_max_value            is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.rcl2_max_val_dp           is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_compare                is 'Define whether UV light is acceptable or not';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_min_value              is 'Define whether UV light is acceptable or not';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_min_val_dp             is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_max_value              is 'Define whether UV light is acceptable or not';
comment on column coss_dim.dim_wtw_water_quality_parameters.uv_max_val_dp             is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_compare          is 'Define whether Fluoride is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_min_value        is 'Define whether Fluoride is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_min_val_dp       is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_max_value        is 'Define whether Fluoride is acceptable or not ';
comment on column coss_dim.dim_wtw_water_quality_parameters.fluoride_max_val_dp       is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_compare                is 'Define whether Manganese is acceptable or not';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_min_value              is 'Define whether Manganese is acceptable or not';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_min_val_dp             is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_max_value              is 'Define whether Manganese is acceptable or not';
comment on column coss_dim.dim_wtw_water_quality_parameters.mn_max_val_dp             is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_compare               is 'Define whether Ammonia is acceptable or not';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_min_value             is 'Define whether Ammonia is acceptable or not';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_min_val_dp            is 'No. of decimal places for min value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_max_value             is 'Define whether Ammonia is acceptable or not';
comment on column coss_dim.dim_wtw_water_quality_parameters.nh3_max_val_dp            is 'No. of decimal places for max value,-1: if the value is null';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_full_name             is 'Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_name                  is 'Name of the location';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_suffix                is 'Suffix of the location';
comment on column coss_dim.dim_wtw_water_quality_parameters.loc_name_chi              is 'Name of the location in Chinese (for reporting)';

```

#### select sql

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
;insert into coss_dim.dim_wtw_water_quality_parameters
select
    t.config_id,                              -- ID of each parameter set
    t.wtw_id,                                 -- ID of the corresponding WTW
    case
        when wtw_id = 1 then 'TW025'
        when wtw_id = 2 then 'TW009'
        when wtw_id = 3 then 'TW015'
        when wtw_id = 4 then 'TW019'
        when wtw_id = 5 then 'TW011'
	      else '10000'
    end as i_code,                            -- installations code
    t.config_type,                            -- Configuration Type 0: parameters for water quality monitoring; 1: parameters for online analyzer verification; 2: sampling frequency
    t.effective_date,                         -- Datetime when the record is created
    t.verification_interval_hr,               -- This field only has meaning if config_type = 2.The interval (hrs) in which the online analyzer verification test is performed. If this field is empty, no online analyzer verification test is required for the specific WTW.
    t.jar_test_interval_hr,                   -- This field only has meaning if config_type = 2.The interval (hrs) in which the jar test is performed. If this field is empty, no jar test is required for the specific WTW.
    t.jar_measure_type,                       -- (if config_type <> 2, use default value 0) 0: the jar test measurement is "絮凝大小"; 1: the jar test measurement is "沉澱速度"
    t.require_to_test,                        -- (if config_type <> 2, use default value false)True: perform taste & odour test;False: no need to perform taste & odour test
    t1.parameter_limit_id,                    -- ID of each item in the parameters
    t1.ph_compare,                            -- ID of each item in the parameters
    t1.ph_min_value,                          -- ID of the corresponding sampling location
    t1.ph_min_val_dp,                         -- Target type: 0: operational target; 1: critical limit
    t1.ph_max_value,                          -- Define whether pH value is acceptable or not
    t1.ph_max_val_dp,                         -- Define whether pH value is acceptable or not
    t1.turb_compare,                          -- No. of decimal places for min value,-1: if the value is null
    t1.turb_min_value,                        -- Define whether pH value is acceptable or not
    t1.turb_min_val_dp,                       -- No. of decimal places for max value,-1: if the value is null
    t1.turb_max_value,                        -- Define whether Turbidity value is acceptable or not
    t1.turb_max_val_dp,                       -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare,                          -- No. of decimal places for min value,-1: if the value is null
    t1.rcl2_min_value,                        -- Define whether Turbidity value is acceptable or not
    t1.rcl2_min_val_dp,                       -- No. of decimal places for max value,-1: if the value is null
    t1.rcl2_max_value,                        -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_val_dp,                       -- Define whether Residual Chlorine is acceptable or not
    t1.uv_compare,                            -- No. of decimal places for min value,-1: if the value is null
    t1.uv_min_value,                          -- Define whether Residual Chlorine is acceptable or not
    t1.uv_min_val_dp,                         -- No. of decimal places for max value,-1: if the value is null
    t1.uv_max_value,                          -- Define whether UV light is acceptable or not
    t1.uv_max_val_dp,                         -- Define whether UV light is acceptable or not
    t1.fluoride_compare,                      -- No. of decimal places for min value,-1: if the value is null
    t1.fluoride_min_value,                    -- Define whether UV light is acceptable or not
    t1.fluoride_min_val_dp,                   -- No. of decimal places for max value,-1: if the value is null
    t1.fluoride_max_value,                    -- Define whether Fluoride is acceptable or not
    t1.fluoride_max_val_dp,                   -- Define whether Fluoride is acceptable or not
    t1.mn_compare,                            -- No. of decimal places for min value,-1: if the value is null
    t1.mn_min_value,                          -- Define whether Fluoride is acceptable or not
    t1.mn_min_val_dp,                         -- No. of decimal places for max value,-1: if the value is null
    t1.mn_max_value,                          -- Define whether Manganese is acceptable or not
    t1.mn_max_val_dp,                         -- Define whether Manganese is acceptable or not
    t1.nh3_compare,                           -- No. of decimal places for min value,-1: if the value is null
    t1.nh3_min_value,                         -- Define whether Manganese is acceptable or not
    t1.nh3_min_val_dp,                        -- No. of decimal places for max value,-1: if the value is null
    t1.nh3_max_value,                         -- Define whether Ammonia is acceptable or not
    t1.nh3_max_val_dp,                        -- Define whether Ammonia is acceptable or not
    t2.loc_full_name,                         -- No. of decimal places for min value,-1: if the value is null
    t2.loc_name,                              -- Define whether Ammonia is acceptable or not
    t2.loc_suffix,                            -- No. of decimal places for max value,-1: if the value is null
    t2.loc_name_chi,                          -- Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.
    now() as dim_update_time,
    now() as dim_load_time
from
    coss_ods.ods_labconnect_wtw_wqmm_config_df t
    inner join coss_ods.ods_labconnect_wtw_wqmm_parameter_limit_df t1 on t.config_id  = t1.config_id
    inner join coss_ods.ods_labconnect_wtw_wqmm_location_df t2 on t1.loc_id = t2.loc_id
ON DUPLICATE KEY update
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



# dws

## dws_wtw_etl_water_quality_day（调度）

### coss_dws.dws_wtw_verification_item_di_year

#### create table

```sql
drop table if exists coss_dws.dws_wtw_verification_item_di_year;
create table if not exists coss_dws.dws_wtw_verification_item_di_year(
    verification_id          int4,                 -- ID of each online analyzer verification record
    wtw_id                   int4,                 -- ID of the corresponding WTW
    status                   int2,                 -- Status of the reminder:0: reported and not yet approved ;1: approved and require acknowledged.;2: approved/acknowledged and not yet reviewed;3: reviewed;-1: rejected
    last_updated_date        timestamp,            -- Datetime when the record is updated
    sample_date              timestamp,            -- Datetime when the sample is taken
    reviewed_date            timestamp,            -- Datetime when the sample record is reviewed
    wtw_code                 text,                 -- WTW Code
    wtw_name                 text,                 -- WTW English Name (for Phase 1 & 3 Reporting)
    wtw_name_chi             text,                 -- WTW Chinese Name (for Phase 2 Reporting)
    phase_1                  bool,                 -- True: WTW has joined Phase 1, which should show up in Phase 1 site.False: WTW should not show up in Phase 1 site
    phase_2                  bool,                 -- True: WTW has joined Phase 2, which should show up in Phase 2 site.False: WTW should not show up in Phase 2 site
    phase_3                  bool,                 -- True: WTW has joined Phase 3, which should show up in Phase 3 site.False: WTW should not show up in Phase 3 site
    verification_item_id     int4,                 -- ID of each record item
    loc_id                   int4,                 -- ID of the sampling location
    loc_full_name            text,                 -- Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.
    loc_name                 text,                 -- Name of the location
    loc_suffix               text,                 -- Suffix of the location
    loc_name_chi             text,                 -- Name of the location in Chinese (for reporting)
    ph_manual                numeric(8, 5),        -- Sample value of pH from manual test
    ph_manual_dp             int2,                 -- No. of decimal places required for the value from manual test
    ph_analyzer              numeric(8, 5),        -- Sample value of pH from online analyzer
    ph_analyzer_dp           int2,                 -- No. of decimal places required for the value from online analyzer
    ph_remarks               text,                 -- Remarks on the pH sample
    turb_manual              numeric(8, 5),        -- Sample value of Turbidity from manual test
    turb_manual_dp           int2,                 -- No. of decimal places required for the value from manual test
    turb_analyzer            numeric(8, 5),        -- Sample value of Turbidity from online analyzer
    turb_analyzer_dp         int2,                 -- No. of decimal places required for the value from online analyzer
    turb_remarks             text,                 -- Remarks on the Turbidity sample
    rcl2_manual              numeric(8, 5),        -- Sample value of Residual Chlorine from manual test
    rcl2_manual_dp           int2,                 -- No. of decimal places required for the value from manual test
    rcl2_analyzer            numeric(8, 5),        -- Sample value of Residual Chlorine from online analyzer
    rcl2_analyzer_dp         int2,                 -- No. of decimal places required for the value from online analyzer
    rcl2_remarks             text,                 -- Remarks on the sample of Residual Chlorine
    fluoride_manual          numeric(8, 5),        -- Sample value of Fluoride from manual test
    fluoride_manual_dp       int2,                 -- No. of decimal places required for the value from manual test
    fluoride_analyzer        numeric(8, 5),        -- Sample value of Fluoride from online analyzer
    fluoride_analyzer_dp     int2,                 -- No. of decimal places required for the value from online analyzer
    fluoride_remarks         text,                 -- Remarks on the sample of Fluoride
    mn_manual                numeric(8, 5),        -- Sample value of Mangenese from manual test
    mn_manual_dp             int2,                 -- No. of decimal places required for the value from manual test
    mn_analyzer              numeric(8, 5),        -- Sample value of Mangenese from online analyzer
    mn_analyzer_dp           int2,                 -- No. of decimal places required for the value from online analyzer
    mn_remarks               text,                 -- Remarks on the sample of Mangenese
    nh3_manual               numeric(8, 5),        -- Sample value of Ammonia from manual test
    nh3_manual_dp            int2,                 -- No. of decimal places required for the value from manual test
    nh3_analyzer             int4,                 -- Sample value of Ammonia from online analyzer
    nh3_analyzer_dp          int2,                 -- No. of decimal places required for the value from online analyzer
    nh3_remarks              text,                 -- Remarks on the sample of Ammonia
    uv_manual                numeric(8, 5),        -- Sample value of UV light from manual test
    uv_manual_dp             int2,                 -- No. of decimal places required for the value from manual test
    uv_analyzer              int4,                 -- Sample value of UV light from online analyzer
    uv_analyzer_dp           int2,                 -- No. of decimal places required for the value from online analyzer
    uv_remarks               text,                 -- Remarks on the sample of UV light
    dws_update_time timestamp(6) default current_timestamp,
    dws_load_time timestamp(6) default current_timestamp,
	CONSTRAINT dws_wtw_verification_item_di_year_pkey PRIMARY KEY (verification_item_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (verification_item_id)
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
comment on table  coss_dws.dws_wtw_verification_item_di_year                         is 'Table to store the sample items in the online analyzer verification results';
comment on column coss_dws.dws_wtw_verification_item_di_year.verification_id         is 'ID of each online analyzer verification record';
comment on column coss_dws.dws_wtw_verification_item_di_year.wtw_id                  is 'ID of the corresponding WTW';
comment on column coss_dws.dws_wtw_verification_item_di_year.status                  is 'Status of the reminder:0: reported and not yet approved ;1: approved and require acknowledged.;2: approved/acknowledged and not yet reviewed;3: reviewed;-1: rejected';
comment on column coss_dws.dws_wtw_verification_item_di_year.last_updated_date       is 'Datetime when the record is updated';
comment on column coss_dws.dws_wtw_verification_item_di_year.sample_date             is 'Datetime when the sample is taken';
comment on column coss_dws.dws_wtw_verification_item_di_year.reviewed_date           is 'Datetime when the sample record is reviewed';
comment on column coss_dws.dws_wtw_verification_item_di_year.wtw_code                is 'WTW Code ';
comment on column coss_dws.dws_wtw_verification_item_di_year.wtw_name                is 'WTW English Name (for Phase 1 & 3 Reporting)';
comment on column coss_dws.dws_wtw_verification_item_di_year.wtw_name_chi            is 'WTW Chinese Name (for Phase 2 Reporting)';
comment on column coss_dws.dws_wtw_verification_item_di_year.phase_1                 is 'True: WTW has joined Phase 1, which should show up in Phase 1 site.False: WTW should not show up in Phase 1 site';
comment on column coss_dws.dws_wtw_verification_item_di_year.phase_2                 is 'True: WTW has joined Phase 2, which should show up in Phase 2 site.False: WTW should not show up in Phase 2 site';
comment on column coss_dws.dws_wtw_verification_item_di_year.phase_3                 is 'True: WTW has joined Phase 3, which should show up in Phase 3 site.False: WTW should not show up in Phase 3 site';
comment on column coss_dws.dws_wtw_verification_item_di_year.verification_item_id    is 'ID of each record item';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_id                  is 'ID of the sampling location';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_full_name           is 'Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_name                is 'Name of the location';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_suffix              is 'Suffix of the location';
comment on column coss_dws.dws_wtw_verification_item_di_year.loc_name_chi            is 'Name of the location in Chinese (for reporting)';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_manual               is 'Sample value of pH from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_manual_dp            is 'No. of decimal places required for the value from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_analyzer             is 'Sample value of pH from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_analyzer_dp          is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.ph_remarks              is 'Remarks on the pH sample';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_manual             is 'Sample value of Turbidity from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_manual_dp          is 'No. of decimal places required for the value from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_analyzer           is 'Sample value of Turbidity from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_analyzer_dp        is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.turb_remarks            is 'Remarks on the Turbidity sample';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_manual             is 'Sample value of Residual Chlorine from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_manual_dp          is 'No. of decimal places required for the value from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_analyzer           is 'Sample value of Residual Chlorine from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_analyzer_dp        is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.rcl2_remarks            is 'Remarks on the sample of Residual Chlorine';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_manual         is 'Sample value of Fluoride from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_manual_dp      is 'No. of decimal places required for the value from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_analyzer       is 'Sample value of Fluoride from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_analyzer_dp    is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.fluoride_remarks        is 'Remarks on the sample of Fluoride';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_manual               is 'Sample value of Mangenese from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_manual_dp            is 'No. of decimal places required for the value from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_analyzer             is 'Sample value of Mangenese from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_analyzer_dp          is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.mn_remarks              is 'Remarks on the sample of Mangenese';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_manual              is 'Sample value of Ammonia from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_manual_dp           is 'No. of decimal places required for the value from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_analyzer            is 'Sample value of Ammonia from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_analyzer_dp         is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.nh3_remarks             is 'Remarks on the sample of Ammonia';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_manual               is 'Sample value of UV light from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_manual_dp            is 'No. of decimal places required for the value from manual test';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_analyzer             is 'Sample value of UV light from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_analyzer_dp          is 'No. of decimal places required for the value from online analyzer';
comment on column coss_dws.dws_wtw_verification_item_di_year.uv_remarks              is 'Remarks on the sample of UV light';

```

#### select sql

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
    t.verification_id,               -- ID of each online analyzer verification record
    t.wtw_id,                        -- ID of the corresponding WTW
    t.status,                        -- Status of the reminder:0: reported and not yet approved ;1: approved and require acknowledged.;2: approved/acknowledged and not yet reviewed;3: reviewed;-1: rejected
    t.last_updated_date,             -- Datetime when the record is updated
    t.sample_date,                   -- Datetime when the sample is taken
    t.reviewed_date,                 -- Datetime when the sample record is reviewed
    t.wtw_code,                      -- WTW Code 
    t.wtw_name,                      -- WTW English Name (for Phase 1 & 3 Reporting)
    t.wtw_name_chi,                  -- WTW Chinese Name (for Phase 2 Reporting)
    t.phase_1,                       -- True: WTW has joined Phase 1, which should show up in Phase 1 site.False: WTW should not show up in Phase 1 site
    t.phase_2,                       -- True: WTW has joined Phase 2, which should show up in Phase 2 site.False: WTW should not show up in Phase 2 site
    t.phase_3,                       -- True: WTW has joined Phase 3, which should show up in Phase 3 site.False: WTW should not show up in Phase 3 site
    t1.verification_item_id,         -- ID of each record item
    t1.loc_id,                       -- ID of the sampling location
    t1.loc_full_name,                -- Location full name (including suffices). This field can also be used for translation in UI and labeling in reports.
    t1.loc_name,                     -- Name of the location
    t1.loc_suffix,                   -- Suffix of the location
    t1.loc_name_chi,                 -- Name of the location in Chinese (for reporting)
    t1.ph_manual,                    -- Sample value of pH from manual test
    t1.ph_manual_dp,                 -- No. of decimal places required for the value from manual test
    t1.ph_analyzer,                  -- Sample value of pH from online analyzer
    t1.ph_analyzer_dp,               -- No. of decimal places required for the value from online analyzer
    t1.ph_remarks,                   -- Remarks on the pH sample
    t1.turb_manual,                  -- Sample value of Turbidity from manual test
    t1.turb_manual_dp,               -- No. of decimal places required for the value from manual test
    t1.turb_analyzer,                -- Sample value of Turbidity from online analyzer
    t1.turb_analyzer_dp,             -- No. of decimal places required for the value from online analyzer
    t1.turb_remarks,                 -- Remarks on the Turbidity sample
    t1.rcl2_manual,                  -- Sample value of Residual Chlorine from manual test
    t1.rcl2_manual_dp,               -- No. of decimal places required for the value from manual test
    t1.rcl2_analyzer,                -- Sample value of Residual Chlorine from online analyzer
    t1.rcl2_analyzer_dp,             -- No. of decimal places required for the value from online analyzer
    t1.rcl2_remarks,                 -- Remarks on the sample of Residual Chlorine
    t1.fluoride_manual,              -- Sample value of Fluoride from manual test
    t1.fluoride_manual_dp,           -- No. of decimal places required for the value from manual test
    t1.fluoride_analyzer,            -- Sample value of Fluoride from online analyzer
    t1.fluoride_analyzer_dp,         -- No. of decimal places required for the value from online analyzer
    t1.fluoride_remarks,             -- Remarks on the sample of Fluoride
    t1.mn_manual,                    -- Sample value of Mangenese from manual test
    t1.mn_manual_dp,                 -- No. of decimal places required for the value from manual test
    t1.mn_analyzer,                  -- Sample value of Mangenese from online analyzer
    t1.mn_analyzer_dp,               -- No. of decimal places required for the value from online analyzer
    t1.mn_remarks,                   -- Remarks on the sample of Mangenese
    t1.nh3_manual,                   -- Sample value of Ammonia from manual test
    t1.nh3_manual_dp,                -- No. of decimal places required for the value from manual test
    t1.nh3_analyzer,                 -- Sample value of Ammonia from online analyzer
    t1.nh3_analyzer_dp,              -- No. of decimal places required for the value from online analyzer
    t1.nh3_remarks,                  -- Remarks on the sample of Ammonia
    t1.uv_manual,                    -- Sample value of UV light from manual test
    t1.uv_manual_dp,                 -- No. of decimal places required for the value from manual test
    t1.uv_analyzer,                  -- Sample value of UV light from online analyzer
    t1.uv_analyzer_dp,               -- No. of decimal places required for the value from online analyzer
    t1.uv_remarks,                   -- Remarks on the sample of UV light
    now() as dws_update_time,
    now() as dws_load_time
from 
    coss_dwd.dwd_wtw_verification_di_year t
    inner join coss_dwd.dwd_wtw_verification_item_di_year t1 on t.verification_id = t1.verification_id
where t.dwd_update_time >= '${dws_update_time}' and t1.dwd_update_time >= '${dws_update_time}'
ON DUPLICATE KEY update
    verification_id =  values(verification_id),
    wtw_id =  values(wtw_id),
    status =  values(status),
    last_updated_date =  values(last_updated_date),
    sample_date =  values(sample_date),
    reviewed_date =  values(reviewed_date),
    wtw_code =  values(wtw_code),
    wtw_name =  values(wtw_name),
    wtw_name_chi =  values(wtw_name_chi),
    phase_1 =  values(phase_1),
    phase_2 =  values(phase_2),
    phase_3 =  values(phase_3),
    loc_id =  values(loc_id),
    loc_full_name =  values(loc_full_name),
    loc_name =  values(loc_name),
    loc_suffix =  values(loc_suffix),
    loc_name_chi =  values(loc_name_chi),
    ph_manual =  values(ph_manual),
    ph_manual_dp =  values(ph_manual_dp),
    ph_analyzer =  values(ph_analyzer),
    ph_analyzer_dp =  values(ph_analyzer_dp),
    ph_remarks =  values(ph_remarks),
    turb_manual =  values(turb_manual),
    turb_manual_dp =  values(turb_manual_dp),
    turb_analyzer =  values(turb_analyzer),
    turb_analyzer_dp =  values(turb_analyzer_dp),
    turb_remarks =  values(turb_remarks),
    rcl2_manual =  values(rcl2_manual),
    rcl2_manual_dp =  values(rcl2_manual_dp),
    rcl2_analyzer =  values(rcl2_analyzer),
    rcl2_analyzer_dp =  values(rcl2_analyzer_dp),
    rcl2_remarks =  values(rcl2_remarks),
    fluoride_manual =  values(fluoride_manual),
    fluoride_manual_dp =  values(fluoride_manual_dp),
    fluoride_analyzer =  values(fluoride_analyzer),
    fluoride_analyzer_dp =  values(fluoride_analyzer_dp),
    fluoride_remarks =  values(fluoride_remarks),
    mn_manual =  values(mn_manual),
    mn_manual_dp =  values(mn_manual_dp),
    mn_analyzer =  values(mn_analyzer),
    mn_analyzer_dp =  values(mn_analyzer_dp),
    mn_remarks =  values(mn_remarks),
    nh3_manual =  values(nh3_manual),
    nh3_manual_dp =  values(nh3_manual_dp),
    nh3_analyzer =  values(nh3_analyzer),
    nh3_analyzer_dp =  values(nh3_analyzer_dp),
    nh3_remarks =  values(nh3_remarks),
    uv_manual =  values(uv_manual),
    uv_manual_dp =  values(uv_manual_dp),
    uv_analyzer =  values(uv_analyzer),
    uv_analyzer_dp =  values(uv_analyzer_dp),
    uv_remarks =  values(uv_remarks),
    dws_update_time =  values(dws_update_time)

```



# dm

## dm_wtw_etl_water_quality_day(调度任务)

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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
    where wtw_id = 5
    and loc_id  = 0
    and parameter_limit_id = 45
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```

### coss_dm.dm_wtw_raw_water_quality_di

```sql
drop table if exists coss_dm.dm_wtw_raw_water_quality_di;
create table if not exists coss_dm.dm_wtw_raw_water_quality_di(
    wtw_id           int4,               -- ID of the corresponding WTW
    loc_id           int4,               -- ID of the sampling location
    i_code           varchar(255),       -- installations code
    sample_date      timestamp,          -- Datetime when the sample is taken
    ph_manual        numeric(8, 5),      -- Sample value of pH from manual test
    ph_analyzer      numeric(8, 5),      -- Sample value of pH from online analyzer
    ph_is_pass       int4,               -- ph is pass
    turb_manual      numeric(8, 5),      -- Sample value of Turbidity from manual test
    turb_analyzer    numeric(8, 5),      -- Sample value of Turbidity from online analyzer
    turb_is_pass     int4,               -- turb is pass
    raw_is_pass      int4,               -- raw water is pass
    ph_compare       text,               -- Define whether pH value is acceptable or not 
    ph_min_value     numeric(8, 5),      -- Define whether pH value is acceptable or not 
    ph_max_value     numeric(8, 5),      -- Define whether pH value is acceptable or not 
    turb_compare     text,               -- Define whether Turbidity value is acceptable or not 
    turb_min_value   numeric(8, 5),      -- Define whether Turbidity value is acceptable or not 
    turb_max_value   numeric(8, 5),      -- Define whether Turbidity value is acceptable or not 
    dm_update_time timestamp(6) default current_timestamp,
    dm_load_time timestamp(6) default current_timestamp,
	CONSTRAINT dim_wtw_water_quality_paramaters_pkey PRIMARY KEY (i_code,loc_id,sample_date)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (i_code);
comment on table  coss_dm.dm_wtw_raw_water_quality_di                         is 'WTW raw water quality';
comment on column coss_dm.dm_wtw_raw_water_quality_di.wtw_id                  is 'ID of the corresponding WTW';
comment on column coss_dm.dm_wtw_raw_water_quality_di.loc_id                  is 'ID of the sampling location';
comment on column coss_dm.dm_wtw_raw_water_quality_di.i_code                  is 'installations code';
comment on column coss_dm.dm_wtw_raw_water_quality_di.sample_date             is 'Datetime when the sample is taken';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_manual               is 'Sample value of pH from manual test';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_analyzer             is 'Sample value of pH from online analyzer';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_is_pass              is 'ph is pass';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_manual             is 'Sample value of Turbidity from manual test';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_analyzer           is 'Sample value of Turbidity from online analyzer';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_is_pass            is 'turb is pass';
comment on column coss_dm.dm_wtw_raw_water_quality_di.raw_is_pass             is 'raw water is pass';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_compare              is 'Define whether pH value is acceptable or not ';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_min_value            is 'Define whether pH value is acceptable or not ';
comment on column coss_dm.dm_wtw_raw_water_quality_di.ph_max_value            is 'Define whether pH value is acceptable or not ';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_compare            is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_min_value          is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dm.dm_wtw_raw_water_quality_di.turb_max_value          is 'Define whether Turbidity value is acceptable or not ';

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
-- coss_dim.dim_wtw_water_quality_paramaters
-- target table
-- coss_dm.dm_wtw_raw_water_quality_di
-- ****************************************************************************************
INSERT INTO coss_dm.dm_wtw_raw_water_quality_di (
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
SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.turb_manual, -- Sample value of Turbidity from manual test
    t.turb_analyzer, -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass, -- turb is pass
    IF((IF(t.ph_manual <= t1.ph_max_value, 1, 0) + IF(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) AS raw_is_pass, -- raw water is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.turb_compare, -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value, -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value, -- Define whether Turbidity value is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 1
      AND loc_id = 0
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 1
      AND loc_id = 0
      AND parameter_limit_id = 19
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.turb_manual, -- Sample value of Turbidity from manual test
    t.turb_analyzer, -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass, -- turb is pass
    IF((IF(t.ph_manual <= t1.ph_max_value, 1, 0) + IF(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) AS raw_is_pass, -- raw water is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.turb_compare, -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value, -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value, -- Define whether Turbidity value is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 2
      AND loc_id = 0
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 2
      AND loc_id = 0
      AND parameter_limit_id = 35
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.turb_manual, -- Sample value of Turbidity from manual test
    t.turb_analyzer, -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass, -- turb is pass
    IF((IF(t.ph_manual <= t1.ph_max_value, 1, 0) + IF(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) AS raw_is_pass, -- raw water is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.turb_compare, -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value, -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value, -- Define whether Turbidity value is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 3
      AND loc_id = 0
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 3
      AND loc_id = 0
      AND parameter_limit_id = 9
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.turb_manual, -- Sample value of Turbidity from manual test
    t.turb_analyzer, -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass, -- turb is pass
    IF((IF(t.ph_manual <= t1.ph_max_value, 1, 0) + IF(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) AS raw_is_pass, -- raw water is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.turb_compare, -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value, -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value, -- Define whether Turbidity value is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 4
      AND loc_id = 0
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 4
      AND loc_id = 0
      AND parameter_limit_id = 1
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.turb_manual, -- Sample value of Turbidity from manual test
    t.turb_analyzer, -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass, -- turb is pass
    IF((IF(t.ph_manual <= t1.ph_max_value, 1, 0) + IF(t.turb_manual <= t1.turb_max_value, 1, 0)) = 2, 1, 0) AS raw_is_pass, -- raw water is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.turb_compare, -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value, -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value, -- Define whether Turbidity value is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        0 AS loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        turb_manual,
        turb_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 5
      AND loc_id IN (1, 2)
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        turb_compare,
        turb_min_value,
        turb_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 5
      AND loc_id = 0
      AND parameter_limit_id = 45
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

ON DUPLICATE KEY UPDATE
    wtw_id = VALUES(wtw_id),
    ph_manual = VALUES(ph_manual),
    ph_analyzer = VALUES(ph_analyzer),
    ph_is_pass = VALUES(ph_is_pass),
    turb_manual = VALUES(turb_manual),
    turb_analyzer = VALUES(turb_analyzer),
    turb_is_pass = VALUES(turb_is_pass),
    raw_is_pass = VALUES(raw_is_pass),
    ph_compare = VALUES(ph_compare),
    ph_min_value = VALUES(ph_min_value),
    ph_max_value = VALUES(ph_max_value),
    turb_compare = VALUES(turb_compare),
    turb_min_value = VALUES(turb_min_value),
    turb_max_value = VALUES(turb_max_value),
    dm_update_time = VALUES(dm_update_time);
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
	CONSTRAINT dm_wtw_dosed_water_quality_di_pkey PRIMARY KEY (i_code,loc_id,sample_date)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (i_code);
comment on table  coss_dm.dm_wtw_dosed_water_quality_di                         is 'WTW dosed water quality';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.wtw_id                 is 'ID of the corresponding WTW';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.loc_id                 is 'ID of the sampling location';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.i_code                 is 'installations code';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.sample_date            is 'Datetime when the sample is taken';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_manual              is 'Sample value of pH from manual test';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_analyzer            is 'Sample value of pH from online analyzer';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_is_pass             is 'ph is pass';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_manual            is 'Sample value of Residual Chlorine from manual test';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_analyzer          is 'Sample value of Residual Chlorine from online analyzer';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_is_pass           is 'rcl2 is pass';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.dosed_is_pass          is 'dosed is pass';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_compare             is 'Define whether pH value is acceptable or not ';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_min_value           is 'Define whether pH value is acceptable or not ';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.ph_max_value           is 'Define whether pH value is acceptable or not ';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_compare           is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_min_value         is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dm.dm_wtw_dosed_water_quality_di.rcl2_max_value         is 'Define whether Residual Chlorine is acceptable or not ';
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
-- coss_dim.dim_wtw_water_quality_paramaters
-- target table
-- coss_dm.dm_wtw_dosed_water_quality_di
-- ****************************************************************************************
INSERT INTO coss_dm.dm_wtw_dosed_water_quality_di (
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
SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.rcl2_manual, -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer, -- Sample value of Residual Chlorine from online analyzer
    IF(TRUE, 1, 0) AS rcl2_is_pass, -- rcl2 is pass
    IF((IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0)) + IF(TRUE, 1, 0) = 2, 1, 0) AS dosed_is_pass, -- dosed is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.rcl2_compare, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value, -- Define whether Residual Chlorine is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 1
      AND loc_id = 20
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 1
      AND loc_id = 20
      AND parameter_limit_id = 21
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.rcl2_manual, -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer, -- Sample value of Residual Chlorine from online analyzer
    IF(TRUE, 1, 0) AS rcl2_is_pass, -- rcl2 is pass
    IF((IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0)) + IF(TRUE, 1, 0) = 2, 1, 0) AS dosed_is_pass, -- dosed is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.rcl2_compare, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value,
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 2
      AND loc_id = 20
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 2
      AND loc_id = 20
      AND parameter_limit_id = 37
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.rcl2_manual, -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer, -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass, -- rcl2 is pass
    IF(
        (IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0)) + 
        (IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) AS dosed_is_pass, -- dosed is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.rcl2_compare, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value, -- Define whether Residual Chlorine is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 3
      AND loc_id = 20
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 3
      AND loc_id = 20
      AND parameter_limit_id = 11
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.rcl2_manual, -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer, -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass, -- rcl2 is pass
    IF(
        (IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0)) + 
        (IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) AS dosed_is_pass, -- dosed is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.rcl2_compare, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value, -- Define whether Residual Chlorine is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 4
      AND loc_id = 20
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 4
      AND loc_id = 20
      AND parameter_limit_id = 3
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.ph_manual, -- Sample value of pH from manual test
    t.ph_analyzer, -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass, -- ph is pass
    t.rcl2_manual, -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer, -- Sample value of Residual Chlorine from online analyzer
    IF(TRUE, 1, 0) AS rcl2_is_pass, -- rcl2 is pass
    IF((IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0)) + IF(TRUE, 1, 0) = 2, 1, 0) AS dosed_is_pass, -- dosed is pass
    t1.ph_compare, -- Define whether pH value is acceptable or not
    t1.ph_min_value, -- Define whether pH value is acceptable or not
    t1.ph_max_value, -- Define whether pH value is acceptable or not
    t1.rcl2_compare, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value, -- Define whether Residual Chlorine is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        ph_manual,
        ph_analyzer,
        rcl2_manual,
        rcl2_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 5
      AND loc_id = 20
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        ph_compare,
        ph_min_value,
        ph_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 5
      AND loc_id = 20
      AND parameter_limit_id = 47
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

ON DUPLICATE KEY UPDATE
    wtw_id = VALUES(wtw_id),
    ph_manual = VALUES(ph_manual),
    ph_analyzer = VALUES(ph_analyzer),
    ph_is_pass = VALUES(ph_is_pass),
    rcl2_manual = VALUES(rcl2_manual),
    rcl2_analyzer = VALUES(rcl2_analyzer),
    rcl2_is_pass = VALUES(rcl2_is_pass),
    dosed_is_pass = VALUES(dosed_is_pass),
    ph_compare = VALUES(ph_compare),
    ph_min_value = VALUES(ph_min_value),
    ph_max_value = VALUES(ph_max_value),
    rcl2_compare = VALUES(rcl2_compare),
    rcl2_min_value = VALUES(rcl2_min_value),
    rcl2_max_value = VALUES(rcl2_max_value),
    dm_update_time = VALUES(dm_update_time);
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
    wtw_id             int4,             -- ID of the corresponding WTW
    loc_id             int4,             -- ID of the sampling location
    i_code             varchar(255),     -- installations code
    sample_date        timestamp,        -- Datetime when the sample is taken
    turb_manual        numeric(8, 5),    -- Sample value of Turbidity from manual test
    turb_analyzer      numeric(8, 5),    -- Sample value of Turbidity from online analyzer
    turb_is_pass       int4,             -- turb is pass
    rcl2_manual        numeric(8, 5),    -- Sample value of Residual Chlorine from manual test
    rcl2_analyzer      numeric(8, 5),    -- Sample value of Residual Chlorine from online analyzer
    rcl2_is_pass       int4,             -- rcl2 is pass
    filtered_is_pass   int4,             -- filtered is pass
    turb_compare       text,             -- Define whether Turbidity value is acceptable or not
    turb_min_value     numeric(8, 5),    -- Define whether Turbidity value is acceptable or not
    turb_max_value     numeric(8, 5),    -- Define whether Turbidity value is acceptable or not
    rcl2_compare       text,             -- Define whether Residual Chlorine is acceptable or not
    rcl2_min_value     numeric(8, 5),    -- Define whether Residual Chlorine is acceptable or not
    rcl2_max_value     numeric(8, 5),    -- Define whether Residual Chlorine is acceptable or not
    dm_update_time timestamp(6) default current_timestamp,
    dm_load_time timestamp(6) default current_timestamp,
	CONSTRAINT dm_wtw_filtered_water_quality_di_pkey PRIMARY KEY (i_code,loc_id,sample_date)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (i_code);
comment on table  coss_dm.dm_wtw_filtered_water_quality_di                         is 'WTW filtered water quality';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.wtw_id                  is 'ID of the corresponding WTW';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.loc_id                  is 'ID of the sampling location';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.i_code                  is 'installations code';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.sample_date             is 'Datetime when the sample is taken';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_manual             is 'Sample value of Turbidity from manual test';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_analyzer           is 'Sample value of Turbidity from online analyzer';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_is_pass            is 'turb is pass';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_manual             is 'Sample value of Residual Chlorine from manual test';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_analyzer           is 'Sample value of Residual Chlorine from online analyzer';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_is_pass            is 'rcl2 is pass';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.filtered_is_pass        is 'filtered is pass';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_compare            is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_min_value          is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.turb_max_value          is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_compare            is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_min_value          is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dm.dm_wtw_filtered_water_quality_di.rcl2_max_value          is 'Define whether Residual Chlorine is acceptable or not ';
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
-- coss_dim.dim_wtw_water_quality_paramaters
-- target table
-- coss_dm.dm_wtw_filtered_water_quality_di
-- ****************************************************************************************
INSERT INTO coss_dm.dm_wtw_filtered_water_quality_di (
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
SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.turb_manual, -- Sample value of Turbidity from manual test
    t.turb_analyzer, -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass, -- turb is pass
    t.rcl2_manual, -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer, -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass, -- rcl2 is pass
    IF(
        (IF(t.turb_manual <= t1.turb_max_value, 1, 0)) + 
        (IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) AS filtered_is_pass, -- filtered is pass
    t1.turb_compare, -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value, -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value, -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value, -- Define whether Residual Chlorine is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 1
      AND loc_id = 40
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 1
      AND loc_id = 40
      AND parameter_limit_id = 27
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.turb_manual, -- Sample value of Turbidity from manual test
    t.turb_analyzer, -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass, -- turb is pass
    t.rcl2_manual, -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer, -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass, -- rcl2 is pass
    IF(
        (IF(t.turb_manual <= t1.turb_max_value, 1, 0)) + 
        (IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) AS filtered_is_pass, -- filtered is pass
    t1.turb_compare, -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value, -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value, -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value, -- Define whether Residual Chlorine is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 2
      AND loc_id = 40
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 2
      AND loc_id = 40
      AND parameter_limit_id = 41
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.turb_manual, -- Sample value of Turbidity from manual test
    t.turb_analyzer, -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass, -- turb is pass
    t.rcl2_manual, -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer, -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass, -- rcl2 is pass
    IF(
        (IF(t.turb_manual <= t1.turb_max_value, 1, 0)) + 
        (IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) AS filtered_is_pass, -- filtered is pass
    t1.turb_compare, -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value, -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value, -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value, -- Define whether Residual Chlorine is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 3
      AND loc_id IN (44, 45)
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 3
      AND loc_id IN (44, 45)
      AND parameter_limit_id IN (13, 15)
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id, -- ID of the corresponding WTW
    t.loc_id, -- ID of the sampling location
    t1.i_code, -- installations code
    t.sample_date, -- Datetime when the sample is taken
    t.turb_manual, -- Sample value of Turbidity from manual test
    t.turb_analyzer, -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass, -- turb is pass
    t.rcl2_manual, -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer, -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass, -- rcl2 is pass
    IF(
        (IF(t.turb_manual <= t1.turb_max_value, 1, 0)) + 
        (IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0)) = 2, 
        1, 
        0
    ) AS filtered_is_pass, -- filtered is pass
    t1.turb_compare, -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value, -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value, -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value, -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value, -- Define whether Residual Chlorine is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
        wtw_id,
        loc_id,
        sample_date,
        turb_manual,
        turb_analyzer,
        rcl2_manual,
        rcl2_analyzer
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 4
      AND loc_id = 40
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
        wtw_id,
        loc_id,
        i_code,
        turb_compare,
        turb_min_value,
        turb_max_value,
        rcl2_compare,
        rcl2_min_value,
        rcl2_max_value
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 4
      AND loc_id = 40
      AND parameter_limit_id = 5
) t1 ON t.wtw_id = t1.wtw_id 
    AND t.loc_id = t1.loc_id

ON DUPLICATE KEY UPDATE
    wtw_id = VALUES(wtw_id),
    turb_manual = VALUES(turb_manual),
    turb_analyzer = VALUES(turb_analyzer),
    turb_is_pass = VALUES(turb_is_pass),
    rcl2_manual = VALUES(rcl2_manual),
    rcl2_analyzer = VALUES(rcl2_analyzer),
    rcl2_is_pass = VALUES(rcl2_is_pass),
    filtered_is_pass = VALUES(filtered_is_pass),
    turb_compare = VALUES(turb_compare),
    turb_min_value = VALUES(turb_min_value),
    turb_max_value = VALUES(turb_max_value),
    rcl2_compare = VALUES(rcl2_compare),
    rcl2_min_value = VALUES(rcl2_min_value),
    rcl2_max_value = VALUES(rcl2_max_value),
    dm_update_time = VALUES(dm_update_time);
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
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
from coss_dim.dim_wtw_water_quality_paramaters 
    where wtw_id = 5
    and loc_id = 100
    and parameter_limit_id = 51
)t1 on t.wtw_id = t1.wtw_id and t.loc_id = t1.loc_id
```

### coss_dm.dm_wtw_final_water_quality_di

```sql
drop table if exists coss_dm.dm_wtw_final_water_quality_di;
create table if not exists coss_dm.dm_wtw_final_water_quality_di(
    wtw_id               int4,             -- ID of the corresponding WTW
    loc_id               int4,             -- ID of the sampling location
    i_code               varchar(255),     -- installations code
    sample_date          timestamp,        -- Datetime when the sample is taken
    ph_manual            numeric(8, 5),    -- Sample value of pH from manual test
    ph_analyzer          numeric(8, 5),    -- Sample value of pH from online analyzer
    ph_is_pass           int4,             -- ph is pass
    turb_manual          numeric(8, 5),    -- Sample value of Turbidity from manual test
    turb_analyzer        numeric(8, 5),    -- Sample value of Turbidity from online analyzer
    turb_is_pass         int4,             -- turb is pass
    rcl2_manual          numeric(8, 5),    -- Sample value of Residual Chlorine from manual test
    rcl2_analyzer        numeric(8, 5),    -- Sample value of Residual Chlorine from online analyzer
    rcl2_is_pass         int4,             -- rcl2 is pass
    fluoride_manual      numeric(8, 5),    -- Sample value of Fluoride from manual test
    fluoride_analyzer    numeric(8, 5),    -- Sample value of Fluoride from online analyzer
    fluoride_is_pass     int4,             -- fluoride is pass
    mn_manual            numeric(8, 5),    -- Sample value of Mangenese from manual test
    mn_analyzer          numeric(8, 5),    -- Sample value of Mangenese from online analyzer
    mn_is_pass           int4,             -- mn is pass
    final_is_pass        int4,             -- final is pass
    ph_compare           text,             -- Define whether pH value is acceptable or not
    ph_min_value         numeric(8, 5),    -- Define whether pH value is acceptable or not
    ph_max_value         numeric(8, 5),    -- Define whether pH value is acceptable or not
    turb_compare         text,             -- Define whether Turbidity value is acceptable or not
    turb_min_value       numeric(8, 5),    -- Define whether Turbidity value is acceptable or not
    turb_max_value       numeric(8, 5),    -- Define whether Turbidity value is acceptable or not
    rcl2_compare         text,             -- Define whether Residual Chlorine is acceptable or not
    rcl2_min_value       numeric(8, 5),    -- Define whether Residual Chlorine is acceptable or not
    rcl2_max_value       numeric(8, 5),    -- Define whether Residual Chlorine is acceptable or not
    fluoride_compare     text,             -- Define whether Fluoride is acceptable or not
    fluoride_min_value   numeric(8, 5),    -- Define whether Fluoride is acceptable or not
    fluoride_max_value   numeric(8, 5),    -- Define whether Fluoride is acceptable or not
    mn_compare           text,             -- Define whether Manganese is acceptable or not
    mn_min_value         numeric(8, 5),    -- Define whether Manganese is acceptable or not
    mn_max_value         numeric(8, 5),    -- Define whether Manganese is acceptable or not
    dm_update_time timestamp(6) default current_timestamp,
    dm_load_time timestamp(6) default current_timestamp,
	CONSTRAINT dm_wtw_final_water_quality_di_pkey PRIMARY KEY (i_code,loc_id,sample_date)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
)
distribute by hash (i_code);
comment on table  coss_dm.dm_wtw_final_water_quality_di                         is 'WTW final water quality';
comment on column coss_dm.dm_wtw_final_water_quality_di.wtw_id                  is 'ID of the corresponding WTW';
comment on column coss_dm.dm_wtw_final_water_quality_di.loc_id                  is 'ID of the sampling location';
comment on column coss_dm.dm_wtw_final_water_quality_di.i_code                  is 'installations code';
comment on column coss_dm.dm_wtw_final_water_quality_di.sample_date             is 'Datetime when the sample is taken';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_manual               is 'Sample value of pH from manual test';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_analyzer             is 'Sample value of pH from online analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_is_pass              is 'ph is pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_manual             is 'Sample value of Turbidity from manual test';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_analyzer           is 'Sample value of Turbidity from online analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_is_pass            is 'turb is pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_manual             is 'Sample value of Residual Chlorine from manual test';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_analyzer           is 'Sample value of Residual Chlorine from online analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_is_pass            is 'rcl2 is pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_manual         is 'Sample value of Fluoride from manual test';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_analyzer       is 'Sample value of Fluoride from online analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_is_pass        is 'fluoride is pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_manual               is 'Sample value of Mangenese from manual test';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_analyzer             is 'Sample value of Mangenese from online analyzer';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_is_pass              is 'mn is pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.final_is_pass           is 'final is pass';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_compare              is 'Define whether pH value is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_min_value            is 'Define whether pH value is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.ph_max_value            is 'Define whether pH value is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_compare            is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_min_value          is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.turb_max_value          is 'Define whether Turbidity value is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_compare            is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_min_value          is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.rcl2_max_value          is 'Define whether Residual Chlorine is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_compare        is 'Define whether Fluoride is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_min_value      is 'Define whether Fluoride is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.fluoride_max_value      is 'Define whether Fluoride is acceptable or not ';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_compare              is 'Define whether Manganese is acceptable or not';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_min_value            is 'Define whether Manganese is acceptable or not';
comment on column coss_dm.dm_wtw_final_water_quality_di.mn_max_value            is 'Define whether Manganese is acceptable or not';

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
-- coss_dim.dim_wtw_water_quality_paramaters
-- target table
-- coss_dm.dm_wtw_final_water_quality_di
-- ****************************************************************************************
INSERT INTO coss_dm.dm_wtw_final_water_quality_di (
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
SELECT
    t.wtw_id,                                                                             -- ID of the corresponding WTW
    t.loc_id,                                                                              -- ID of the sampling location
    t1.i_code,                                                                            -- installations code
    t.sample_date,                                                                         -- Datetime when the sample is taken
    t.ph_manual,                                                                           -- Sample value of pH from manual test
    t.ph_analyzer,                                                                         -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass,  -- ph is pass
    t.turb_manual,                                                                         -- Sample value of Turbidity from manual test
    t.turb_analyzer,                                                                       -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass,                          -- turb is pass
    t.rcl2_manual,                                                                         -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer,                                                                       -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass,                          -- rcl2 is pass
    t.fluoride_manual,                                                                     -- Sample value of Fluoride from manual test
    t.fluoride_analyzer,                                                                   -- Sample value of Fluoride from online analyzer
    IF(t.fluoride_manual <= t1.fluoride_max_value, 1, 0) AS fluoride_is_pass,              -- fluoride is pass
    t.mn_manual,                                                                           -- Sample value of Mangenese from manual test
    t.mn_analyzer,                                                                         -- Sample value of Mangenese from online analyzer
    1 AS mn_is_pass,                                                                       -- mn is pass
    IF(
        IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) + 
        IF(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        IF(t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        IF(t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) AS final_is_pass,                                                                    -- final is pass
    t1.ph_compare,                                                                         -- Define whether pH value is acceptable or not
    t1.ph_min_value,                                                                       -- Define whether pH value is acceptable or not
    t1.ph_max_value,                                                                       -- Define whether pH value is acceptable or not
    t1.turb_compare,                                                                       -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare,                                                                       -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.fluoride_compare,                                                                   -- Define whether Fluoride is acceptable or not
    t1.fluoride_min_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.fluoride_max_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.mn_compare,                                                                         -- Define whether Manganese is acceptable or not
    t1.mn_min_value,                                                                       -- Define whether Manganese is acceptable or not
    t1.mn_max_value,                                                                       -- Define whether Manganese is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
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
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 1
      AND loc_id = 100
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
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
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 1
      AND loc_id = 100
      AND parameter_limit_id = 34
) t1 ON t.wtw_id = t1.wtw_id 
   AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id,                                                                             -- ID of the corresponding WTW
    t.loc_id,                                                                              -- ID of the sampling location
    t1.i_code,                                                                            -- installations code
    t.sample_date,                                                                         -- Datetime when the sample is taken
    t.ph_manual,                                                                           -- Sample value of pH from manual test
    t.ph_analyzer,                                                                         -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass,  -- ph is pass
    t.turb_manual,                                                                         -- Sample value of Turbidity from manual test
    t.turb_analyzer,                                                                       -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass,                          -- turb is pass
    t.rcl2_manual,                                                                         -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer,                                                                       -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass,  -- rcl2 is pass
    t.fluoride_manual,                                                                     -- Sample value of Fluoride from manual test
    t.fluoride_analyzer,                                                                   -- Sample value of Fluoride from online analyzer
    IF(t.fluoride_manual >= t1.fluoride_min_value AND t.fluoride_manual <= t1.fluoride_max_value, 1, 0) AS fluoride_is_pass,  -- fluoride is pass
    t.mn_manual,                                                                           -- Sample value of Mangenese from manual test
    t.mn_analyzer,                                                                         -- Sample value of Mangenese from online analyzer
    1 AS mn_is_pass,                                                                       -- mn is pass
    IF(
        IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) + 
        IF(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        IF(t.fluoride_manual >= t1.fluoride_min_value AND t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) AS final_is_pass,                                                                    -- final is pass
    t1.ph_compare,                                                                         -- Define whether pH value is acceptable or not
    t1.ph_min_value,                                                                       -- Define whether pH value is acceptable or not
    t1.ph_max_value,                                                                       -- Define whether pH value is acceptable or not
    t1.turb_compare,                                                                       -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare,                                                                       -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.fluoride_compare,                                                                   -- Define whether Fluoride is acceptable or not
    t1.fluoride_min_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.fluoride_max_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.mn_compare,                                                                         -- Define whether Manganese is acceptable or not
    t1.mn_min_value,                                                                       -- Define whether Manganese is acceptable or not
    t1.mn_max_value,                                                                       -- Define whether Manganese is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
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
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 2
      AND loc_id = 100
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
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
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 2
      AND loc_id = 100
      AND parameter_limit_id = 43
) t1 ON t.wtw_id = t1.wtw_id 
   AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id,                                                                             -- ID of the corresponding WTW
    t.loc_id,                                                                              -- ID of the sampling location
    t1.i_code,                                                                            -- installations code
    t.sample_date,                                                                         -- Datetime when the sample is taken
    t.ph_manual,                                                                           -- Sample value of pH from manual test
    t.ph_analyzer,                                                                         -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass,  -- ph is pass
    t.turb_manual,                                                                         -- Sample value of Turbidity from manual test
    t.turb_analyzer,                                                                       -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass,                          -- turb is pass
    t.rcl2_manual,                                                                         -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer,                                                                       -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass,  -- rcl2 is pass
    t.fluoride_manual,                                                                     -- Sample value of Fluoride from manual test
    t.fluoride_analyzer,                                                                   -- Sample value of Fluoride from online analyzer
    IF(t.fluoride_manual >= t1.fluoride_min_value AND t.fluoride_manual <= t1.fluoride_max_value, 1, 0) AS fluoride_is_pass,  -- fluoride is pass
    t.mn_manual,                                                                           -- Sample value of Mangenese from manual test
    t.mn_analyzer,                                                                         -- Sample value of Mangenese from online analyzer
    1 AS mn_is_pass,                                                                       -- mn is pass
    IF(
        IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) + 
        IF(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        IF(t.fluoride_manual >= t1.fluoride_min_value AND t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) AS final_is_pass,                                                                    -- final is pass
    t1.ph_compare,                                                                         -- Define whether pH value is acceptable or not
    t1.ph_min_value,                                                                       -- Define whether pH value is acceptable or not
    t1.ph_max_value,                                                                       -- Define whether pH value is acceptable or not
    t1.turb_compare,                                                                       -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare,                                                                       -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.fluoride_compare,                                                                   -- Define whether Fluoride is acceptable or not
    t1.fluoride_min_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.fluoride_max_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.mn_compare,                                                                         -- Define whether Manganese is acceptable or not
    t1.mn_min_value,                                                                       -- Define whether Manganese is acceptable or not
    t1.mn_max_value,                                                                       -- Define whether Manganese is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
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
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 3
      AND loc_id = 100
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
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
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 3
      AND loc_id = 100
      AND parameter_limit_id = 17
) t1 ON t.wtw_id = t1.wtw_id 
   AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id,                                                                             -- ID of the corresponding WTW
    t.loc_id,                                                                              -- ID of the sampling location
    t1.i_code,                                                                            -- installations code
    t.sample_date,                                                                         -- Datetime when the sample is taken
    t.ph_manual,                                                                           -- Sample value of pH from manual test
    t.ph_analyzer,                                                                         -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass,  -- ph is pass
    t.turb_manual,                                                                         -- Sample value of Turbidity from manual test
    t.turb_analyzer,                                                                       -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass,                          -- turb is pass
    t.rcl2_manual,                                                                         -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer,                                                                       -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass,  -- rcl2 is pass
    t.fluoride_manual,                                                                     -- Sample value of Fluoride from manual test
    t.fluoride_analyzer,                                                                   -- Sample value of Fluoride from online analyzer
    IF(t.fluoride_manual >= t1.fluoride_min_value AND t.fluoride_manual <= t1.fluoride_max_value, 1, 0) AS fluoride_is_pass,  -- fluoride is pass
    t.mn_manual,                                                                           -- Sample value of Mangenese from manual test
    t.mn_analyzer,                                                                         -- Sample value of Mangenese from online analyzer
    1 AS mn_is_pass,                                                                       -- mn is pass
    IF(
        IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) + 
        IF(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        IF(t.fluoride_manual >= t1.fluoride_min_value AND t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) AS final_is_pass,                                                                    -- final is pass
    t1.ph_compare,                                                                         -- Define whether pH value is acceptable or not
    t1.ph_min_value,                                                                       -- Define whether pH value is acceptable or not
    t1.ph_max_value,                                                                       -- Define whether pH value is acceptable or not
    t1.turb_compare,                                                                       -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare,                                                                       -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.fluoride_compare,                                                                   -- Define whether Fluoride is acceptable or not
    t1.fluoride_min_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.fluoride_max_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.mn_compare,                                                                         -- Define whether Manganese is acceptable or not
    t1.mn_min_value,                                                                       -- Define whether Manganese is acceptable or not
    t1.mn_max_value,                                                                       -- Define whether Manganese is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
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
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 4
      AND loc_id = 100
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
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
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 4
      AND loc_id = 100
      AND parameter_limit_id = 7
) t1 ON t.wtw_id = t1.wtw_id 
   AND t.loc_id = t1.loc_id

UNION ALL

SELECT
    t.wtw_id,                                                                             -- ID of the corresponding WTW
    t.loc_id,                                                                              -- ID of the sampling location
    t1.i_code,                                                                            -- installations code
    t.sample_date,                                                                         -- Datetime when the sample is taken
    t.ph_manual,                                                                           -- Sample value of pH from manual test
    t.ph_analyzer,                                                                         -- Sample value of pH from online analyzer
    IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) AS ph_is_pass,  -- ph is pass
    t.turb_manual,                                                                         -- Sample value of Turbidity from manual test
    t.turb_analyzer,                                                                       -- Sample value of Turbidity from online analyzer
    IF(t.turb_manual <= t1.turb_max_value, 1, 0) AS turb_is_pass,                          -- turb is pass
    t.rcl2_manual,                                                                         -- Sample value of Residual Chlorine from manual test
    t.rcl2_analyzer,                                                                       -- Sample value of Residual Chlorine from online analyzer
    IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) AS rcl2_is_pass,  -- rcl2 is pass
    t.fluoride_manual,                                                                     -- Sample value of Fluoride from manual test
    t.fluoride_analyzer,                                                                   -- Sample value of Fluoride from online analyzer
    IF(t.fluoride_manual >= t1.fluoride_min_value AND t.fluoride_manual <= t1.fluoride_max_value, 1, 0) AS fluoride_is_pass,  -- fluoride is pass
    t.mn_manual,                                                                           -- Sample value of Mangenese from manual test
    t.mn_analyzer,                                                                         -- Sample value of Mangenese from online analyzer
    1 AS mn_is_pass,                                                                       -- mn is pass
    IF(
        IF(t.ph_manual >= t1.ph_min_value AND t.ph_manual <= t1.ph_max_value, 1, 0) + 
        IF(t.turb_manual <= t1.turb_max_value, 1, 0) + 
        IF(t.rcl2_manual >= t1.rcl2_min_value AND t.rcl2_manual <= t1.rcl2_max_value, 1, 0) + 
        IF(t.fluoride_manual >= t1.fluoride_min_value AND t.fluoride_manual <= t1.fluoride_max_value, 1, 0) + 1 = 5, 
        1, 
        0
    ) AS final_is_pass,                                                                    -- final is pass
    t1.ph_compare,                                                                         -- Define whether pH value is acceptable or not
    t1.ph_min_value,                                                                       -- Define whether pH value is acceptable or not
    t1.ph_max_value,                                                                       -- Define whether pH value is acceptable or not
    t1.turb_compare,                                                                       -- Define whether Turbidity value is acceptable or not
    t1.turb_min_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.turb_max_value,                                                                     -- Define whether Turbidity value is acceptable or not
    t1.rcl2_compare,                                                                       -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_min_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.rcl2_max_value,                                                                     -- Define whether Residual Chlorine is acceptable or not
    t1.fluoride_compare,                                                                   -- Define whether Fluoride is acceptable or not
    t1.fluoride_min_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.fluoride_max_value,                                                                 -- Define whether Fluoride is acceptable or not
    t1.mn_compare,                                                                         -- Define whether Manganese is acceptable or not
    t1.mn_min_value,                                                                       -- Define whether Manganese is acceptable or not
    t1.mn_max_value,                                                                       -- Define whether Manganese is acceptable or not
    NOW() AS dm_update_time,
    NOW() AS dm_load_time
FROM (
    SELECT
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
    FROM coss_dws.dws_wtw_verification_item_di_year
    WHERE wtw_id = 5
      AND loc_id = 100
      AND dws_update_time >= '${dm_update_time}'
) t
INNER JOIN (
    SELECT
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
    FROM coss_dim.dim_wtw_water_quality_paramaters
    WHERE wtw_id = 5
      AND loc_id = 100
      AND parameter_limit_id = 51
) t1 ON t.wtw_id = t1.wtw_id 
   AND t.loc_id = t1.loc_id

ON DUPLICATE KEY UPDATE
    wtw_id = VALUES(wtw_id),
    ph_manual = VALUES(ph_manual),
    ph_analyzer = VALUES(ph_analyzer),
    ph_is_pass = VALUES(ph_is_pass),
    turb_manual = VALUES(turb_manual),
    turb_analyzer = VALUES(turb_analyzer),
    turb_is_pass = VALUES(turb_is_pass),
    rcl2_manual = VALUES(rcl2_manual),
    rcl2_analyzer = VALUES(rcl2_analyzer),
    rcl2_is_pass = VALUES(rcl2_is_pass),
    fluoride_manual = VALUES(fluoride_manual),
    fluoride_analyzer = VALUES(fluoride_analyzer),
    fluoride_is_pass = VALUES(fluoride_is_pass),
    mn_manual = VALUES(mn_manual),
    mn_analyzer = VALUES(mn_analyzer),
    mn_is_pass = VALUES(mn_is_pass),
    final_is_pass = VALUES(final_is_pass),
    ph_compare = VALUES(ph_compare),
    ph_min_value = VALUES(ph_min_value),
    ph_max_value = VALUES(ph_max_value),
    turb_compare = VALUES(turb_compare),
    turb_min_value = VALUES(turb_min_value),
    turb_max_value = VALUES(turb_max_value),
    rcl2_compare = VALUES(rcl2_compare),
    rcl2_min_value = VALUES(rcl2_min_value),
    rcl2_max_value = VALUES(rcl2_max_value),
    fluoride_compare = VALUES(fluoride_compare),
    fluoride_min_value = VALUES(fluoride_min_value),
    fluoride_max_value = VALUES(fluoride_max_value),
    mn_compare = VALUES(mn_compare),
    mn_min_value = VALUES(mn_min_value),
    mn_max_value = VALUES(mn_max_value),
    dm_update_time = VALUES(dm_update_time)
```

### coss_dm.dm_wtw_water_quality_verification_item_di

```sql
DROP TABLE if exists  coss_dm.dm_wtw_water_quality_verification_item_di;
CREATE TABLE if not exists coss_dm.dm_wtw_water_quality_verification_item_di (
	verification_id numeric(15) NULL, -- verification item id
	i_code varchar(255) NULL, -- local id
	sample_date timestamp(6) NULL, -- sample date
	verification_item_id numeric(15) NOT NULL, -- verification item id
	loc_id numeric(15) NULL, -- loc id
	loc_full_name varchar(255) NULL, -- local full name
	water_type_code varchar(255) NULL, -- water type code
	water_type_en varchar(255) NULL, -- water type en
	water_type_tc varchar(255) NULL, -- water type tc
	water_type_cn varchar(255) NULL, -- water type cn
	ph_manual numeric(15, 5) NULL, -- ph manual
	turb_manual numeric(15, 5) NULL, -- Turbidity manual
	rcl2_manual numeric(15, 5) NULL, -- Residual chlorine manual
	fluoride_manual numeric(15, 5) NULL, -- fluoride manual
	mn_manual numeric(15, 5) NULL, -- Manganese ions manual
	nh3_manual numeric(15, 5) NULL, -- NH₃ manual
	uv_manual numeric(15, 5) NULL, -- organic matter manual
	dm_update_time timestamp(6) NULL, -- dm update time
	dm_load_time timestamp(6) NULL, -- dm load time
	CONSTRAINT dm_wtw_water_quality_verification_item_di_pkey PRIMARY KEY (verification_item_id)
)
WITH (
	orientation=row,
	compression=no
);
COMMENT ON TABLE coss_dm.dm_wtw_water_quality_verification_item_di IS 'water treatment works of water quality verification item';

-- Column comments

COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.verification_id IS 'verification item id';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.i_code IS 'local id';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.sample_date IS 'sample date';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.verification_item_id IS 'verification item id';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.loc_id IS 'loc id';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.loc_full_name IS 'local full name';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.water_type_code IS 'water type code';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.water_type_en IS 'water type en';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.water_type_tc IS 'water type tc';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.water_type_cn IS 'water type cn';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.ph_manual IS 'ph manual';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.turb_manual IS 'Turbidity manual';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.rcl2_manual IS 'Residual chlorine manual';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.fluoride_manual IS 'fluoride manual';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.mn_manual IS 'Manganese ions manual';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.nh3_manual IS 'NH₃ manual';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.uv_manual IS 'organic matter manual';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.dm_update_time IS 'dm update time';
COMMENT ON COLUMN coss_dm.dm_wtw_water_quality_verification_item_di.dm_load_time IS 'dm load time';

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













