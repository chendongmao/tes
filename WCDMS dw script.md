# ods

## 1.ods_wcdms_tmu_meter_di

```sql
drop table if exists coss_ods.ods_wcdms_tmu_meter_di;

create table if not exists coss_ods.ods_wcdms_tmu_meter_di(
    meter_id         varchar(32),
    meter_no         varchar(12),
    meter_type_code  varchar(20),
    meter_sts_ind    bpchar(1),
    serial_no        varchar(16),
    rcv_date         timestamp(6),
    retire_date      timestamp(6),
    comments         varchar(400),
    retire_rsn_code  varchar(32),
    recond_date      timestamp(6),
    created_by       varchar(20),
    created_date     timestamp(6),
    modified_by      varchar(20),
    modified_date    timestamp(6),
    "timestamp"      timestamp(6),
    ods_update_time  timestamp(6) default pg_systimestamp(),
    ods_load_time    timestamp(6) default pg_systimestamp(),
    primary key(meter_id)
);

comment on table coss_ods.ods_wcdms_tmu_meter_di is 'Customer Meter';
comment on column coss_ods.ods_wcdms_tmu_meter_di.meter_id is 'Meter Id';
comment on column coss_ods.ods_wcdms_tmu_meter_di.meter_no is 'Meter No';
comment on column coss_ods.ods_wcdms_tmu_meter_di.meter_type_code is 'Meter Type Code';
comment on column coss_ods.ods_wcdms_tmu_meter_di.meter_sts_ind is 'Meter Sts Ind';
comment on column coss_ods.ods_wcdms_tmu_meter_di.serial_no is 'Serial No';
comment on column coss_ods.ods_wcdms_tmu_meter_di.rcv_date is 'Receive Date';
comment on column coss_ods.ods_wcdms_tmu_meter_di.retire_date is 'Retire Date';
comment on column coss_ods.ods_wcdms_tmu_meter_di.comments is 'Comments';
comment on column coss_ods.ods_wcdms_tmu_meter_di.retire_rsn_code is 'Retire Rsn Code';
comment on column coss_ods.ods_wcdms_tmu_meter_di.recond_date is 'Recond Date';
comment on column coss_ods.ods_wcdms_tmu_meter_di.created_by is 'Created By';
comment on column coss_ods.ods_wcdms_tmu_meter_di.created_date is 'Created Date';
comment on column coss_ods.ods_wcdms_tmu_meter_di.modified_by is 'Modified By';
comment on column coss_ods.ods_wcdms_tmu_meter_di.modified_date is 'Modified Date';
comment on column coss_ods.ods_wcdms_tmu_meter_di."timestamp" is 'Timestamp';
comment on column coss_ods.ods_wcdms_tmu_meter_di.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_wcdms_tmu_meter_di.ods_load_time is 'Ods Load Time';
```

datax

```sql
select
    "METER_ID"   as meter_id,
    "METER_NO"   as meter_no,
    "METER_TYPE_CODE"   as meter_type_code,
    "METER_STS_IND"   as meter_sts_ind,
    "SERIAL_NO"   as serial_no,
    "RCV_DATE"   as rcv_date,
    "RETIRE_DATE"   as retire_date,
    "COMMENTS"   as comments,
    "RETIRE_RSN_CODE"   as retire_rsn_code,
    "RECOND_DATE"   as recond_date,
    "CREATED_BY"   as created_by,
    "CREATED_DATE"   as created_date,
    "MODIFIED_BY"   as modified_by,
    "MODIFIED_DATE"   as modified_date,
    "TIMESTAMP"   as timestamp,
    current_timestamp    as ods_update_time,
    current_timestamp    as ods_load_time
from wcdms."METER" m 
-- where "MODIFIED_DATE" >= '${modified_date}'
```

etl

```sql
-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function    Describe: Terminal User Meter
-- Create      By: dongmaochen
-- Create      Date: 2025-12-04
-- Modify Date       Modify By       Modify Content
-- None              None            None
-- Source Table
-- wcdms."METER"
-- Target Table
-- coss_ods.ods_wcdms_tmu_meter_di
-- ****************************************************************************************
insert into coss_ods.ods_wcdms_tmu_meter_di (
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
    created_by,
    created_date,
    modified_by,
    modified_date,
    "timestamp",
    ods_update_time,
    ods_load_time
)
select
    meter_id,                     -- Meter Id
    meter_no,                     -- Meter No
    meter_type_code,              -- Meter Type Code
    meter_sts_ind,                -- Meter Sts Ind
    serial_no,                    -- Serial No
    rcv_date,                     -- Receive Date
    retire_date,                  -- Retire Date
    comments,                     -- Comments
    retire_rsn_code,              -- Retire Rsn Code
    recond_date,                  -- Recond Date
    created_by,                   -- Created By
    created_date,                 -- Created Date
    modified_by,                  -- Modified By
    modified_date,                -- Modified Date
    "timestamp",                  -- Timestamp
    current_timestamp,            -- Ods Update Time
    current_timestamp             -- Ods Load Time
from
    coss_ods.ods_wcdms_tmu_meter_di_tmp
on duplicate key update
    meter_no = values(meter_no),
    meter_type_code = values(meter_type_code),
    meter_sts_ind = values(meter_sts_ind),
    serial_no = values(serial_no),
    rcv_date = values(rcv_date),
    retire_date = values(retire_date),
    comments = values(comments),
    retire_rsn_code = values(retire_rsn_code),
    recond_date = values(recond_date),
    created_by = values(created_by),
    created_date = values(created_date),
    modified_by = values(modified_by),
    modified_date = values(modified_date),
    "timestamp" = values("timestamp"),
    ods_update_time = values(ods_update_time)
```



## 2.ods_wcdms_tmu_meter_read_di_year

