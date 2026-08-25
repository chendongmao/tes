# ABPMS ODS 层数仓代码

## 源系统与目标表映射关系

| 源表名称 | 目标表名称 |
|---|---|
| give_up | coss_ods.ods_abpms_tmu_give_up_di |
| adj | coss_ods.ods_abpms_tmu_adj_di |
| adj_refund_chq | coss_ods.ods_abpms_tmu_adj_refund_di |

---

## 1. ods_abpms_tmu_give_up_di

### create sql

```sql
drop table if exists coss_ods.ods_abpms_tmu_give_up_di;
create table if not exists coss_ods.ods_abpms_tmu_give_up_di (
    give_up_id bpchar(12) null,                              -- Give Up Id
    give_up_type_ind bpchar(1) null,                         -- Give Up Type Indicator
    give_up_sts_ind bpchar(1) null,                          -- Give Up Status Indicator
    eff_date timestamp(6) null,                              -- Effective Date
    phone_no varchar(24) null,                               -- Phone Number
    account_id bpchar(10) null,                              -- Account Id
    mail_addr_sw bpchar(1) null,                             -- Mailing Address Switch
    addr_line1 varchar(64) null,                             -- Address Line1
    addr_line2 varchar(64) null,                             -- Address Line2
    addr_line3 varchar(64) null,                             -- Address Line3
    premise_id bpchar(10) null,                              -- Premise Id
    meter_read_id varchar(32) null,                          -- Meter Read Id
    reading numeric(15, 4) null,                             -- Reading
    meter_read_date timestamp(6) null,                       -- Meter Read Date
    deposit_retain_ind varchar(16) null,                     -- Deposit Retain Indicator
    meter_read_src_code varchar(12) null,                    -- Meter Read Source Code
    inc_ch varchar(16) null,                                 -- Inc Channel
    canc_rsn_code varchar(4) null,                           -- Cancel Reason Code
    ref_no varchar(8) null,                                  -- Reference Number
    cust_comm_id bpchar(10) null,                            -- Customer Communication Id
    sys_log varchar(256) null,                               -- System Log
    created_by varchar(50) null,                             -- Created By
    created_date timestamp(6) null,                          -- Created Date
    modified_by varchar(50) null,                            -- Modified By
    modified_date timestamp(6) null,                         -- Modified Date
    "timestamp" timestamp(6) null,                           -- Timestamp
    submitted_date timestamp(6) null,                        -- Submitted Date
    bill_win_end_date timestamp(6) null,                     -- Bill Win End Date
    supervisor_override bool null,                           -- Supervisor Override
    icms_id varchar(32) null,                                -- Icms Id
    workflow_id varchar(32) null,                            -- Workflow Id
    letter_id varchar(32) null,                             -- Letter Id
    letter_date timestamp(6) null,                           -- Letter Date
    pems_id varchar(32) null,                                -- Pems Id
    automation_id bpchar(10) null,                           -- Automation Id
    ods_load_time timestamp(6) default pg_systimestamp(),   -- Data Load Time
    ods_update_time timestamp(6) default pg_systimestamp(),  -- Data Update Time
    primary key(give_up_id)
)
with (
    orientation=row,
    compression=no
);

comment on table  coss_ods.ods_abpms_tmu_give_up_di                  is 'Give Up, Records The Give-Up Application When A Customer Terminates Consumership';
comment on column coss_ods.ods_abpms_tmu_give_up_di.give_up_id       is 'Give Up Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.give_up_type_ind is 'Give Up Type Indicator';
comment on column coss_ods.ods_abpms_tmu_give_up_di.give_up_sts_ind  is 'Give Up Status Indicator';
comment on column coss_ods.ods_abpms_tmu_give_up_di.eff_date         is 'Effective Date';
comment on column coss_ods.ods_abpms_tmu_give_up_di.phone_no        is 'Phone Number';
comment on column coss_ods.ods_abpms_tmu_give_up_di.account_id      is 'Account Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.mail_addr_sw    is 'Mailing Address Switch';
comment on column coss_ods.ods_abpms_tmu_give_up_di.addr_line1      is 'Address Line1';
comment on column coss_ods.ods_abpms_tmu_give_up_di.addr_line2      is 'Address Line2';
comment on column coss_ods.ods_abpms_tmu_give_up_di.addr_line3      is 'Address Line3';
comment on column coss_ods.ods_abpms_tmu_give_up_di.premise_id      is 'Premise Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.meter_read_id   is 'Meter Read Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.reading          is 'Reading';
comment on column coss_ods.ods_abpms_tmu_give_up_di.meter_read_date is 'Meter Read Date';
comment on column coss_ods.ods_abpms_tmu_give_up_di.deposit_retain_ind is 'Deposit Retain Indicator';
comment on column coss_ods.ods_abpms_tmu_give_up_di.meter_read_src_code is 'Meter Read Source Code';
comment on column coss_ods.ods_abpms_tmu_give_up_di.inc_ch          is 'Inc Channel';
comment on column coss_ods.ods_abpms_tmu_give_up_di.canc_rsn_code   is 'Cancel Reason Code';
comment on column coss_ods.ods_abpms_tmu_give_up_di.ref_no          is 'Reference Number';
comment on column coss_ods.ods_abpms_tmu_give_up_di.cust_comm_id    is 'Customer Communication Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.sys_log         is 'System Log';
comment on column coss_ods.ods_abpms_tmu_give_up_di.created_by      is 'Created By';
comment on column coss_ods.ods_abpms_tmu_give_up_di.created_date    is 'Created Date';
comment on column coss_ods.ods_abpms_tmu_give_up_di.modified_by     is 'Modified By';
comment on column coss_ods.ods_abpms_tmu_give_up_di.modified_date   is 'Modified Date';
comment on column coss_ods.ods_abpms_tmu_give_up_di.timestamp       is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_give_up_di.submitted_date  is 'Submitted Date';
comment on column coss_ods.ods_abpms_tmu_give_up_di.bill_win_end_date is 'Bill Win End Date';
comment on column coss_ods.ods_abpms_tmu_give_up_di.supervisor_override is 'Supervisor Override';
comment on column coss_ods.ods_abpms_tmu_give_up_di.icms_id        is 'Icms Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.workflow_id    is 'Workflow Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.letter_id       is 'Letter Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.letter_date     is 'Letter Date';
comment on column coss_ods.ods_abpms_tmu_give_up_di.pems_id         is 'Pems Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.automation_id  is 'Automation Id';
comment on column coss_ods.ods_abpms_tmu_give_up_di.ods_load_time   is 'Data Load Time';
comment on column coss_ods.ods_abpms_tmu_give_up_di.ods_update_time is 'Data Update Time';
```

