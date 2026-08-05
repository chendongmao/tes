# ods_pems_cus_t_order_workorder_mini_year

## create table

```sql
drop table if exists coss_ods.ods_pems_cus_t_order_workorder_mini_year;

create table if not exists coss_ods.ods_pems_cus_t_order_workorder_mini_year(
    ordernum varchar(30),
    msgid int8,
    agentgroupid int8,
    cusid varchar(50),
    channeltype int4,
    busicenter varchar(50),
    classify1 int8,
    classify2 int8,
    subarea int8,
    system int8,
    classify3 int8,
    classify4 int8,
    realclassify1 int8,
    realclassify2 int8,
    bigregion varchar(30),
    subregion int8,
    dayshift int4,
    dutyshift int4,
    urgency int4,
    isclosed int4,
    state int4,
    orderstate int4,
    isdelay int4,
    delayday int4,
    iscomplant int4,
    isreply int4,
    replychannel varchar(20),
    casesource int8,
    transferivr int4,
    chargeback int4,
    ivrlanguage int4,
    district1 varchar(30),
    district2 varchar(30),
    isrepeatedcomplaint int4,
    subcomplaint int4,
    receivedepartment int8,
    receiver int8,
    printedflag int4,
    isregionorder int4,
    outstandingdays int4,
    finalreplydays int4,
    completedbyregion varchar(5),
    pledgeachieved varchar(5),
    actualreplytime timestamp,
    repairdays int4,
    grantedhowlong int4,
    notificationdays int4,
    totalprocessingdays int4,
    referinwsd int4,
    isdelete bpchar(1),
    basecallpid int8,
    complantlastupdator int8,
    complantlastupdatetime timestamp,
    isdone int4,
    createdby int8,
    createdat timestamp,
    lastupdatedby int8,
    lastupdateat timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    ods_update_time timestamp(6) default current_timestamp,
    primary key (ordernum)
)
with (
    orientation = row,
    compression = no
)
partition by range (createdat)
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

comment on table coss_ods.ods_pems_cus_t_order_workorder_mini_year is 'PEMS System Work Order Main Table';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.ordernum is 'Work Order Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.msgid is 'Message Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.agentgroupid is 'Agent Group Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.cusid is 'Customer Id (Linked To Customer Table)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.channeltype is 'Channel Type';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.busicenter is 'Business Center (Department)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.classify1 is 'Work Order Category 1';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.classify2 is 'Work Order Category 2';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.subarea is 'Region - Branch';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.system is 'Dispatch System';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.classify3 is 'Work Order Category 3';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.classify4 is 'Work Order Category 4';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.realclassify1 is 'Actual Work Order Category 3';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.realclassify2 is 'Actual Work Order Category 4';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.bigregion is 'Administrative Region';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.subregion is 'Region & Branch – Sub-Region';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.dayshift is 'Day Shift Team';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.dutyshift is 'On-Duty Team';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.urgency is 'Urgency Level';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.isclosed is '1=Closed, 2=Dispatched';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.state is 'External Status';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.orderstate is 'Work Order Status: 1=Pending, 2=In Progress, 3=Completed';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.isdelay is 'Is Overdue: 1=Yes';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.delayday is 'Overdue Days';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.iscomplant is 'Is Complaint Ticket: 1=Yes, 2=Tree-Related, 0=No';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.isreply is 'Reply Required: 1=Yes';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.replychannel is 'Reply Channel';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.casesource is 'Case Source';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.transferivr is 'Transferred To Ivr';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.chargeback is 'Returned Order';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.ivrlanguage is 'Ivr Language Selection';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.district1 is 'Primary Concern Area';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.district2 is 'Secondary Concern Area';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.isrepeatedcomplaint is 'Repeat Complaint Flag';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.subcomplaint is 'Sub-Complaint Flag';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.receivedepartment is 'Acceptance Department';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.receiver is 'Handler / Assignee';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.printedflag is 'Printed Flag';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.isregionorder is 'Region-Based Ticket Creation: 1=Cs, 2=Hw';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.outstandingdays is 'Pending Days As Of Current Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.finalreplydays is 'Required Final Response Days';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.completedbyregion is 'Case Completed By Regional Team';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.pledgeachieved is 'Service Commitment Met Flag';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.actualreplytime is 'Actual Response Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.repairdays is 'Allowed Maintenance Days';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.grantedhowlong is 'Eot Extension Days (If Granted)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.notificationdays is 'Notification Period (Days) Specified In Fj';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.totalprocessingdays is 'Total Handling Days';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.referinwsd is 'Internal Transfer Flag: 1=Yes';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.isdelete is 'Deletable Flag: 1=Yes, 0=No';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.basecallpid is 'Basecallpid';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.complantlastupdator is 'Last Complaint Ticket Modifier';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.complantlastupdatetime is 'Last Complaint Ticket Modification Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.isdone is 'Flag: 1=Processed In Abpms System';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.createdby is 'Created By';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.createdat is 'Data Warehouse Load Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.lastupdatedby is 'Last Updated By';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.lastupdateat is 'Last Update Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.ods_load_time is 'Ods Table Load Timestamp';
comment on column coss_ods.ods_pems_cus_t_order_workorder_mini_year.ods_update_time is 'Ods Table Update Timestamp';
```



## select sql

```sql
select 
    ordernum, -- Work Order Id
    msgid, -- Message Id
    agentgroupid, -- Agent Group Id
    cusid, -- Customer Id (Linked To Customer Table)
    channeltype, -- Channel Type
    busicenter, -- Business Center (Department)
    classify1, -- Work Order Category 1
    classify2, -- Work Order Category 2
    subarea, -- Region - Branch
    system, -- Dispatch System
    classify3, -- Work Order Category 3
    classify4, -- Work Order Category 4
    realclassify1, -- Actual Work Order Category 3
    realclassify2, -- Actual Work Order Category 4
    bigregion, -- Administrative Region
    subregion, -- Region & Branch – Sub-Region
    dayshift, -- Day Shift Team
    dutyshift, -- On-Duty Team
    urgency, -- Urgency Level
    isclosed, -- 1=Closed, 2=Dispatched
    state, -- External Status
    orderstate, -- Work Order Status: 1=Pending, 2=In Progress, 3=Completed
    isdelay, -- Is Overdue: 1=Yes
    delayday, -- Overdue Days
    iscomplant, -- Is Complaint Ticket: 1=Yes, 2=Tree-Related, 0=No
    isreply, -- Reply Required: 1=Yes
    replychannel, -- Reply Channel
    casesource, -- Case Source
    transferivr, -- Transferred To Ivr
    chargeback, -- Returned Order
    ivrlanguage, -- Ivr Language Selection
    district1, -- Primary Concern Area
    district2, -- Secondary Concern Area
    isrepeatedcomplaint, -- Repeat Complaint Flag
    subcomplaint, -- Sub-Complaint Flag
    receivedepartment, -- Acceptance Department
    receiver, -- Handler / Assignee
    printedflag, -- Printed Flag
    isregionorder, -- Region-Based Ticket Creation: 1=Cs, 2=Hw
    outstandingdays, -- Pending Days As Of Current Date
    finalreplydays, -- Required Final Response Days
    completedbyregion, -- Case Completed By Regional Team
    pledgeachieved, -- Service Commitment Met Flag
    actualreplytime, -- Actual Response Time
    repairdays, -- Allowed Maintenance Days
    grantedhowlong, -- Eot Extension Days (If Granted)
    notificationdays, -- Notification Period (Days) Specified In Fj
    totalprocessingdays, -- Total Handling Days
    referinwsd, -- Internal Transfer Flag: 1=Yes
    isdelete, -- Deletable Flag: 1=Yes, 0=No
    basecallpid, -- Basecallpid
    complantlastupdator, -- Last Complaint Ticket Modifier
    complantlastupdatetime, -- Last Complaint Ticket Modification Time
    isdone, -- Flag: 1=Processed In Abpms System
    createdby, -- Created By
    createdat, -- Data Warehouse Load Time
    lastupdatedby, -- Last Updated By
    lastupdateat, -- Last Update Time,
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from pems.t_order_workorder
where
	(complantlastupdatetime >= '${complantlastupdatetime}'
	or createdat >= '${createdat}')
	and classify3 = 10
```

## update sql

```sql



-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Main Work Order Info Full Load & Upsert
-- Create         By: dongmaochen
-- Create       Date: 2026-04-23
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_pems_cus_t_order_workorder_stg_mini
-- Target Table:  coss_ods.ods_pems_cus_t_order_workorder_mini_year
-- ****************************************************************************************
insert into coss_ods.ods_pems_cus_t_order_workorder_mini_year
select
    ordernum, -- Work Order Id
    msgid, -- Message Id
    agentgroupid, -- Agent Group Id
    cusid, -- Customer Id (Linked To Customer Table)
    channeltype, -- Channel Type
    busicenter, -- Business Center (Department)
    classify1, -- Work Order Category 1
    classify2, -- Work Order Category 2
    subarea, -- Region - Branch
    system, -- Dispatch System
    classify3, -- Work Order Category 3
    classify4, -- Work Order Category 4
    realclassify1, -- Actual Work Order Category 3
    realclassify2, -- Actual Work Order Category 4
    bigregion, -- Administrative Region
    subregion, -- Region & Branch – Sub-Region
    dayshift, -- Day Shift Team
    dutyshift, -- On-Duty Team
    urgency, -- Urgency Level
    isclosed, -- 1=Closed, 2=Dispatched
    state, -- External Status
    orderstate, -- Work Order Status: 1=Pending, 2=In Progress, 3=Completed
    isdelay, -- Is Overdue: 1=Yes
    delayday, -- Overdue Days
    iscomplant, -- Is Complaint Ticket: 1=Yes, 2=Tree-Related, 0=No
    isreply, -- Reply Required: 1=Yes
    replychannel, -- Reply Channel
    casesource, -- Case Source
    transferivr, -- Transferred To Ivr
    chargeback, -- Returned Order
    ivrlanguage, -- Ivr Language Selection
    district1, -- Primary Concern Area
    district2, -- Secondary Concern Area
    isrepeatedcomplaint, -- Repeat Complaint Flag
    subcomplaint, -- Sub-Complaint Flag
    receivedepartment, -- Acceptance Department
    receiver, -- Handler / Assignee
    printedflag, -- Printed Flag
    isregionorder, -- Region-Based Ticket Creation: 1=Cs, 2=Hw
    outstandingdays, -- Pending Days As Of Current Date
    finalreplydays, -- Required Final Response Days
    completedbyregion, -- Case Completed By Regional Team
    pledgeachieved, -- Service Commitment Met Flag
    actualreplytime, -- Actual Response Time
    repairdays, -- Allowed Maintenance Days
    grantedhowlong, -- Eot Extension Days (If Granted)
    notificationdays, -- Notification Period (Days) Specified In Fj
    totalprocessingdays, -- Total Handling Days
    referinwsd, -- Internal Transfer Flag: 1=Yes
    isdelete, -- Deletable Flag: 1=Yes, 0=No
    basecallpid, -- Basecallpid
    complantlastupdator, -- Last Complaint Ticket Modifier
    complantlastupdatetime, -- Last Complaint Ticket Modification Time
    isdone, -- Flag: 1=Processed In Abpms System
    createdby, -- Created By
    createdat, -- Data Warehouse Load Time
    lastupdatedby, -- Last Updated By
    lastupdateat, -- Last Update Time
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from coss_ods.ods_pems_cus_t_order_workorder_stg_mini
on duplicate key update
    msgid = values(msgid),
    agentgroupid = values(agentgroupid),
    cusid = values(cusid),
    channeltype = values(channeltype),
    busicenter = values(busicenter),
    classify1 = values(classify1),
    classify2 = values(classify2),
    subarea = values(subarea),
    system = values(system),
    classify3 = values(classify3),
    classify4 = values(classify4),
    realclassify1 = values(realclassify1),
    realclassify2 = values(realclassify2),
    bigregion = values(bigregion),
    subregion = values(subregion),
    dayshift = values(dayshift),
    dutyshift = values(dutyshift),
    urgency = values(urgency),
    isclosed = values(isclosed),
    state = values(state),
    orderstate = values(orderstate),
    isdelay = values(isdelay),
    delayday = values(delayday),
    iscomplant = values(iscomplant),
    isreply = values(isreply),
    replychannel = values(replychannel),
    casesource = values(casesource),
    transferivr = values(transferivr),
    chargeback = values(chargeback),
    ivrlanguage = values(ivrlanguage),
    district1 = values(district1),
    district2 = values(district2),
    isrepeatedcomplaint = values(isrepeatedcomplaint),
    subcomplaint = values(subcomplaint),
    receivedepartment = values(receivedepartment),
    receiver = values(receiver),
    printedflag = values(printedflag),
    isregionorder = values(isregionorder),
    outstandingdays = values(outstandingdays),
    finalreplydays = values(finalreplydays),
    completedbyregion = values(completedbyregion),
    pledgeachieved = values(pledgeachieved),
    actualreplytime = values(actualreplytime),
    repairdays = values(repairdays),
    grantedhowlong = values(grantedhowlong),
    notificationdays = values(notificationdays),
    totalprocessingdays = values(totalprocessingdays),
    referinwsd = values(referinwsd),
    isdelete = values(isdelete),
    basecallpid = values(basecallpid),
    complantlastupdator = values(complantlastupdator),
    complantlastupdatetime = values(complantlastupdatetime),
    isdone = values(isdone),
    createdby = values(createdby),
    createdat = values(createdat),
    lastupdatedby = values(lastupdatedby),
    lastupdateat = values(lastupdateat),
    ods_update_time = values(ods_update_time)
    
 
```