```sql
drop table if exists coss_ods.ods_wcdms_tmu_meter_read_di_year;

create table if not exists coss_ods.ods_wcdms_tmu_meter_read_di_year(
    meter_read_id               varchar(32),
    meter_read_cyc_code         varchar(32),
    meter_read_route_code       varchar(20),
    meter_read_src_code         varchar(20),
    premise_id                  varchar(32),
    account_id                  varchar(11),
    meter_id                    varchar(32),
    svc_id                      varchar(32),
    read_type_ind               varchar(2),
    meter_reader_id             varchar(32),
    last_billed_date            timestamp(6),
    last_billed_reading         numeric(15, 6),
    last_meter_reading          numeric(15, 6),
    last_meter_read_date        timestamp(6),
    meter_reading               numeric(15, 6),
    meter_reading_consumption   numeric(15, 6),
    meter_read_date             timestamp(6),
    adc_c                       numeric(15, 6),
    adc_p                       numeric(15, 6),
    lo_limit                    numeric(15, 6),
    hi_limit                    numeric(15, 6),
    hilo_exception              varchar(20),
    rollover                    bpchar(1),
    has_exceeded_threshold      bpchar(1),
    est_reading                 numeric(15, 6),
    est_consumption             numeric(15, 6),
    est_date                    timestamp(6),
    est_basis                   varchar(300),
    billed_reading              numeric(15, 6),
    billed_consumption          numeric(15, 6),
    billed_date                 timestamp(6),
    free_consumption            numeric(15, 6),
    billable_sw                 bpchar(1),
    act_id                      varchar(32),
    sec_grp                     varchar(20),
    "timestamp"                 timestamp(6),
    created_by                  varchar(20),
    created_date                timestamp(6),
    modified_by                 varchar(20),
    modified_date               timestamp(6),
    mr_supy_id                  varchar(32),
    sec_userid                  varchar(32),
    meter_no                    varchar(12),
    last_read_type_ind          varchar(2),
    serial_no                   varchar(20),
    is_canceled_sw              bpchar(1),
    canceled_date               timestamp(6),
    canceled_by                 varchar(20),
    mra_type_cd                 varchar(32),
    ods_update_time             timestamp(6) default pg_systimestamp(),
    ods_load_time               timestamp(6) default pg_systimestamp(),
    primary key(meter_read_id)
)
partition by range (meter_read_date)
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

comment on table coss_ods.ods_wcdms_tmu_meter_read_di_year is 'Customer Meter Read';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_read_id is 'Meter Read Id';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_read_cyc_code is 'Meter Read Cyc Code';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_read_route_code is 'Meter Read Route Code';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_read_src_code is 'Meter Read Src Code';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.premise_id is 'Premise Id';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.account_id is 'Account Id';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_id is 'Meter Id';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.svc_id is 'Svc Id';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.read_type_ind is 'Read Type Ind';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_reader_id is 'Meter Reader Id';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.last_billed_date is 'Last Billed Date';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.last_billed_reading is 'Last Billed Reading';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.last_meter_reading is 'Last Meter Reading';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.last_meter_read_date is 'Last Meter Read Date';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_reading is 'Meter Reading';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_reading_consumption is 'Meter Reading Consumption';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_read_date is 'Meter Read Date';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.adc_c is 'Adc C';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.adc_p is 'Adc P';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.lo_limit is 'Lo Limit';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.hi_limit is 'Hi Limit';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.hilo_exception is 'Hilo Exception';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.rollover is 'Rollover';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.has_exceeded_threshold is 'Has Exceeded Threshold';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.est_reading is 'Est Reading';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.est_consumption is 'Est Consumption';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.est_date is 'Est Date';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.est_basis is 'Est Basis';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.billed_reading is 'Billed Reading';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.billed_consumption is 'Billed Consumption';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.billed_date is 'Billed Date';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.free_consumption is 'Free Consumption';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.billable_sw is 'Billable Sw';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.act_id is 'Act Id';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.sec_grp is 'Sec Grp';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year."timestamp" is 'Timestamp';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.created_by is 'Created By';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.created_date is 'Created Date';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.modified_by is 'Modified By';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.modified_date is 'Modified Date';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.mr_supy_id is 'Mr Supy Id';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.sec_userid is 'Sec Userid';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.meter_no is 'Meter No';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.last_read_type_ind is 'Last Read Type Ind';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.serial_no is 'Serial No';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.is_canceled_sw is 'Is Canceled Sw';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.canceled_date is 'Canceled Date';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.canceled_by is 'Canceled By';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.mra_type_cd is 'Mra Type Cd';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_wcdms_tmu_meter_read_di_year.ods_load_time is 'Ods Load Time';
```

datax

```sql
select
    "METER_READ_ID" as meter_read_id,
    "METER_READ_CYC_CODE" as meter_read_cyc_code,
    "METER_READ_ROUTE_CODE" as meter_read_route_code,
    "METER_READ_SRC_CODE" as meter_read_src_code,
    "PREMISE_ID" as premise_id,
    "ACCOUNT_ID" as account_id,
    "METER_ID" as meter_id,
    "SVC_ID" as svc_id,
    "READ_TYPE_IND" as read_type_ind,
    "METER_READER_ID" as meter_reader_id,
    "LAST_BILLED_DATE" as last_billed_date,
    "LAST_BILLED_READING" as last_billed_reading,
    "LAST_METER_READING" as last_meter_reading,
    "LAST_METER_READ_DATE" as last_meter_read_date,
    "METER_READING" as meter_reading,
    "METER_READING_CONSUMPTION" as meter_reading_consumption,
    "METER_READ_DATE" as meter_read_date,
    "ADC_C" as adc_c,
    "ADC_P" as adc_p,
    "LO_LIMIT" as lo_limit,
    "HI_LIMIT" as hi_limit,
    "HILO_EXCEPTION" as hilo_exception,
    "ROLLOVER" as rollover,
    "HAS_EXCEEDED_THRESHOLD" as has_exceeded_threshold,
    "EST_READING" as est_reading,
    "EST_CONSUMPTION" as est_consumption,
    "EST_DATE" as est_date,
    "EST_BASIS" as est_basis,
    "BILLED_READING" as billed_reading,
    "BILLED_CONSUMPTION" as billed_consumption,
    "BILLED_DATE" as billed_date,
    "FREE_CONSUMPTION" as free_consumption,
    "BILLABLE_SW" as billable_sw,
    "ACT_ID" as act_id,
    "SEC_GRP" as sec_grp,
    "TIMESTAMP" as timestamp,
    "CREATED_BY" as created_by,
    "CREATED_DATE" as created_date,
    "MODIFIED_BY" as modified_by,
    "MODIFIED_DATE" as modified_date,
    "MR_SUPY_ID" as mr_supy_id,
    "SEC_USERID" as sec_userid,
    "METER_NO" as meter_no,
    "LAST_READ_TYPE_IND" as last_read_type_ind,
    "SERIAL_NO" as serial_no,
    "IS_CANCELED_SW" as is_canceled_sw,
    "CANCELED_DATE" as canceled_date,
    "CANCELED_BY" as canceled_by,
    "MRA_TYPE_CD" as mra_type_cd,
    current_timestamp as ods_update_time,
    current_timestamp as ods_load_time
from wcdms."METER_READ" mr 
-- where "MODIFIED_DATE" >= '${modified_date}'
```