### datax sql

```sql
select
    give_up_id,                             -- Give Up Id
    give_up_type_ind,                       -- Give Up Type Indicator
    give_up_sts_ind,                        -- Give Up Status Indicator
    eff_date,                               -- Effective Date
    phone_no,                               -- Phone Number
    account_id,                             -- Account Id
    mail_addr_sw,                           -- Mailing Address Switch
    addr_line1,                             -- Address Line1
    addr_line2,                             -- Address Line2
    addr_line3,                             -- Address Line3
    premise_id,                             -- Premise Id
    meter_read_id,                          -- Meter Read Id
    reading,                                -- Reading
    meter_read_date,                        -- Meter Read Date
    deposit_retain_ind,                     -- Deposit Retain Indicator
    meter_read_src_code,                    -- Meter Read Source Code
    inc_ch,                                 -- Inc Channel
    canc_rsn_code,                          -- Cancel Reason Code
    ref_no,                                 -- Reference Number
    cust_comm_id,                           -- Customer Communication Id
    sys_log,                                -- System Log
    created_by,                             -- Created By
    created_date,                           -- Created Date
    modified_by,                            -- Modified By
    modified_date,                          -- Modified Date
    timestamp,                              -- Timestamp
    submitted_date,                         -- Submitted Date
    bill_win_end_date,                      -- Bill Win End Date
    supervisor_override,                    -- Supervisor Override
    icms_id,                                -- Icms Id
    workflow_id,                            -- Workflow Id
    letter_id,                              -- Letter Id
    letter_date,                            -- Letter Date
    pems_id,                                -- Pems Id
    automation_id,                          -- Automation Id
    current_timestamp ods_load_time,        -- Data Load Time
    current_timestamp ods_update_time       -- Data Update Time
from abpms.give_up
where modified_date >= '${modified_date}'
```

### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: ABPMS
-- Function Describe: Give Up
-- Create         By: dongmaochen
-- Create       Date: 2025-08-20
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- abpms.give_up
-- Target Table
-- coss_ods.ods_abpms_tmu_give_up_di
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_give_up_di
select
    give_up_id,                             -- Give Up Id
    give_up_type_ind,                       -- Give Up Type Indicator
    give_up_sts_ind,                        -- Give Up Status Indicator
    eff_date,                               -- Effective Date
    phone_no,                               -- Phone Number
    account_id,                             -- Account Id
    mail_addr_sw,                           -- Mailing Address Switch
    addr_line1,                             -- Address Line1
    addr_line2,                             -- Address Line2
    addr_line3,                             -- Address Line3
    premise_id,                             -- Premise Id
    meter_read_id,                          -- Meter Read Id
    reading,                                -- Reading
    meter_read_date,                        -- Meter Read Date
    deposit_retain_ind,                     -- Deposit Retain Indicator
    meter_read_src_code,                    -- Meter Read Source Code
    inc_ch,                                 -- Inc Channel
    canc_rsn_code,                          -- Cancel Reason Code
    ref_no,                                 -- Reference Number
    cust_comm_id,                           -- Customer Communication Id
    sys_log,                                -- System Log
    created_by,                             -- Created By
    created_date,                           -- Created Date
    modified_by,                            -- Modified By
    modified_date,                          -- Modified Date
    timestamp,                              -- Timestamp
    submitted_date,                         -- Submitted Date
    bill_win_end_date,                      -- Bill Win End Date
    supervisor_override,                    -- Supervisor Override
    icms_id,                                -- Icms Id
    workflow_id,                            -- Workflow Id
    letter_id,                              -- Letter Id
    letter_date,                            -- Letter Date
    pems_id,                                -- Pems Id
    automation_id,                          -- Automation Id
    current_timestamp ods_load_time,        -- Data Load Time
    current_timestamp ods_update_time       -- Data Update Time
from coss_ods.ods_abpms_tmu_give_up_di_tmp
on duplicate key update
    give_up_type_ind = values(give_up_type_ind),
    give_up_sts_ind = values(give_up_sts_ind),
    eff_date = values(eff_date),
    phone_no = values(phone_no),
    account_id = values(account_id),
    mail_addr_sw = values(mail_addr_sw),
    addr_line1 = values(addr_line1),
    addr_line2 = values(addr_line2),
    addr_line3 = values(addr_line3),
    premise_id = values(premise_id),
    meter_read_id = values(meter_read_id),
    reading = values(reading),
    meter_read_date = values(meter_read_date),
    deposit_retain_ind = values(deposit_retain_ind),
    meter_read_src_code = values(meter_read_src_code),
    inc_ch = values(inc_ch),
    canc_rsn_code = values(canc_rsn_code),
    ref_no = values(ref_no),
    cust_comm_id = values(cust_comm_id),
    sys_log = values(sys_log),
    created_by = values(created_by),
    created_date = values(created_date),
    modified_by = values(modified_by),
    modified_date = values(modified_date),
    timestamp = values(timestamp),
    submitted_date = values(submitted_date),
    bill_win_end_date = values(bill_win_end_date),
    supervisor_override = values(supervisor_override),
    icms_id = values(icms_id),
    workflow_id = values(workflow_id),
    letter_id = values(letter_id),
    letter_date = values(letter_date),
    pems_id = values(pems_id),
    automation_id = values(automation_id),
    ods_update_time = values(ods_update_time)