# ods_pems_cus_t_order_workorder_entity_mini_year

## create table

```sql
drop table if exists coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year;

create table if not exists coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year(
    ordernum varchar(30),
    accountid varchar(20),
    customerid varchar(20),
    meterno varchar(50),
    consumptionpointid varchar(20),
    telno varchar(50),
    faxno varchar(50),
    contactno varchar(50),
    address varchar(500),
    servicecontent varchar(4000),
    compliantmemo varchar(2000),
    wsdcreateat timestamp(0),
    completedate date,
    casenumber varchar(50),
    street varchar(200),
    estate varchar(200),
    term varchar(100),
    village varchar(200),
    buildingno varchar(100),
    buildingname varchar(200),
    floor varchar(200),
    company varchar(200),
    relateorder varchar(500),
    thirdid varchar(50),
    responsedate date,
    complainttype varchar(50),
    initialcomplaintdate timestamp(0),
    regionreceivingdate timestamp(0),
    finishtime timestamp,
    actiontaken varchar(1000),
    nature varchar(35),
    responsibleofficer varchar(35),
    interimreplydate date,
    finalreplydate date,
    casereferredothers varchar(35),
    actionsreplycontent varchar(1000),
    repairtype varchar(50),
    repairdate date,
    repairexpirydate date,
    firstrepairreinspectiondate date,
    referringcasedate date,
    issuingdate date,
    expirydate date,
    firstreinspectiondate date,
    methodcompletion varchar(100),
    responsibleai varchar(35),
    responsiblecsi varchar(35),
    supplytype varchar(50),
    slopefeature varchar(35),
    glano varchar(35),
    groupval varchar(35),
    complaintlodged varchar(255),
    email varchar(50),
    acknowledgementdate timestamp(0),
    regiondistrict varchar(50),
    venue varchar(50),
    waterqualitycode varchar(50),
    waterqualitycodecategory bpchar(1),
    interimreplytargetdate date,
    buildingcsuid varchar(19),
    locationx varchar(6),
    locationy varchar(6),
    intervenescase bpchar(1),
    docindexdesc text,
    processingdesc text,
    appointmentremovaldate date,
    appointmentremovalapm varchar(2),
    appointmentwitnessdate date,
    appointmentwitnesstime varchar(12),
    sourcetype bpchar(10),
    remarks varchar(2000),
    createdby int4,
    createdat timestamp,
    lastupdatedby int8,
    lastupdateat timestamp,
    ccid varchar(15),
    ods_load_time timestamp(6) default current_timestamp,
    ods_update_time timestamp(6) default current_timestamp,
    primary key (ordernum)
)
with (
    orientation = row,
    compression = no
)
partition by range (createdat)
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

comment on table coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year is 'PEMS System   Work Order Entity Detail Table';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.ordernum is 'Work Order Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.accountid is 'Account Number';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.customerid is 'Customer Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.meterno is 'Water Meter Number';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.consumptionpointid is 'Water Meter Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.telno is 'Registration No.';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.faxno is 'Fax Number';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.contactno is 'Contact / Landline Phone';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.address is 'Address';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.servicecontent is 'Service Content';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.compliantmemo is 'Complaint Description';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.wsdcreateat is 'Wsd Complaint Receipt Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.completedate is 'Completion Deadline Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.casenumber is '1823 Case Reference No.';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.street is 'Street';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.estate is 'Estate / Village';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.term is 'Phase';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.village is 'Village';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.buildingno is 'Building Number';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.buildingname is 'Building Name';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.floor is 'Floor';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.company is 'Flat / Unit';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.relateorder is 'Linked Work Order Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.thirdid is '3Rd Party Work Order Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.responsedate is 'Response Deadline Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.complainttype is 'Complainant Type';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.initialcomplaintdate is 'Complaint Lodged Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.regionreceivingdate is 'Regional Office Receipt Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.finishtime is 'Work Order Completion Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.actiontaken is 'Action Taken';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.nature is 'Case Type';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.responsibleofficer is 'Case Handler';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.interimreplydate is 'Interim Response Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.finalreplydate is 'Substantive Response Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.casereferredothers is 'Case Referred To Other Staff (E.g. Jo/Distribution Team)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.actionsreplycontent is 'Follow-Up Actions After Response';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.repairtype is 'Repair Notice Type Issued';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.repairdate is 'Repair Notice Issue Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.repairexpirydate is 'Repair Validity Period';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.firstrepairreinspectiondate is '1St Repair Notice Re-Inspection Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.referringcasedate is 'Time Sent To Regional Office';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.issuingdate is 'Fj Issue Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.expirydate is 'Fj Expiry Date (Validity)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.firstreinspectiondate is '1St Fj Re-Inspection Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.methodcompletion is 'Works Completion Method';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.responsibleai is 'Responsible Ai Agent';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.responsiblecsi is 'Responsible Csi Officer';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.supplytype is 'Water Supply Type';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.slopefeature is 'Slope';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.glano is '[Null]';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.groupval is '[Null]';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.complaintlodged is 'Complaint Short Code';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.email is 'Email Address';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.acknowledgementdate is 'Acknowledgement Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.regiondistrict is 'District';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.venue is 'Premises';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.waterqualitycode is 'Water Quality Dictionary Code';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.waterqualitycodecategory is 'System Subcategory: Independent(I)/Multiple(M) For Other Water Quality, Fresh Water Turbidity & Odour Complaints (Flushing Water)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.interimreplytargetdate is 'Interim Reply Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.buildingcsuid is 'Lot & Utility Reference No.';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.locationx is 'X Coordinate';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.locationy is 'Y Coordinate';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.intervenescase is 'Ombudsman Intervention Flag (Y/N)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.docindexdesc is 'Related Document Reference Index';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.processingdesc is 'Case Handling Status';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.appointmentremovaldate is 'Meter Removal Date (Dd/Mm/Yyyy)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.appointmentremovalapm is 'Meter Removal Session (Am/Pm Only)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.appointmentwitnessdate is 'Site Test Witness Date (Dd/Mm/Yyyy)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.appointmentwitnesstime is 'Site Test Witness Time Slot (Hh:mm-Hh:mm)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.sourcetype is 'Ticket Creation Source Channel (Page)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.remarks is 'Remark';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.createdby is 'Created By';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.createdat is 'Data Warehouse Load Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.lastupdatedby is 'Last Updated By';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.lastupdateat is 'Last Update Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.ccid is 'Cc Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.ods_load_time is 'Ods Table Load Timestamp';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year.ods_update_time is 'Ods Table Update Timestamp';
```

## select sql

```sql
select 
    t1.ordernum, -- Work Order Id
    t1.accountid, -- Account Number
    t1.customerid, -- Customer Id
    t1.meterno, -- Water Meter Number
    t1.consumptionpointid, -- Water Meter Id
    t1.telno, -- Registration No.
    t1.faxno, -- Fax Number
    t1.contactno, -- Contact / Landline Phone
    t1.address, -- Address
    t1.servicecontent, -- Service Content
    t1.compliantmemo, -- Complaint Description
    t1.wsdcreateat, -- Wsd Complaint Receipt Time
    t1.completedate, -- Completion Deadline Date
    t1.casenumber, -- 1823 Case Reference No.
    t1.street, -- Street
    t1.estate, -- Estate / Village
    t1.term, -- Phase
    t1.village, -- Village
    t1.buildingno, -- Building Number
    t1.buildingname, -- Building Name
    t1.floor, -- Floor
    t1.company, -- Flat / Unit
    t1.relateorder, -- Linked Work Order Id
    t1.thirdid, -- 3Rd Party Work Order Id
    t1.responsedate, -- Response Deadline Date
    t1.complainttype, -- Complainant Type
    t1.initialcomplaintdate, -- Complaint Lodged Time
    t1.regionreceivingdate, -- Regional Office Receipt Time
    t1.finishtime, -- Work Order Completion Time
    t1.actiontaken, -- Action Taken
    t1.nature, -- Case Type
    t1.responsibleofficer, -- Case Handler
    t1.interimreplydate, -- Interim Response Date
    t1.finalreplydate, -- Substantive Response Date
    t1.casereferredothers, -- Case Referred To Other Staff (E.g. Jo/Distribution Team)
    t1.actionsreplycontent, -- Follow-Up Actions After Response
    t1.repairtype, -- Repair Notice Type Issued
    t1.repairdate, -- Repair Notice Issue Date
    t1.repairexpirydate, -- Repair Validity Period
    t1.firstrepairreinspectiondate, -- 1St Repair Notice Re-Inspection Date
    t1.referringcasedate, -- Time Sent To Regional Office
    t1.issuingdate, -- Fj Issue Date
    t1.expirydate, -- Fj Expiry Date (Validity)
    t1.firstreinspectiondate, -- 1St Fj Re-Inspection Date
    t1.methodcompletion, -- Works Completion Method
    t1.responsibleai, -- Responsible Ai Agent
    t1.responsiblecsi, -- Responsible Csi Officer
    t1.supplytype, -- Water Supply Type
    t1.slopefeature, -- Slope
    t1.glano, -- [Null]
    t1.groupval, -- [Null]
    t1.complaintlodged, -- Complaint Short Code
    t1.email, -- Email Address
    t1.acknowledgementdate, -- Acknowledgement Time
    t1.regiondistrict, -- District
    t1.venue, -- Premises
    t1.waterqualitycode, -- Water Quality Dictionary Code
    t1.waterqualitycodecategory, -- System Subcategory: Independent(I)/Multiple(M) For Other Water Quality, Fresh Water Turbidity & Odour Complaints (Flushing Water)
    t1.interimreplytargetdate, -- Interim Reply Date
    t1.buildingcsuid, -- Lot & Utility Reference No.
    t1.locationx, -- X Coordinate
    t1.locationy, -- Y Coordinate
    t1.intervenescase, -- Ombudsman Intervention Flag (Y/N)
    t1.docindexdesc, -- Related Document Reference Index
    t1.processingdesc, -- Case Handling Status
    t1.appointmentremovaldate, -- Meter Removal Date (Dd/Mm/Yyyy)
    t1.appointmentremovalapm, -- Meter Removal Session (Am/Pm Only)
    t1.appointmentwitnessdate, -- Site Test Witness Date (Dd/Mm/Yyyy)
    t1.appointmentwitnesstime, -- Site Test Witness Time Slot (Hh:mm-Hh:mm)
    t1.sourcetype, -- Ticket Creation Source Channel (Page)
    t1.remarks, -- Remark
    t1.createdby, -- Created By
    t1.createdat, -- Data Warehouse Load Time
    t1.lastupdatedby, -- Last Updated By
    t1.lastupdateat, -- Last Update Time
    t1.ccid, -- Cc Id,
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from pems.t_order_workorder t
inner join pems.t_order_workorder_entity t1 on t.ordernum = t1.ordernum
where
	(t.complantlastupdatetime >= '${complantlastupdatetime}'
	or t.createdat >= '${createdat}')
	and t.classify3 = 10
	
```

## update sql 