etl

```sql
-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function    Describe: Terminal User Meter Read Data Insertion and Update
-- Create      By: dongmaochen
-- Create      Date: 2025-12-04
-- Modify Date       Modify By       Modify Content
-- None              None            None
-- Source Table: 
-- wcdms."METER_READ"
-- coss_ods.ods_wcdms_tmu_meter_read_di_year_tmp
-- Target Table: coss_ods.ods_wcdms_tmu_meter_read_di_year
-- ****************************************************************************************
insert into coss_ods.ods_wcdms_tmu_meter_read_di_year (
    meter_read_id,
    meter_read_cyc_code,
    meter_read_route_code,
    meter_read_src_code,
    premise_id,
    account_id,
    meter_id,
    svc_id,
    read_type_ind,
    meter_reader_id,
    last_billed_date,
    last_billed_reading,
    last_meter_reading,
    last_meter_read_date,
    meter_reading,
    meter_reading_consumption,
    meter_read_date,
    adc_c,
    adc_p,
    lo_limit,
    hi_limit,
    hilo_exception,
    rollover,
    has_exceeded_threshold,
    est_reading,
    est_consumption,
    est_date,
    est_basis,
    billed_reading,
    billed_consumption,
    billed_date,
    free_consumption,
    billable_sw,
    act_id,
    sec_grp,
    "timestamp",
    created_by,
    created_date,
    modified_by,
    modified_date,
    mr_supy_id,
    sec_userid,
    meter_no,
    last_read_type_ind,
    serial_no,
    is_canceled_sw,
    canceled_date,
    canceled_by,
    mra_type_cd,
    ods_update_time,
    ods_load_time
)
select
    meter_read_id,                     -- Meter Read Id
    meter_read_cyc_code,               -- Meter Read Cyc Code
    meter_read_route_code,             -- Meter Read Route Code
    meter_read_src_code,               -- Meter Read Src Code
    premise_id,                        -- Premise Id
    account_id,                        -- Account Id
    meter_id,                          -- Meter Id
    svc_id,                            -- Svc Id
    read_type_ind,                     -- Read Type Ind
    meter_reader_id,                   -- Meter Reader Id
    last_billed_date,                  -- Last Billed Date
    last_billed_reading,               -- Last Billed Reading
    last_meter_reading,                -- Last Meter Reading
    last_meter_read_date,              -- Last Meter Read Date
    meter_reading,                     -- Meter Reading
    meter_reading_consumption,         -- Meter Reading Consumption
    meter_read_date,                   -- Meter Read Date
    adc_c,                             -- Adc C
    adc_p,                             -- Adc P
    lo_limit,                          -- Lo Limit
    hi_limit,                          -- Hi Limit
    hilo_exception,                    -- Hilo Exception
    rollover,                          -- Rollover
    has_exceeded_threshold,            -- Has Exceeded Threshold
    est_reading,                       -- Est Reading
    est_consumption,                   -- Est Consumption
    est_date,                          -- Est Date
    est_basis,                         -- Est Basis
    billed_reading,                    -- Billed Reading
    billed_consumption,                -- Billed Consumption
    billed_date,                       -- Billed Date
    free_consumption,                  -- Free Consumption
    billable_sw,                       -- Billable Sw
    act_id,                            -- Act Id
    sec_grp,                           -- Sec Grp
    "timestamp",                       -- Timestamp
    created_by,                        -- Created By
    created_date,                      -- Created Date
    modified_by,                       -- Modified By
    modified_date,                     -- Modified Date
    mr_supy_id,                        -- Mr Supy Id
    sec_userid,                        -- Sec Userid
    meter_no,                          -- Meter No
    last_read_type_ind,                -- Last Read Type Ind
    serial_no,                         -- Serial No
    is_canceled_sw,                    -- Is Canceled Sw
    canceled_date,                     -- Canceled Date
    canceled_by,                       -- Canceled By
    mra_type_cd,                       -- Mra Type Cd
    current_timestamp,                 -- Ods Update Time
    current_timestamp                  -- Ods Load Time
from
    coss_ods.ods_wcdms_tmu_meter_read_di_year_tmp
on duplicate key update
    meter_read_cyc_code = values(meter_read_cyc_code),
    meter_read_route_code = values(meter_read_route_code),
    meter_read_src_code = values(meter_read_src_code),
    premise_id = values(premise_id),
    account_id = values(account_id),
    meter_id = values(meter_id),
    svc_id = values(svc_id),
    read_type_ind = values(read_type_ind),
    meter_reader_id = values(meter_reader_id),
    last_billed_date = values(last_billed_date),
    last_billed_reading = values(last_billed_reading),
    last_meter_reading = values(last_meter_reading),
    last_meter_read_date = values(last_meter_read_date),
    meter_reading = values(meter_reading),
    meter_reading_consumption = values(meter_reading_consumption),
    meter_read_date = values(meter_read_date),
    adc_c = values(adc_c),
    adc_p = values(adc_p),
    lo_limit = values(lo_limit),
    hi_limit = values(hi_limit),
    hilo_exception = values(hilo_exception),
    rollover = values(rollover),
    has_exceeded_threshold = values(has_exceeded_threshold),
    est_reading = values(est_reading),
    est_consumption = values(est_consumption),
    est_date = values(est_date),
    est_basis = values(est_basis),
    billed_reading = values(billed_reading),
    billed_consumption = values(billed_consumption),
    billed_date = values(billed_date),
    free_consumption = values(free_consumption),
    billable_sw = values(billable_sw),
    act_id = values(act_id),
    sec_grp = values(sec_grp),
    "timestamp" = values("timestamp"),
    created_by = values(created_by),
    created_date = values(created_date),
    modified_by = values(modified_by),
    modified_date = values(modified_date),
    mr_supy_id = values(mr_supy_id),
    sec_userid = values(sec_userid),
    meter_no = values(meter_no),
    last_read_type_ind = values(last_read_type_ind),
    serial_no = values(serial_no),
    is_canceled_sw = values(is_canceled_sw),
    canceled_date = values(canceled_date),
    canceled_by = values(canceled_by),
    mra_type_cd = values(mra_type_cd),
    ods_update_time = values(ods_update_time)
```



