# 源系统数据表

-- abpms.give_up definition

-- Drop table

-- DROP TABLE abpms.give_up;

CREATE TABLE abpms.give_up (
	give_up_id bpchar(12) NOT NULL,
	give_up_type_ind bpchar(1) NOT NULL,
	give_up_sts_ind bpchar(1) NOT NULL,
	eff_date timestamp(0) NOT NULL,
	phone_no varchar(24) NULL,
	account_id bpchar(10) NOT NULL,
	mail_addr_sw bpchar(1) NULL,
	addr_line1 varchar(64) NULL,
	addr_line2 varchar(64) NULL,
	addr_line3 varchar(64) NULL,
	premise_id bpchar(10) NOT NULL,
	meter_read_id varchar(32) NULL,
	reading numeric(15, 4) NULL,
	meter_read_date timestamp(0) NULL,
	deposit_retain_ind varchar(16) NULL,
	meter_read_src_code varchar(12) NULL,
	inc_ch varchar(16) NULL,
	canc_rsn_code varchar(4) NULL,
	ref_no varchar(8) NULL,
	cust_comm_id bpchar(10) NULL,
	sys_log varchar(256) NULL,
	created_by varchar(50) NOT NULL,
	created_date timestamp(0) NOT NULL,
	modified_by varchar(50) NOT NULL,
	modified_date timestamp(0) NOT NULL,
	"timestamp" timestamp(6) NOT NULL,
	submitted_date timestamp(0) NULL,
	bill_win_end_date timestamp(0) NULL,
	supervisor_override bool NULL,
	icms_id varchar(32) NULL,
	workflow_id varchar(32) NULL,
	letter_id varchar(32) NULL,
	letter_date timestamp(0) NULL,
	pems_id varchar(32) NULL,
	automation_id bpchar(10) NULL,
	CONSTRAINT give_up_pkey PRIMARY KEY (give_up_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=USTORE,
	segment=off
);
CREATE INDEX idx_give_up_01 ON abpms.give_up USING ubtree (premise_id) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_give_up_02 ON abpms.give_up USING ubtree (account_id) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_give_up_03 ON abpms.give_up USING ubtree (created_by) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_give_up_04 ON abpms.give_up USING ubtree (created_date, created_by) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_give_up_05 ON abpms.give_up USING ubtree (modified_date, modified_by) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_give_up_06 ON abpms.give_up USING ubtree (cust_comm_id) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_give_up_07 ON abpms.give_up USING ubtree (give_up_sts_ind) WITH (storage_type=ustore) TABLESPACE pg_default;

-- Permissions;





-- abpms.adj definition

-- Drop table

-- DROP TABLE abpms.adj;

CREATE TABLE abpms.adj (
	adj_id bpchar(12) NOT NULL,
	svc_id bpchar(10) NOT NULL,
	adj_type_code varchar(8) NOT NULL,
	adj_sts_ind bpchar(2) NOT NULL,
	created_date timestamp(0) NOT NULL,
	canc_rsn_code varchar(4) NULL,
	adj_amt numeric(15, 2) NOT NULL,
	txfr_adj_id bpchar(12) NULL,
	rmk varchar(254) NULL,
	base_amt numeric(15, 2) NOT NULL,
	created_by varchar(50) NOT NULL,
	modified_by varchar(50) NOT NULL,
	modified_date timestamp(0) NOT NULL,
	"timestamp" timestamp(6) NOT NULL,
	bill_id bpchar(12) NULL,
	pems_id varchar(40) NULL,
	workflow_id varchar(40) NULL,
	CONSTRAINT adj_pkey PRIMARY KEY (adj_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=USTORE,
	segment=off
);
CREATE INDEX idx_adj_01 ON abpms.adj USING ubtree (svc_id, adj_type_code) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_adj_02 ON abpms.adj USING ubtree (adj_id, txfr_adj_id) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_adj_03 ON abpms.adj USING ubtree (bill_id) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_adj_04 ON abpms.adj USING ubtree (adj_type_code, adj_sts_ind) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_bc397_adj_refund_recent ON abpms.adj USING ubtree (created_date, adj_id) WITH (storage_type=USTORE) TABLESPACE pg_default WHERE (((adj_type_code)::text = ANY ((ARRAY['REFUNDG'::character varying, 'REFDEPG'::character varying, 'REFUDEPG'::character varying])::text[])) AND (adj_sts_ind <> ALL (ARRAY['10'::bpchar, '30'::bpchar])));

-- Permissions;







-- abpms.adj_refund_chq definition

-- Drop table

-- DROP TABLE abpms.adj_refund_chq;

CREATE TABLE abpms.adj_refund_chq (
	adj_refund_chq_id bpchar(12) NOT NULL,
	adj_id bpchar(12) NOT NULL,
	addr_line1 varchar(64) NULL,
	addr_line2 varchar(64) NULL,
	addr_line3 varchar(64) NULL,
	addr_line4 varchar(64) NULL,
	paid_amt numeric(15, 2) NULL,
	sched_payment_date timestamp(0) NULL,
	payment_date timestamp(0) NULL,
	pst_name varchar(64) NOT NULL,
	payment_doc_id varchar(20) NULL,
	payment_doc_date timestamp(0) NULL,
	payment_id bpchar(12) NULL,
	payment_method_ind varchar(10) NULL,
	payment_select_sts_ind bpchar(1) NULL,
	batch_job_code varchar(8) NOT NULL,
	batch_no numeric(10) NOT NULL,
	fin_year numeric(4) NULL,
	dvn varchar(12) NULL,
	user_code varchar(19) NULL,
	batch_ref varchar(20) NULL,
	adj_refund_chq_desc1 varchar(30) NULL,
	adj_refund_chq_desc2 varchar(30) NULL,
	vio bpchar(1) NULL,
	next_auth_id numeric(8) NULL,
	prepared_by numeric(8) NULL,
	adj_refund_chq_sts_ind varchar(2) NULL,
	generated_by varchar(8) NULL,
	generated_date timestamp(0) NULL,
	lang_code bpchar(1) NULL,
	payee_type varchar(10) NULL,
	creditor_ref_no varchar(30) NULL,
	payment_vou_no varchar(20) NULL,
	treasury_vou_no varchar(20) NULL,
	chq_no varchar(10) NULL,
	voucher_amt numeric(15, 2) NULL,
	rmk varchar(254) NULL,
	created_by varchar(50) NOT NULL,
	created_date timestamp(0) NOT NULL,
	modified_by varchar(50) NOT NULL,
	modified_date timestamp(0) NOT NULL,
	"timestamp" timestamp(6) NOT NULL,
	CONSTRAINT adj_refund_chq_pkey PRIMARY KEY (adj_refund_chq_id)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=USTORE,
	segment=off
);
CREATE INDEX idx_adj_refund_chq_01 ON abpms.adj_refund_chq USING ubtree (adj_id) WITH (storage_type=ustore) TABLESPACE pg_default;
CREATE INDEX idx_adj_refund_chq_02 ON abpms.adj_refund_chq USING ubtree (dvn) WITH (storage_type=ustore) TABLESPACE pg_default;

-- Permissions;





# 样例sql：



## 2.ods_abpms_tmu_svc_dtl_di

### create sql

```sql
drop table if exists coss_ods.ods_abpms_tmu_svc_dtl_di;
create table if not exists coss_ods.ods_abpms_tmu_svc_dtl_di (
    svc_id bpchar(10) null,                        -- Service Id
    svc_type_code varchar(8) null,                 -- Service Type Code
    start_date timestamp(6) null,                  -- Start Date
    svc_dtl_sts_ind bpchar(2) null,                -- Sd Status Indicator
    account_id bpchar(10) null,                    -- Account Id
    end_date timestamp(6) null,                    -- End Date
    wis_account_no varchar(15) null,               -- Wis Account Number
    cust_read_sw bpchar(1) null,                   -- Whether To Support Customer Self-Uploaded Meter Readings
    hsic_code varchar(8) null,                     -- Industry Classification Hsic Code
    request_deposit_amt numeric(15, 2) null,       -- Deposit Amount
    svc_dtl_relation_id varchar(10) null,          -- Service Detail Relationship Id
    start_req_by varchar(50) null,                 -- If The Sd Status Is 20 (Active), Fill In Cc Create_By To This Field.
    stop_req_by varchar(50) null,                  -- If The Sd Status Is 40 (Discontinued), Fill In Cc Create_By To This Field.
    high_bill_amt numeric(15, 2) null,             -- Used For Generating Some Reports.
    exp_date timestamp(6) null,                    -- When Cc Creates A Locksmith Sd, Check If This Field Is Expired. If The Sd Status Is Expired, Change It To 40 And Fill In Enddate.
    created_by varchar(8) null,                    -- Creator
    created_date timestamp(6) null,                -- Creation Time
    modified_by varchar(8) null,                   -- Updater
    modified_date timestamp(6) null,               -- Update Time
    "timestamp" timestamp(6) null,                 -- Timestamp
    premise_id bpchar(10) null,                    -- Building Id
    svc_dtl_start_date timestamp(6) null,          -- When The First Meter Reading Is Done, Record The Startdate In Bitem To Calculate Water Usage.
    start_meter_read_id bpchar(12) null,           -- When Opening A Bill For The First Time, Use This To Retrieve The First Meter Reading Form.
    svc_dtl_stop_date timestamp(6) null,           -- Service Detail End Date
    usage_ind varchar(2) null,                     -- Only One Value, '+' When Creating A Bitem Account, This Field Is Synchronized To Bitem.
    stop_meter_read_id bpchar(12) null,            -- Stop Meter Reading Id
    rmk varchar(500) null,                         -- Notes
    workflow_id bpchar(50) null,                   -- Work Order Id
    instal_svc_dtl_for_deposit_sw bpchar(1) null,  -- Deposit Download Service Details Switch
    start_rsn_ind varchar(4) null,                 -- Start Reason Indicator
    stop_rsn_ind varchar(4) null,                  -- End Reason Indicator
    no_payment_periods numeric null,               -- Non-Payment Deadline
    cust_comm_id bpchar(12) null,                  -- Ccid
    special_usage_ind varchar(4) null,             -- Prop And Null
    ods_load_time timestamp(6) default pg_systimestamp(),                    -- Data Loading Time
    ods_update_time timestamp(6) default pg_systimestamp(),                  -- Data Update Time
    primary key(svc_id)
)
with (
    orientation=row,
    compression=no
);

comment on table  coss_ods.ods_abpms_tmu_svc_dtl_di                                    is 'Service Details, User Account Billing Intermediate Table, Through Which Prices And Some Switches Required For Billing Can Be Obtained';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.svc_id                             is 'Service Id';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.svc_type_code                      is 'Service Type Code';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.start_date                         is 'Start Date';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.svc_dtl_sts_ind                    is 'Sd Status Indicator';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.account_id                         is 'Account Id';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.end_date                           is 'End Date';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.wis_account_no                     is 'Wis Account Number';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.cust_read_sw                       is 'Whether To Support Customer Self-Uploaded Meter Readings';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.hsic_code                          is 'Industry Classification Hsic Code';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.request_deposit_amt                is 'Deposit Amount';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.svc_dtl_relation_id                is 'Service Detail Relationship Id';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.start_req_by                       is 'If The Sd Status Is 20 (Active), Fill In Cc Create_By To This Field.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.stop_req_by                        is 'If The Sd Status Is 40 (Discontinued), Fill In Cc Create_By To This Field.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.high_bill_amt                      is 'Used For Generating Some Reports.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.exp_date                           is 'When Cc Creates A Locksmith Sd, Check If This Field Is Expired. If The Sd Status Is Expired, Change It To 40 And Fill In Enddate.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.created_by                         is 'Creator';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.created_date                       is 'Creation Time';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.modified_by                        is 'Updater';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.modified_date                      is 'Update Time';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.timestamp                          is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.premise_id                         is 'Building Id';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.svc_dtl_start_date                 is 'When The First Meter Reading Is Done, Record The Startdate In Bitem To Calculate Water Usage.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.start_meter_read_id                is 'When Opening A Bill For The First Time, Use This To Retrieve The First Meter Reading Form.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.svc_dtl_stop_date                  is 'Service Detail End Date';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.usage_ind                          is 'Only One Value, + When Creating A Bitem Account, This Field Is Synchronized To Bitem.';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.stop_meter_read_id                 is 'Stop Meter Reading Id';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.rmk                                is 'Notes';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.workflow_id                        is 'Work Order Id';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.instal_svc_dtl_for_deposit_sw      is 'Deposit Download Service Details Switch';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.start_rsn_ind                      is 'Start Reason Indicator';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.stop_rsn_ind                       is 'End Reason Indicator';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.no_payment_periods                 is 'Non-Payment Deadline';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.cust_comm_id                       is 'Ccid';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.special_usage_ind                  is 'Prop And Null';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.ods_load_time                      is 'Data Load Time';
comment on column coss_ods.ods_abpms_tmu_svc_dtl_di.ods_update_time                    is 'Data Update Time';
```

### datax sql

```sql
select
    svc_id,                            -- Service Id
    svc_type_code,                    -- Service Type Code
    start_date,                       -- Start Date
    svc_dtl_sts_ind,                  -- Sd Status Indicator
    account_id,                       -- Account Id
    end_date,                         -- End Date
    wis_account_no,                   -- Wis Account Number
    cust_read_sw,                     -- Whether To Support Customer Self-Uploaded Meter Readings
    hsic_code,                        -- Industry Classification Hsic Code
    request_deposit_amt,              -- Deposit Amount
    svc_dtl_relation_id,              -- Service Detail Relationship Id
    start_req_by,                     -- If The Sd Status Is 20 (Active), Fill In Cc Create_By To This Field.
    stop_req_by,                      -- If The Sd Status Is 40 (Discontinued), Fill In Cc Create_By To This Field.
    high_bill_amt,                    -- Used For Generating Some Reports.
    exp_date,                         -- When Cc Creates A Locksmith Sd, Check If This Field Is Expired. If The Sd Status Is Expired, Change It To 40 And Fill In Enddate.
    created_by,                       -- Creator
    created_date,                     -- Creation Time
    modified_by,                      -- Updater
    modified_date,                    -- Update Time
    timestamp,                        -- Timestamp
    premise_id,                       -- Building Id
    svc_dtl_start_date,               -- When The First Meter Reading Is Done, Record The Startdate In Bitem To Calculate Water Usage.
    start_meter_read_id,              -- When Opening A Bill For The First Time, Use This To Retrieve The First Meter Reading Form.
    svc_dtl_stop_date,                -- Service Detail End Date
    usage_ind,                        -- Only One Value, '+' When Creating A Bitem Account, This Field Is Synchronized To Bitem.
    stop_meter_read_id,               -- Stop Meter Reading Id
    rmk,                              -- Notes
    workflow_id,                      -- Work Order Id
    instal_svc_dtl_for_deposit_sw,    -- Deposit Download Service Details Switch
    start_rsn_ind,                    -- Start Reason Indicator
    stop_rsn_ind,                     -- End Reason Indicator
    no_payment_periods,               -- Non-Payment Deadline
    cust_comm_id,                     -- Ccid
    special_usage_ind,                -- Prop And Null
    current_timestamp ods_load_time,  -- Data Load Time
    current_timestamp ods_update_time  -- Data Update Time
from abpms.svc_dtl
where modified_date >= '${modified_date}'
```

### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: ABPMS
-- Function Describe: Service Details
-- Create         By: dongmaochen
-- Create       Date: 2025-08-09
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- abpms.svc_dtl
-- Target Table
-- coss_ods.ods_abpms_tmu_svc_dtl_di
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_svc_dtl_di
select
    svc_id,                            -- Service Id
    svc_type_code,                    -- Service Type Code
    start_date,                       -- Start Date
    svc_dtl_sts_ind,                  -- Sd Status Indicator
    account_id,                       -- Account Id
    end_date,                         -- End Date
    wis_account_no,                   -- Wis Account Number
    cust_read_sw,                     -- Whether To Support Customer Self-Uploaded Meter Readings
    hsic_code,                        -- Industry Classification Hsic Code
    request_deposit_amt,              -- Deposit Amount
    svc_dtl_relation_id,              -- Service Detail Relationship Id
    start_req_by,                     -- If The Sd Status Is 20 (Active), Fill In Cc Create_By To This Field.
    stop_req_by,                      -- If The Sd Status Is 40 (Discontinued), Fill In Cc Create_By To This Field.
    high_bill_amt,                    -- Used For Generating Some Reports.
    exp_date,                         -- When Cc Creates A Locksmith Sd, Check If This Field Is Expired. If The Sd Status Is Expired, Change It To 40 And Fill In Enddate.
    created_by,                       -- Creator
    created_date,                     -- Creation Time
    modified_by,                      -- Updater
    modified_date,                    -- Update Time
    timestamp,                        -- Timestamp
    premise_id,                       -- Building Id
    svc_dtl_start_date,               -- When The First Meter Reading Is Done, Record The Startdate In Bitem To Calculate Water Usage.
    start_meter_read_id,              -- When Opening A Bill For The First Time, Use This To Retrieve The First Meter Reading Form.
    svc_dtl_stop_date,                -- Service Detail End Date
    usage_ind,                        -- Only One Value, '+' When Creating A Bitem Account, This Field Is Synchronized To Bitem.
    stop_meter_read_id,               -- Stop Meter Reading Id
    rmk,                              -- Notes
    workflow_id,                      -- Work Order Id
    instal_svc_dtl_for_deposit_sw,    -- Deposit Download Service Details Switch
    start_rsn_ind,                    -- Start Reason Indicator
    stop_rsn_ind,                     -- End Reason Indicator
    no_payment_periods,               -- Non-Payment Deadline
    cust_comm_id,                     -- Ccid
    special_usage_ind,                -- Prop And Null
    current_timestamp ods_load_time,  -- Data Load Time
    current_timestamp ods_update_time  -- Data Update Time
from coss_ods.ods_abpms_tmu_svc_dtl_di_tmp
on duplicate key update
    svc_type_code = values(svc_type_code),
    start_date = values(start_date),
    svc_dtl_sts_ind = values(svc_dtl_sts_ind),
    account_id = values(account_id),
    end_date = values(end_date),
    wis_account_no = values(wis_account_no),
    cust_read_sw = values(cust_read_sw),
    hsic_code = values(hsic_code),
    request_deposit_amt = values(request_deposit_amt),
    svc_dtl_relation_id = values(svc_dtl_relation_id),
    start_req_by = values(start_req_by),
    stop_req_by = values(stop_req_by),
    high_bill_amt = values(high_bill_amt),
    exp_date = values(exp_date),
    created_by = values(created_by),
    created_date = values(created_date),
    modified_by = values(modified_by),
    modified_date = values(modified_date),
    timestamp = values(timestamp),
    premise_id = values(premise_id),
    svc_dtl_start_date = values(svc_dtl_start_date),
    start_meter_read_id = values(start_meter_read_id),
    svc_dtl_stop_date = values(svc_dtl_stop_date),
    usage_ind = values(usage_ind),
    stop_meter_read_id = values(stop_meter_read_id),
    rmk = values(rmk),
    workflow_id = values(workflow_id),
    instal_svc_dtl_for_deposit_sw = values(instal_svc_dtl_for_deposit_sw),
    start_rsn_ind = values(start_rsn_ind),
    stop_rsn_ind = values(stop_rsn_ind),
    no_payment_periods = values(no_payment_periods),
    cust_comm_id = values(cust_comm_id),
    special_usage_ind = values(special_usage_ind),
    ods_update_time = values(ods_update_time)
    
```