```sql
-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Work Order Entity Detail Full Load & Upsert
-- Create         By: dongmaochen
-- Create       Date: 2026-04-23
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini
-- Target Table:  coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year
-- ****************************************************************************************
insert into coss_ods.ods_pems_cus_t_order_workorder_entity_mini_year
select
    ordernum, -- Work Order Id
    accountid, -- Account Number
    customerid, -- Customer Id
    meterno, -- Water Meter Number
    consumptionpointid, -- Water Meter Id
    telno, -- Registration No.
    faxno, -- Fax Number
    contactno, -- Contact / Landline Phone
    address, -- Address
    servicecontent, -- Service Content
    compliantmemo, -- Complaint Description
    wsdcreateat, -- Wsd Complaint Receipt Time
    completedate, -- Completion Deadline Date
    casenumber, -- 1823 Case Reference No.
    street, -- Street
    estate, -- Estate / Village
    term, -- Phase
    village, -- Village
    buildingno, -- Building Number
    buildingname, -- Building Name
    floor, -- Floor
    company, -- Flat / Unit
    relateorder, -- Linked Work Order Id
    thirdid, -- 3Rd Party Work Order Id
    responsedate, -- Response Deadline Date
    complainttype, -- Complainant Type
    initialcomplaintdate, -- Complaint Lodged Time
    regionreceivingdate, -- Regional Office Receipt Time
    finishtime, -- Work Order Completion Time
    actiontaken, -- Action Taken
    nature, -- Case Type
    responsibleofficer, -- Case Handler
    interimreplydate, -- Interim Response Date
    finalreplydate, -- Substantive Response Date
    casereferredothers, -- Case Referred To Other Staff (E.g. Jo/Distribution Team)
    actionsreplycontent, -- Follow-Up Actions After Response
    repairtype, -- Repair Notice Type Issued
    repairdate, -- Repair Notice Issue Date
    repairexpirydate, -- Repair Validity Period
    firstrepairreinspectiondate, -- 1St Repair Notice Re-Inspection Date
    referringcasedate, -- Time Sent To Regional Office
    issuingdate, -- Fj Issue Date
    expirydate, -- Fj Expiry Date (Validity)
    firstreinspectiondate, -- 1St Fj Re-Inspection Date
    methodcompletion, -- Works Completion Method
    responsibleai, -- Responsible Ai Agent
    responsiblecsi, -- Responsible Csi Officer
    supplytype, -- Water Supply Type
    slopefeature, -- Slope
    glano, -- [Null]
    groupval, -- [Null]
    complaintlodged, -- Complaint Short Code
    email, -- Email Address
    acknowledgementdate, -- Acknowledgement Time
    regiondistrict, -- District
    venue, -- Premises
    waterqualitycode, -- Water Quality Dictionary Code
    waterqualitycodecategory, -- System Subcategory: Independent(I)/Multiple(M) For Other Water Quality, Fresh Water Turbidity & Odour Complaints (Flushing Water)
    interimreplytargetdate, -- Interim Reply Date
    buildingcsuid, -- Lot & Utility Reference No.
    locationx, -- X Coordinate
    locationy, -- Y Coordinate
    intervenescase, -- Ombudsman Intervention Flag (Y/N)
    docindexdesc, -- Related Document Reference Index
    processingdesc, -- Case Handling Status
    appointmentremovaldate, -- Meter Removal Date (Dd/Mm/Yyyy)
    appointmentremovalapm, -- Meter Removal Session (Am/Pm Only)
    appointmentwitnessdate, -- Site Test Witness Date (Dd/Mm/Yyyy)
    appointmentwitnesstime, -- Site Test Witness Time Slot (Hh:mm-Hh:mm)
    sourcetype, -- Ticket Creation Source Channel (Page)
    remarks, -- Remark
    createdby, -- Created By
    createdat, -- Data Warehouse Load Time
    lastupdatedby, -- Last Updated By
    lastupdateat, -- Last Update Time
    ccid, -- Cc Id
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini
on duplicate key update
    accountid = values(accountid),
    customerid = values(customerid),
    meterno = values(meterno),
    consumptionpointid = values(consumptionpointid),
    telno = values(telno),
    faxno = values(faxno),
    contactno = values(contactno),
    address = values(address),
    servicecontent = values(servicecontent),
    compliantmemo = values(compliantmemo),
    wsdcreateat = values(wsdcreateat),
    completedate = values(completedate),
    casenumber = values(casenumber),
    street = values(street),
    estate = values(estate),
    term = values(term),
    village = values(village),
    buildingno = values(buildingno),
    buildingname = values(buildingname),
    floor = values(floor),
    company = values(company),
    relateorder = values(relateorder),
    thirdid = values(thirdid),
    responsedate = values(responsedate),
    complainttype = values(complainttype),
    initialcomplaintdate = values(initialcomplaintdate),
    regionreceivingdate = values(regionreceivingdate),
    finishtime = values(finishtime),
    actiontaken = values(actiontaken),
    nature = values(nature),
    responsibleofficer = values(responsibleofficer),
    interimreplydate = values(interimreplydate),
    finalreplydate = values(finalreplydate),
    casereferredothers = values(casereferredothers),
    actionsreplycontent = values(actionsreplycontent),
    repairtype = values(repairtype),
    repairdate = values(repairdate),
    repairexpirydate = values(repairexpirydate),
    firstrepairreinspectiondate = values(firstrepairreinspectiondate),
    referringcasedate = values(referringcasedate),
    issuingdate = values(issuingdate),
    expirydate = values(expirydate),
    firstreinspectiondate = values(firstreinspectiondate),
    methodcompletion = values(methodcompletion),
    responsibleai = values(responsibleai),
    responsiblecsi = values(responsiblecsi),
    supplytype = values(supplytype),
    slopefeature = values(slopefeature),
    glano = values(glano),
    groupval = values(groupval),
    complaintlodged = values(complaintlodged),
    email = values(email),
    acknowledgementdate = values(acknowledgementdate),
    regiondistrict = values(regiondistrict),
    venue = values(venue),
    waterqualitycode = values(waterqualitycode),
    waterqualitycodecategory = values(waterqualitycodecategory),
    interimreplytargetdate = values(interimreplytargetdate),
    buildingcsuid = values(buildingcsuid),
    locationx = values(locationx),
    locationy = values(locationy),
    intervenescase = values(intervenescase),
    docindexdesc = values(docindexdesc),
    processingdesc = values(processingdesc),
    appointmentremovaldate = values(appointmentremovaldate),
    appointmentremovalapm = values(appointmentremovalapm),
    appointmentwitnessdate = values(appointmentwitnessdate),
    appointmentwitnesstime = values(appointmentwitnesstime),
    sourcetype = values(sourcetype),
    remarks = values(remarks),
    createdby = values(createdby),
    createdat = values(createdat),
    lastupdatedby = values(lastupdatedby),
    lastupdateat = values(lastupdateat),
    ccid = values(ccid),
    ods_update_time = values(ods_update_time)
```







# ods_pems_cus_t_order_workorder_di_year

```sql
drop table if exists coss_ods.ods_pems_cus_t_order_workorder_di_year;

create table if not exists coss_ods.ods_pems_cus_t_order_workorder_di_year(
    ordernum varchar(30),
    msgid int8,
    agentgroupid int8,
    cusid varchar(50),
    channeltype int4,
    busicenter varchar(50),
    classify1 int8,
    classify2 int8,
    subarea int8,
    system int8,
    classify3 int8,
    classify4 int8,
    realclassify1 int8,
    realclassify2 int8,
    bigregion varchar(30),
    subregion int8,
    dayshift int4,
    dutyshift int4,
    urgency int4,
    isclosed int4,
    state int4,
    orderstate int4,
    isdelay int4,
    delayday int4,
    iscomplant int4,
    isreply int4,
    replychannel varchar(20),
    casesource int8,
    transferivr int4,
    chargeback int4,
    ivrlanguage int4,
    district1 varchar(30),
    district2 varchar(30),
    isrepeatedcomplaint int4,
    subcomplaint int4,
    receivedepartment int8,
    receiver int8,
    printedflag int4,
    isregionorder int4,
    outstandingdays int4,
    finalreplydays int4,
    completedbyregion varchar(5),
    pledgeachieved varchar(5),
    actualreplytime timestamp,
    repairdays int4,
    grantedhowlong int4,
    notificationdays int4,
    totalprocessingdays int4,
    referinwsd int4,
    isdelete bpchar(1),
    basecallpid int8,
    complantlastupdator int8,
    complantlastupdatetime timestamp,
    isdone int4,
    createdby int8,
    createdat timestamp,
    lastupdatedby int8,
    lastupdateat timestamp,
    ods_load_time timestamp(6) default current_timestamp,
    ods_update_time timestamp(6) default current_timestamp,
    primary key (ordernum)
)
with (
    orientation = row,
    compression = no
)
partition by range (createdat)
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

comment on table coss_ods.ods_pems_cus_t_order_workorder_di_year is 'PEMS System Work Order Main Table';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.ordernum is 'Work Order Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.msgid is 'Message Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.agentgroupid is 'Agent Group Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.cusid is 'Customer Id (Linked To Customer Table)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.channeltype is 'Channel Type';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.busicenter is 'Business Center (Department)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.classify1 is 'Work Order Category 1';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.classify2 is 'Work Order Category 2';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.subarea is 'Region - Branch';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.system is 'Dispatch System';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.classify3 is 'Work Order Category 3';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.classify4 is 'Work Order Category 4';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.realclassify1 is 'Actual Work Order Category 3';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.realclassify2 is 'Actual Work Order Category 4';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.bigregion is 'Administrative Region';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.subregion is 'Region & Branch – Sub-Region';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.dayshift is 'Day Shift Team';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.dutyshift is 'On-Duty Team';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.urgency is 'Urgency Level';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.isclosed is '1=Closed, 2=Dispatched';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.state is 'External Status';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.orderstate is 'Work Order Status: 1=Pending, 2=In Progress, 3=Completed';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.isdelay is 'Is Overdue: 1=Yes';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.delayday is 'Overdue Days';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.iscomplant is 'Is Complaint Ticket: 1=Yes, 2=Tree-Related, 0=No';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.isreply is 'Reply Required: 1=Yes';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.replychannel is 'Reply Channel';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.casesource is 'Case Source';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.transferivr is 'Transferred To Ivr';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.chargeback is 'Returned Order';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.ivrlanguage is 'Ivr Language Selection';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.district1 is 'Primary Concern Area';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.district2 is 'Secondary Concern Area';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.isrepeatedcomplaint is 'Repeat Complaint Flag';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.subcomplaint is 'Sub-Complaint Flag';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.receivedepartment is 'Acceptance Department';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.receiver is 'Handler / Assignee';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.printedflag is 'Printed Flag';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.isregionorder is 'Region-Based Ticket Creation: 1=Cs, 2=Hw';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.outstandingdays is 'Pending Days As Of Current Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.finalreplydays is 'Required Final Response Days';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.completedbyregion is 'Case Completed By Regional Team';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.pledgeachieved is 'Service Commitment Met Flag';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.actualreplytime is 'Actual Response Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.repairdays is 'Allowed Maintenance Days';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.grantedhowlong is 'Eot Extension Days (If Granted)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.notificationdays is 'Notification Period (Days) Specified In Fj';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.totalprocessingdays is 'Total Handling Days';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.referinwsd is 'Internal Transfer Flag: 1=Yes';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.isdelete is 'Deletable Flag: 1=Yes, 0=No';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.basecallpid is 'Basecallpid';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.complantlastupdator is 'Last Complaint Ticket Modifier';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.complantlastupdatetime is 'Last Complaint Ticket Modification Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.isdone is 'Flag: 1=Processed In Abpms System';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.createdby is 'Created By';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.createdat is 'Data Warehouse Load Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.lastupdatedby is 'Last Updated By';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.lastupdateat is 'Last Update Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.ods_load_time is 'Ods Table Load Timestamp';
comment on column coss_ods.ods_pems_cus_t_order_workorder_di_year.ods_update_time is 'Ods Table Update Timestamp';






select
    ordernum, -- Work Order Id
    msgid, -- Message Id
    agentgroupid, -- Agent Group Id
    cusid, -- Customer Id (Linked To Customer Table)
    channeltype, -- Channel Type
    busicenter, -- Business Center (Department)
    classify1, -- Work Order Category 1
    classify2, -- Work Order Category 2
    subarea, -- Region - Branch
    system, -- Dispatch System
    classify3, -- Work Order Category 3
    classify4, -- Work Order Category 4
    realclassify1, -- Actual Work Order Category 3
    realclassify2, -- Actual Work Order Category 4
    bigregion, -- Administrative Region
    subregion, -- Region & Branch – Sub-Region
    dayshift, -- Day Shift Team
    dutyshift, -- On-Duty Team
    urgency, -- Urgency Level
    isclosed, -- 1=Closed, 2=Dispatched
    state, -- External Status
    orderstate, -- Work Order Status: 1=Pending, 2=In Progress, 3=Completed
    isdelay, -- Is Overdue: 1=Yes
    delayday, -- Overdue Days
    iscomplant, -- Is Complaint Ticket: 1=Yes, 2=Tree-Related, 0=No
    isreply, -- Reply Required: 1=Yes
    replychannel, -- Reply Channel
    casesource, -- Case Source
    transferivr, -- Transferred To Ivr
    chargeback, -- Returned Order
    ivrlanguage, -- Ivr Language Selection
    district1, -- Primary Concern Area
    district2, -- Secondary Concern Area
    isrepeatedcomplaint, -- Repeat Complaint Flag
    subcomplaint, -- Sub-Complaint Flag
    receivedepartment, -- Acceptance Department
    receiver, -- Handler / Assignee
    printedflag, -- Printed Flag
    isregionorder, -- Region-Based Ticket Creation: 1=Cs, 2=Hw
    outstandingdays, -- Pending Days As Of Current Date
    finalreplydays, -- Required Final Response Days
    completedbyregion, -- Case Completed By Regional Team
    pledgeachieved, -- Service Commitment Met Flag
    actualreplytime, -- Actual Response Time
    repairdays, -- Allowed Maintenance Days
    grantedhowlong, -- Eot Extension Days (If Granted)
    notificationdays, -- Notification Period (Days) Specified In Fj
    totalprocessingdays, -- Total Handling Days
    referinwsd, -- Internal Transfer Flag: 1=Yes
    isdelete, -- Deletable Flag: 1=Yes, 0=No
    basecallpid, -- Basecallpid
    complantlastupdator, -- Last Complaint Ticket Modifier
    complantlastupdatetime, -- Last Complaint Ticket Modification Time
    isdone, -- Flag: 1=Processed In Abpms System
    createdby, -- Created By
    createdat, -- Data Warehouse Load Time
    lastupdatedby, -- Last Updated By
    lastupdateat, -- Last Update Time,
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from pems.t_order_workorder
where
	(complantlastupdatetime >= '${complantlastupdatetime}'
	or createdat >= '${createdat}')
	and classify3 = 10




-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Main Work Order Info Full Load & Upsert
-- Create         By: dongmaochen
-- Create       Date: 2026-04-23
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_pems_cus_t_order_workorder_stg_di
-- Target Table:  coss_ods.ods_pems_cus_t_order_workorder_di_year
-- ****************************************************************************************
insert into coss_ods.ods_pems_cus_t_order_workorder_di_year
select
    ordernum, -- Work Order Id
    msgid, -- Message Id
    agentgroupid, -- Agent Group Id
    cusid, -- Customer Id (Linked To Customer Table)
    channeltype, -- Channel Type
    busicenter, -- Business Center (Department)
    classify1, -- Work Order Category 1
    classify2, -- Work Order Category 2
    subarea, -- Region - Branch
    system, -- Dispatch System
    classify3, -- Work Order Category 3
    classify4, -- Work Order Category 4
    realclassify1, -- Actual Work Order Category 3
    realclassify2, -- Actual Work Order Category 4
    bigregion, -- Administrative Region
    subregion, -- Region & Branch – Sub-Region
    dayshift, -- Day Shift Team
    dutyshift, -- On-Duty Team
    urgency, -- Urgency Level
    isclosed, -- 1=Closed, 2=Dispatched
    state, -- External Status
    orderstate, -- Work Order Status: 1=Pending, 2=In Progress, 3=Completed
    isdelay, -- Is Overdue: 1=Yes
    delayday, -- Overdue Days
    iscomplant, -- Is Complaint Ticket: 1=Yes, 2=Tree-Related, 0=No
    isreply, -- Reply Required: 1=Yes
    replychannel, -- Reply Channel
    casesource, -- Case Source
    transferivr, -- Transferred To Ivr
    chargeback, -- Returned Order
    ivrlanguage, -- Ivr Language Selection
    district1, -- Primary Concern Area
    district2, -- Secondary Concern Area
    isrepeatedcomplaint, -- Repeat Complaint Flag
    subcomplaint, -- Sub-Complaint Flag
    receivedepartment, -- Acceptance Department
    receiver, -- Handler / Assignee
    printedflag, -- Printed Flag
    isregionorder, -- Region-Based Ticket Creation: 1=Cs, 2=Hw
    outstandingdays, -- Pending Days As Of Current Date
    finalreplydays, -- Required Final Response Days
    completedbyregion, -- Case Completed By Regional Team
    pledgeachieved, -- Service Commitment Met Flag
    actualreplytime, -- Actual Response Time
    repairdays, -- Allowed Maintenance Days
    grantedhowlong, -- Eot Extension Days (If Granted)
    notificationdays, -- Notification Period (Days) Specified In Fj
    totalprocessingdays, -- Total Handling Days
    referinwsd, -- Internal Transfer Flag: 1=Yes
    isdelete, -- Deletable Flag: 1=Yes, 0=No
    basecallpid, -- Basecallpid
    complantlastupdator, -- Last Complaint Ticket Modifier
    complantlastupdatetime, -- Last Complaint Ticket Modification Time
    isdone, -- Flag: 1=Processed In Abpms System
    createdby, -- Created By
    createdat, -- Data Warehouse Load Time
    lastupdatedby, -- Last Updated By
    lastupdateat, -- Last Update Time
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from coss_ods.ods_pems_cus_t_order_workorder_stg_di
on duplicate key update
    msgid = values(msgid),
    agentgroupid = values(agentgroupid),
    cusid = values(cusid),
    channeltype = values(channeltype),
    busicenter = values(busicenter),
    classify1 = values(classify1),
    classify2 = values(classify2),
    subarea = values(subarea),
    system = values(system),
    classify3 = values(classify3),
    classify4 = values(classify4),
    realclassify1 = values(realclassify1),
    realclassify2 = values(realclassify2),
    bigregion = values(bigregion),
    subregion = values(subregion),
    dayshift = values(dayshift),
    dutyshift = values(dutyshift),
    urgency = values(urgency),
    isclosed = values(isclosed),
    state = values(state),
    orderstate = values(orderstate),
    isdelay = values(isdelay),
    delayday = values(delayday),
    iscomplant = values(iscomplant),
    isreply = values(isreply),
    replychannel = values(replychannel),
    casesource = values(casesource),
    transferivr = values(transferivr),
    chargeback = values(chargeback),
    ivrlanguage = values(ivrlanguage),
    district1 = values(district1),
    district2 = values(district2),
    isrepeatedcomplaint = values(isrepeatedcomplaint),
    subcomplaint = values(subcomplaint),
    receivedepartment = values(receivedepartment),
    receiver = values(receiver),
    printedflag = values(printedflag),
    isregionorder = values(isregionorder),
    outstandingdays = values(outstandingdays),
    finalreplydays = values(finalreplydays),
    completedbyregion = values(completedbyregion),
    pledgeachieved = values(pledgeachieved),
    actualreplytime = values(actualreplytime),
    repairdays = values(repairdays),
    grantedhowlong = values(grantedhowlong),
    notificationdays = values(notificationdays),
    totalprocessingdays = values(totalprocessingdays),
    referinwsd = values(referinwsd),
    isdelete = values(isdelete),
    basecallpid = values(basecallpid),
    complantlastupdator = values(complantlastupdator),
    complantlastupdatetime = values(complantlastupdatetime),
    isdone = values(isdone),
    createdby = values(createdby),
    createdat = values(createdat),
    lastupdatedby = values(lastupdatedby),
    lastupdateat = values(lastupdateat),
    ods_update_time = values(ods_update_time)

 
```