## 3.ods_wcdms_tmu_cfg_meter_type_di

```sql
drop table if exists coss_ods.ods_wcdms_tmu_cfg_meter_type_di;

create table if not exists coss_ods.ods_wcdms_tmu_cfg_meter_type_di(
    meter_type_code        varchar(20),
    svc_cls_code           varchar(2),
    allow_dup_meter_sw     bpchar(1),
    pre_paid_meter_sw      bpchar(1),
    ctrl_sw                bpchar(1),
    track_loc_ind          varchar(32),
    meter_type_desc        varchar(100),
    meter_type_desc_tc     varchar(100),
    meter_type_desc_sc     varchar(100),
    obs_sw                 bpchar(1),
    created_by             varchar(20),
    created_date           timestamp(6),
    modified_by            varchar(20),
    modified_date          timestamp(6),
    "timestamp"            timestamp(6),
    protocol_code          varchar(20),
    no_of_dgts_lft         numeric(2),
    usage_ind              varchar(2),
    no_of_dgts_rgt         numeric(2),
    uom_code               varchar(32),
    mfr_code               varchar(20),
    model_code             varchar(20),
    ods_update_time        timestamp(6) default pg_systimestamp(),
    ods_load_time          timestamp(6) default pg_systimestamp(),
    primary key(meter_type_code)
);

comment on table coss_ods.ods_wcdms_tmu_cfg_meter_type_di is 'Meter Type Config';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.meter_type_code is 'Meter Type Code';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.svc_cls_code is 'Svc Cls Code';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.allow_dup_meter_sw is 'Allow Dup Meter Sw';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.pre_paid_meter_sw is 'Pre Paid Meter Sw';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.ctrl_sw is 'Ctrl Sw';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.track_loc_ind is 'Track Loc Ind';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.meter_type_desc is 'Meter Type Desc';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.meter_type_desc_tc is 'Meter Type Desc Tc';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.meter_type_desc_sc is 'Meter Type Desc Sc';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.obs_sw is 'Obs Sw';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.created_by is 'Created By';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.created_date is 'Created Date';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.modified_by is 'Modified By';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.modified_date is 'Modified Date';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di."timestamp" is 'Timestamp';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.protocol_code is 'Protocol Code';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.no_of_dgts_lft is 'No Of Dgts Lft';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.usage_ind is 'Usage Ind';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.no_of_dgts_rgt is 'No Of Dgts Rgt';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.uom_code is 'Uom Code';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.mfr_code is 'Mfr Code';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.model_code is 'Model Code';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.ods_update_time is 'Ods Update Time';
comment on column coss_ods.ods_wcdms_tmu_cfg_meter_type_di.ods_load_time is 'Ods Load Time';
```

datax

```sql
select 
    "METER_TYPE_CODE" as meter_type_code,
    "SVC_CLS_CODE" as svc_cls_code,
    "ALLOW_DUP_METER_SW" as allow_dup_meter_sw,
    "PRE_PAID_METER_SW" as pre_paid_meter_sw,
    "CTRL_SW" as ctrl_sw,
    "TRACK_LOC_IND" as track_loc_ind,
    "METER_TYPE_DESC" as meter_type_desc,
    "METER_TYPE_DESC_TC" as meter_type_desc_tc,
    "METER_TYPE_DESC_SC" as meter_type_desc_sc,
    "OBS_SW" as obs_sw,
    "CREATED_BY" as created_by,
    "CREATED_DATE" as created_date,
    "MODIFIED_BY" as modified_by,
    "MODIFIED_DATE" as modified_date,
    "TIMESTAMP" as timestamp,
    "PROTOCOL_CODE" as protocol_code,
    "NO_OF_DGTS_LFT" as no_of_dgts_lft,
    "USAGE_IND" as usage_ind,
    "NO_OF_DGTS_RGT" as no_of_dgts_rgt,
    "UOM_CODE" as uom_code,
    "MFR_CODE" as mfr_code,
    "MODEL_CODE" as model_code,
    current_timestamp as ods_update_time,
    current_timestamp as ods_load_time
from wcdms."CFG_METER_TYPE" cmt 
-- where "MODIFIED_DATE" >= '${modified_date}'
```

etl