```

---

## 2. ods_abpms_tmu_adj_di

### create sql

```sql
drop table if exists coss_ods.ods_abpms_tmu_adj_di;
create table if not exists coss_ods.ods_abpms_tmu_adj_di (
    adj_id bpchar(12) null,                                  -- Adjustment Id
    svc_id bpchar(10) null,                                  -- Service Id
    adj_type_code varchar(8) null,                           -- Adjustment Type Code
    adj_sts_ind bpchar(2) null,                              -- Adjustment Status Indicator
    created_date timestamp(6) null,                          -- Created Date
    canc_rsn_code varchar(4) null,                           -- Cancel Reason Code
    adj_amt numeric(15, 2) null,                             -- Adjustment Amount
    txfr_adj_id bpchar(12) null,                             -- Transfer Adjustment Id
    rmk varchar(254) null,                                   -- Remark
    base_amt numeric(15, 2) null,                            -- Base Amount
    created_by varchar(50) null,                             -- Created By
    modified_by varchar(50) null,                            -- Modified By
    modified_date timestamp(6) null,                         -- Modified Date
    "timestamp" timestamp(6) null,                           -- Timestamp
    bill_id bpchar(12) null,                                 -- Bill Id
    pems_id varchar(40) null,                                -- Pems Id
    workflow_id varchar(40) null,                            -- Workflow Id
    ods_load_time timestamp(6) default pg_systimestamp(),   -- Data Load Time
    ods_update_time timestamp(6) default pg_systimestamp(),  -- Data Update Time
    primary key(adj_id)
)
with (
    orientation=row,
    compression=no
);

comment on table  coss_ods.ods_abpms_tmu_adj_di             is 'Adjustment, Records All Types Of Monetary Adjustments To Service Details Including Deposit Offset Refund Transfer And Write-Off';
comment on column coss_ods.ods_abpms_tmu_adj_di.adj_id     is 'Adjustment Id';
comment on column coss_ods.ods_abpms_tmu_adj_di.svc_id     is 'Service Id';
comment on column coss_ods.ods_abpms_tmu_adj_di.adj_type_code is 'Adjustment Type Code';
comment on column coss_ods.ods_abpms_tmu_adj_di.adj_sts_ind is 'Adjustment Status Indicator';
comment on column coss_ods.ods_abpms_tmu_adj_di.created_date is 'Created Date';
comment on column coss_ods.ods_abpms_tmu_adj_di.canc_rsn_code is 'Cancel Reason Code';
comment on column coss_ods.ods_abpms_tmu_adj_di.adj_amt     is 'Adjustment Amount';
comment on column coss_ods.ods_abpms_tmu_adj_di.txfr_adj_id is 'Transfer Adjustment Id';
comment on column coss_ods.ods_abpms_tmu_adj_di.rmk        is 'Remark';
comment on column coss_ods.ods_abpms_tmu_adj_di.base_amt   is 'Base Amount';
comment on column coss_ods.ods_abpms_tmu_adj_di.created_by is 'Created By';
comment on column coss_ods.ods_abpms_tmu_adj_di.modified_by is 'Modified By';
comment on column coss_ods.ods_abpms_tmu_adj_di.modified_date is 'Modified Date';
comment on column coss_ods.ods_abpms_tmu_adj_di.timestamp  is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_adj_di.bill_id    is 'Bill Id';
comment on column coss_ods.ods_abpms_tmu_adj_di.pems_id    is 'Pems Id';
comment on column coss_ods.ods_abpms_tmu_adj_di.workflow_id is 'Workflow Id';
comment on column coss_ods.ods_abpms_tmu_adj_di.ods_load_time is 'Data Load Time';
comment on column coss_ods.ods_abpms_tmu_adj_di.ods_update_time is 'Data Update Time';
```

### datax sql

```sql
select
    adj_id,                                 -- Adjustment Id
    svc_id,                                 -- Service Id
    adj_type_code,                          -- Adjustment Type Code
    adj_sts_ind,                            -- Adjustment Status Indicator
    created_date,                           -- Created Date
    canc_rsn_code,                          -- Cancel Reason Code
    adj_amt,                                -- Adjustment Amount
    txfr_adj_id,                            -- Transfer Adjustment Id
    rmk,                                    -- Remark
    base_amt,                               -- Base Amount
    created_by,                             -- Created By
    modified_by,                            -- Modified By
    modified_date,                          -- Modified Date
    timestamp,                              -- Timestamp
    bill_id,                                -- Bill Id
    pems_id,                                -- Pems Id
    workflow_id,                            -- Workflow Id
    current_timestamp ods_load_time,        -- Data Load Time
    current_timestamp ods_update_time       -- Data Update Time