# ods_pems_cus_t_order_workorder_entity_di_year



```sql
drop table if exists coss_ods.ods_pems_cus_t_order_workorder_entity_di_year;

create table if not exists coss_ods.ods_pems_cus_t_order_workorder_entity_di_year(
    ordernum varchar(30),
    accountid varchar(20),
    customerid varchar(20),
    meterno varchar(50),
    consumptionpointid varchar(20),
    telno varchar(50),
    faxno varchar(50),
    contactno varchar(50),
    address varchar(500),
    servicecontent varchar(4000),
    compliantmemo varchar(2000),
    wsdcreateat timestamp(0),
    completedate date,
    casenumber varchar(50),
    street varchar(200),
    estate varchar(200),
    term varchar(100),
    village varchar(200),
    buildingno varchar(100),
    buildingname varchar(200),
    floor varchar(200),
    company varchar(200),
    relateorder varchar(500),
    thirdid varchar(50),
    responsedate date,
    complainttype varchar(50),
    initialcomplaintdate timestamp(0),
    regionreceivingdate timestamp(0),
    finishtime timestamp,
    actiontaken varchar(1000),
    nature varchar(35),
    responsibleofficer varchar(35),
    interimreplydate date,
    finalreplydate date,
    casereferredothers varchar(35),
    actionsreplycontent varchar(1000),
    repairtype varchar(50),
    repairdate date,
    repairexpirydate date,
    firstrepairreinspectiondate date,
    referringcasedate date,
    issuingdate date,
    expirydate date,
    firstreinspectiondate date,
    methodcompletion varchar(100),
    responsibleai varchar(35),
    responsiblecsi varchar(35),
    supplytype varchar(50),
    slopefeature varchar(35),
    glano varchar(35),
    groupval varchar(35),
    complaintlodged varchar(255),
    email varchar(50),
    acknowledgementdate timestamp(0),
    regiondistrict varchar(50),
    venue varchar(50),
    waterqualitycode varchar(50),
    waterqualitycodecategory bpchar(1),
    interimreplytargetdate date,
    buildingcsuid varchar(19),
    locationx varchar(6),
    locationy varchar(6),
    intervenescase bpchar(1),
    docindexdesc text,
    processingdesc text,
    appointmentremovaldate date,
    appointmentremovalapm varchar(2),
    appointmentwitnessdate date,
    appointmentwitnesstime varchar(12),
    sourcetype bpchar(10),
    remarks varchar(2000),
    createdby int4,
    createdat timestamp,
    lastupdatedby int8,
    lastupdateat timestamp,
    ccid varchar(15),
    ods_load_time timestamp(6) default current_timestamp,
    ods_update_time timestamp(6) default current_timestamp,
    primary key (ordernum)
)
with (
    orientation = row,
    compression = no
)
partition by range (createdat)
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

comment on table coss_ods.ods_pems_cus_t_order_workorder_entity_di_year is 'PEMS System   Work Order Entity Detail Table';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.ordernum is 'Work Order Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.accountid is 'Account Number';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.customerid is 'Customer Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.meterno is 'Water Meter Number';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.consumptionpointid is 'Water Meter Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.telno is 'Registration No.';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.faxno is 'Fax Number';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.contactno is 'Contact / Landline Phone';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.address is 'Address';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.servicecontent is 'Service Content';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.compliantmemo is 'Complaint Description';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.wsdcreateat is 'Wsd Complaint Receipt Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.completedate is 'Completion Deadline Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.casenumber is '1823 Case Reference No.';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.street is 'Street';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.estate is 'Estate / Village';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.term is 'Phase';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.village is 'Village';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.buildingno is 'Building Number';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.buildingname is 'Building Name';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.floor is 'Floor';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.company is 'Flat / Unit';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.relateorder is 'Linked Work Order Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.thirdid is '3Rd Party Work Order Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.responsedate is 'Response Deadline Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.complainttype is 'Complainant Type';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.initialcomplaintdate is 'Complaint Lodged Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.regionreceivingdate is 'Regional Office Receipt Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.finishtime is 'Work Order Completion Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.actiontaken is 'Action Taken';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.nature is 'Case Type';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.responsibleofficer is 'Case Handler';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.interimreplydate is 'Interim Response Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.finalreplydate is 'Substantive Response Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.casereferredothers is 'Case Referred To Other Staff (E.g. Jo/Distribution Team)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.actionsreplycontent is 'Follow-Up Actions After Response';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.repairtype is 'Repair Notice Type Issued';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.repairdate is 'Repair Notice Issue Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.repairexpirydate is 'Repair Validity Period';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.firstrepairreinspectiondate is '1St Repair Notice Re-Inspection Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.referringcasedate is 'Time Sent To Regional Office';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.issuingdate is 'Fj Issue Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.expirydate is 'Fj Expiry Date (Validity)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.firstreinspectiondate is '1St Fj Re-Inspection Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.methodcompletion is 'Works Completion Method';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.responsibleai is 'Responsible Ai Agent';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.responsiblecsi is 'Responsible Csi Officer';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.supplytype is 'Water Supply Type';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.slopefeature is 'Slope';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.glano is '[Null]';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.groupval is '[Null]';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.complaintlodged is 'Complaint Short Code';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.email is 'Email Address';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.acknowledgementdate is 'Acknowledgement Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.regiondistrict is 'District';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.venue is 'Premises';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.waterqualitycode is 'Water Quality Dictionary Code';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.waterqualitycodecategory is 'System Subcategory: Independent(I)/Multiple(M) For Other Water Quality, Fresh Water Turbidity & Odour Complaints (Flushing Water)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.interimreplytargetdate is 'Interim Reply Date';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.buildingcsuid is 'Lot & Utility Reference No.';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.locationx is 'X Coordinate';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.locationy is 'Y Coordinate';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.intervenescase is 'Ombudsman Intervention Flag (Y/N)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.docindexdesc is 'Related Document Reference Index';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.processingdesc is 'Case Handling Status';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.appointmentremovaldate is 'Meter Removal Date (Dd/Mm/Yyyy)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.appointmentremovalapm is 'Meter Removal Session (Am/Pm Only)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.appointmentwitnessdate is 'Site Test Witness Date (Dd/Mm/Yyyy)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.appointmentwitnesstime is 'Site Test Witness Time Slot (Hh:mm-Hh:mm)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.sourcetype is 'Ticket Creation Source Channel (Page)';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.remarks is 'Remark';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.createdby is 'Created By';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.createdat is 'Data Warehouse Load Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.lastupdatedby is 'Last Updated By';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.lastupdateat is 'Last Update Time';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.ccid is 'Cc Id';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.ods_load_time is 'Ods Table Load Timestamp';
comment on column coss_ods.ods_pems_cus_t_order_workorder_entity_di_year.ods_update_time is 'Ods Table Update Timestamp';








select
    ordernum, -- Work Order Id
    accountid, -- Account Number
    customerid, -- Customer Id
    meterno, -- Water Meter Number
    consumptionpointid, -- Water Meter Id
    telno, -- Registration No.
    faxno, -- Fax Number
    contactno, -- Contact / Landline Phone
    address, -- Address
    servicecontent, -- Service Content
    compliantmemo, -- Complaint Description
    wsdcreateat, -- Wsd Complaint Receipt Time
    completedate, -- Completion Deadline Date
    casenumber, -- 1823 Case Reference No.
    street, -- Street
    estate, -- Estate / Village
    term, -- Phase
    village, -- Village
    buildingno, -- Building Number
    buildingname, -- Building Name
    floor, -- Floor
    company, -- Flat / Unit
    relateorder, -- Linked Work Order Id
    thirdid, -- 3Rd Party Work Order Id
    responsedate, -- Response Deadline Date
    complainttype, -- Complainant Type
    initialcomplaintdate, -- Complaint Lodged Time
    regionreceivingdate, -- Regional Office Receipt Time
    finishtime, -- Work Order Completion Time
    actiontaken, -- Action Taken
    nature, -- Case Type
    responsibleofficer, -- Case Handler
    interimreplydate, -- Interim Response Date
    finalreplydate, -- Substantive Response Date
    casereferredothers, -- Case Referred To Other Staff (E.g. Jo/Distribution Team)
    actionsreplycontent, -- Follow-Up Actions After Response
    repairtype, -- Repair Notice Type Issued
    repairdate, -- Repair Notice Issue Date
    repairexpirydate, -- Repair Validity Period
    firstrepairreinspectiondate, -- 1St Repair Notice Re-Inspection Date
    referringcasedate, -- Time Sent To Regional Office
    issuingdate, -- Fj Issue Date
    expirydate, -- Fj Expiry Date (Validity)
    firstreinspectiondate, -- 1St Fj Re-Inspection Date
    methodcompletion, -- Works Completion Method
    responsibleai, -- Responsible Ai Agent
    responsiblecsi, -- Responsible Csi Officer
    supplytype, -- Water Supply Type
    slopefeature, -- Slope
    glano, -- [Null]
    groupval, -- [Null]
    complaintlodged, -- Complaint Short Code
    email, -- Email Address
    acknowledgementdate, -- Acknowledgement Time
    regiondistrict, -- District
    venue, -- Premises
    waterqualitycode, -- Water Quality Dictionary Code
    waterqualitycodecategory, -- System Subcategory: Independent(I)/Multiple(M) For Other Water Quality, Fresh Water Turbidity & Odour Complaints (Flushing Water)
    interimreplytargetdate, -- Interim Reply Date
    buildingcsuid, -- Lot & Utility Reference No.
    locationx, -- X Coordinate
    locationy, -- Y Coordinate
    intervenescase, -- Ombudsman Intervention Flag (Y/N)
    docindexdesc, -- Related Document Reference Index
    processingdesc, -- Case Handling Status
    appointmentremovaldate, -- Meter Removal Date (Dd/Mm/Yyyy)
    appointmentremovalapm, -- Meter Removal Session (Am/Pm Only)
    appointmentwitnessdate, -- Site Test Witness Date (Dd/Mm/Yyyy)
    appointmentwitnesstime, -- Site Test Witness Time Slot (Hh:mm-Hh:mm)
    sourcetype, -- Ticket Creation Source Channel (Page)
    remarks, -- Remark
    createdby, -- Created By
    createdat, -- Data Warehouse Load Time
    lastupdatedby, -- Last Updated By
    lastupdateat, -- Last Update Time
    ccid, -- Cc Id,
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from pems.t_order_workorder_entity
where
    (lastupdateat >= '${lastupdateat}'
    or createdat >= '${createdat}')






-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Work Order Entity Detail Full Load & Upsert
-- Create         By: dongmaochen
-- Create       Date: 2026-04-23
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini
-- Target Table:  coss_ods.ods_pems_cus_t_order_workorder_entity_di_year
-- ****************************************************************************************
insert into coss_ods.ods_pems_cus_t_order_workorder_entity_di_year
select
    ordernum, -- Work Order Id
    accountid, -- Account Number
    customerid, -- Customer Id
    meterno, -- Water Meter Number
    consumptionpointid, -- Water Meter Id
    telno, -- Registration No.
    faxno, -- Fax Number
    contactno, -- Contact / Landline Phone
    address, -- Address
    servicecontent, -- Service Content
    compliantmemo, -- Complaint Description
    wsdcreateat, -- Wsd Complaint Receipt Time
    completedate, -- Completion Deadline Date
    casenumber, -- 1823 Case Reference No.
    street, -- Street
    estate, -- Estate / Village
    term, -- Phase
    village, -- Village
    buildingno, -- Building Number
    buildingname, -- Building Name
    floor, -- Floor
    company, -- Flat / Unit
    relateorder, -- Linked Work Order Id
    thirdid, -- 3Rd Party Work Order Id
    responsedate, -- Response Deadline Date
    complainttype, -- Complainant Type
    initialcomplaintdate, -- Complaint Lodged Time
    regionreceivingdate, -- Regional Office Receipt Time
    finishtime, -- Work Order Completion Time
    actiontaken, -- Action Taken
    nature, -- Case Type
    responsibleofficer, -- Case Handler
    interimreplydate, -- Interim Response Date
    finalreplydate, -- Substantive Response Date
    casereferredothers, -- Case Referred To Other Staff (E.g. Jo/Distribution Team)
    actionsreplycontent, -- Follow-Up Actions After Response
    repairtype, -- Repair Notice Type Issued
    repairdate, -- Repair Notice Issue Date
    repairexpirydate, -- Repair Validity Period
    firstrepairreinspectiondate, -- 1St Repair Notice Re-Inspection Date
    referringcasedate, -- Time Sent To Regional Office
    issuingdate, -- Fj Issue Date
    expirydate, -- Fj Expiry Date (Validity)
    firstreinspectiondate, -- 1St Fj Re-Inspection Date
    methodcompletion, -- Works Completion Method
    responsibleai, -- Responsible Ai Agent
    responsiblecsi, -- Responsible Csi Officer
    supplytype, -- Water Supply Type
    slopefeature, -- Slope
    glano, -- [Null]
    groupval, -- [Null]
    complaintlodged, -- Complaint Short Code
    email, -- Email Address
    acknowledgementdate, -- Acknowledgement Time
    regiondistrict, -- District
    venue, -- Premises
    waterqualitycode, -- Water Quality Dictionary Code
    waterqualitycodecategory, -- System Subcategory: Independent(I)/Multiple(M) For Other Water Quality, Fresh Water Turbidity & Odour Complaints (Flushing Water)
    interimreplytargetdate, -- Interim Reply Date
    buildingcsuid, -- Lot & Utility Reference No.
    locationx, -- X Coordinate
    locationy, -- Y Coordinate
    intervenescase, -- Ombudsman Intervention Flag (Y/N)
    docindexdesc, -- Related Document Reference Index
    processingdesc, -- Case Handling Status
    appointmentremovaldate, -- Meter Removal Date (Dd/Mm/Yyyy)
    appointmentremovalapm, -- Meter Removal Session (Am/Pm Only)
    appointmentwitnessdate, -- Site Test Witness Date (Dd/Mm/Yyyy)
    appointmentwitnesstime, -- Site Test Witness Time Slot (Hh:mm-Hh:mm)
    sourcetype, -- Ticket Creation Source Channel (Page)
    remarks, -- Remark
    createdby, -- Created By
    createdat, -- Data Warehouse Load Time
    lastupdatedby, -- Last Updated By
    lastupdateat, -- Last Update Time
    ccid, -- Cc Id
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from coss_ods.ods_pems_cus_t_order_workorder_entity_stg_di
on duplicate key update
    accountid = values(accountid),
    customerid = values(customerid),
    meterno = values(meterno),
    consumptionpointid = values(consumptionpointid),
    telno = values(telno),
    faxno = values(faxno),
    contactno = values(contactno),
    address = values(address),
    servicecontent = values(servicecontent),
    compliantmemo = values(compliantmemo),
    wsdcreateat = values(wsdcreateat),
    completedate = values(completedate),
    casenumber = values(casenumber),
    street = values(street),
    estate = values(estate),
    term = values(term),
    village = values(village),
    buildingno = values(buildingno),
    buildingname = values(buildingname),
    floor = values(floor),
    company = values(company),
    relateorder = values(relateorder),
    thirdid = values(thirdid),
    responsedate = values(responsedate),
    complainttype = values(complainttype),
    initialcomplaintdate = values(initialcomplaintdate),
    regionreceivingdate = values(regionreceivingdate),
    finishtime = values(finishtime),
    actiontaken = values(actiontaken),
    nature = values(nature),
    responsibleofficer = values(responsibleofficer),
    interimreplydate = values(interimreplydate),
    finalreplydate = values(finalreplydate),
    casereferredothers = values(casereferredothers),
    actionsreplycontent = values(actionsreplycontent),
    repairtype = values(repairtype),
    repairdate = values(repairdate),
    repairexpirydate = values(repairexpirydate),
    firstrepairreinspectiondate = values(firstrepairreinspectiondate),
    referringcasedate = values(referringcasedate),
    issuingdate = values(issuingdate),
    expirydate = values(expirydate),
    firstreinspectiondate = values(firstreinspectiondate),
    methodcompletion = values(methodcompletion),
    responsibleai = values(responsibleai),
    responsiblecsi = values(responsiblecsi),
    supplytype = values(supplytype),
    slopefeature = values(slopefeature),
    glano = values(glano),
    groupval = values(groupval),
    complaintlodged = values(complaintlodged),
    email = values(email),
    acknowledgementdate = values(acknowledgementdate),
    regiondistrict = values(regiondistrict),
    venue = values(venue),
    waterqualitycode = values(waterqualitycode),
    waterqualitycodecategory = values(waterqualitycodecategory),
    interimreplytargetdate = values(interimreplytargetdate),
    buildingcsuid = values(buildingcsuid),
    locationx = values(locationx),
    locationy = values(locationy),
    intervenescase = values(intervenescase),
    docindexdesc = values(docindexdesc),
    processingdesc = values(processingdesc),
    appointmentremovaldate = values(appointmentremovaldate),
    appointmentremovalapm = values(appointmentremovalapm),
    appointmentwitnessdate = values(appointmentwitnessdate),
    appointmentwitnesstime = values(appointmentwitnesstime),
    sourcetype = values(sourcetype),
    remarks = values(remarks),
    createdby = values(createdby),
    createdat = values(createdat),
    lastupdatedby = values(lastupdatedby),
    lastupdateat = values(lastupdateat),
    ccid = values(ccid),
    ods_update_time = values(ods_update_time)
```