```sql
-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function    Describe: Terminal User Meter Type Config Data Insertion and Update
-- Create      By: dongmaochen
-- Create      Date: 2025-12-04
-- Modify Date       Modify By       Modify Content
-- None              None            None
-- Source Table: 
-- wcdms."CFG_METER_TYPE"
-- coss_ods.ods_wcdms_tmu_cfg_meter_type_di_tmp
-- Target Table: 
-- coss_ods.ods_wcdms_tmu_cfg_meter_type_di
-- ****************************************************************************************
insert into coss_ods.ods_wcdms_tmu_cfg_meter_type_di (
    meter_type_code,
    svc_cls_code,
    allow_dup_meter_sw,
    pre_paid_meter_sw,
    ctrl_sw,
    track_loc_ind,
    meter_type_desc,
    meter_type_desc_tc,
    meter_type_desc_sc,
    obs_sw,
    created_by,
    created_date,
    modified_by,
    modified_date,
    "timestamp",
    protocol_code,
    no_of_dgts_lft,
    usage_ind,
    no_of_dgts_rgt,
    uom_code,
    mfr_code,
    model_code,
    ods_update_time,
    ods_load_time
)
select
    meter_type_code,               -- Meter Type Code
    svc_cls_code,                  -- Svc Cls Code
    allow_dup_meter_sw,            -- Allow Dup Meter Sw
    pre_paid_meter_sw,             -- Pre Paid Meter Sw
    ctrl_sw,                       -- Ctrl Sw
    track_loc_ind,                 -- Track Loc Ind
    meter_type_desc,               -- Meter Type Desc
    meter_type_desc_tc,            -- Meter Type Desc Tc
    meter_type_desc_sc,            -- Meter Type Desc Sc
    obs_sw,                        -- Obs Sw
    created_by,                    -- Created By
    created_date,                  -- Created Date
    modified_by,                   -- Modified By
    modified_date,                 -- Modified Date
    "timestamp",                   -- Timestamp
    protocol_code,                 -- Protocol Code
    no_of_dgts_lft,                -- No Of Dgts Lft
    usage_ind,                     -- Usage Ind
    no_of_dgts_rgt,                -- No Of Dgts Rgt
    uom_code,                      -- Uom Code
    mfr_code,                      -- Mfr Code
    model_code,                    -- Model Code
    ods_update_time,               -- Ods Update Time
    ods_load_time                  -- Ods Load Time
from
    coss_ods.ods_wcdms_tmu_cfg_meter_type_di_tmp
on duplicate key update
    svc_cls_code = values(svc_cls_code),
    allow_dup_meter_sw = values(allow_dup_meter_sw),
    pre_paid_meter_sw = values(pre_paid_meter_sw),
    ctrl_sw = values(ctrl_sw),
    track_loc_ind = values(track_loc_ind),
    meter_type_desc = values(meter_type_desc),
    meter_type_desc_tc = values(meter_type_desc_tc),
    meter_type_desc_sc = values(meter_type_desc_sc),
    obs_sw = values(obs_sw),
    created_by = values(created_by),
    created_date = values(created_date),
    modified_by = values(modified_by),
    modified_date = values(modified_date),
    "timestamp" = values("timestamp"),
    protocol_code = values(protocol_code),
    no_of_dgts_lft = values(no_of_dgts_lft),
    usage_ind = values(usage_ind),
    no_of_dgts_rgt = values(no_of_dgts_rgt),
    uom_code = values(uom_code),
    mfr_code = values(mfr_code),
    model_code = values(model_code),
    ods_update_time = values(ods_update_time)
```



# dwd

## 1.dwd_tmu_meter_di

```sql
drop table if exists coss_dwd.dwd_tmu_meter_di;

create table if not exists coss_dwd.dwd_tmu_meter_di(
    meter_id              varchar(32),
    meter_no              varchar(12),
    meter_type_code       varchar(20),
    svc_cls_code          varchar(2),
    allow_dup_meter_sw    bpchar(1),
    pre_paid_meter_sw     bpchar(1),
    ctrl_sw               bpchar(1),
    track_loc_ind         varchar(32),
    meter_type_desc       varchar(100),
    meter_type_desc_tc    varchar(100),
    meter_type_desc_sc    varchar(100),
    obs_sw                bpchar(1),
    protocol_code         varchar(20),
    no_of_dgts_lft        numeric(2),
    usage_ind             varchar(2),
    no_of_dgts_rgt        numeric(2),
    uom_code              varchar(32),
    mfr_code              varchar(20),
    model_code            varchar(20),
    meter_sts_ind         bpchar(1),
    serial_no             varchar(16),
    rcv_date              timestamp(6),
    retire_date           timestamp(6),
    comments              varchar(400),
    retire_rsn_code       varchar(32),
    recond_date           timestamp(6),
    created_date          timestamp(6),
    modified_date         timestamp(6),
    dwd_update_time       timestamp(6) default pg_systimestamp(),
    dwd_load_time         timestamp(6) default pg_systimestamp(),
    primary key(meter_id)
);

comment on table coss_dwd.dwd_tmu_meter_di is 'Customer Meter';
comment on column coss_dwd.dwd_tmu_meter_di.meter_id is 'Meter Id';
comment on column coss_dwd.dwd_tmu_meter_di.meter_no is 'Meter No';
comment on column coss_dwd.dwd_tmu_meter_di.meter_type_code is 'Meter Type Code';
comment on column coss_dwd.dwd_tmu_meter_di.svc_cls_code is 'Svc Cls Code';
comment on column coss_dwd.dwd_tmu_meter_di.allow_dup_meter_sw is 'Allow Dup Meter Sw';
comment on column coss_dwd.dwd_tmu_meter_di.pre_paid_meter_sw is 'Pre Paid Meter Sw';
comment on column coss_dwd.dwd_tmu_meter_di.ctrl_sw is 'Ctrl Sw';
comment on column coss_dwd.dwd_tmu_meter_di.track_loc_ind is 'Track Loc Ind';
comment on column coss_dwd.dwd_tmu_meter_di.meter_type_desc is 'Meter Type Desc';
comment on column coss_dwd.dwd_tmu_meter_di.meter_type_desc_tc is 'Meter Type Desc Tc';
comment on column coss_dwd.dwd_tmu_meter_di.meter_type_desc_sc is 'Meter Type Desc Sc';
comment on column coss_dwd.dwd_tmu_meter_di.obs_sw is 'Obs Sw';
comment on column coss_dwd.dwd_tmu_meter_di.protocol_code is 'Protocol Code';
comment on column coss_dwd.dwd_tmu_meter_di.no_of_dgts_lft is 'No Of Dgts Lft';
comment on column coss_dwd.dwd_tmu_meter_di.usage_ind is 'Usage Ind';
comment on column coss_dwd.dwd_tmu_meter_di.no_of_dgts_rgt is 'No Of Dgts Rgt';
comment on column coss_dwd.dwd_tmu_meter_di.uom_code is 'Uom Code';
comment on column coss_dwd.dwd_tmu_meter_di.mfr_code is 'Mfr Code';
comment on column coss_dwd.dwd_tmu_meter_di.model_code is 'Model Code';
comment on column coss_dwd.dwd_tmu_meter_di.meter_sts_ind is 'Meter Sts Ind';
comment on column coss_dwd.dwd_tmu_meter_di.serial_no is 'Serial No';
comment on column coss_dwd.dwd_tmu_meter_di.rcv_date is 'Receive Date';
comment on column coss_dwd.dwd_tmu_meter_di.retire_date is 'Retire Date';
comment on column coss_dwd.dwd_tmu_meter_di.comments is 'Comments';
comment on column coss_dwd.dwd_tmu_meter_di.retire_rsn_code is 'Retire Rsn Code';
comment on column coss_dwd.dwd_tmu_meter_di.recond_date is 'Recond Date';
comment on column coss_dwd.dwd_tmu_meter_di.created_date is 'Created Date';
comment on column coss_dwd.dwd_tmu_meter_di.modified_date is 'Modified Date';
comment on column coss_dwd.dwd_tmu_meter_di.dwd_update_time is 'Dwd Update Time';
comment on column coss_dwd.dwd_tmu_meter_di.dwd_load_time is 'Dwd Load Time';
```