from abpms.adj
where modified_date >= '${modified_date}'
```

### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: ABPMS
-- Function Describe: Adjustment
-- Create         By: dongmaochen
-- Create       Date: 2025-08-20
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- abpms.adj
-- Target Table
-- coss_ods.ods_abpms_tmu_adj_di
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_adj_di
select
    adj_id,                                 -- Adjustment Id
    svc_id,                                 -- Service Id
    adj_type_code,                          -- Adjustment Type Code
    adj_sts_ind,                            -- Adjustment Status Indicator
    created_date,                           -- Created Date
    canc_rsn_code,                          -- Cancel Reason Code
    adj_amt,                                -- Adjustment Amount
    txfr_adj_id,                            -- Transfer Adjustment Id
    rmk,                                    -- Remark
    base_amt,                               -- Base Amount
    created_by,                             -- Created By
    modified_by,                            -- Modified By
    modified_date,                          -- Modified Date
    timestamp,                              -- Timestamp
    bill_id,                                -- Bill Id
    pems_id,                                -- Pems Id
    workflow_id,                            -- Workflow Id
    current_timestamp ods_load_time,        -- Data Load Time
    current_timestamp ods_update_time       -- Data Update Time
from coss_ods.ods_abpms_tmu_adj_di_tmp
on duplicate key update
    svc_id = values(svc_id),
    adj_type_code = values(adj_type_code),
    adj_sts_ind = values(adj_sts_ind),
    created_date = values(created_date),
    canc_rsn_code = values(canc_rsn_code),
    adj_amt = values(adj_amt),
    txfr_adj_id = values(txfr_adj_id),
    rmk = values(rmk),
    base_amt = values(base_amt),
    created_by = values(created_by),
    modified_by = values(modified_by),
    modified_date = values(modified_date),
    timestamp = values(timestamp),
    bill_id = values(bill_id),
    pems_id = values(pems_id),
    workflow_id = values(workflow_id),
    ods_update_time = values(ods_update_time)
```

---

## 3. ods_abpms_tmu_adj_refund_di

### create sql