# ods_pems_cus_t_dic_actionregion_df

```sql
ods_pems_cus_t_dic_actionregion_df
create table
sql
drop table if exists coss_ods.ods_pems_cus_t_dic_actionregion_df;
create table if not exists coss_ods.ods_pems_cus_t_dic_actionregion_df(
    id int4,
    nametc varchar(100),
    namesc varchar(100),
    nameen varchar(100),
    isvalid int4,
    createdat timestamp,
    createdby int4,
    lastupdateat timestamp,
    updatedby int4,
    ods_load_time timestamp(6) default current_timestamp,
    ods_update_time timestamp(6) default current_timestamp,
    primary key (id)
)
with (
    orientation = row,
    compression = no
);
comment on table coss_ods.ods_pems_cus_t_dic_actionregion_df is 'PEMS System Action Region Dictionary Table';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.id is 'Region ID Primary Key';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.nametc is 'Traditional Chinese Region Name';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.namesc is 'Simplified Chinese Region Name';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.nameen is 'English Region Name';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.isvalid is 'Valid Flag:1=Valid,0=Invalid';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.createdat is 'Record Create Time';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.createdby is 'Creator User ID';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.lastupdateat is 'Last Update Time';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.updatedby is 'Last Update User ID';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.ods_load_time is 'Ods Table Load Timestamp';
comment on column coss_ods.ods_pems_cus_t_dic_actionregion_df.ods_update_time is 'Ods Table Update Timestamp';
select sql
sql
select 
    id, -- Region ID Primary Key
    nametc, -- Traditional Chinese Region Name
    namesc, -- Simplified Chinese Region Name
    nameen, -- English Region Name
    isvalid, -- Valid Flag:1=Valid,0=Invalid
    createdat, -- Record Create Time
    createdby, -- Creator User ID
    lastupdateat, -- Last Update Time
    updatedby, -- Last Update User ID
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from pems.t_dic_actionregion


update sql
sql
-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Action Region Dictionary Full Load & Upsert
-- Create       Date: 2026-07-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_pems_cus_t_dic_actionregion_stg_df
-- Target Table:  coss_ods.ods_pems_cus_t_dic_actionregion_df
-- ****************************************************************************************
insert into coss_ods.ods_pems_cus_t_dic_actionregion_df
select
    id, -- Region ID Primary Key
    nametc, -- Traditional Chinese Region Name
    namesc, -- Simplified Chinese Region Name
    nameen, -- English Region Name
    isvalid, -- Valid Flag:1=Valid,0=Invalid
    createdat, -- Record Create Time
    createdby, -- Creator User ID
    lastupdateat, -- Last Update Time
    updatedby, -- Last Update User ID
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from coss_ods.ods_pems_cus_t_dic_actionregion_stg_df
on duplicate key update
    nametc = values(nametc),
    namesc = values(namesc),
    nameen = values(nameen),
    isvalid = values(isvalid),
    createdat = values(createdat),
    createdby = values(createdby),
    lastupdateat = values(lastupdateat),
    updatedby = values(updatedby),
    ods_update_time = values(ods_update_time);
```

# ods_pems_cus_t_dic_bigclass_df



```sql
create table
sql
drop table if exists coss_ods.ods_pems_cus_t_dic_bigclass_df;
create table if not exists coss_ods.ods_pems_cus_t_dic_bigclass_df(
    id int8,
    center varchar(20),
    namesc varchar(100),
    nametc varchar(100),
    nameen varchar(100),
    parentid int8,
    level int4,
    createdat timestamp,
    createdby int4,
    isregionorder int4,
    lastupdateat timestamp,
    updatedby int4,
    descriptionsc varchar(1000),
    descriptiontc varchar(1000),
    descriptionen varchar(1000),
    ods_load_time timestamp(6) default current_timestamp,
    ods_update_time timestamp(6) default current_timestamp,
    primary key (id)
)
with (
    orientation = row,
    compression = no
);
comment on table coss_ods.ods_pems_cus_t_dic_bigclass_df is 'PEMS System Level 1&2 Work Order Category Dictionary Table';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.id is 'Category Primary Key ID';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.center is 'Business Center Code';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.namesc is 'Simplified Chinese Category Name';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.nametc is 'Traditional Chinese Category Name';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.nameen is 'English Category Name';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.parentid is 'Parent Category ID';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.level is 'Category Hierarchy Level';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.createdat is 'Record Create Time';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.createdby is 'Creator User ID';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.isregionorder is 'Region-Based Ticket Creation: 1=CS, 2=HW';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.lastupdateat is 'Last Update Time';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.updatedby is 'Last Update User ID';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.descriptionsc is 'Simplified Chinese Description';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.descriptiontc is 'Traditional Chinese Description';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.descriptionen is 'English Description';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.ods_load_time is 'Ods Table Load Timestamp';
comment on column coss_ods.ods_pems_cus_t_dic_bigclass_df.ods_update_time is 'Ods Table Update Timestamp';
select sql
sql
select
    id, -- Category Primary Key ID
    center, -- Business Center Code
    namesc, -- Simplified Chinese Category Name
    nametc, -- Traditional Chinese Category Name
    nameen, -- English Category Name
    parentid, -- Parent Category ID
    level, -- Category Hierarchy Level
    createdat, -- Record Create Time
    createdby, -- Creator User ID
    isregionorder, -- Region-Based Ticket Creation: 1=CS, 2=HW
    lastupdateat, -- Last Update Time
    updatedby, -- Last Update User ID
    descriptionsc, -- Simplified Chinese Description
    descriptiontc, -- Traditional Chinese Description
    descriptionen, -- English Description
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from pems.t_dic_bigclass

update sql
sql
-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Work Order Level 1&2 Category Dict Full Load & Upsert
-- Create       Date: 2026-07-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_pems_cus_t_dic_bigclass_stg_mini
-- Target Table:  coss_ods.ods_pems_cus_t_dic_bigclass_df
-- ****************************************************************************************
insert into coss_ods.ods_pems_cus_t_dic_bigclass_df
select
    id, -- Category Primary Key ID
    center, -- Business Center Code
    namesc, -- Simplified Chinese Category Name
    nametc, -- Traditional Chinese Category Name
    nameen, -- English Category Name
    parentid, -- Parent Category ID
    level, -- Category Hierarchy Level
    createdat, -- Record Create Time
    createdby, -- Creator User ID
    isregionorder, -- Region-Based Ticket Creation: 1=CS, 2=HW
    lastupdateat, -- Last Update Time
    updatedby, -- Last Update User ID
    descriptionsc, -- Simplified Chinese Description
    descriptiontc, -- Traditional Chinese Description
    descriptionen, -- English Description
    current_timestamp as ods_load_time, -- Ods Table Load Timestamp
    current_timestamp as ods_update_time -- Ods Table Update Timestamp
from coss_ods.ods_pems_cus_t_dic_bigclass_stg_df
on duplicate key update
    center = values(center),
    namesc = values(namesc),
    nametc = values(nametc),
    nameen = values(nameen),
    parentid = values(parentid),
    level = values(level),
    createdat = values(createdat),
    createdby = values(createdby),
    isregionorder = values(isregionorder),
    lastupdateat = values(lastupdateat),
    updatedby = values(updatedby),
    descriptionsc = values(descriptionsc),
    descriptiontc = values(descriptiontc),
    descriptionen = values(descriptionen),
    ods_update_time = values(ods_update_time);
```