```sql
-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function    Describe: Terminal User Meter Data Integration (ODS to DWD Layer)
-- Create      By: dongmaochen
-- Create      Date: 2025-12-04
-- Modify Date       Modify By       Modify Content
-- None              None            None
-- Source Table: 
-- coss_ods.ods_wcdms_tmu_meter_di
-- coss_ods.ods_wcdms_tmu_cfg_meter_type_di
-- Target Table: 
-- coss_dwd.dwd_tmu_meter_di
-- ****************************************************************************************
insert into coss_dwd.dwd_tmu_meter_di (
    meter_id,
    meter_no,
    meter_type_code,
    svc_cls_code,
    allow_dup_meter_sw,
    pre_paid_meter_sw,
    ctrl_sw,
    track_loc_ind,
    meter_type_desc,
    meter_type_desc_tc,
    meter_type_desc_sc,
    obs_sw,
    protocol_code,
    no_of_dgts_lft,
    usage_ind,
    no_of_dgts_rgt,
    uom_code,
    mfr_code,
    model_code,
    meter_sts_ind,
    serial_no,
    rcv_date,
    retire_date,
    comments,
    retire_rsn_code,
    recond_date,
    created_date,
    modified_date,
    dwd_update_time,
    dwd_load_time
)
select
    t.meter_id,                     -- Meter Id
    t.meter_no,                     -- Meter No
    t.meter_type_code,              -- Meter Type Code
    t1.svc_cls_code,                -- Svc Cls Code
    t1.allow_dup_meter_sw,          -- Allow Dup Meter Sw
    t1.pre_paid_meter_sw,           -- Pre Paid Meter Sw
    t1.ctrl_sw,                     -- Ctrl Sw
    t1.track_loc_ind,               -- Track Loc Ind
    t1.meter_type_desc,             -- Meter Type Desc
    t1.meter_type_desc_tc,          -- Meter Type Desc Tc
    t1.meter_type_desc_sc,          -- Meter Type Desc Sc
    t1.obs_sw,                      -- Obs Sw
    t1.protocol_code,               -- Protocol Code
    t1.no_of_dgts_lft,              -- No Of Dgts Lft
    t1.usage_ind,                   -- Usage Ind
    t1.no_of_dgts_rgt,              -- No Of Dgts Rgt
    t1.uom_code,                    -- Uom Code
    t1.mfr_code,                    -- Mfr Code
    t1.model_code,                  -- Model Code
    t.meter_sts_ind,                -- Meter Sts Ind
    t.serial_no,                    -- Serial No
    t.rcv_date,                     -- Receive Date
    t.retire_date,                  -- Retire Date
    t.comments,                     -- Comments
    t.retire_rsn_code,              -- Retire Rsn Code
    t.recond_date,                  -- Recond Date
    t.created_date,                 -- Created Date
    t.modified_date,                -- Modified Date
    current_timestamp,              -- Dwd Update Time
    current_timestamp               -- Dwd Load Time
from
    coss_ods.ods_wcdms_tmu_meter_di t
inner join
    coss_ods.ods_wcdms_tmu_cfg_meter_type_di t1 
    on t.meter_type_code = t1.meter_type_code
-- where
--     t.ods_update_time >= '${dwd_update_time}'
on duplicate key update
    meter_no = values(meter_no),
    meter_type_code = values(meter_type_code),
    svc_cls_code = values(svc_cls_code),
    allow_dup_meter_sw = values(allow_dup_meter_sw),
    pre_paid_meter_sw = values(pre_paid_meter_sw),
    ctrl_sw = values(ctrl_sw),
    track_loc_ind = values(track_loc_ind),
    meter_type_desc = values(meter_type_desc),
    meter_type_desc_tc = values(meter_type_desc_tc),
    meter_type_desc_sc = values(meter_type_desc_sc),
    obs_sw = values(obs_sw),
    protocol_code = values(protocol_code),
    no_of_dgts_lft = values(no_of_dgts_lft),
    usage_ind = values(usage_ind),
    no_of_dgts_rgt = values(no_of_dgts_rgt),
    uom_code = values(uom_code),
    mfr_code = values(mfr_code),
    model_code = values(model_code),
    meter_sts_ind = values(meter_sts_ind),
    serial_no = values(serial_no),
    rcv_date = values(rcv_date),
    retire_date = values(retire_date),
    comments = values(comments),
    retire_rsn_code = values(retire_rsn_code),
    recond_date = values(recond_date),
    created_date = values(created_date),
    modified_date = values(modified_date),
    dwd_update_time = values(dwd_update_time); 
```

## 2.dwd_tmu_meter_read_di_year