```sql
drop table if exists coss_ods.ods_abpms_tmu_adj_refund_di;
create table if not exists coss_ods.ods_abpms_tmu_adj_refund_di (
    adj_refund_chq_id bpchar(12) null,                       -- Adjustment Refund Cheque Id
    adj_id bpchar(12) null,                                  -- Adjustment Id
    addr_line1 varchar(64) null,                             -- Address Line1
    addr_line2 varchar(64) null,                             -- Address Line2
    addr_line3 varchar(64) null,                             -- Address Line3
    addr_line4 varchar(64) null,                             -- Address Line4
    paid_amt numeric(15, 2) null,                            -- Paid Amount
    sched_payment_date timestamp(6) null,                    -- Scheduled Payment Date
    payment_date timestamp(6) null,                          -- Payment Date
    pst_name varchar(64) null,                               -- Payee Name
    payment_doc_id varchar(20) null,                        -- Payment Document Id
    payment_doc_date timestamp(6) null,                     -- Payment Document Date
    payment_id bpchar(12) null,                              -- Payment Id
    payment_method_ind varchar(10) null,                     -- Payment Method Indicator
    payment_select_sts_ind bpchar(1) null,                   -- Payment Select Status Indicator
    batch_job_code varchar(8) null,                          -- Batch Job Code
    batch_no numeric(10) null,                               -- Batch Number
    fin_year numeric(4) null,                                -- Financial Year
    dvn varchar(12) null,                                    -- Division
    user_code varchar(19) null,                              -- User Code
    batch_ref varchar(20) null,                              -- Batch Reference
    adj_refund_chq_desc1 varchar(30) null,                   -- Adjustment Refund Cheque Desc1
    adj_refund_chq_desc2 varchar(30) null,                   -- Adjustment Refund Cheque Desc2
    vio bpchar(1) null,                                      -- Vio
    next_auth_id numeric(8) null,                            -- Next Auth Id
    prepared_by numeric(8) null,                             -- Prepared By
    adj_refund_chq_sts_ind varchar(2) null,                  -- Adjustment Refund Cheque Status Indicator
    generated_by varchar(8) null,                            -- Generated By
    generated_date timestamp(6) null,                        -- Generated Date
    lang_code bpchar(1) null,                                -- Language Code
    payee_type varchar(10) null,                             -- Payee Type
    creditor_ref_no varchar(30) null,                        -- Creditor Reference Number
    payment_vou_no varchar(20) null,                         -- Payment Voucher Number
    treasury_vou_no varchar(20) null,                        -- Treasury Voucher Number
    chq_no varchar(10) null,                                 -- Cheque Number
    voucher_amt numeric(15, 2) null,                         -- Voucher Amount
    rmk varchar(254) null,                                   -- Remark
    created_by varchar(50) null,                             -- Created By
    created_date timestamp(6) null,                          -- Created Date
    modified_by varchar(50) null,                            -- Modified By
    modified_date timestamp(6) null,                         -- Modified Date
    "timestamp" timestamp(6) null,                           -- Timestamp
    ods_load_time timestamp(6) default pg_systimestamp(),   -- Data Load Time
    ods_update_time timestamp(6) default pg_systimestamp(),  -- Data Update Time
    primary key(adj_refund_chq_id)
)
with (
    orientation=row,
    compression=no
);

comment on table  coss_ods.ods_abpms_tmu_adj_refund_di                    is 'Adjustment Refund Cheque, Records The Cheque Details For Refund Adjustments Processed Through Gfmis';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.adj_refund_chq_id  is 'Adjustment Refund Cheque Id';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.adj_id             is 'Adjustment Id';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.addr_line1         is 'Address Line1';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.addr_line2         is 'Address Line2';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.addr_line3         is 'Address Line3';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.addr_line4         is 'Address Line4';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.paid_amt          is 'Paid Amount';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.sched_payment_date is 'Scheduled Payment Date';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.payment_date       is 'Payment Date';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.pst_name          is 'Payee Name';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.payment_doc_id     is 'Payment Document Id';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.payment_doc_date  is 'Payment Document Date';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.payment_id        is 'Payment Id';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.payment_method_ind is 'Payment Method Indicator';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.payment_select_sts_ind is 'Payment Select Status Indicator';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.batch_job_code    is 'Batch Job Code';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.batch_no          is 'Batch Number';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.fin_year          is 'Financial Year';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.dvn               is 'Division';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.user_code         is 'User Code';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.batch_ref        is 'Batch Reference';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.adj_refund_chq_desc1 is 'Adjustment Refund Cheque Desc1';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.adj_refund_chq_desc2 is 'Adjustment Refund Cheque Desc2';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.vio               is 'Vio';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.next_auth_id      is 'Next Auth Id';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.prepared_by       is 'Prepared By';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.adj_refund_chq_sts_ind is 'Adjustment Refund Cheque Status Indicator';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.generated_by      is 'Generated By';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.generated_date    is 'Generated Date';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.lang_code         is 'Language Code';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.payee_type       is 'Payee Type';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.creditor_ref_no   is 'Creditor Reference Number';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.payment_vou_no    is 'Payment Voucher Number';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.treasury_vou_no   is 'Treasury Voucher Number';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.chq_no           is 'Cheque Number';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.voucher_amt      is 'Voucher Amount';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.rmk              is 'Remark';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.created_by       is 'Created By';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.created_date     is 'Created Date';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.modified_by      is 'Modified By';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.modified_date    is 'Modified Date';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.timestamp         is 'Timestamp';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.ods_load_time     is 'Data Load Time';
comment on column coss_ods.ods_abpms_tmu_adj_refund_di.ods_update_time  is 'Data Update Time';
```