# ods_pems_cus_t_dic_concerndistric_df



```sql
ods_pems_cus_t_dic_concerndistric_df
create table
sql
drop table if exists coss_ods.ods_pems_cus_t_dic_concerndistric_df;
create table if not exists coss_ods.ods_pems_cus_t_dic_concerndistric_df(
    id int8,
    namesc varchar(100),
    nametc varchar(100),
    nameen varchar(100),
    isvalid int4,
    createdat timestamp,
    lastupdateat timestamp,
    code varchar(30),
    dtmf int4,
    sort int4,
    createdby int4,
    updatedby int4,
    ods_load_time timestamp(6) default current_timestamp,
    ods_update_time timestamp(6) default current_timestamp,
    primary key (id)
)
with (
    orientation = row,
    compression = no
);
comment on table coss_ods.ods_pems_cus_t_dic_concerndistric_df is 'PEMS System Concern Area Dictionary Table';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.id is 'Concern Area Primary Key ID';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.namesc is 'Simplified Chinese Area Name';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.nametc is 'Traditional Chinese Area Name';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.nameen is 'English Area Name';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.isvalid is 'Valid Flag:1=Valid,0=Invalid';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.createdat is 'Record Create Time';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.lastupdateat is 'Last Update Time';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.code is 'Area Code';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.dtmf is 'Corresponding IVR Key';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.sort is 'Area Sort Value Under IVR Key';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.createdby is 'Creator User ID';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.updatedby is 'Last Update User ID';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.ods_load_time is 'Ods Load Timestamp';
comment on column coss_ods.ods_pems_cus_t_dic_concerndistric_df.ods_update_time is 'Ods Update Timestamp';
select sql
sql
select 
    id, -- Concern Area Primary Key ID
    namesc, -- Simplified Chinese Area Name
    nametc, -- Traditional Chinese Area Name
    nameen, -- English Area Name
    isvalid, -- Valid Flag:1=Valid,0=Invalid
    createdat, -- Record Create Time
    lastupdateat, -- Last Update Time
    code, -- Area Code
    dtmf, -- Corresponding IVR Key
    sort, -- Area Sort Value Under IVR Key
    createdby, -- Creator User ID
    updatedby, -- Last Update User ID
    current_timestamp as ods_load_time, -- Ods Load Timestamp
    current_timestamp as ods_update_time -- Ods Update Timestamp
from pems.t_dic_concerndistric


update sql
sql
-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Concern Area Dictionary Full Load & Upsert
-- Create         By: data_dev
-- Create       Date: 2026-07-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_pems_cus_t_dic_concerndistric_stg_df
-- Target Table:  coss_ods.ods_pems_cus_t_dic_concerndistric_df
-- ****************************************************************************************
insert into coss_ods.ods_pems_cus_t_dic_concerndistric_df
select
    id, -- Concern Area Primary Key ID
    namesc, -- Simplified Chinese Area Name
    nametc, -- Traditional Chinese Area Name
    nameen, -- English Area Name
    isvalid, -- Valid Flag:1=Valid,0=Invalid
    createdat, -- Record Create Time
    lastupdateat, -- Last Update Time
    code, -- Area Code
    dtmf, -- Corresponding IVR Key
    sort, -- Area Sort Value Under IVR Key
    createdby, -- Creator User ID
    updatedby, -- Last Update User ID
    current_timestamp as ods_load_time, -- Ods Load Timestamp
    current_timestamp as ods_update_time -- Ods Update Timestamp
from coss_ods.ods_pems_cus_t_dic_concerndistric_stg_df
on duplicate key update
    namesc = values(namesc),
    nametc = values(nametc),
    nameen = values(nameen),
    isvalid = values(isvalid),
    createdat = values(createdat),
    lastupdateat = values(lastupdateat),
    code = values(code),
    dtmf = values(dtmf),
    sort = values(sort),
    createdby = values(createdby),
    updatedby = values(updatedby),
    ods_update_time = values(ods_update_time);
```



# ods_pems_cus_t_annon_watersupplyinfo_di



```sql
ods_pems_cus_t_annon_watersupplyinfo_di
create table
sql
drop table if exists coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di;
create table if not exists coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di(
    id int8,
    recid int8,
    logid int8,
    watersupplytype int4,
    watersupplyaddressen varchar(1000),
    watersupplyaddresssc varchar(1000),
    watersupplyaddresstc varchar(1000),
    watersupplytime timestamp,
    opentime timestamp,
    endtime timestamp,
    quality int4,
    watersupplyremark varchar(4000),
    createdat timestamp,
    createdby int4,
    location varchar(100),
    leavingtime timestamp,
    vechiclenumber varchar(100),
    drivername varchar(50),
    driverphone varchar(50),
    workman1 varchar(50),
    workman2 varchar(50),
    workmanphone1 varchar(50),
    workmanphone2 varchar(50),
    locationx varchar(100),
    locationy varchar(100),
    isvalid int4,
    lastupdateat timestamp,
    updatedby int4,
    ods_load_time timestamp(6) default current_timestamp,
    ods_update_time timestamp(6) default current_timestamp,
    primary key (id)
)
with (
    orientation = row,
    compression = no
);
comment on table coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di is 'PEMS System Temporary Water Supply Information Table';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.id is 'Primary Key ID';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.recid is 'Announcement ID';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.logid is 'Announcement Record ID';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.watersupplytype is 'Temporary Water Supply Type';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.watersupplyaddressen is 'Temporary Water Supply Address (English)';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.watersupplyaddresssc is 'Temporary Water Supply Address (Simplified Chinese)';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.watersupplyaddresstc is 'Temporary Water Supply Address (Traditional Chinese)';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.watersupplytime is 'Temporary Water Supply Apply Time';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.opentime is 'Open Time';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.endtime is 'End Time';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.quality is 'Quantity';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.watersupplyremark is 'Remark';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.createdat is 'Record Create Time';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.createdby is 'Creator User ID';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.location is 'Coordinate';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.leavingtime is 'Departure Time';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.vechiclenumber is 'Vehicle License Plate Number';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.drivername is 'Driver Name';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.driverphone is 'Driver Contact Phone';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.workman1 is 'Staff 1';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.workman2 is 'Staff 2';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.workmanphone1 is 'Staff 1 Contact Phone';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.workmanphone2 is 'Staff 2 Contact Phone';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.locationx is 'X Coordinate';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.locationy is 'Y Coordinate';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.isvalid is 'Valid Flag:0=Invalid,1=Valid';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.lastupdateat is 'Last Update Time';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.updatedby is 'Last Update User ID';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.ods_load_time is 'Ods Load Timestamp';
comment on column coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di.ods_update_time is 'Ods Update Timestamp';

select sql
sql
select 
    id, -- Primary Key ID
    recid, -- Announcement ID
    logid, -- Announcement Record ID
    watersupplytype, -- Temporary Water Supply Type
    watersupplyaddressen, -- Temporary Water Supply Address (English)
    watersupplyaddresssc, -- Temporary Water Supply Address (Simplified Chinese)
    watersupplyaddresstc, -- Temporary Water Supply Address (Traditional Chinese)
    watersupplytime, -- Temporary Water Supply Apply Time
    opentime, -- Open Time
    endtime, -- End Time
    quality, -- Quantity
    watersupplyremark, -- Remark
    createdat, -- Record Create Time
    createdby, -- Creator User ID
    location, -- Coordinate
    leavingtime, -- Departure Time
    vechiclenumber, -- Vehicle License Plate Number
    drivername, -- Driver Name
    driverphone, -- Driver Contact Phone
    workman1, -- Staff 1
    workman2, -- Staff 2
    workmanphone1, -- Staff 1 Contact Phone
    workmanphone2, -- Staff 2 Contact Phone
    locationx, -- X Coordinate
    locationy, -- Y Coordinate
    isvalid, -- Valid Flag:0=Invalid,1=Valid
    lastupdateat, -- Last Update Time
    updatedby, -- Last Update User ID
    current_timestamp as ods_load_time, -- Ods Load Timestamp
    current_timestamp as ods_update_time -- Ods Update Timestamp
from pems.t_annon_watersupplyinfo
where
    lastupdateat >= '${lastupdateat}'
    or createdat >= '${createdat}'

update sql
sql
-- ****************************************************************************************
-- Subject     Areas: Customer Service
-- Function Describe: Temporary Water Supply Info Full Load & Upsert
-- Create         By: data_dev
-- Create       Date: 2026-07-17
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_pems_cus_t_annon_watersupplyinfo_stg_di
-- Target Table:  coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di
-- ****************************************************************************************
insert into coss_ods.ods_pems_cus_t_annon_watersupplyinfo_di
select
    id, -- Primary Key ID
    recid, -- Announcement ID
    logid, -- Announcement Record ID
    watersupplytype, -- Temporary Water Supply Type
    watersupplyaddressen, -- Temporary Water Supply Address (English)
    watersupplyaddresssc, -- Temporary Water Supply Address (Simplified Chinese)
    watersupplyaddresstc, -- Temporary Water Supply Address (Traditional Chinese)
    watersupplytime, -- Temporary Water Supply Apply Time
    opentime, -- Open Time
    endtime, -- End Time
    quality, -- Quantity
    watersupplyremark, -- Remark
    createdat, -- Record Create Time
    createdby, -- Creator User ID
    location, -- Coordinate
    leavingtime, -- Departure Time
    vechiclenumber, -- Vehicle License Plate Number
    drivername, -- Driver Name
    driverphone, -- Driver Contact Phone
    workman1, -- Staff 1
    workman2, -- Staff 2
    workmanphone1, -- Staff 1 Contact Phone
    workmanphone2, -- Staff 2 Contact Phone
    locationx, -- X Coordinate
    locationy, -- Y Coordinate
    isvalid, -- Valid Flag:0=Invalid,1=Valid
    lastupdateat, -- Last Update Time
    updatedby, -- Last Update User ID
    current_timestamp as ods_load_time, -- Ods Load Timestamp
    current_timestamp as ods_update_time -- Ods Update Timestamp
from coss_ods.ods_pems_cus_t_annon_watersupplyinfo_stg_di
on duplicate key update
    recid = values(recid),
    logid = values(logid),
    watersupplytype = values(watersupplytype),
    watersupplyaddressen = values(watersupplyaddressen),
    watersupplyaddresssc = values(watersupplyaddresssc),
    watersupplyaddresstc = values(watersupplyaddresstc),
    watersupplytime = values(watersupplytime),
    opentime = values(opentime),
    endtime = values(endtime),
    quality = values(quality),
    watersupplyremark = values(watersupplyremark),
    createdat = values(createdat),
    createdby = values(createdby),
    location = values(location),
    leavingtime = values(leavingtime),
    vechiclenumber = values(vechiclenumber),
    drivername = values(drivername),
    driverphone = values(driverphone),
    workman1 = values(workman1),
    workman2 = values(workman2),
    workmanphone1 = values(workmanphone1),
    workmanphone2 = values(workmanphone2),
    locationx = values(locationx),
    locationy = values(locationy),
    isvalid = values(isvalid),
    lastupdateat = values(lastupdateat),
    updatedby = values(updatedby),
    ods_update_time = values(ods_update_time);

```



# 