```sql
drop table if exists coss_dwd.dwd_tmu_meter_read_di_year;

create table if not exists coss_dwd.dwd_tmu_meter_read_di_year (
    meter_read_id               varchar(32) not null,  -- Meter Read Id
    meter_read_cyc_code         varchar(32) null,     -- Meter Read Cyc Code
    meter_read_route_code       varchar(20) null,     -- Meter Read Route Code
    meter_read_src_code         varchar(20) null,     -- Meter Read Src Code
    premise_id                  varchar(32) null,     -- Premise Id
    account_id                  varchar(11) null,     -- Account Id
    meter_id                    varchar(32) null,     -- Meter Id
    svc_id                      varchar(32) null,     -- Svc Id
    read_type_ind               varchar(2) null,      -- Read Type Ind
    meter_reader_id             varchar(32) null,     -- Meter Reader Id
    last_billed_date            timestamp(6) null,    -- Last Billed Date
    last_billed_reading         numeric(15, 6) null,  -- Last Billed Reading
    last_meter_reading          numeric(15, 6) null,  -- Last Meter Reading
    last_meter_read_date        timestamp(6) null,    -- Last Meter Read Date
    meter_reading               numeric(15, 6) null,  -- Meter Reading
    meter_reading_consumption   numeric(15, 6) null,  -- Meter Reading Consumption
    meter_read_date             timestamp(6) null,    -- Meter Read Date
    adc_c                       numeric(15, 6) null,  -- Adc C
    adc_p                       numeric(15, 6) null,  -- Adc P
    lo_limit                    numeric(15, 6) null,  -- Lo Limit
    hi_limit                    numeric(15, 6) null,  -- Hi Limit
    hilo_exception              varchar(20) null,     -- Hilo Exception
    rollover                    bpchar(1) null,       -- Rollover
    has_exceeded_threshold      bpchar(1) null,       -- Has Exceeded Threshold
    est_reading                 numeric(15, 6) null,  -- Est Reading
    est_consumption             numeric(15, 6) null,  -- Est Consumption
    est_date                    timestamp(6) null,    -- Est Date
    est_basis                   varchar(300) null,    -- Est Basis
    billed_reading              numeric(15, 6) null,  -- Billed Reading
    billed_consumption          numeric(15, 6) null,  -- Billed Consumption
    billed_date                 timestamp(6) null,    -- Billed Date
    free_consumption            numeric(15, 6) null,  -- Free Consumption
    billable_sw                 bpchar(1) null,       -- Billable Sw
    act_id                      varchar(32) null,     -- Act Id
    sec_grp                     varchar(20) null,     -- Sec Grp
    "timestamp"                 timestamp(6) null,    -- Timestamp
    created_date                timestamp(6) null,    -- Created Date
    modified_date               timestamp(6) null,    -- Modified Date
    mr_supy_id                  varchar(32) null,     -- Mr Supy Id
    sec_userid                  varchar(32) null,     -- Sec Userid
    meter_no                    varchar(12) null,     -- Meter No
    last_read_type_ind          varchar(2) null,      -- Last Read Type Ind
    serial_no                   varchar(20) null,     -- Serial No
    is_canceled_sw              bpchar(1) null,       -- Is Canceled Sw
    canceled_date               timestamp(6) null,    -- Canceled Date
    canceled_by                 varchar(20) null,     -- Canceled By
    mra_type_cd                 varchar(32) null,     -- Mra Type Cd
    dwd_update_time             timestamp(6) null default pg_systimestamp(),  -- Dwd Update Time
    dwd_load_time               timestamp(6) null default pg_systimestamp(),  -- Dwd Load Time
    primary key(meter_read_id)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
)
partition by range (meter_read_date)
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

comment on table coss_dwd.dwd_tmu_meter_read_di_year is 'Customer Meter Read';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_read_id is 'Meter Read Id';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_read_cyc_code is 'Meter Read Cyc Code';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_read_route_code is 'Meter Read Route Code';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_read_src_code is 'Meter Read Src Code';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.premise_id is 'Premise Id';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.account_id is 'Account Id';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_id is 'Meter Id';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.svc_id is 'Svc Id';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.read_type_ind is 'Read Type Ind';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_reader_id is 'Meter Reader Id';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.last_billed_date is 'Last Billed Date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.last_billed_reading is 'Last Billed Reading';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.last_meter_reading is 'Last Meter Reading';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.last_meter_read_date is 'Last Meter Read Date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_reading is 'Meter Reading';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_reading_consumption is 'Meter Reading Consumption';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_read_date is 'Meter Read Date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.adc_c is 'Adc C';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.adc_p is 'Adc P';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.lo_limit is 'Lo Limit';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.hi_limit is 'Hi Limit';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.hilo_exception is 'Hilo Exception';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.rollover is 'Rollover';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.has_exceeded_threshold is 'Has Exceeded Threshold';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.est_reading is 'Est Reading';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.est_consumption is 'Est Consumption';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.est_date is 'Est Date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.est_basis is 'Est Basis';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.billed_reading is 'Billed Reading';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.billed_consumption is 'Billed Consumption';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.billed_date is 'Billed Date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.free_consumption is 'Free Consumption';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.billable_sw is 'Billable Sw';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.act_id is 'Act Id';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.sec_grp is 'Sec Grp';
comment on column coss_dwd.dwd_tmu_meter_read_di_year."timestamp" is 'Timestamp';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.created_date is 'Created Date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.modified_date is 'Modified Date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.mr_supy_id is 'Mr Supy Id';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.sec_userid is 'Sec Userid';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.meter_no is 'Meter No';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.last_read_type_ind is 'Last Read Type Ind';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.serial_no is 'Serial No';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.is_canceled_sw is 'Is Canceled Sw';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.canceled_date is 'Canceled Date';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.canceled_by is 'Canceled By';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.mra_type_cd is 'Mra Type Cd';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.dwd_update_time is 'Dwd Update Time';
comment on column coss_dwd.dwd_tmu_meter_read_di_year.dwd_load_time is 'Dwd Load Time';
```