### datax sql

```sql
select
    adj_refund_chq_id,                      -- Adjustment Refund Cheque Id
    adj_id,                                 -- Adjustment Id
    addr_line1,                             -- Address Line1
    addr_line2,                             -- Address Line2
    addr_line3,                             -- Address Line3
    addr_line4,                             -- Address Line4
    paid_amt,                               -- Paid Amount
    sched_payment_date,                     -- Scheduled Payment Date
    payment_date,                           -- Payment Date
    pst_name,                               -- Payee Name
    payment_doc_id,                         -- Payment Document Id
    payment_doc_date,                       -- Payment Document Date
    payment_id,                             -- Payment Id
    payment_method_ind,                     -- Payment Method Indicator
    payment_select_sts_ind,                 -- Payment Select Status Indicator
    batch_job_code,                        -- Batch Job Code
    batch_no,                              -- Batch Number
    fin_year,                               -- Financial Year
    dvn,                                    -- Division
    user_code,                              -- User Code
    batch_ref,                              -- Batch Reference
    adj_refund_chq_desc1,                   -- Adjustment Refund Cheque Desc1
    adj_refund_chq_desc2,                   -- Adjustment Refund Cheque Desc2
    vio,                                    -- Vio
    next_auth_id,                           -- Next Auth Id
    prepared_by,                            -- Prepared By
    adj_refund_chq_sts_ind,                 -- Adjustment Refund Cheque Status Indicator
    generated_by,                           -- Generated By
    generated_date,                         -- Generated Date
    lang_code,                              -- Language Code
    payee_type,                             -- Payee Type
    creditor_ref_no,                        -- Creditor Reference Number
    payment_vou_no,                         -- Payment Voucher Number
    treasury_vou_no,                        -- Treasury Voucher Number
    chq_no,                                 -- Cheque Number
    voucher_amt,                            -- Voucher Amount
    rmk,                                    -- Remark
    created_by,                             -- Created By
    created_date,                           -- Created Date
    modified_by,                            -- Modified By
    modified_date,                          -- Modified Date
    timestamp,                              -- Timestamp
    current_timestamp ods_load_time,        -- Data Load Time
    current_timestamp ods_update_time       -- Data Update Time
from abpms.adj_refund_chq
where modified_date >= '${modified_date}'
```

### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: ABPMS
-- Function Describe: Adjustment Refund Cheque
-- Create         By: dongmaochen
-- Create       Date: 2025-08-20
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table
-- abpms.adj_refund_chq
-- Target Table
-- coss_ods.ods_abpms_tmu_adj_refund_di
-- ****************************************************************************************
insert into coss_ods.ods_abpms_tmu_adj_refund_di
select
    adj_refund_chq_id,                      -- Adjustment Refund Cheque Id
    adj_id,                                 -- Adjustment Id
    addr_line1,                             -- Address Line1
    addr_line2,                             -- Address Line2
    addr_line3,                             -- Address Line3
    addr_line4,                             -- Address Line4
    paid_amt,                               -- Paid Amount
    sched_payment_date,                     -- Scheduled Payment Date
    payment_date,                           -- Payment Date
    pst_name,                               -- Payee Name
    payment_doc_id,                         -- Payment Document Id
    payment_doc_date,                       -- Payment Document Date
    payment_id,                             -- Payment Id
    payment_method_ind,                     -- Payment Method Indicator
    payment_select_sts_ind,                 -- Payment Select Status Indicator
    batch_job_code,                        -- Batch Job Code
    batch_no,                              -- Batch Number
    fin_year,                               -- Financial Year
    dvn,                                    -- Division
    user_code,                              -- User Code
    batch_ref,                              -- Batch Reference
    adj_refund_chq_desc1,                   -- Adjustment Refund Cheque Desc1
    adj_refund_chq_desc2,                   -- Adjustment Refund Cheque Desc2
    vio,                                    -- Vio
    next_auth_id,                           -- Next Auth Id
    prepared_by,                            -- Prepared By
    adj_refund_chq_sts_ind,                 -- Adjustment Refund Cheque Status Indicator
    generated_by,                           -- Generated By
    generated_date,                         -- Generated Date
    lang_code,                              -- Language Code
    payee_type,                             -- Payee Type
    creditor_ref_no,                        -- Creditor Reference Number
    payment_vou_no,                         -- Payment Voucher Number
    treasury_vou_no,                        -- Treasury Voucher Number
    chq_no,                                 -- Cheque Number
    voucher_amt,                            -- Voucher Amount
    rmk,                                    -- Remark
    created_by,                             -- Created By
    created_date,                           -- Created Date
    modified_by,                            -- Modified By
    modified_date,                          -- Modified Date
    timestamp,                              -- Timestamp
    current_timestamp ods_load_time,        -- Data Load Time
    current_timestamp ods_update_time       -- Data Update Time
from coss_ods.ods_abpms_tmu_adj_refund_di_tmp
on duplicate key update
    adj_id = values(adj_id),
    addr_line1 = values(addr_line1),
    addr_line2 = values(addr_line2),
    addr_line3 = values(addr_line3),
    addr_line4 = values(addr_line4),
    paid_amt = values(paid_amt),
    sched_payment_date = values(sched_payment_date),
    payment_date = values(payment_date),
    pst_name = values(pst_name),
    payment_doc_id = values(payment_doc_id),
    payment_doc_date = values(payment_doc_date),
    payment_id = values(payment_id),
    payment_method_ind = values(payment_method_ind),
    payment_select_sts_ind = values(payment_select_sts_ind),
    batch_job_code = values(batch_job_code),
    batch_no = values(batch_no),
    fin_year = values(fin_year),
    dvn = values(dvn),
    user_code = values(user_code),
    batch_ref = values(batch_ref),
    adj_refund_chq_desc1 = values(adj_refund_chq_desc1),
    adj_refund_chq_desc2 = values(adj_refund_chq_desc2),
    vio = values(vio),
    next_auth_id = values(next_auth_id),
    prepared_by = values(prepared_by),
    adj_refund_chq_sts_ind = values(adj_refund_chq_sts_ind),
    generated_by = values(generated_by),
    generated_date = values(generated_date),
    lang_code = values(lang_code),
    payee_type = values(payee_type),
    creditor_ref_no = values(creditor_ref_no),
    payment_vou_no = values(payment_vou_no),
    treasury_vou_no = values(treasury_vou_no),
    chq_no = values(chq_no),
    voucher_amt = values(voucher_amt),
    rmk = values(rmk),
    created_by = values(created_by),
    created_date = values(created_date),
    modified_by = values(modified_by),
    modified_date = values(modified_date),
    timestamp = values(timestamp),
    ods_update_time = values(ods_update_time)
```