```
-- coss_ods.ods_pems_cus_t_order_workorder_stg_mini definition

-- Drop table

-- DROP TABLE coss_ods.ods_pems_cus_t_order_workorder_stg_mini;

CREATE TABLE coss_ods.ods_pems_cus_t_order_workorder_stg_mini (
	ordernum varchar(30) NOT NULL, -- Work Order Id
	msgid int8 NULL, -- Message Id
	agentgroupid int8 NULL, -- Agent Group Id
	cusid varchar(50) NULL, -- Customer Id (Linked To Customer Table)
	channeltype int4 NULL, -- Channel Type
	busicenter varchar(50) NULL, -- Business Center (Department)
	classify1 int8 NULL, -- Work Order Category 1
	classify2 int8 NULL, -- Work Order Category 2
	subarea int8 NULL, -- Region - Branch
	"system" int8 NULL, -- Dispatch System
	classify3 int8 NULL, -- Work Order Category 3
	classify4 int8 NULL, -- Work Order Category 4
	realclassify1 int8 NULL, -- Actual Work Order Category 3
	realclassify2 int8 NULL, -- Actual Work Order Category 4
	bigregion varchar(30) NULL, -- Administrative Region
	subregion int8 NULL, -- Region & Branch – Sub-Region
	dayshift int4 NULL, -- Day Shift Team
	dutyshift int4 NULL, -- On-Duty Team
	urgency int4 NULL, -- Urgency Level
	isclosed int4 NULL, -- 1=Closed, 2=Dispatched
	state int4 NULL, -- External Status
	orderstate int4 NULL, -- Work Order Status: 1=Pending, 2=In Progress, 3=Completed
	isdelay int4 NULL, -- Is Overdue: 1=Yes
	delayday int4 NULL, -- Overdue Days
	iscomplant int4 NULL, -- Is Complaint Ticket: 1=Yes, 2=Tree-Related, 0=No
	isreply int4 NULL, -- Reply Required: 1=Yes
	replychannel varchar(20) NULL, -- Reply Channel
	casesource int8 NULL, -- Case Source
	transferivr int4 NULL, -- Transferred To Ivr
	chargeback int4 NULL, -- Returned Order
	ivrlanguage int4 NULL, -- Ivr Language Selection
	district1 varchar(30) NULL, -- Primary Concern Area
	district2 varchar(30) NULL, -- Secondary Concern Area
	isrepeatedcomplaint int4 NULL, -- Repeat Complaint Flag
	subcomplaint int4 NULL, -- Sub-Complaint Flag
	receivedepartment int8 NULL, -- Acceptance Department
	receiver int8 NULL, -- Handler / Assignee
	printedflag int4 NULL, -- Printed Flag
	isregionorder int4 NULL, -- Region-Based Ticket Creation: 1=Cs, 2=Hw
	outstandingdays int4 NULL, -- Pending Days As Of Current Date
	finalreplydays int4 NULL, -- Required Final Response Days
	completedbyregion varchar(5) NULL, -- Case Completed By Regional Team
	pledgeachieved varchar(5) NULL, -- Service Commitment Met Flag
	actualreplytime timestamp NULL, -- Actual Response Time
	repairdays int4 NULL, -- Allowed Maintenance Days
	grantedhowlong int4 NULL, -- Eot Extension Days (If Granted)
	notificationdays int4 NULL, -- Notification Period (Days) Specified In Fj
	totalprocessingdays int4 NULL, -- Total Handling Days
	referinwsd int4 NULL, -- Internal Transfer Flag: 1=Yes
	isdelete bpchar(1) NULL, -- Deletable Flag: 1=Yes, 0=No
	basecallpid int8 NULL, -- Basecallpid
	complantlastupdator int8 NULL, -- Last Complaint Ticket Modifier
	complantlastupdatetime timestamp NULL, -- Last Complaint Ticket Modification Time
	isdone int4 NULL, -- Flag: 1=Processed In Abpms System
	createdby int8 NULL, -- Created By
	createdat timestamp NULL, -- Data Warehouse Load Time
	lastupdatedby int8 NULL, -- Last Updated By
	lastupdateat timestamp NULL, -- Last Update Time
	ods_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Ods Table Load Timestamp
	ods_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Ods Table Update Timestamp
	CONSTRAINT ods_pems_cus_t_order_workorder_stg_mini_pkey PRIMARY KEY (ordernum) INCLUDE (tableoid)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=USTORE,
	segment=off
);
COMMENT ON TABLE coss_ods.ods_pems_cus_t_order_workorder_stg_mini IS 'PEMS System Work Order Main Table';

-- Column comments

COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.ordernum IS 'Work Order Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.msgid IS 'Message Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.agentgroupid IS 'Agent Group Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.cusid IS 'Customer Id (Linked To Customer Table)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.channeltype IS 'Channel Type';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.busicenter IS 'Business Center (Department)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.classify1 IS 'Work Order Category 1';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.classify2 IS 'Work Order Category 2';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.subarea IS 'Region - Branch';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini."system" IS 'Dispatch System';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.classify3 IS 'Work Order Category 3';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.classify4 IS 'Work Order Category 4';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.realclassify1 IS 'Actual Work Order Category 3';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.realclassify2 IS 'Actual Work Order Category 4';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.bigregion IS 'Administrative Region';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.subregion IS 'Region & Branch – Sub-Region';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.dayshift IS 'Day Shift Team';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.dutyshift IS 'On-Duty Team';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.urgency IS 'Urgency Level';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.isclosed IS '1=Closed, 2=Dispatched';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.state IS 'External Status';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.orderstate IS 'Work Order Status: 1=Pending, 2=In Progress, 3=Completed';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.isdelay IS 'Is Overdue: 1=Yes';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.delayday IS 'Overdue Days';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.iscomplant IS 'Is Complaint Ticket: 1=Yes, 2=Tree-Related, 0=No';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.isreply IS 'Reply Required: 1=Yes';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.replychannel IS 'Reply Channel';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.casesource IS 'Case Source';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.transferivr IS 'Transferred To Ivr';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.chargeback IS 'Returned Order';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.ivrlanguage IS 'Ivr Language Selection';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.district1 IS 'Primary Concern Area';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.district2 IS 'Secondary Concern Area';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.isrepeatedcomplaint IS 'Repeat Complaint Flag';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.subcomplaint IS 'Sub-Complaint Flag';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.receivedepartment IS 'Acceptance Department';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.receiver IS 'Handler / Assignee';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.printedflag IS 'Printed Flag';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.isregionorder IS 'Region-Based Ticket Creation: 1=Cs, 2=Hw';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.outstandingdays IS 'Pending Days As Of Current Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.finalreplydays IS 'Required Final Response Days';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.completedbyregion IS 'Case Completed By Regional Team';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.pledgeachieved IS 'Service Commitment Met Flag';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.actualreplytime IS 'Actual Response Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.repairdays IS 'Allowed Maintenance Days';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.grantedhowlong IS 'Eot Extension Days (If Granted)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.notificationdays IS 'Notification Period (Days) Specified In Fj';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.totalprocessingdays IS 'Total Handling Days';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.referinwsd IS 'Internal Transfer Flag: 1=Yes';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.isdelete IS 'Deletable Flag: 1=Yes, 0=No';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.basecallpid IS 'Basecallpid';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.complantlastupdator IS 'Last Complaint Ticket Modifier';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.complantlastupdatetime IS 'Last Complaint Ticket Modification Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.isdone IS 'Flag: 1=Processed In Abpms System';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.createdby IS 'Created By';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.createdat IS 'Data Warehouse Load Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.lastupdatedby IS 'Last Updated By';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.lastupdateat IS 'Last Update Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.ods_load_time IS 'Ods Table Load Timestamp';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_stg_mini.ods_update_time IS 'Ods Table Update Timestamp';

-- Permissions

ALTER TABLE coss_ods.ods_pems_cus_t_order_workorder_stg_mini OWNER TO coss;
GRANT ALL ON TABLE coss_ods.ods_pems_cus_t_order_workorder_stg_mini TO coss;




-- coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini definition

-- Drop table

-- DROP TABLE coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini;

CREATE TABLE coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini (
	ordernum varchar(30) NOT NULL, -- Work Order Id
	accountid varchar(20) NULL, -- Account Number
	customerid varchar(20) NULL, -- Customer Id
	meterno varchar(50) NULL, -- Water Meter Number
	consumptionpointid varchar(20) NULL, -- Water Meter Id
	telno varchar(50) NULL, -- Registration No.
	faxno varchar(50) NULL, -- Fax Number
	contactno varchar(50) NULL, -- Contact / Landline Phone
	address varchar(500) NULL, -- Address
	servicecontent varchar(4000) NULL, -- Service Content
	compliantmemo varchar(2000) NULL, -- Complaint Description
	wsdcreateat timestamp(0) NULL, -- Wsd Complaint Receipt Time
	completedate date NULL, -- Completion Deadline Date
	casenumber varchar(50) NULL, -- 1823 Case Reference No.
	street varchar(200) NULL, -- Street
	estate varchar(200) NULL, -- Estate / Village
	term varchar(100) NULL, -- Phase
	village varchar(200) NULL, -- Village
	buildingno varchar(100) NULL, -- Building Number
	buildingname varchar(200) NULL, -- Building Name
	floor varchar(200) NULL, -- Floor
	company varchar(200) NULL, -- Flat / Unit
	relateorder varchar(500) NULL, -- Linked Work Order Id
	thirdid varchar(50) NULL, -- 3Rd Party Work Order Id
	responsedate date NULL, -- Response Deadline Date
	complainttype varchar(50) NULL, -- Complainant Type
	initialcomplaintdate timestamp(0) NULL, -- Complaint Lodged Time
	regionreceivingdate timestamp(0) NULL, -- Regional Office Receipt Time
	finishtime timestamp NULL, -- Work Order Completion Time
	actiontaken varchar(1000) NULL, -- Action Taken
	nature varchar(35) NULL, -- Case Type
	responsibleofficer varchar(35) NULL, -- Case Handler
	interimreplydate date NULL, -- Interim Response Date
	finalreplydate date NULL, -- Substantive Response Date
	casereferredothers varchar(35) NULL, -- Case Referred To Other Staff (E.g. Jo/Distribution Team)
	actionsreplycontent varchar(1000) NULL, -- Follow-Up Actions After Response
	repairtype varchar(50) NULL, -- Repair Notice Type Issued
	repairdate date NULL, -- Repair Notice Issue Date
	repairexpirydate date NULL, -- Repair Validity Period
	firstrepairreinspectiondate date NULL, -- 1St Repair Notice Re-Inspection Date
	referringcasedate date NULL, -- Time Sent To Regional Office
	issuingdate date NULL, -- Fj Issue Date
	expirydate date NULL, -- Fj Expiry Date (Validity)
	firstreinspectiondate date NULL, -- 1St Fj Re-Inspection Date
	methodcompletion varchar(100) NULL, -- Works Completion Method
	responsibleai varchar(35) NULL, -- Responsible Ai Agent
	responsiblecsi varchar(35) NULL, -- Responsible Csi Officer
	supplytype varchar(50) NULL, -- Water Supply Type
	slopefeature varchar(35) NULL, -- Slope
	glano varchar(35) NULL, -- [Null]
	groupval varchar(35) NULL, -- [Null]
	complaintlodged varchar(255) NULL, -- Complaint Short Code
	email varchar(50) NULL, -- Email Address
	acknowledgementdate timestamp(0) NULL, -- Acknowledgement Time
	regiondistrict varchar(50) NULL, -- District
	venue varchar(50) NULL, -- Premises
	waterqualitycode varchar(50) NULL, -- Water Quality Dictionary Code
	waterqualitycodecategory bpchar(1) NULL, -- System Subcategory: Independent(I)/Multiple(M) For Other Water Quality, Fresh Water Turbidity & Odour Complaints (Flushing Water)
	interimreplytargetdate date NULL, -- Interim Reply Date
	buildingcsuid varchar(19) NULL, -- Lot & Utility Reference No.
	locationx varchar(6) NULL, -- X Coordinate
	locationy varchar(6) NULL, -- Y Coordinate
	intervenescase bpchar(1) NULL, -- Ombudsman Intervention Flag (Y/N)
	docindexdesc text NULL, -- Related Document Reference Index
	processingdesc text NULL, -- Case Handling Status
	appointmentremovaldate date NULL, -- Meter Removal Date (Dd/Mm/Yyyy)
	appointmentremovalapm varchar(2) NULL, -- Meter Removal Session (Am/Pm Only)
	appointmentwitnessdate date NULL, -- Site Test Witness Date (Dd/Mm/Yyyy)
	appointmentwitnesstime varchar(12) NULL, -- Site Test Witness Time Slot (Hh:mm-Hh:mm)
	sourcetype bpchar(10) NULL, -- Ticket Creation Source Channel (Page)
	remarks varchar(2000) NULL, -- Remark
	createdby int4 NULL, -- Created By
	createdat timestamp NULL, -- Data Warehouse Load Time
	lastupdatedby int8 NULL, -- Last Updated By
	lastupdateat timestamp NULL, -- Last Update Time
	ccid varchar(15) NULL, -- Cc Id
	ods_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Ods Table Load Timestamp
	ods_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Ods Table Update Timestamp
	CONSTRAINT ods_pems_cus_t_order_workorder_entity_stg_mini_pkey PRIMARY KEY (ordernum) INCLUDE (tableoid)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=USTORE,
	segment=off
);
COMMENT ON TABLE coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini IS 'PEMS System   Work Order Entity Detail Table';

-- Column comments

COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.ordernum IS 'Work Order Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.accountid IS 'Account Number';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.customerid IS 'Customer Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.meterno IS 'Water Meter Number';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.consumptionpointid IS 'Water Meter Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.telno IS 'Registration No.';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.faxno IS 'Fax Number';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.contactno IS 'Contact / Landline Phone';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.address IS 'Address';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.servicecontent IS 'Service Content';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.compliantmemo IS 'Complaint Description';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.wsdcreateat IS 'Wsd Complaint Receipt Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.completedate IS 'Completion Deadline Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.casenumber IS '1823 Case Reference No.';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.street IS 'Street';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.estate IS 'Estate / Village';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.term IS 'Phase';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.village IS 'Village';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.buildingno IS 'Building Number';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.buildingname IS 'Building Name';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.floor IS 'Floor';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.company IS 'Flat / Unit';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.relateorder IS 'Linked Work Order Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.thirdid IS '3Rd Party Work Order Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.responsedate IS 'Response Deadline Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.complainttype IS 'Complainant Type';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.initialcomplaintdate IS 'Complaint Lodged Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.regionreceivingdate IS 'Regional Office Receipt Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.finishtime IS 'Work Order Completion Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.actiontaken IS 'Action Taken';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.nature IS 'Case Type';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.responsibleofficer IS 'Case Handler';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.interimreplydate IS 'Interim Response Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.finalreplydate IS 'Substantive Response Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.casereferredothers IS 'Case Referred To Other Staff (E.g. Jo/Distribution Team)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.actionsreplycontent IS 'Follow-Up Actions After Response';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.repairtype IS 'Repair Notice Type Issued';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.repairdate IS 'Repair Notice Issue Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.repairexpirydate IS 'Repair Validity Period';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.firstrepairreinspectiondate IS '1St Repair Notice Re-Inspection Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.referringcasedate IS 'Time Sent To Regional Office';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.issuingdate IS 'Fj Issue Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.expirydate IS 'Fj Expiry Date (Validity)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.firstreinspectiondate IS '1St Fj Re-Inspection Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.methodcompletion IS 'Works Completion Method';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.responsibleai IS 'Responsible Ai Agent';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.responsiblecsi IS 'Responsible Csi Officer';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.supplytype IS 'Water Supply Type';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.slopefeature IS 'Slope';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.glano IS '[Null]';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.groupval IS '[Null]';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.complaintlodged IS 'Complaint Short Code';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.email IS 'Email Address';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.acknowledgementdate IS 'Acknowledgement Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.regiondistrict IS 'District';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.venue IS 'Premises';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.waterqualitycode IS 'Water Quality Dictionary Code';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.waterqualitycodecategory IS 'System Subcategory: Independent(I)/Multiple(M) For Other Water Quality, Fresh Water Turbidity & Odour Complaints (Flushing Water)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.interimreplytargetdate IS 'Interim Reply Date';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.buildingcsuid IS 'Lot & Utility Reference No.';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.locationx IS 'X Coordinate';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.locationy IS 'Y Coordinate';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.intervenescase IS 'Ombudsman Intervention Flag (Y/N)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.docindexdesc IS 'Related Document Reference Index';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.processingdesc IS 'Case Handling Status';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.appointmentremovaldate IS 'Meter Removal Date (Dd/Mm/Yyyy)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.appointmentremovalapm IS 'Meter Removal Session (Am/Pm Only)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.appointmentwitnessdate IS 'Site Test Witness Date (Dd/Mm/Yyyy)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.appointmentwitnesstime IS 'Site Test Witness Time Slot (Hh:mm-Hh:mm)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.sourcetype IS 'Ticket Creation Source Channel (Page)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.remarks IS 'Remark';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.createdby IS 'Created By';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.createdat IS 'Data Warehouse Load Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.lastupdatedby IS 'Last Updated By';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.lastupdateat IS 'Last Update Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.ccid IS 'Cc Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.ods_load_time IS 'Ods Table Load Timestamp';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini.ods_update_time IS 'Ods Table Update Timestamp';

-- Permissions

ALTER TABLE coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini OWNER TO coss;
GRANT ALL ON TABLE coss_ods.ods_pems_cus_t_order_workorder_entity_stg_mini TO coss;
```