```sql
-- ****************************************************************************************
-- Subject     Areas: Terminal User
-- Function    Describe: Terminal User Meter Reading Data Integration (ODS to DWD Layer)
-- Create      By: dongmaochen
-- Create      Date: 2025-12-04
-- Modify Date       Modify By       Modify Content
-- None              None            None
-- Source Table: 
-- coss_ods.ods_wcdms_tmu_meter_read_di_year
-- Target Table: 
-- coss_dwd.dwd_tmu_meter_read_di_year
-- ****************************************************************************************
insert into coss_dwd.dwd_tmu_meter_read_di_year (
    meter_read_id,
    meter_read_cyc_code,
    meter_read_route_code,
    meter_read_src_code,
    premise_id,
    account_id,
    meter_id,
    svc_id,
    read_type_ind,
    meter_reader_id,
    last_billed_date,
    last_billed_reading,
    last_meter_reading,
    last_meter_read_date,
    meter_reading,
    meter_reading_consumption,
    meter_read_date,
    adc_c,
    adc_p,
    lo_limit,
    hi_limit,
    hilo_exception,
    rollover,
    has_exceeded_threshold,
    est_reading,
    est_consumption,
    est_date,
    est_basis,
    billed_reading,
    billed_consumption,
    billed_date,
    free_consumption,
    billable_sw,
    act_id,
    sec_grp,
    "timestamp",
    created_date,
    modified_date,
    mr_supy_id,
    sec_userid,
    meter_no,
    last_read_type_ind,
    serial_no,
    is_canceled_sw,
    canceled_date,
    canceled_by,
    mra_type_cd,
    dwd_update_time,
    dwd_load_time
)
select
    meter_read_id,                     -- Meter Read Id
    meter_read_cyc_code,               -- Meter Read Cyc Code
    meter_read_route_code,             -- Meter Read Route Code
    meter_read_src_code,               -- Meter Read Src Code
    premise_id,                        -- Premise Id
    account_id,                        -- Account Id
    meter_id,                          -- Meter Id
    svc_id,                            -- Svc Id
    read_type_ind,                     -- Read Type Ind
    meter_reader_id,                   -- Meter Reader Id
    last_billed_date,                  -- Last Billed Date
    last_billed_reading,               -- Last Billed Reading
    last_meter_reading,                -- Last Meter Reading
    last_meter_read_date,              -- Last Meter Read Date
    meter_reading,                     -- Meter Reading
    meter_reading_consumption,         -- Meter Reading Consumption
    meter_read_date,                   -- Meter Read Date
    adc_c,                             -- Adc C
    adc_p,                             -- Adc P
    lo_limit,                          -- Lo Limit
    hi_limit,                          -- Hi Limit
    hilo_exception,                    -- Hilo Exception
    rollover,                          -- Rollover
    has_exceeded_threshold,            -- Has Exceeded Threshold
    est_reading,                       -- Est Reading
    est_consumption,                   -- Est Consumption
    est_date,                          -- Est Date
    est_basis,                         -- Est Basis
    billed_reading,                    -- Billed Reading
    billed_consumption,                -- Billed Consumption
    billed_date,                       -- Billed Date
    free_consumption,                  -- Free Consumption
    billable_sw,                       -- Billable Sw
    act_id,                            -- Act Id
    sec_grp,                           -- Sec Grp
    "timestamp",                       -- Timestamp
    created_date,                      -- Created Date
    modified_date,                     -- Modified Date
    mr_supy_id,                        -- Mr Supy Id
    sec_userid,                        -- Sec Userid
    meter_no,                          -- Meter No
    last_read_type_ind,                -- Last Read Type Ind
    serial_no,                         -- Serial No
    is_canceled_sw,                    -- Is Canceled Sw
    canceled_date,                     -- Canceled Date
    canceled_by,                       -- Canceled By
    mra_type_cd,                       -- Mra Type Cd
    current_timestamp dwd_update_time,                   -- Dwd Update Time
    current_timestamp dwd_load_time                      -- Dwd Load Time
from
    coss_ods.ods_wcdms_tmu_meter_read_di_year
-- where 
-- 	ods_update_time >= '${dwd_update_time}'
on duplicate key update
    meter_read_cyc_code = values(meter_read_cyc_code),
    meter_read_route_code = values(meter_read_route_code),
    meter_read_src_code = values(meter_read_src_code),
    premise_id = values(premise_id),
    account_id = values(account_id),
    meter_id = values(meter_id),
    svc_id = values(svc_id),
    read_type_ind = values(read_type_ind),
    meter_reader_id = values(meter_reader_id),
    last_billed_date = values(last_billed_date),
    last_billed_reading = values(last_billed_reading),
    last_meter_reading = values(last_meter_reading),
    last_meter_read_date = values(last_meter_read_date),
    meter_reading = values(meter_reading),
    meter_reading_consumption = values(meter_reading_consumption),
    meter_read_date = values(meter_read_date),
    adc_c = values(adc_c),
    adc_p = values(adc_p),
    lo_limit = values(lo_limit),
    hi_limit = values(hi_limit),
    hilo_exception = values(hilo_exception),
    rollover = values(rollover),
    has_exceeded_threshold = values(has_exceeded_threshold),
    est_reading = values(est_reading),
    est_consumption = values(est_consumption),
    est_date = values(est_date),
    est_basis = values(est_basis),
    billed_reading = values(billed_reading),
    billed_consumption = values(billed_consumption),
    billed_date = values(billed_date),
    free_consumption = values(free_consumption),
    billable_sw = values(billable_sw),
    act_id = values(act_id),
    sec_grp = values(sec_grp),
    "timestamp" = values("timestamp"),
    created_date = values(created_date),
    modified_date = values(modified_date),
    mr_supy_id = values(mr_supy_id),
    sec_userid = values(sec_userid),
    meter_no = values(meter_no),
    last_read_type_ind = values(last_read_type_ind),
    serial_no = values(serial_no),
    is_canceled_sw = values(is_canceled_sw),
    canceled_date = values(canceled_date),
    canceled_by = values(canceled_by),
    mra_type_cd = values(mra_type_cd),
    dwd_update_time = values(dwd_update_time)
```