```sql
DROP TABLE coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di;

CREATE TABLE coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di (
	recid int8 NOT NULL, -- Announcement ID
	actionregion int4 NULL, -- Action Region
	subactionregion int4 NULL, -- Sub Action Region
	actiongroup varchar(50) NULL, -- Action Group
	"type" int4 NULL, -- Water Supply Type
	"level" int4 NULL, -- Water Cut Off Level
	cutofftime timestamp NULL, -- Water Cut Off Time
	noticetime timestamp NULL, -- Notice Publish Time
	prerecoverytime timestamp NULL, -- Expected Recovery Time
	actualrecoverytime timestamp NULL, -- Actual Recovery Time
	linkperson1sc varchar(100) NULL, -- Contact Person 1(Simplified Chinese)
	linkphone1 varchar(20) NULL, -- Contact Phone 1
	linkperson2sc varchar(100) NULL, -- Contact Person 2(Simplified Chinese)
	linkphone2 varchar(20) NULL, -- Contact Phone 2
	buildlocation varchar(100) NULL, -- Construction Location
	locationcoord varchar(100) NULL, -- Location Coordinate
	state varchar(5) NULL, -- Status
	cutoffcase int4 NULL, -- Water Cut Off Reason Code
	cutoffcaseen varchar(100) NULL, -- Water Cut Off Reason English
	cutoffcasesc varchar(100) NULL, -- Water Cut Off Reason Simplified Chinese
	pushoff varchar(100) NULL, -- Publish Target Channel
	noticecontentsc varchar(1000) NULL, -- Notice Content Simplified Chinese
	noticecontenttc varchar(1000) NULL, -- Notice Content Traditional Chinese
	noticecontenten varchar(1000) NULL, -- Notice Content English
	remarkforinside varchar(1000) NULL, -- Internal Remark
	remarkforoutsidesc varchar(1000) NULL, -- External Remark Simplified Chinese
	affectedaddresssc varchar(1000) NULL, -- Affected Address Simplified Chinese
	affectedaddresstc varchar(1000) NULL, -- Affected Address Traditional Chinese
	affectedaddressen varchar(1000) NULL, -- Affected Address English
	createdby int4 NULL, -- Creator User ID
	createdat timestamp NULL, -- Record Create Time
	updatedby int4 NULL, -- Modifier User ID
	lastupdateat timestamp NULL, -- Last Update Time
	watsunid int8 NULL, -- WATSUN Query ID
	title int4 NULL, -- Title Code
	forml int4 NULL, -- Water Cut Off Notice Sent Flag
	linkperson2tc varchar(100) NULL, -- Contact Person 2 Traditional Chinese
	linkperson2en varchar(100) NULL, -- Contact Person 2 English
	relateorder varchar(50) NULL, -- Related Work Order No
	filesc varchar(255) NULL, -- Attachment File Simplified Chinese
	filetc varchar(255) NULL, -- Attachment File Traditional Chinese
	fileen varchar(255) NULL, -- Attachment File English
	locationx varchar(100) NULL, -- Coordinate X
	locationy varchar(100) NULL, -- Coordinate Y
	remarkforoutsidetc varchar(1000) NULL, -- External Remark Traditional Chinese
	remarkforoutsideen varchar(1000) NULL, -- External Remark English
	createname varchar(50) NULL, -- Creator Name
	updatename varchar(50) NULL, -- Modifier Name
	createposttitle varchar(50) NULL, -- Create Post Title
	updateposttitle varchar(50) NULL, -- Update Post Title
	linkperson1tc varchar(100) NULL, -- Contact Person 1 Traditional Chinese
	linkperson1en varchar(100) NULL, -- Contact Person 1 English
	prerecoverytimeend timestamp NULL, -- Expected Recovery End Time
	ods_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Ods Table Load Timestamp
	ods_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Ods Table Update Timestamp
	CONSTRAINT ods_pems_cus_t_annon_watercutoffnotice_di_pkey PRIMARY KEY (recid)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=USTORE,
	segment=off
);
COMMENT ON TABLE coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di IS 'PEMS System Water Cut Off Announcement Table';

-- Column comments

COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.recid IS 'Announcement ID';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.actionregion IS 'Action Region';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.subactionregion IS 'Sub Action Region';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.actiongroup IS 'Action Group';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di."type" IS 'Water Supply Type';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di."level" IS 'Water Cut Off Level';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.cutofftime IS 'Water Cut Off Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.noticetime IS 'Notice Publish Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.prerecoverytime IS 'Expected Recovery Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.actualrecoverytime IS 'Actual Recovery Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.linkperson1sc IS 'Contact Person 1(Simplified Chinese)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.linkphone1 IS 'Contact Phone 1';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.linkperson2sc IS 'Contact Person 2(Simplified Chinese)';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.linkphone2 IS 'Contact Phone 2';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.buildlocation IS 'Construction Location';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.locationcoord IS 'Location Coordinate';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.state IS 'Status';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.cutoffcase IS 'Water Cut Off Reason Code';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.cutoffcaseen IS 'Water Cut Off Reason English';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.cutoffcasesc IS 'Water Cut Off Reason Simplified Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.pushoff IS 'Publish Target Channel';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.noticecontentsc IS 'Notice Content Simplified Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.noticecontenttc IS 'Notice Content Traditional Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.noticecontenten IS 'Notice Content English';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.remarkforinside IS 'Internal Remark';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.remarkforoutsidesc IS 'External Remark Simplified Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.affectedaddresssc IS 'Affected Address Simplified Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.affectedaddresstc IS 'Affected Address Traditional Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.affectedaddressen IS 'Affected Address English';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.createdby IS 'Creator User ID';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.createdat IS 'Record Create Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.updatedby IS 'Modifier User ID';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.lastupdateat IS 'Last Update Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.watsunid IS 'WATSUN Query ID';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.title IS 'Title Code';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.forml IS 'Water Cut Off Notice Sent Flag';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.linkperson2tc IS 'Contact Person 2 Traditional Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.linkperson2en IS 'Contact Person 2 English';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.relateorder IS 'Related Work Order No';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.filesc IS 'Attachment File Simplified Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.filetc IS 'Attachment File Traditional Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.fileen IS 'Attachment File English';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.locationx IS 'Coordinate X';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.locationy IS 'Coordinate Y';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.remarkforoutsidetc IS 'External Remark Traditional Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.remarkforoutsideen IS 'External Remark English';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.createname IS 'Creator Name';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.updatename IS 'Modifier Name';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.createposttitle IS 'Create Post Title';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.updateposttitle IS 'Update Post Title';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.linkperson1tc IS 'Contact Person 1 Traditional Chinese';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.linkperson1en IS 'Contact Person 1 English';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.prerecoverytimeend IS 'Expected Recovery End Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.ods_load_time IS 'Ods Table Load Timestamp';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_annon_watercutoffnotice_di.ods_update_time IS 'Ods Table Update Timestamp';


```





```
-- coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year definition

-- Drop table

-- DROP TABLE coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year;

CREATE TABLE coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year (
	id int8 NOT NULL, -- Auto-Increment Id
	agentid int4 NOT NULL, -- Agent Id
	workno varchar(255) NOT NULL, -- Employee ID
	consn int8 NULL, -- Connection SN
	callsn int8 NULL, -- Call SN
	accessmediatype varchar(255) NULL, -- Access Media Type
	status int4 NULL, -- Agent Current Status
	statusname varchar(255) NOT NULL, -- Agent Status Name
	begintime timestamp NOT NULL, -- Status Start Time
	endtime timestamp NULL, -- End Time
	statetime int4 NOT NULL, -- State Time
	operatetype int4 NULL, -- Operation Type Id
	operatename varchar(255) NOT NULL, -- Operation Type Name
	operateworkno varchar(255) NULL, -- Operator Employee ID
	operatefailcause int4 NULL, -- Operation Failure Reason
	logoutreasoncode varchar(255) NULL, -- Exit Reason
	auxcode int4 NULL, -- Code Under Aux Status
	vdnname varchar(50) NULL, -- Vdn Name
	vdnid int4 NULL, -- Vdn Id
	agentname varchar(100) NULL, -- Agent Name
	logintime timestamp NULL, -- Login Time
	logintimelen int4 NULL, -- Login Time Len
	agroutelogpid int8 NULL, -- Agroute Log Pid
	basecallpid int8 NULL, -- Basecall Pid
	parentcallpid int8 NULL, -- Parentcall Pid
	ods_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Ods Load Time
	ods_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Ods Update Time
	CONSTRAINT ods_pems_cus_t_icip_ag_state_trk_record_di_year_pkey PRIMARY KEY (id, agentid, workno, statusname, begintime, statetime, operatename)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
);
COMMENT ON TABLE coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year IS 'Agent State Track Record Annual Table';

-- Column comments

COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.id IS 'Auto-Increment Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.agentid IS 'Agent Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.workno IS 'Employee ID';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.consn IS 'Connection SN';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.callsn IS 'Call SN';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.accessmediatype IS 'Access Media Type';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.status IS 'Agent Current Status';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.statusname IS 'Agent Status Name';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.begintime IS 'Status Start Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.endtime IS 'End Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.statetime IS 'State Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.operatetype IS 'Operation Type Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.operatename IS 'Operation Type Name';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.operateworkno IS 'Operator Employee ID';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.operatefailcause IS 'Operation Failure Reason';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.logoutreasoncode IS 'Exit Reason';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.auxcode IS 'Code Under Aux Status';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.vdnname IS 'Vdn Name';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.vdnid IS 'Vdn Id';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.agentname IS 'Agent Name';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.logintime IS 'Login Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.logintimelen IS 'Login Time Len';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.agroutelogpid IS 'Agroute Log Pid';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.basecallpid IS 'Basecall Pid';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.parentcallpid IS 'Parentcall Pid';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.ods_load_time IS 'Ods Load Time';
COMMENT ON COLUMN coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year.ods_update_time IS 'Ods Update Time';

-- Permissions

ALTER TABLE coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year OWNER TO coss;
GRANT ALL ON TABLE coss_ods.ods_pems_cus_t_icip_ag_state_trk_record_di_year TO coss;
```



# 需要添加ods_pems_cus_t_dic_district_df