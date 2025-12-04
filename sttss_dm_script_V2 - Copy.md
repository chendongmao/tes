# 1.RWS

## 1.coss_dm.dm_rws_daily_rw_yield_di

### create table 

```sql
;drop table if exists coss_dm.dm_rws_daily_rw_yield_di
;create table if not exists coss_dm.dm_rws_daily_rw_yield_di(
statistical_day               decimal(20,0)
,island_change_storage         decimal(20,5)
,mainland_change_storage       decimal(20,5)
,total_change_storage          decimal(20,5)
,island_current_storage        decimal(20,5)
,island_design_storage         decimal(20,5)
,mainland_current_storage      decimal(20,5)
,mainland_design_storage       decimal(20,5)
,total_current_storage         decimal(20,5)
,total_design_storage          decimal(20,5)
,island_yield                  decimal(20,5)
,mainland_yield                decimal(20,5)
,total_local_yield             decimal(20,5)
,dj_yield                      decimal(20,5)
,total_yield                   decimal(20,5)
,dm_update_time  timestamp(6)       default current_timestamp
,dm_load_time    timestamp(6)       default current_timestamp
,primary key(statistical_day)
)

;comment on table coss_dm.dm_rws_daily_rw_yield_di is 'daily raw yield'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.statistical_day          is 'statistical day'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.island_change_storage    is 'island change storage'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.mainland_change_storage  is 'mainland change storage'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.total_change_storage     is 'total change storage'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.island_current_storage   is 'island current storage'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.island_design_storage    is 'island design storage'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.mainland_current_storage is 'mainland current storage'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.mainland_design_storage  is 'mainland design storage'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.total_current_storage    is 'total current storage'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.total_design_storage     is 'total design storage'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.island_yield             is 'island yield'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.mainland_yield           is 'mainland yield'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.total_local_yield        is 'total local yield'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.dj_yield                 is 'dj yield'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.total_yield              is 'total yield'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.dm_update_time            is 'dm update time'
;comment on column coss_dm.dm_rws_daily_rw_yield_di.dm_load_time              is 'dm load time'
```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Raw  Water Supply
-- function describe: Raw  Water Supply Yield
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dwd_rws_gd_agr_supply_di_year
-- coss_dwd.dwd_rws_channel_flow_detail_di_year
-- coss_dws.dws_rws_rw_supply_detail_di_year
-- coss_dim.dim_ass_channels_df
-- coss_dim.dim_ass_rw_src_df
-- target table
-- coss_dm.dm_rws_daily_rw_yield_di
-- ****************************************************************************************
-- get raw water output impounding reservoir
drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_01;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_01 as 
select
dt
,t1.src_id as ig_id
,if(sum(if(left(t1.src_id, 2) = 'IG' and t.qty_del >= 0 , t.qty_del ,0)) <0, 0, sum(if(left(t1.src_id, 2) = 'IG' and t.qty_del >= 0  , t.qty_del ,0))) as to_wtc
from 
(select 
dt,
option_no,
ch_id,
qty_del
from coss_dwd.dwd_rws_channel_flow_detail_di_year ) t
inner join  coss_dim.dim_ass_channels_df t1 on t.option_no = t1.option_no and t.ch_id =t1.ch_id 
where left(t1.src_id, 2) = 'IG' 
-- and t.rec_dt >= ${}
group by
dt
,ig_id ;


-- get raw water to impounding reservoir
drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_02;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_02 as 
select 
	dt
	,t1.dest_id as ig_id
	,if(sum(if(left(t1.dest_id, 2) = 'IG' 
	and t.qty_del >= 0 , t.qty_del ,0))<0,0, sum(if(left(t1.dest_id, 2) = 'IG' 
	and t.qty_del >= 0 , t.qty_del ,0))) as from_wtc
from 
(select 
qty_del,
option_no,
ch_id,
dt
from coss_dwd.dwd_rws_channel_flow_detail_di_year ) t
inner join  coss_dim.dim_ass_channels_df t1 on t.option_no = t1.option_no and t.ch_id =t1.ch_id 
where left(t1.dest_id, 2) = 'IG'
-- and t.rec_dt >= ${}
group by
dt
,ig_id;



-- get raw water present storage and capacity 
drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_03;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_03 as 
select 
rw_id
,dt
,rw_name
,rw_cname
,present_storage
,capacity
from 
(select 
rw_id
,dt
,rw_name
,rw_cname
,present_storage
,capacity
from coss_dws.dws_rws_rw_supply_detail_di_year) t 
where left(rw_id, 2) = 'IG'
-- and rec_dt >=${}
;

-- get raw water present storage and capacity 
drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_04;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_04 as 
select 
rw_id
,dt
,rw_name
,rw_cname
,present_storage
,capacity
from 
(select 
rw_id
,dt
,rw_name
,rw_cname
,present_storage
,capacity
from coss_dws.dws_rws_rw_supply_detail_di_year ) t 
where left(rw_id, 2) = 'IG'
-- and t.rec_dt >= ${}
;

drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_05;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_05 as 
select 
ig_id
,dt
,rw_name
,rw_cname
,to_wtc
,ifnull(from_wtc,0) as from_wtc
,delivery
from 
(
select 
t.dt
,t.ig_id
,t.to_wtc
,t1.from_wtc
,t.to_wtc - ifnull(t1.from_wtc, 0) as delivery
from 
coss_tmp.dm_rws_daily_rw_yield_di_01 t
left join coss_tmp.dm_rws_daily_rw_yield_di_02 t1 on t.dt = t1.dt and t.ig_id = t1.ig_id
) t 
left join coss_dim.dim_ass_rw_src_df t1 on t.ig_id = t1.rw_id
;

drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_06;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_06 as 
select 
t.rw_id as ig_id
,t.dt
,t.rw_name
,t.rw_cname
,t.present_storage
,t.capacity
,(t1.present_storage - t.present_storage) change_storage
from coss_tmp.dm_rws_daily_rw_yield_di_03 t 
left join coss_tmp.dm_rws_daily_rw_yield_di_04 t1 on t.dt = to_char(to_date(t1.dt,'yyyymmdd') + integer '-1','yyyymmdd')
and t.rw_id = t1.rw_id
;

drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_07;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_07 as 
--ir supply
select 
t.ig_id rw_id
,t.dt
,t.delivery + t1.change_storage as yield
,t1.present_storage  current_storage
,t1.capacity         design_storage
,t1.change_storage   change_storage
from 
coss_tmp.dm_rws_daily_rw_yield_di_05 t
left join 
coss_tmp.dm_rws_daily_rw_yield_di_06 t1 on t.ig_id = t1.ig_id and t.dt = t1.dt
-- river supply
union all
select 
t.src_id rw_id
,t.dt
,qty_del yield
,0  current_storage
,0  design_storage
,0  change_storage
from 
(select 
option_no,
ch_id,
qty_del,
src_id,
dt
from coss_dwd.dwd_rws_channel_flow_detail_di_year where src_id = 'RW00000003'
-- where rec_dt >= ${}
) t
left join coss_dim.dim_ass_channels_df t1 on t.option_no = t1.option_no and t.ch_id = t1.ch_id 

--DJ supply
union all 
select 
rw_id
,cast(to_char(rec_dt,'yyyymmdd') as int) dt
,(agr_vol - dis_vol) as yield
,0  current_storage
,0  design_storage
,0  change_storage
from coss_dwd.dwd_rws_gd_agr_supply_di_year
-- where rec_dt >= ${}
;

drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_08;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_08 as 
select 
t.rw_id 
,dt 
,yield
,change_storage
,current_storage
,design_storage
,region_ind 
from 
(select * from coss_tmp.dm_rws_daily_rw_yield_di_07 ) t
left join coss_dim.dim_ass_rw_src_df t1 on t.rw_id = t1.rw_id 
where 
t1.rw_id != 'RW00000001'
;

drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_09;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_09 as 
select 
t.rw_id 
,dt 
,yield
,region_ind 
,change_storage
,current_storage
,design_storage
from 
(select 
rw_id 
,dt 
,yield
,change_storage
,current_storage
,design_storage
from coss_tmp.dm_rws_daily_rw_yield_di_07) t
left join coss_dim.dim_ass_rw_src_df t1 on t.rw_id = t1.rw_id 
where 
t1.rw_id = 'RW00000001'
;

drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_10;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_10 as 
select
dt
,sum(yield)          as yield
,sum(change_storage) as change_storage
,sum(current_storage) as current_storage
,sum(design_storage)  as design_storage
from coss_tmp.dm_rws_daily_rw_yield_di_08 t
where t.region_ind = 'I'
group by 
dt
;

drop table if exists coss_tmp.dm_rws_daily_rw_yield_di_11;
create table if not exists coss_tmp.dm_rws_daily_rw_yield_di_11 as 
select
dt
,sum(yield) as yield
,sum(change_storage) as change_storage
,sum(current_storage) as current_storage
,sum(design_storage)  as design_storage
from coss_tmp.dm_rws_daily_rw_yield_di_08 t
where t.region_ind = 'M'
group by 
dt
;

insert into coss_dm.dm_rws_daily_rw_yield_di 
select
  t.dt                                          as statistical_day
  ,if(t.current_storage=0 or t.current_storage is null,0, (t.change_storage/t.current_storage)*100) as island_change_storage
  ,if(t1.current_storage=0 or t1.current_storage is null,0, (t1.change_storage/t1.current_storage)*100) as mainland_change_storage
  ,if((t.current_storage+t1.current_storage) = 0 or (t.current_storage+t1.current_storage) is null,0,
(t.change_storage+t1.change_storage)/(t.current_storage+t1.current_storage)*100) as total_change_storage
  ,(t.current_storage)/1000                      as island_current_storage      -- convert ML to mcm
  ,(t.design_storage)/1000                       as island_design_storage       -- convert ML to mcm
  ,(t1.current_storage)/1000                     as mainland_current_storage    -- convert ML to mcm
  ,(t1.design_storage)/1000                      as mainland_design_storage     -- convert ML to mcm
  ,(t.current_storage + t1.current_storage)/1000 as total_current_storage       -- convert ML to mcm
  ,(t.design_storage + t1.design_storage)/1000   as total_design_storage        -- convert ML to mcm
  ,(t.yield)/1000                                as island_yield                -- convert ML to mcm
  ,(t1.yield)/1000                               as mainland_yield              -- convert ML to mcm
  ,(t.yield + t1.yield)/1000                     as total_local_yield           -- convert ML to mcm
  ,(t2.yield)/1000                               as dj_yield                    -- convert ML to mcm
  ,(t.yield + t1.yield + t2.yield)/1000          as total_yield                 -- convert ML to mcm
  ,current_timestamp dm_update_time
  ,current_timestamp dm_load_time
from 
coss_tmp.dm_rws_daily_rw_yield_di_10 t
left join 
coss_tmp.dm_rws_daily_rw_yield_di_11 t1 on t.dt = t1.dt
left join coss_tmp.dm_rws_daily_rw_yield_di_09 t2 on t1.dt = t2.dt   
on duplicate key update
    island_change_storage = values(island_change_storage),
    mainland_change_storage = values(mainland_change_storage),
    total_change_storage = values(total_change_storage),
    island_current_storage = values(island_current_storage),
    island_design_storage = values(island_design_storage),
    mainland_current_storage = values(mainland_current_storage),
    mainland_design_storage = values(mainland_design_storage),
    total_current_storage = values(total_current_storage),
    total_design_storage = values(total_design_storage),
    island_yield = values(island_yield),
    mainland_yield = values(mainland_yield),
    total_local_yield = values(total_local_yield),
    dj_yield = values(dj_yield),
    total_yield = values(total_yield),
    dm_update_time = values(dm_update_time)  
;
delete coss_dm.dm_rws_daily_rw_yield_di where statistical_day >= (select max(statistical_day)-100 statistical_day from coss_dm.dm_rws_daily_rw_yield_di )
```



## 2.coss_dm.dm_rws_monthly_rw_yield_di

### create table

```sql
drop TABLE if exists coss_dm.dm_rws_monthly_rw_yield_di; 
CREATE TABLE if not exists coss_dm.dm_rws_monthly_rw_yield_di (
	statistical_month numeric(20) NULL,
	island_yield numeric(20, 5) NULL,
	mainland_yield numeric(20, 5) NULL,
	total_local_yield numeric(20, 5) NULL,
	dj_yield numeric(20, 5) NULL,
	total_yield numeric(20, 5) NULL,
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time
	primary key(statistical_month)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
);
;comment on table coss_dm.dm_rws_monthly_rw_yield_di is 'raw water yield'
;comment on column coss_dm.dm_rws_monthly_rw_yield_di.statistical_month    is 'statistical month'
;comment on column coss_dm.dm_rws_monthly_rw_yield_di.island_yield         is 'island yield'
;comment on column coss_dm.dm_rws_monthly_rw_yield_di.mainland_yield       is 'mainland yield'
;comment on column coss_dm.dm_rws_monthly_rw_yield_di.total_local_yield    is 'total local yield'
;comment on column coss_dm.dm_rws_monthly_rw_yield_di.dj_yield             is 'dj yield'
;comment on column coss_dm.dm_rws_monthly_rw_yield_di.total_yield          is 'total yield'
;comment on column coss_dm.dm_rws_monthly_rw_yield_di.dm_update_time       is 'Data Update Time'
;comment on column coss_dm.dm_rws_monthly_rw_yield_di.dm_load_time         is 'Data Loading Time'
```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Raw Water Supply
-- function describe: Raw Water Monthly Yield
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dm.dm_rws_daily_rw_yield_di
-- target table
-- coss_dm.dm_rws_monthly_rw_yield_di
-- ****************************************************************************************
;insert into coss_dm.dm_rws_monthly_rw_yield_di
select
  round(statistical_day/100) as statistical_month
  ,sum(island_yield)          as island_yield                  
  ,sum(mainland_yield)        as mainland_yield                
  ,sum(total_local_yield)     as total_local_yield       
  ,sum(dj_yield)              as dj_yield                
  ,sum(total_yield)           as total_yield
  ,current_timestamp dm_update_time
  ,current_timestamp dm_load_time
from coss_dm.dm_rws_daily_rw_yield_di
where island_yield          is not null
and mainland_yield       is not null
and total_local_yield    is not null
and dj_yield             is not null
and total_yield          is not null
-- and statistical_day >=${}
group by
statistical_month
on duplicate key update
    island_yield = values(island_yield),
    mainland_yield = values(mainland_yield),
    total_local_yield = values(total_local_yield),
    dj_yield = values(dj_yield),
    total_yield = values(total_yield),
    dm_update_time = values(dm_update_time)
```

## 3.coss_dm.dm_rws_annual_rw_yield_di

### create table

```sql
DROP TABLE coss_dm.dm_rws_annual_rw_yield_di;

CREATE TABLE coss_dm.dm_rws_annual_rw_yield_di (
	statistical_year numeric(20) NULL,
	island_yield numeric(20, 5) NULL,
	mainland_yield numeric(20, 5) NULL,
	total_local_yield numeric(20, 5) NULL,
	dj_yield numeric(20, 5) NULL,
	total_yield numeric(20, 5) NULL,
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time
	primary key(statistical_year)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
);
;comment on table coss_dm.dm_rws_annual_rw_yield_di is 'annual raw water yield'
;comment on column coss_dm.dm_rws_annual_rw_yield_di.statistical_year   is 'statistical year'
;comment on column coss_dm.dm_rws_annual_rw_yield_di.island_yield       is 'island yield'
;comment on column coss_dm.dm_rws_annual_rw_yield_di.mainland_yield     is 'mainland yield'
;comment on column coss_dm.dm_rws_annual_rw_yield_di.total_local_yield  is 'total local yield'
;comment on column coss_dm.dm_rws_annual_rw_yield_di.dj_yield           is 'dj yield'
;comment on column coss_dm.dm_rws_annual_rw_yield_di.total_yield        is 'total yield'
;comment on column coss_dm.dm_rws_annual_rw_yield_di.dm_update_time     is 'update time'
;comment on column coss_dm.dm_rws_annual_rw_yield_di.dm_load_time       is 'load time'

```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Raw Water Supply
-- function describe: Raw Water Annual Yield
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dm.dm_rws_daily_rw_yield_di
-- target table
-- coss_dm.dm_rws_annual_rw_yield_di
-- ****************************************************************************************
;insert into coss_dm.dm_rws_annual_rw_yield_di
select
  round(statistical_day/10000) as statistical_year
  ,sum(island_yield)            as island_yield
  ,sum(mainland_yield)          as mainland_yield
  ,sum(total_local_yield)       as total_local_yield
  ,sum(dj_yield)                as dj_yield
  ,sum(total_yield)             as total_yield
  ,current_timestamp dm_update_time
  ,current_timestamp dm_load_time
from coss_dm.dm_rws_daily_rw_yield_di
where island_yield       is not null
and mainland_yield     is not null
and total_local_yield  is not null
and dj_yield           is not null
and total_yield   is not null
-- and statistical_day >= ${}
group by
statistical_year
on duplicate key update
    island_yield = values(island_yield),
    mainland_yield = values(mainland_yield),
    total_local_yield = values(total_local_yield),
    dj_yield = values(dj_yield),
    total_yield = values(total_yield),
    dm_update_time = values(dm_update_time)
```

## 4.coss_dm.dm_rws_daily_ir_storage_yield_di

### create table 

```sql
DROP TABLE if exists coss_dm.dm_rws_daily_ir_storage_yield_di;

CREATE TABLE if not exists coss_dm.dm_rws_daily_ir_storage_yield_di (
	rw_id varchar(50) NULL,
	rw_name varchar(50) NULL,
	rw_cname varchar(50) NULL,
	rpt_label varchar(50) NULL,
	region_code varchar(50) NULL,
	region_name varchar(100) NULL,
	region_cname varchar(200) NULL,
	region_ind varchar(50) NULL,
	ig_ind varchar(50) NULL,
	yield numeric(20, 5) NULL,
	current_storage numeric(20, 5) NULL,
	design_storage numeric(20, 5) NULL,
	change_storage numeric(20, 5) NULL,
	dt numeric(10) NULL,
    dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time
	PRIMARY KEY (rw_id,dt)
)
WITH (
	orientation=row,
	compression=no,
	storage_type=ustore,
	segment=off
);
;comment on table coss_dm.dm_rws_daily_ir_storage_yield_di is 'daily impounding reservoir storage and yield'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.rw_id              is 'raw water id'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.rw_name            is 'raw water name'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.rw_cname           is 'raw water tc name'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.rpt_label          is 'report label'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.region_code        is 'region code'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.region_name        is 'region name'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.region_cname       is 'region cname'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.region_ind         is 'region ind'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.ig_ind             is 'impounding reservoir group index'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.yield              is 'yield'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.current_storage    is 'current storage'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.design_storage     is 'design storage'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.change_storage     is 'change storage'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.dt                 is 'date'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.dm_update_time     is 'update time'
;comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.dm_load_time       is 'load time'
```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Raw Water Supply
-- function describe: Raw Water Impounding Reservoir Yield
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dwd_rws_channel_flow_detail_di_year
-- coss_dws.dws_rws_rw_supply_detail_di_year
-- coss_dim.dim_ass_channels_df
-- coss_dim.dim_ass_rw_src_df
-- target table
-- coss_dm.dm_rws_daily_ir_storage_yield_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_rws_daily_ir_storage_yield_di_01;
create table if not exists coss_tmp.dm_rws_daily_ir_storage_yield_di_01 as 
-- delivery volume
select
dt
,t1.src_id as ig_id
,if(sum(if(left(t1.src_id, 2) = 'IG' and t.qty_del >= 0 , t.qty_del ,0)) <0, 0, sum(if(left(t1.src_id, 2) = 'IG' and t.qty_del >= 0  , t.qty_del ,0))) as to_wtc
from 
(
select 
option_no,
ch_id,
qty_del,
dt,
rec_dt
 from coss_dwd.dwd_rws_channel_flow_detail_di_year
-- where rec_dt>= ${}
) t
inner join  coss_dim.dim_ass_channels_df t1 on t.option_no = t1.option_no and t.ch_id =t1.ch_id 
where left(t1.src_id, 2) = 'IG' 
group by
dt
,ig_id
;   


drop table if exists coss_tmp.dm_rws_daily_ir_storage_yield_di_02;
create table if not exists coss_tmp.dm_rws_daily_ir_storage_yield_di_02 as 
select 
dt
,t1.dest_id as ig_id
,if(sum(if(left(t1.dest_id, 2) = 'IG' and t.qty_del >= 0 , t.qty_del ,0))<0,0, sum(if(left(t1.dest_id, 2) = 'IG' and t.qty_del >= 0 , t.qty_del ,0))) as from_wtc
from 
(select 
option_no,
ch_id,
qty_del,
dt,
rec_dt
from coss_dwd.dwd_rws_channel_flow_detail_di_year 
-- where rec_dt>= ${}
) t
inner join  coss_dim.dim_ass_channels_df t1 on t.option_no = t1.option_no and t.ch_id =t1.ch_id 
where left(t1.dest_id, 2) = 'IG'
group by
dt
,ig_id ;


drop table if exists coss_tmp.dm_rws_daily_ir_storage_yield_di_03;
create table if not exists coss_tmp.dm_rws_daily_ir_storage_yield_di_03 as 
select 
	rw_id
	,dt
	,rw_name
	,rw_cname
	,present_storage
	,capacity
from coss_dws.dws_rws_rw_supply_detail_di_year
where left(rw_id, 2) = 'IG'
-- and rec_dt>= ${}
;

drop table if exists coss_tmp.dm_rws_daily_ir_storage_yield_di_04;
create table if not exists coss_tmp.dm_rws_daily_ir_storage_yield_di_04 as 
select 
rw_id
,dt
,rw_name
,rw_cname
,present_storage
,capacity
from coss_dws.dws_rws_rw_supply_detail_di_year 
where left(rw_id, 2) = 'IG'
-- and rec_dt>= ${}
;

drop table if exists coss_tmp.dm_rws_daily_ir_storage_yield_di_05;
create table if not exists coss_tmp.dm_rws_daily_ir_storage_yield_di_05 as 
select 
ig_id
,dt
,rw_name
,rw_cname
,to_wtc
,from_wtc
,delivery
from 
(select 
t.dt
,t.ig_id
,t.to_wtc
,t1.from_wtc
,t.to_wtc - ifnull(t1.from_wtc, 0) as delivery
from 
coss_tmp.dm_rws_daily_ir_storage_yield_di_01 t
left join coss_tmp.dm_rws_daily_ir_storage_yield_di_02 t1 on t.dt = t1.dt and t.ig_id = t1.ig_id) t 
left join coss_dim.dim_ass_rw_src_df t1 on t.ig_id = t1.rw_id 
;


drop table if exists coss_tmp.dm_rws_daily_ir_storage_yield_di_06;
create table if not exists coss_tmp.dm_rws_daily_ir_storage_yield_di_06 as 
select 
t.rw_id as ig_id
,t.dt
,t.rw_name
,t.rw_cname
,t.present_storage
,t.capacity
,(t1.present_storage - t.present_storage) change_storage
from coss_tmp.dm_rws_daily_ir_storage_yield_di_03 t 
left join coss_tmp.dm_rws_daily_ir_storage_yield_di_04 t1 on t.dt = to_char(to_date(t1.dt,'yyyymmdd') + integer '-1','yyyymmdd')
and t.rw_id = t1.rw_id
;

insert into coss_dm.dm_rws_daily_ir_storage_yield_di
--ir supply
select
t.ig_id rw_id
,t2.rw_name
,t2.rw_cname
,t2.rpt_label
,t2.region_code
,t2.region_name
,t2.region_cname
,t2.region_ind
,t2.ig_ind
,t.delivery + t1.change_storage as yield
,t1.present_storage  current_storage
,t1.capacity         design_storage
,t1.change_storage   change_storage
,t.dt
,current_timestamp dm_update_time
,current_timestamp dm_load_time
from
 coss_tmp.dm_rws_daily_ir_storage_yield_di_05 t
left join
 coss_tmp.dm_rws_daily_ir_storage_yield_di_06 t1 on t.ig_id = t1.ig_id and t.dt = t1.dt
left join coss_dim.dim_ass_rw_src_df t2 on t.ig_id = t2.rw_id
where t1.present_storage != 0
on duplicate key update
  rw_name = values(rw_name),
  rw_cname = values(rw_cname),
  rpt_label = values(rpt_label),
  region_code = values(region_code),
  region_name = values(region_name),
  region_cname = values(region_cname),
  region_ind = values(region_ind),
  ig_ind = values(ig_ind),
  yield = values(yield),
  current_storage = values(current_storage),
  design_storage = values(design_storage),
  change_storage = values(change_storage),
  dm_update_time = values(dm_update_time)
  
  
  
```

## 5.coss_dm.dm_rws_daily_ir_level_storage_di

### create table

```sql
;drop table if exists coss_dm.dm_rws_daily_ir_level_storage_di
;create table if not exists coss_dm.dm_rws_daily_ir_level_storage_di(
ir_id             varchar(50)
,i_code           varchar(50)
,ir_rpt_label     varchar(100)
,ir_name          varchar(100)
,ir_cname         varchar(100)
,region_code      varchar(100)
,region_name      varchar(100)
,region_cname     varchar(100)
,region_ind       varchar(50)
,level_type       varchar(50)
,level_unit       varchar(50)
,dead_storage     decimal(20,5)
,twl              decimal(20,5)
,capacity         decimal(20,5)
,min_storage      decimal(20,5)
,limit_m          decimal(20,5)
,wl_mpd           decimal(20,5)
,storage          decimal(20,5)
,avg_7_mpd        decimal(20,5)
,avg_7_storage    decimal(20,5)
,avg_28_mpd       decimal(20,5)
,avg_28_storage   decimal(20,5)
,rec_dt           timestamp(6)
,dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp() -- Data Update Time
,dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp() -- Data Loading Time
,primary key(ir_id, rec_dt)
)
;comment on table coss_dm.dm_rws_daily_ir_level_storage_di is 'impounding reservoir level and storage'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.ir_id               is 'impounding reservoir id'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.i_code              is 'installation code'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.ir_rpt_label        is 'impounding reservoir report label'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.ir_name             is 'impounding reservoir name'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.ir_cname            is 'impounding reservoir cname'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.region_code         is 'region code'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.region_name         is 'region name'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.region_cname        is 'region cname'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.region_ind          is 'region ind'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.level_type          is 'level type'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.level_unit          is 'level unit'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.dead_storage        is 'dead storage'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.twl                 is 'twl'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.capacity            is 'capacity'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.min_storage         is 'min storage'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.limit_m             is 'limit m'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.wl_mpd              is 'wl mpd'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.storage             is 'storage'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.avg_7_mpd           is 'avg 7 mpd'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.avg_7_storage       is 'avg 7 storage'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.avg_28_mpd          is 'avg 28 mpd'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.avg_28_storage      is 'avg 28 storage'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.rec_dt              is 're dt'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.dm_update_time      is 'dm update time'
;comment on column coss_dm.dm_rws_daily_ir_level_storage_di.dm_load_time        is 'dm load time'
```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Raw Water Supply
-- function describe: Raw Water Impounding Reservoir Level And Storage
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dws.dws_rws_ir_storage_detail_di_year
-- coss_dim.dim_ass_ir_df
-- target table
-- coss_dm.dm_rws_daily_ir_level_storage_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_rws_daily_ir_level_storage_di_01;
create table if not exists coss_tmp.dm_rws_daily_ir_level_storage_di_01 as
select
ir_id
,rec_dt
,wl_mpd
,present_storage
,sum(wl_mpd) over(
  partition by ir_id
  order by rec_dt desc
  rows between current row and 6 following )/7 as avg_7_mpd
,sum(present_storage) over(
  partition by ir_id
  order by rec_dt desc
  rows between current row and 6 following )/7 as avg_7_storage

  ,sum(wl_mpd) over(
  partition by ir_id
  order by rec_dt desc
  rows between current row and 27 following )/28 as avg_28_mpd
,sum(present_storage) over(
  partition by ir_id
  order by rec_dt desc
  rows between current row and 27 following )/28 as avg_28_storage
from coss_dws.dws_rws_ir_storage_detail_di_year
where wl_mpd is not null
and present_storage is not null
-- and rec_dt >= ${}
order by rec_dt
;

drop table if exists coss_tmp.dm_rws_daily_ir_level_storage_di_02;
create table if not exists coss_tmp.dm_rws_daily_ir_level_storage_di_02 as
select
  t.ig_id           as ig_id            -- Impounding Reservoir Group ID with format IGNNNNNNNN
  ,t.ig_name        as ig_name          -- Name of Impounding Reservoir Group
  ,t.ig_cname       as ig_cname         -- Chinese Name of Impounding Reservoir Group
  ,t.region_code         as region_code      -- Region
  ,t.region_name        as region_name      -- Description of Region
  ,t.region_cname       as region_cname     -- Chinese Description of Region
  ,t.region_ind      as region_ind       -- Possible Values: {"I" - HK Island, "M" - Mainland}
  ,t.ir_id           as ir_id            -- Impounding Reservoir ID with format IRNNNNNNNN
  ,t.i_code          as i_code           -- Installation Code of Impounding Reservoir
  ,t.ir_rpt_label          as ir_rpt_label     -- Labels used in reports
  ,t.ir_name         as ir_name          -- Impounding reservoir name
  ,t.ir_cname        as ir_cname         -- Impounding Reservoir Chinese Name
  ,t.level_type      as level_type       -- Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}
  ,t.level_unit      as level_unit       -- Possible Values:{"F" - Feet / Inch, "M" - Meter}
  ,t.dead_storage    as dead_storage     -- Dead Storage of an Impounding Reservoir.  Unit is in mcm
  ,t.twl             as twl              -- TWL
  ,t.capacity        as capacity         -- Capacity of IR.  Unit is in mcm
  ,t.min_storage     as min_storage      -- Allowable Minimum Storage.  Unit is in mcm
  ,t.limit_m         as limit_m          -- Preset Limit for Water Level.  Unit is in m
  ,current_timestamp    as dw_etl_time      -- Data Warehouse ETL Time
from coss_dim.dim_ass_ir_df t
;

insert into coss_dm.dm_rws_daily_ir_level_storage_di
select
  t1.ir_id
  ,t1.i_code
  ,t1.ir_rpt_label
  ,t1.ir_name
  ,t1.ir_cname
  ,t1.region_code
  ,t1.region_name
  ,t1.region_cname
  ,t1.region_ind
  ,t1.level_type
  ,t1.level_unit
  ,t1.dead_storage
  ,t1.twl
  ,t1.capacity
  ,t1.min_storage
  ,t1.limit_m
  ,t.wl_mpd
  ,t.present_storage/t1.capacity*100  as storage
  ,t.avg_7_mpd
  ,t.avg_7_storage/t1.capacity*100 as avg_7_storage
  ,t.avg_28_mpd
  ,t.avg_28_storage/t1.capacity*100 as avg_28_storage
  ,t.rec_dt
  ,current_timestamp dm_load_time
  ,current_timestamp dm_update_time
from coss_tmp.dm_rws_daily_ir_level_storage_di_01 t
  left join coss_tmp.dm_rws_daily_ir_level_storage_di_02 t1 on t.ir_id = t1.ir_id
on duplicate key update 
    i_code = values(i_code),
    ir_rpt_label = values(ir_rpt_label),
    ir_name = values(ir_name),
    ir_cname = values(ir_cname),
    region_code = values(region_code),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    level_type = values(level_type),
    level_unit = values(level_unit),
    dead_storage = values(dead_storage),
    twl = values(twl),
    capacity = values(capacity),
    min_storage = values(min_storage),
    limit_m = values(limit_m),
    wl_mpd = values(wl_mpd),
    storage = values(storage),
    avg_7_mpd = values(avg_7_mpd),
    avg_7_storage = values(avg_7_storage),
    avg_28_mpd = values(avg_28_mpd),
    avg_28_storage = values(avg_28_storage),
    dm_update_time = values(dm_update_time)
```

## 6.coss_dm.dm_rws_region_day_kpi_dip 

### create table

```sql
;drop table if exists coss_dm.dm_rws_region_day_kpi_dip
;CREATE TABLE if not exists coss_dm.dm_rws_region_day_kpi_dip (
	id varchar(42) NULL,
	region varchar(200) NULL,
	item_code varchar(200) NULL,
	item_name varchar(300) NULL,
	item_value numeric(20, 5) NULL,
	"unit" varchar(50) NULL,
	etl_time timestamp(6) NULL,
	dt numeric(10) NULL,
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time	
	primary key(region, item_code, dt)
)
WITH (
	orientation=row,
	compression=no
);
comment on table coss_dm.dm_rws_region_day_kpi_dip is 'Raw water supply daily kpi';
comment on column coss_dm.dm_rws_region_day_kpi_dip.id is 'id';
comment on column coss_dm.dm_rws_region_day_kpi_dip.region is 'region';
comment on column coss_dm.dm_rws_region_day_kpi_dip.item_code is 'item code';
comment on column coss_dm.dm_rws_region_day_kpi_dip.item_name is 'item name';
comment on column coss_dm.dm_rws_region_day_kpi_dip.item_value is 'item value';
comment on column coss_dm.dm_rws_region_day_kpi_dip.unit is 'unit';
comment on column coss_dm.dm_rws_region_day_kpi_dip.etl_time is 'etl time';
comment on column coss_dm.dm_rws_region_day_kpi_dip.dt is 'statistical day';
comment on column coss_dm.dm_rws_region_day_kpi_dip.dm_update_time is 'update time';
comment on column coss_dm.dm_rws_region_day_kpi_dip.dm_load_time  is 'load time';
```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Raw Water Supply
-- function describe: Raw Water Daily KPI
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dws.dws_rws_rw_supply_detail_di_year
-- target table
-- coss_dm.dm_rws_region_day_kpi_dip
-- ****************************************************************************************

 -- precomputation Metrics of propose and actual supply
 drop table if exists coss_tmp.dm_rws_region_day_kpi_dip_01;
 create table if not exists coss_tmp.dm_rws_region_day_kpi_dip_01 as
 select
  region_code region
  ,sum(p_qty) p_qty
  ,sum(qty_del) qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where dt >= ${dt1}
group by
  region_code
  ,dt
 ;
 
 drop table if exists coss_tmp.dm_rws_region_day_kpi_dip_02;
 create table if not exists coss_tmp.dm_rws_region_day_kpi_dip_02 as
 select
  'HKSAR'           region
  ,sum(p_qty)  p_qty
  ,sum(qty_del) qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where dt >= ${dt1}
group by
  region_code
  ,dt
  ;

 drop table if exists coss_tmp.dm_rws_region_day_kpi_dip_03;
 create table if not exists coss_tmp.dm_rws_region_day_kpi_dip_03 as
select
  region_code region
  ,dt
  ,sum(p_qty)/count(1) p_qty
  ,sum(qty_del)/count(1) qty_del
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where dt >= ${dt1}
group by
  region_code
  ,dt
  ;


drop table if exists coss_tmp.dm_rws_region_day_kpi_dip_04;
create table if not exists coss_tmp.dm_rws_region_day_kpi_dip_04 as
select
  'HKSAR'           as region
  ,dt               as dt
  ,sum(p_qty)       as p_qty
  ,sum(qty_del)     as qty_del
from coss_dws.dws_rws_rw_supply_detail_di_year 
-- where dt >= ${dt1}
group by
  region_code
  ,dt
  ;


insert into coss_dm.dm_rws_region_day_kpi_dip
-- HKSAR Raw Water Actual Supply Volume
select
   uuid()                            as id
   ,region                           as region
   ,'bi_p_224'                       as item_code
   ,'Raw Water Actual Supply Volume' as item_name
   ,qty_del                          as item_value
   ,'Ml'                             as unit
   ,localtimestamp                   as etl_time
   ,t.dt                             as dt
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_day_kpi_dip_02 t

union all
-- Region Raw Water Actual Supply Volume
select
   uuid()                            as id
   ,region                           as region
   ,'bi_p_225'                       as item_code
   ,'Raw Water Actual Supply Volume' as item_name
   ,qty_del                          as item_value
   ,'Ml'                             as unit
   ,localtimestamp                   as etl_time
   ,t.dt                             as dt
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_day_kpi_dip_01 t

union all
-- HKSAR Raw Water Propose Supply Volume
select
   uuid()                             as id
   ,region                            as region
   ,'bi_p_226'                        as item_code
   ,'Raw Water Propose Supply Volume' as item_name
   ,p_qty                             as item_value
   ,'Ml'                              as unit
   ,localtimestamp                    as etl_time
   ,t.dt                              as dt
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_day_kpi_dip_02 t

union all
-- Region Raw Water Propose Supply Volume
select
   uuid()                             as id
   ,region                            as region
   ,'bi_p_227'                        as item_code
   ,'Raw Water Propose Supply Volume' as item_name
   ,p_qty                             as item_value
   ,'Ml'                              as unit
   ,localtimestamp                    as etl_time
   ,t.dt                              as dt
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_day_kpi_dip_01 t

union all
-- HKSAR Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water
select
  uuid()                                                                               as id
  ,t.region                                                                            as region
  ,'bi_p_230'                                                                          as item_code
  ,'Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water'                   as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                   as item_value
  ,'%'                                                                                  as unit
  ,localtimestamp                                                                       as etl_time
  ,t.dt                                                                                   as dt
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_day_kpi_dip_04 t
left join coss_tmp.dm_rws_region_day_kpi_dip_04 t1 on t.dt = t1.dt+10000

union all
-- Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water
select
  uuid()                                                                                as id
  ,t.region                                                                             as region
  ,'bi_p_231'                                                                           as item_code
  ,'Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water'                    as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                   as item_value
  ,'%'                                                                                  as unit
  ,localtimestamp                                                                       as etl_time
  ,t.dt                                                                                   as dt
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_day_kpi_dip_03 t
left join coss_tmp.dm_rws_region_day_kpi_dip_03 t1 on t.region = t1.region and t.dt = t1.dt+10000

union all
-- HKSAR Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water
select
  uuid()                                                                                  as id
  ,t.region                                                                               as region
  ,'bi_p_234'                                                                             as item_code
  ,'Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water'                    as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                     as item_value
  ,'%'                                                                                    as unit
  ,localtimestamp                                                                         as etl_time
  ,t.dt                                                                                     as dt
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_day_kpi_dip_04 t
left join coss_tmp.dm_rws_region_day_kpi_dip_04 t1 on t.dt = t1.dt+10000


union all
-- Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water
select
  uuid()                                                                                  as id
  ,t.region                                                                               as region
  ,'bi_p_235'                                                                             as item_code
  ,'Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water '                   as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                     as item_value
  ,'%'                                                                                    as unit
  ,localtimestamp                                                                         as etl_time
  ,t.dt                                                                                     as dt
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_day_kpi_dip_03 t
left join coss_tmp.dm_rws_region_day_kpi_dip_03 t1 on t.region = t1.region and t.dt = t1.dt+10000
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time)
```

## 7.coss_dm.dm_rws_region_month_kpi_dip

### create table

```sql
;drop table if exists coss_dm.dm_rws_region_month_kpi_dip
;create table if not exists coss_dm.dm_rws_region_month_kpi_dip (
	id varchar(42) NULL,
	region varchar(200) NULL,
	item_code varchar(200) NULL,
	item_name varchar(300) NULL,
	item_value numeric(20, 5) NULL,
	"unit" varchar(50) NULL,
	etl_time timestamp(6) NULL,
	mh numeric(10) NULL,
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time
    primary key(region,item_code,mh)
)
WITH (
	orientation=row,
	compression=no
);
comment on table coss_dm.dm_rws_region_month_kpi_dip is 'raw water supply region monthly kpi';
comment on column coss_dm.dm_rws_region_month_kpi_dip.id  is 'id';
comment on column coss_dm.dm_rws_region_month_kpi_dip.region  is 'region';
comment on column coss_dm.dm_rws_region_month_kpi_dip.item_code  is 'item code';
comment on column coss_dm.dm_rws_region_month_kpi_dip.item_name  is 'item name';
comment on column coss_dm.dm_rws_region_month_kpi_dip.item_value  is 'item value';
comment on column coss_dm.dm_rws_region_month_kpi_dip.unit  is 'unit';
comment on column coss_dm.dm_rws_region_month_kpi_dip.etl_time  is 'etl time';
comment on column coss_dm.dm_rws_region_month_kpi_dip.mh  is 'statistical month';
comment on column coss_dm.dm_rws_region_month_kpi_dip.dm_update_time is 'update time';
comment on column coss_dm.dm_rws_region_month_kpi_dip.dm_load_time  is 'load time';
```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Raw Water Supply
-- function describe: Raw Water Daily KPI
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dws.dws_rws_ir_storage_detail_di_year
-- coss_dim.dim_ass_ir_df
-- target table
-- coss_dm.dm_rws_daily_ir_level_storage_di
-- ****************************************************************************************
-- precomputation Metrics of propose and quantity delivery volume
drop table if exists coss_tmp.dm_rws_region_month_kpi_dip_01;
create table if not exists coss_tmp.dm_rws_region_month_kpi_dip_01 as
select
  region_code region
  ,sum(p_qty) p_qty
  ,sum(qty_del) qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where dt >= to_char(date_trunc('month', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
--   and dt <= ${dt1}
group by
  region_code
  ,dt;


drop table if exists coss_tmp.dm_rws_region_month_kpi_dip_02;
create table if not exists coss_tmp.dm_rws_region_month_kpi_dip_02 as
select
  'HKSAR'           region
  ,sum(p_qty)  p_qty
  ,sum(qty_del) qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where dt >= to_char(date_trunc('month', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
--   and dt <= ${dt1}
group by
  region_code
  ,dt
 ;


 drop table if exists coss_tmp.dm_rws_region_month_kpi_dip_03;
create table if not exists coss_tmp.dm_rws_region_month_kpi_dip_03 as

select
  region                  as region
  ,round(dt/100)          as mh
  ,sum(p_qty)/count(1)    as p_qty
  ,sum(qty_del)/ count(1) as qty_del
from
(select
  region_code region
  ,sum(p_qty) p_qty
  ,sum(qty_del) qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where (dt >= to_char(date_trunc('month', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
--   and dt <= ${dt1})
--   or(dt >= to_char(date_trunc('month', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')-10000
--   and dt <= ${dt1}-10000)
group by
  region_code
  ,dt) t
group by
  region
 ,mh;

 drop table if exists coss_tmp.dm_rws_region_month_kpi_dip_04;
create table if not exists coss_tmp.dm_rws_region_month_kpi_dip_04 as
select
  region                  as region
  ,round(dt/100)          as mh
  ,sum(p_qty)/count(1)    as p_qty
  ,sum(qty_del)/ count(1) as qty_del
from
(select
  'HKSAR'           as region
  ,sum(p_qty)       as p_qty
  ,sum(qty_del)     as qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where (dt >= to_char(date_trunc('month', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
--   and dt <= ${dt1})
--   or(dt >= to_char(date_trunc('month', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')-10000
--   and dt <= ${dt1}-10000)
group by
  region_code
  ,dt) t
group by
  region
 ,mh
;

insert into coss_dm.dm_rws_region_month_kpi_dip
-- HKSAR Raw Water Actual Supply Volume
select
   uuid()                            as id
   ,region                           as region
   ,'bi_p_224'                       as item_code
   ,'Raw Water Actual Supply Volume' as item_name
   ,sum(qty_del)/count(*)            as item_value
   ,'Ml'                             as unit
   ,localtimestamp                   as etl_time
   ,round(t.dt/100)                  as mh
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_month_kpi_dip_02 t
group by
  region
  ,mh

union all
-- Region Raw Water Actual Supply Volume
select
   uuid()                            as id
   ,region                           as region
   ,'bi_p_225'                       as item_code
   ,'Raw Water Actual Supply Volume' as item_name
   ,sum(qty_del)/count(*)            as item_value
   ,'Ml'                             as unit
   ,localtimestamp                   as etl_time
   ,round(t.dt/100)                  as mh
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_month_kpi_dip_01 t
group by
  region
  ,mh

union all
-- HKSAR Raw Water Propose Supply Volume
select
   uuid()                             as id
   ,region                            as region
   ,'bi_p_226'                        as item_code
   ,'Raw Water Propose Supply Volume' as item_name
   ,sum(p_qty)/count(*)               as item_value
   ,'Ml'                              as unit
   ,localtimestamp                    as etl_time
   ,round(t.dt/100)                  as mh
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_month_kpi_dip_02 t
group by
  region
  ,mh

union all
-- Region Raw Water Propose Supply Volume
select
   uuid()                             as id
   ,region                            as region
   ,'bi_p_227'                        as item_code
   ,'Raw Water Propose Supply Volume' as item_name
   ,sum(p_qty)/count(*)               as item_value
   ,'Ml'                              as unit
   ,localtimestamp                    as etl_time
   ,round(t.dt/100)                  as mh
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_month_kpi_dip_01 t
group by
  region
  ,mh

union all
-- HKSAR Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water
select
  uuid()                                                                               as id
  ,t.region                                                                            as region
  ,'bi_p_230'                                                                          as item_code
  ,'Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water'                   as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                   as item_value
  ,'%'                                                                                  as unit
  ,localtimestamp                                                                       as etl_time
  ,t.mh                                                                                 as mh
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_month_kpi_dip_04 t
left join coss_tmp.dm_rws_region_month_kpi_dip_04 t1 on t.mh = t1.mh+100

union all
-- Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water
select
  uuid()                                                                                as id
  ,t.region                                                                             as region
  ,'bi_p_231'                                                                           as item_code
  ,'Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water'                    as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                   as item_value
  ,'%'                                                                                  as unit
  ,localtimestamp                                                                       as etl_time
  ,t.mh                                                                                 as mh
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_month_kpi_dip_03 t
left join coss_tmp.dm_rws_region_month_kpi_dip_03 t1 on t.region = t1.region and t.mh = t1.mh+100

union all
-- HKSAR Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water
select
  uuid()                                                                                  as id
  ,t.region                                                                               as region
  ,'bi_p_234'                                                                             as item_code
  ,'Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water'                    as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                     as item_value
  ,'%'                                                                                    as unit
  ,localtimestamp                                                                         as etl_time
  ,t.mh                                                                                   as mh
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_month_kpi_dip_04 t
left join coss_tmp.dm_rws_region_month_kpi_dip_04 t1 on t.mh = t1.mh+100

union all
-- Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water
select
  uuid()                                                                                  as id
  ,t.region                                                                               as region
  ,'bi_p_235'                                                                             as item_code
  ,'Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water '                   as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                     as item_value
  ,'%'                                                                                    as unit
  ,localtimestamp                                                                         as etl_time
  ,t.mh                                                                                   as mh
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_tmp.dm_rws_region_month_kpi_dip_03 t
left join coss_tmp.dm_rws_region_month_kpi_dip_03 t1 on t.region = t1.region and t.mh = t1.mh+100
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time)
```

## 8.coss_dm.dm_rws_region_year_kpi_dip

### create tbale 

```sql
drop table if exists coss_dm.dm_rws_region_year_kpi_dip;

CREATE table if not exists coss_dm.dm_rws_region_year_kpi_dip (
	id varchar(42) NULL,
	region varchar(200) NULL,
	item_code varchar(200) NULL,
	item_name varchar(300) NULL,
	item_value numeric(20, 5) NULL,
	"unit" varchar(50) NULL,
	etl_time timestamp(6) NULL,
	yr numeric(10) null,
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time
	primary key(region, item_code, yr)
)
WITH (
	orientation=row,
	compression=no
);
comment on table coss_dm.dm_rws_region_year_kpi_dip is 'Raw Water annual kpi';
comment on column coss_dm.dm_rws_region_year_kpi_dip.id is 'id';
comment on column coss_dm.dm_rws_region_year_kpi_dip.region is 'region';
comment on column coss_dm.dm_rws_region_year_kpi_dip.item_code is 'item code';
comment on column coss_dm.dm_rws_region_year_kpi_dip.item_name is 'item name';
comment on column coss_dm.dm_rws_region_year_kpi_dip.item_value is 'item value';
comment on column coss_dm.dm_rws_region_year_kpi_dip.unit is 'unit';
comment on column coss_dm.dm_rws_region_year_kpi_dip.etl_time is 'etl time';
comment on column coss_dm.dm_rws_region_year_kpi_dip.yr is 'statistical year';
    comment on column coss_dm.dm_rws_region_year_kpi_dip.dm_update_time is 'update time';
    comment on column coss_dm.dm_rws_region_year_kpi_dip.dm_load_time  is 'load time';
```

### select sql

```sql
-- precomputation Metrics of propose and quantity delivery volume
drop table if exists coss_dm.dm_rws_region_year_kpi_dip_01;
create table coss_dm.dm_rws_region_year_kpi_dip_01 as
select
  region_code region
  ,sum(p_qty) p_qty
  ,sum(qty_del) qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where dt >= to_char(date_trunc('year', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
--  and dt <= ${dt1}
group by
  region_code
  ,dt;

drop table if exists coss_dm.dm_rws_region_year_kpi_dip_02;
create table coss_dm.dm_rws_region_year_kpi_dip_02 as
select
  'HKSAR'           region
  ,sum(p_qty)  p_qty
  ,sum(qty_del) qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where dt >= to_char(date_trunc('year', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
--   and dt <= ${dt1}
group by
  region_code
  ,dt;

drop table if exists coss_dm.dm_rws_region_year_kpi_dip_03;
create table coss_dm.dm_rws_region_year_kpi_dip_03 as
select
  region                  as region
  ,round(dt/10000)          as yr
  ,sum(p_qty)/count(1)    as p_qty
  ,sum(qty_del)/ count(1) as qty_del
from
(select
  region_code region
  ,sum(p_qty) p_qty
  ,sum(qty_del) qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year
-- where (dt >= to_char(date_trunc('year', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
--  and dt <= ${dt1})
--  or(dt >= to_char(date_trunc('year', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')-10000
--  and dt <= ${dt1}-10000)
group by
  region_code
  ,dt) t
group by
  region
 ,yr;


drop table if exists coss_dm.dm_rws_region_year_kpi_dip_04;
create table coss_dm.dm_rws_region_year_kpi_dip_04 as
select
  region                  as region
  ,round(dt/10000)          as yr
  ,sum(p_qty)/count(1)    as p_qty
  ,sum(qty_del)/ count(1) as qty_del
from
(select
  'HKSAR'           as region
  ,sum(p_qty)       as p_qty
  ,sum(qty_del)     as qty_del
  ,dt
from coss_dws.dws_rws_rw_supply_detail_di_year drrsddy 
--where  (dt >= to_char(date_trunc('year', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
--  and dt <= ${dt1})
--  or(dt >= to_char(date_trunc('year', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')-10000
--  and dt <= ${dt1}-10000)
group by
  region_code
  ,dt) t
group by
  region
 ,yr;


insert into coss_dm.dm_rws_region_year_kpi_dip
-- HKSAR Raw Water Actual Supply Volume
select
   uuid()                            as id
   ,region                           as region
   ,'bi_p_224'                       as item_code
   ,'Raw Water Actual Supply Volume' as item_name
   ,sum(qty_del)/count(1)            as item_value
   ,'Ml'                             as unit
   ,localtimestamp                   as etl_time
   ,round(t.dt/10000)                as yr
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_dm.dm_rws_region_year_kpi_dip_02 t
group by
  region
  ,yr

union all
-- Region Raw Water Actual Supply Volume
select
   uuid()                            as id
   ,region                           as region
   ,'bi_p_225'                       as item_code
   ,'Raw Water Actual Supply Volume' as item_name
   ,sum(qty_del)/count(1)            as item_value
   ,'Ml'                             as unit
   ,localtimestamp                   as etl_time
   ,round(t.dt/10000)                as yr
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_dm.dm_rws_region_year_kpi_dip_01 t
group by
  region
  ,yr

union all
-- HKSAR Raw Water Propose Supply Volume
select
   uuid()                             as id
   ,region                            as region
   ,'bi_p_226'                        as item_code
   ,'Raw Water Propose Supply Volume' as item_name
   ,sum(p_qty)/count(1)               as item_value
   ,'Ml'                              as unit
   ,localtimestamp                    as etl_time
   ,round(t.dt/10000)                 as yr
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_dm.dm_rws_region_year_kpi_dip_02 t
group by
  region
  ,yr

union all
-- Region Raw Water Propose Supply Volume
select
   uuid()                             as id
   ,region                            as region
   ,'bi_p_227'                        as item_code
   ,'Raw Water Propose Supply Volume' as item_name
   ,sum(p_qty)/count(1)               as item_value
   ,'Ml'                              as unit
   ,localtimestamp                    as etl_time
   ,round(t.dt/10000)                 as yr
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_dm.dm_rws_region_year_kpi_dip_01 t
group by
  region
  ,yr

union all

-- HKSAR Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water
select
  uuid()                                                                               as id
  ,t.region                                                                            as region
  ,'bi_p_230'                                                                          as item_code
  ,'Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water'                   as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                   as item_value
  ,'%'                                                                                  as unit
  ,localtimestamp                                                                       as etl_time
  ,t.yr                                                                                 as yr
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_dm.dm_rws_region_year_kpi_dip_04 t
left join coss_dm.dm_rws_region_year_kpi_dip_04 t1 on t.yr = t1.yr+1

union all
-- Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water
select
  uuid()                                                                                as id
  ,t.region                                                                             as region
  ,'bi_p_231'                                                                           as item_code
  ,'Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water'                    as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                   as item_value
  ,'%'                                                                                  as unit
  ,localtimestamp                                                                       as etl_time
  ,t.yr                                                                                 as yr
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_dm.dm_rws_region_year_kpi_dip_03 t
left join coss_dm.dm_rws_region_year_kpi_dip_03 t1 on t.region = t1.region and t.yr = t1.yr+1

union all
-- HKSAR Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water
select
  uuid()                                                                                  as id
  ,t.region                                                                               as region
  ,'bi_p_234'                                                                             as item_code
  ,'Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water'                    as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                     as item_value
  ,'%'                                                                                    as unit
  ,localtimestamp                                                                         as etl_time
  ,t.yr                                                                                   as yr
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time  
from coss_dm.dm_rws_region_year_kpi_dip_04 t
left join coss_dm.dm_rws_region_year_kpi_dip_04 t1 on t.yr = t1.yr+1


union all
-- Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water
select
  uuid()                                                                                  as id
  ,t.region                                                                               as region
  ,'bi_p_235'                                                                             as item_code
  ,'Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water '                   as item_name
  ,case
    when t1.qty_del is null or t1.qty_del = 0  then 0.0
    else (t.qty_del - t1.qty_del) / t1.qty_del * 100
  end                                                                                     as item_value
  ,'%'                                                                                    as unit
  ,localtimestamp                                                                         as etl_time
  ,t.yr                                                                                   as yr
   ,current_timestamp dm_update_time
   ,current_timestamp dm_load_time
from coss_dm.dm_rws_region_year_kpi_dip_03 t
left join coss_dm.dm_rws_region_year_kpi_dip_03 t1 on t.region = t1.region and t.yr = t1.yr+1
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time)
```

## 9.coss_dm.dm_srs_daily_sr_wl_qty_item_di

### create table

```sql
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

comment on table coss_dm.dm_srs_daily_sr_wl_qty_item_di is 'Service Reservoir Water Level And Qty_del Detail';

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
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.a_wl            is 'A Water Level';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.b_wl            is 'B Water Level ';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.qty_del         is 'Qty Del';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.rec_dt          is 'Rec Date';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.dm_update_time  is 'Dm Update Time';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.dm_load_time    is 'Dm Load Time';

```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Service Reservoir Supply
-- function describe: Service Reservoir Water Level And Quantity
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dwd_srs_sr_storage_detail_dip
-- coss_dwd.dwd_rws_channel_flow_detail_dip
-- coss_dim.dim_sr_installation_info
-- target table
-- coss_dm.dm_srs_daily_sr_wl_qty_item_di
-- ****************************************************************************************
drop table if exists coss_tmp.dm_srs_daily_sr_wl_qty_item_di_01;
create table if not exists coss_tmp.dm_srs_daily_sr_wl_qty_item_di_01 (
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
    a_wl            numeric(20, 5) null,
    b_wl            numeric(20, 5) null,
    qty_del         numeric(20, 5) null,
    rec_dt          timestamp(6) null,
    dm_update_time  timestamp(6) null default pg_systimestamp(),
    dm_load_time    timestamp(6) null default pg_systimestamp()
);

;with t_b as(
 select
 t.sr_id
,t.a_wl
,t.b_wl
,t1.qty_del
,t.rec_dt
 from (
select
sr_id
,a_wl
,b_wl
,rec_dt
from coss_dwd.dwd_srs_sr_storage_detail_dip
-- where rec_dt >= ${}
) t
left join (
select
src_id
,rec_dt
,sum(qty_del) as qty_del
from coss_dwd.dwd_rws_channel_flow_detail_dip
where left(src_id,2) = 'SR'
and qty_del is not null
and qty_del > 0
-- and rec_dt > ${}
group by
src_id
,rec_dt
) t1 on t.sr_id = t1.src_id and t.rec_dt = t1.rec_dt
)
insert into coss_tmp.dm_srs_daily_sr_wl_qty_item_di_01
select
    t1.sr_id           ,                     -- Service Reservoir Id
    t1.i_code          ,                     -- Installation Code
    t1.sr_name         ,                     -- Service Reservoir Name En
    t1.sr_cname        ,                     -- Service Reservoir Name Tc
    t1.rpt_label       ,                     -- Report Label
    t1.region_code     ,                     -- Region Code
    t1.sub_region      ,                     -- Sub Region
    t1.region_name     ,                     -- Region Name En
    t1.region_cname    ,                     -- Region Name Tc
    t1.region_ind      ,                     -- Region Ind
    t1.w_type          ,                     -- Water Type
    t1.w_type_desc     ,                     -- Water Type Describe
    t.a_wl            ,                      -- A Water Level
    t.b_wl            ,                      -- B Water Level
    t.qty_del         ,                      -- Qty Del
    t.rec_dt          ,                      -- Rec Date
    current_timestamp dm_update_time  ,      -- Dm Update Time
    current_timestamp dm_load_time           -- Dm Load Time
from t_b t
inner join coss_dim.dim_sr_installation_info t1 on t.sr_id = t1.sr_id;

insert into coss_dm.dm_srs_daily_sr_wl_qty_item_di
select
    sr_id,                -- Service Reservoir Id
    i_code,               -- Installation Code
    sr_name,              -- Service Reservoir Name En
    sr_cname,             -- Service Reservoir Name Tc
    rpt_label,            -- Report Label
    region_code,          -- Region Code
    sub_region,           -- Sub Region
    region_name,          -- Region Name En
    region_cname,         -- Region Name Tc
    region_ind,           -- Region Ind
    w_type,               -- Water Type
    w_type_desc,          -- Water Type Describe
    a_wl,                 -- A Water Level
    b_wl,                 -- B Water Level
    qty_del,              -- Qty Del
    rec_dt,               -- Rec Date
    dm_update_time,       -- Dm Update Time
    dm_load_time         -- Dm Load Time
from
    coss_tmp.dm_srs_daily_sr_wl_qty_item_di_01
on duplicate key update
    i_code = values(i_code),
    sr_name = values(sr_name),
    sr_cname = values(sr_cname),
    rpt_label = values(rpt_label),
    region_code = values(region_code),
    sub_region = values(sub_region),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    w_type = values(w_type),
    w_type_desc = values(w_type_desc),
    a_wl = values(a_wl),
    b_wl = values(b_wl),
    qty_del = values(qty_del),
    dm_update_time = values(dm_update_time)
```

## 10.coss_dm.dm_srs_monthly_sr_qty_di

### create table

```sql
drop table if exists coss_dm.dm_srs_monthly_sr_qty_di;
create table if not exists coss_dm.dm_srs_monthly_sr_qty_di (
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

comment on table coss_dm.dm_srs_monthly_sr_qty_di is 'Service Reservoir Quantity Delivery';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.statistical_month  is 'Statistical Month';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.sr_id              is 'Service Reservoir Id';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.i_code             is 'Installation Code';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.sr_name_en         is 'Service Reservoir Name';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.sr_name_tc         is 'Service Reservoir Name Tc';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.rpt_label          is 'Report Label';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.region_abbr        is 'Region Abbr';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.sub_region         is 'Sub Region ';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.qty_del            is 'Quantity Deliver';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.dm_update_time     is 'Dm Update Time';
comment on column coss_dm.dm_srs_monthly_sr_qty_di.dm_load_time       is 'Dm Load Time ';
```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Service Reservoir Supply
-- function describe: Service Reservoir Water Quantity
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dwd_rws_channel_flow_detail_di_year
-- coss_dim.dim_sr_installation_qty_info
-- target table
-- coss_dm.dm_srs_monthly_sr_qty_di
-- ****************************************************************************************
insert into coss_dm.dm_srs_monthly_sr_qty_di
select
    round(dt/100) statistical_month   ,         -- Statistical Month
    t1.sr_id               ,                    -- Service Reservoir Id
    t1.i_code              ,                    -- Installation Code
    t1.sr_name_en          ,                    -- Service Reservoir Name
    t1.sr_name_tc          ,                    -- Service Reservoir Name Tc
    t1.rpt_label           ,                    -- Report Label
    t1.region_abbr         ,                    -- Region Abbr
    t1.sub_region          ,                    -- Sub Region
    ifnull(sum(t.qty_del), 0) qty_del  ,        -- Quantity Deliver
    current_timestamp dm_update_time      ,     -- Dm Update Time
    current_timestamp dm_load_time              -- Dm Load Time
from coss_dwd.dwd_rws_channel_flow_detail_di_year t
inner join coss_dim.dim_sr_installation_qty_info t1 on t.src_id = t1.sr_id
-- where rec_dt >= ${}
group by
t1.sr_id,
statistical_month
on duplicate key update
    i_code           = values(i_code        ) ,
    sr_name_en       = values(sr_name_en    ) ,
    sr_name_tc       = values(sr_name_tc    ) ,
    rpt_label        = values(rpt_label     ) ,
    region_abbr      = values(region_abbr   ) ,
    sub_region       = values(sub_region    ) ,
    qty_del          = values(qty_del       ) ,
    dm_update_time   = values(dm_update_time)
```



## 11.coss_dm.dm_srs_annual_sr_pool_stopped_di(修改了表名称)

### create table 

```sql
drop table if exists coss_dm.dm_srs_annual_sr_pool_stopped_di;

create table if not exists coss_dm.dm_srs_annual_sr_pool_stopped_di (
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

comment on table coss_dm.dm_srs_annual_sr_pool_stopped_di is 'Service Reservoir Annual Pool Stoped Situation';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.statistical_year  is 'Statistical Year';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.sr_id              is 'Service Reservoir Id';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.i_code             is 'Installation Code';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.sr_name_en         is 'Service Reservoir Name EN';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.sr_name_tc         is 'Service Reservoir Name Tc';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.rpt_label          is 'Report Label';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.region_abbr        is 'Region Abbr';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.sub_region         is 'Sub Region ';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.a_stoped           is 'Number of Days When Pool A Is Stopped';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.b_stoped           is 'Number of Days When Pool B Is Stopped';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.dm_update_time     is 'Dm Update Time';
comment on column coss_dm.dm_srs_annual_sr_pool_stopped_di.dm_load_time       is 'Dm Load Time ';
```

### select sql

```sql
-- ****************************************************************************************
-- subject     areas: Service Reservoir Supply
-- function describe: Service Reservoir Water Pool Stopped
-- create         by: dongmaochen
-- create       date: 2025-11-14
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dwd_srs_sr_storage_detail_di_year
-- target table
-- coss_dm.dm_srs_annual_sr_pool_stopped_di
-- ****************************************************************************************

drop table if exists coss_tmp.dm_srs_annual_sr_pool_stopped_di_01;
create table if not exists coss_tmp.dm_srs_annual_sr_pool_stopped_di_01 (
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
    dm_load_time        timestamp(6) null default pg_systimestamp()
);

with t_a as (
select
sr_id,
round(dt/10000) yr,
count(distinct rec_dt) days_num
from coss_dwd.dwd_srs_sr_storage_detail_di_year
where a_wl = 0
and a_wl is not null
group by
sr_id,
yr
), t_b as (
select
sr_id,
round(dt/10000) yr,
count(distinct rec_dt) days_num
from coss_dwd.dwd_srs_sr_storage_detail_di_year
where b_wl = 0
and b_wl is not null
group by
sr_id,
yr
)
insert into coss_tmp.dm_rws_annual_sr_pool_stoped_di_01
select
     t.yr as statistical_year                       
    ,t1.sr_id                                  
    ,t1.i_code                                 
    ,t1.sr_name as sr_name_en                  
    ,t1.sr_cname as sr_name_tc                 
    ,t1.rpt_label                              
    ,t1.region_code as region_abbr             
    ,t1.sub_region                             
    ,a_stoped                                  
    ,b_stoped                                  
    ,current_timestamp as dm_update_time       
    ,current_timestamp as dm_load_time         
from
(
select
ifnull(t.sr_id,t1.sr_id) sr_id,
ifnull(t.yr,t1.yr) yr,
ifnull(t.days_num,0) a_stoped,
ifnull(t1.days_num,0) b_stoped
from t_a t
full join t_b t1 on t.sr_id = t1.sr_id and t.yr = t1.yr) as t
inner join coss_dim.dim_sr_installation_info t1 on t.sr_id = t1.sr_id;

insert into coss_dm.dm_srs_annual_sr_pool_stopped_di
select
    statistical_year ,      -- Statistical Year                                 
    sr_id            ,      -- Service Reservoir Id    
    i_code           ,      -- Installation Code     
    sr_name_en       ,      -- Service Reservoir Name EN                    
    sr_name_tc       ,      -- Service Reservoir Name Tc                     
    rpt_label        ,      -- Report Label        
    region_abbr      ,      -- Region Abbr                         
    sub_region       ,      -- Sub Region          
    a_stoped         ,      -- Number of Days When Pool A Is Stopped    
    b_stoped         ,      -- Number of Days When Pool B Is Stopped    
    dm_update_time   ,      -- Dm Update Time                               
    dm_load_time            -- Dm Load Time                              
from
coss_tmp.dm_srs_annual_sr_pool_stopped_di_01
on duplicate key update
    i_code           = values(i_code          ) ,
    sr_name_en       = values(sr_name_en      ) ,
    sr_name_tc       = values(sr_name_tc      ) ,
    rpt_label        = values(rpt_label       ) ,
    region_abbr      = values(region_abbr     ) ,
    sub_region       = values(sub_region      ) ,
    a_stoped         = values(a_stoped        ) ,
    b_stoped         = values(b_stoped        ) ,
    dm_update_time   = values(dm_update_time  ) ;
```



# DIM

## 1.coss_dim.dim_sr_installation_info

```SQL
-- drop table if exists coss_dim.dim_sr_installation_info;

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
    dim_load_time    timestamp(6) null default pg_systimestamp(),
    primary key(sr_id)
) with (
    orientation=row,
    compression=no
);

comment on table coss_dim.dim_sr_installation_info is 'Service Reservoir Installation Information';
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
```

## 2.coss_dim.dim_sr_installation_qty_info

```sql
drop table if exists coss_dim.dim_sr_installation_qty_info;
create table if not exists coss_dim.dim_sr_installation_qty_info (
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



```











# ============

## 5.coss_dm.dm_srs_region_day_kpi_dip

### create table

```sql
drop table if exists coss_dm.dm_srs_region_day_kpi_dip;
;CREATE TABLE if not exists coss_dm.dm_srs_region_day_kpi_dip (
	id varchar(42) NULL,
	region varchar(200) NULL,
	item_code varchar(200) NULL,
	item_name varchar(300) NULL,
	item_value numeric(20, 5) NULL,
	"unit" varchar(50) NULL,
	etl_time timestamp(6) NULL,
	dt numeric(10) NULL,
	dm_update_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Update Time
	dm_load_time timestamp(6) NULL DEFAULT pg_systimestamp(), -- Data Loading Time
	primary key(region, item_code, dt)
)
WITH (
	orientation=row,
	compression=no
);
comment on table coss_dm.dm_srs_region_day_kpi_dip is 'service reservoir region daily kpi';
comment on column coss_dm.dm_srs_region_day_kpi_dip.id is 'id';
comment on column coss_dm.dm_srs_region_day_kpi_dip.region is 'region';
comment on column coss_dm.dm_srs_region_day_kpi_dip.item_code is 'item code';
comment on column coss_dm.dm_srs_region_day_kpi_dip.item_name is 'item name';
comment on column coss_dm.dm_srs_region_day_kpi_dip.item_value is 'item value';
comment on column coss_dm.dm_srs_region_day_kpi_dip.unit is 'unit';
comment on column coss_dm.dm_srs_region_day_kpi_dip.etl_time is 'etl time';
comment on column coss_dm.dm_srs_region_day_kpi_dip.dt is 'statistical day';
```



```sql
-- ****************************************************************************************
-- source     system: STTSS(Smart Trunk Transfer Support System)
-- function describe: Service reservoir daily kpi information
-- create         by: dongmaochen
-- create       date: 2025-04-24
-- modify date                modify by                    modify content
-- None                       None                         None
-- source table
-- coss_dwd.dim_ass_sr_dfn
-- target table
-- coss_dm.dm_srs_region_day_kpi_dip
-- ****************************************************************************************

/**
 * delete history metrics data
 * input parameter ${dt} = 20250314
 * fresh and salt water design capacity
 */
;delete
from coss_dm.dm_srs_region_day_kpi_dip
where  item_code in  ('bi_p_212'
  ,'bi_p_213'
  ,'bi_p_214'
  ,'bi_p_215'
  )
  and dt = ${dt1}
/**
 * Calculation for fresh and salt water design capacity
 */
;with t_a as(
select
  region_code         as region
  ,w_type             as w_type
  ,sum(capacity)      as capacity
  ,${dt1}             as dt
from coss_dwd.dim_ass_sr_dfn
group by
  region_code
  ,w_type
)

insert into coss_dm.dm_srs_region_day_kpi_dip
select
  uuid()                                     as id
  ,'HKSAR'                                   as region
  ,'bi_p_212'                                as item_code
  ,'Fresh Water Service Reservoir Capacity'  as item_name
  , sum(capacity)/1000000                    as item_value -- convert cum to mcm
  ,'mcm'                                     as unit
  ,localtimestamp                            as etl_time
  ,t.dt                                      as dt
from t_a t
where w_type = 'F'
group by
  t.dt

union all

select
  uuid()                                     as id
  ,t.region                                  as region
  ,'bi_p_213'                                as item_code
  ,'Fresh Water Service Reservoir Capacity'  as item_name
  ,  capacity/1000000                        as item_value -- convert cum to mcm
  ,'mcm'                                     as unit
  ,localtimestamp                            as etl_time
  ,t.dt                                      as dt
from t_a t
where w_type = 'F'

 union all

select
  uuid()                                   as id
  ,'HKSAR'                                 as region
  ,'bi_p_214'                              as item_code
  ,'Salt Water Service Reservoir Capacity' as item_name
  , sum(capacity)/1000000                  as item_value -- convert cum to mcm
  ,'mcm'                                   as unit
  ,localtimestamp                          as etl_time
  ,t.dt                                    as dt
from t_a t
where w_type = 'S'
group by
  t.dt

union all

select
  uuid()                                   as id
  ,t.region                                as region
  ,'bi_p_215'                              as item_code
  ,'Salt Water Service Reservoir Capacity' as item_name
  ,capacity/1000000                        as item_value -- convert cum to mcm
  ,'mcm'                                   as unit
  ,localtimestamp                          as etl_time
  ,t.dt                                    as dt
from t_a t
where w_type = 'S'
```

## 



## coss_dm.dm_srs_region_month_kpi_dip

```sql
/**
 * delete history metrics data
 * input parameter ${dt} = 20250314
 */
;delete
from coss_dm.dm_srs_region_month_kpi_dip
where  item_code in  ('bi_p_212'
  ,'bi_p_213'
  ,'bi_p_214'
  ,'bi_p_215')
  and mh = round(${dt1}/100, 0)
  
/**
 * Calculation for Service Reservoir Capacity
 */
;with t_a as(
select 
  region_code         as region 
  ,w_type             as w_type
  ,sum(capacity)      as capacity  
  ,round(${dt}/100,0) as mh
from
coss_dwd.dim_ass_sr_dfn 
group by 
  region_code
  ,w_type
)
insert into coss_dm.dm_srs_region_month_kpi_dip
select
  uuid()                                                   as id
  ,'HKSAR'                                                 as region
  ,'bi_p_212'                                              as item_code
  ,'Fresh Water Service Reservoir Capacity' as item_name
  , sum(capacity)/1000000                                  as item_value -- convert cum to mcm
  ,'mcm'                                                   as unit
  ,localtimestamp                                          as etl_time
  ,t.mh                                                    as mh
from t_a t
where w_type = 'F'
group by 
  t.mh
  
union all 

select
  uuid()                                                   as id
  ,t.region                                                as region
  ,'bi_p_213'                                              as item_code
  ,'Fresh Water Service Reservoir Capacity' as item_name
  ,  capacity/1000000                                      as item_value -- convert cum to mcm
  ,'mcm'                                                   as unit
  ,localtimestamp                                          as etl_time
  ,t.mh                                                    as mh
from t_a t
where w_type = 'F'
  
 union all
 
select
  uuid()                                                   as id
  ,'HKSAR'                                                 as region
  ,'bi_p_214'                                              as item_code
  ,'Salt Water Service Reservoir Capacity' as item_name
  , sum(capacity)/1000000                                  as item_value -- convert cum to mcm
  ,'mcm'                                                   as unit
  ,localtimestamp                                          as etl_time
  ,t.mh                                                    as mh
from t_a t
where w_type = 'S'
group by 
  t.mh
  
union all 

select
  uuid()                                                   as id
  ,t.region                                                as region
  ,'bi_p_215'                                              as item_code
  ,'Salt Water Service Reservoir Capacity' as item_name
  ,  capacity/1000000                                      as item_value -- convert cum to mcm
  ,'mcm'                                                   as unit
  ,localtimestamp                                          as etl_time
  ,t.mh                                                    as mh
from t_a t
where w_type = 'S'
```

## coss_dm.dm_srs_region_month_kpi_dip

```sql
/**
 * Calculation for quantity delivery of region monthly
 */

;drop table if exists coss_tmp.tmp_srs_sr_storage_detail_dip_1
;create table if not exists coss_tmp.tmp_srs_sr_storage_detail_dip_1 as
select
  region_code      as region
  ,sum(qty_del)    as qty_del
  ,round(dt/100,0) as mh
from coss_dws.dws_srs_sr_storage_detail_dip
where w_type = 'F' 
  and qty_del is not null
  and dt >= to_char(date_trunc('month', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
  and dt <= ${dt}
group by
  region_code
  ,w_type
  ,round(dt/100,0)
  
/**
 * delete history metrics data
 */
;delete 
from coss_dm.dm_srs_region_month_kpi_dip
 where item_code in 
  ('bi_p_216'
  ,'bi_p_217')
  and mh= round(${dt1}/100, 0)

;with t_a as(
select
  region                                      as region
  ,qty_del                                    as qty_del
  ,sum(qty_del) over(
  partition by region
  order by mh desc
  rows between current row and 5 following ) as qty_del_6mh
  ,mh                                        as mh
from coss_tmp.tmp_srs_sr_storage_detail_dip_1 t
order by
  mh
),t_b as (
select
  qty_del                                      as qty_del
  ,sum(qty_del) over(
   order by mh desc
   rows between current row and 5 following )  as qty_del_6mh
  ,mh                                          as mh
from
(
select
  sum(qty_del)   as qty_del
  ,mh            as mh
from coss_tmp.tmp_srs_sr_storage_detail_dip_1 t
group by
  mh
) t
)

insert into  coss_dm.dm_srs_region_month_kpi_dip
select
  uuid()                               as id
  ,'HKSAR'                             as region
  ,'bi_p_216'                          as item_code
  ,'Service Reservoir Supply Volume'   as item_name
  ,(t.qty_del_6mh*1000)/6              as item_value -- convert Mld to cum
  ,'cum'                               as unit
  ,localtimestamp                      as etl_time
  ,t.mh                                as mh
from t_b t

union all

select
  uuid()                             as id
  ,t.region                          as region
  ,'bi_p_217'                        as item_code
  ,'Service Reservoir Supply Volume' as item_name
  ,(t.qty_del_6mh*1000)/6            as item_value -- convert Mld to cum
  ,'cum'                             as unit
  ,localtimestamp                    as etl_time
  ,t.mh                              as mh
from t_a t
```



## 6.❤🆗coss_dm.dm_srs_region_year_kpi_dip

```sql
CREATE TABLE coss_dm.dm_srs_region_year_kpi_dip (
	id varchar(42) NULL,
	region varchar(200) NULL,
	item_code varchar(200) NULL,
	item_name varchar(300) NULL,
	item_value numeric(20, 5) NULL,
	"unit" varchar(50) NULL,
	etl_time timestamp(6) NULL,
	yr numeric(10) NULL
)
WITH (
	orientation=row,
	compression=no
);
/**
 * delete history metrics data
 */
;delete 
from coss_dm.dm_srs_region_year_kpi_dip
 where item_code in 
  ('bi_p_216'
  ,'bi_p_217')
  and yr = round(${dt1}/10000)
  
;with t_a as(
select
  region_code        as region
  ,sum(qty_del)/1000 as qty_del         -- convert Mld to mcm
  ,round(dt/10000,0) as yr
from coss_dws.dws_srs_sr_storage_detail_dip
where w_type = 'F' and qty_del is not null
and dt >= to_char(date_trunc('year', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
and dt <= ${dt1}
group by
  region_code
  ,yr
), t_b as(
select
  sum(qty_del)/1000     as qty_del       -- convert Mld to mcm
  ,round(dt/10000,0)    as yr
from coss_dws.dws_srs_sr_storage_detail_dip
where w_type = 'F' and qty_del is not null
and dt >= to_char(date_trunc('year', to_date(${dt1},'yyyy-mm-dd')),'yyyymmdd')
and dt <= ${dt1}
group by
  yr
)

insert into  coss_dm.dm_srs_region_year_kpi_dip
select
  uuid()                               as id
  ,'HKSAR'                             as region
  ,'bi_p_216'                          as item_code
  ,'Service Reservoir Supply Volume'   as item_name
  ,qty_del                             as item_value
  ,'cum'                               as unit
  ,localtimestamp                      as etl_time
  ,t.yr                                as yr
from t_b t

union all
select
  uuid()                             as id
  ,t.region                          as region
  ,'bi_p_217'                        as item_code
  ,'Service Reservoir Supply Volume' as item_name
  ,qty_del                           as item_value
  ,'cum'                             as unit
  ,localtimestamp                    as etl_time
  ,t.yr                              as yr
from t_a t
```

## 10.❤coss_dm.dm_rws_rw_supply_hist_dip

```sql
CREATE TABLE coss_dm.dm_rws_rw_supply_hist_dip (
	rw_id varchar(20) NULL,
	rw_name varchar(200) NULL,
	rw_cname varchar(300) NULL,
	region_code varchar(10) NULL,
	source_rw varchar(2) NULL,
	p_qty numeric(12, 4) NULL,
	qty_del numeric(12, 4) NULL,
	present_storage numeric(16, 8) NULL,
	capacity numeric(12, 4) NULL,
	min_storage numeric(12, 4) NULL,
	rec_dt timestamp(6) NULL,
	dt numeric(10) NULL
)
WITH (
	orientation=row,
	compression=no
);

;delete from coss_dm.dm_rws_rw_supply_hist_dip where dt = ${dt1}
;insert into coss_dm.dm_rws_rw_supply_hist_dip
select
  rw_id 
  ,rw_name
  ,rw_cname 
  ,region_code 
  ,source_rw 
  ,p_qty 
  ,qty_del
  ,present_storage 
  ,capacity 
  ,min_storage 
  ,rec_dt
  ,dt
from coss_dws.dws_rws_rw_supply_detail_dip
where dt = ${dt1}
```



# 新增指标

## 配水库供水量

```sql





```



## 2.配水库停水天数

```sql

with t_a as (
select 
sr_id,
round(dt/10000) yr,
count(distinct rec_dt) days_num
from coss_dwd.dwd_srs_sr_storage_detail_di_year 
where a_wl = 0
and a_wl is not null 
group by 
sr_id,
yr
), t_b as (
select 
sr_id,
round(dt/10000) yr,
count(distinct rec_dt) days_num
from coss_dwd.dwd_srs_sr_storage_detail_di_year 
where b_wl = 0
and b_wl is not null 
group by 
sr_id,
yr
)
select 
ifnull(t.sr_id,t1.sr_id) sr_id,
ifnull(t.yr,t1.yr) yr,
ifnull(t.days_num,0) a_stoped,
ifnull(t1.days_num,0) b_stoped
from t_a t 
full join t_b t1 on t.sr_id = t1.sr_id and t.yr = t1.yr
```





> coss_dm.dm_srs_daily_sr_wl_qty_item_di 这张数据表需要重建
>
> coss_dm.dm_rws_monthly_sr_qty_di
>
> coss_dm.dm_rws_annual_sr_pool_stoped_di
>
> coss_dim.dim_sr_installation_qty_info 已处理
>
> coss_dim.dim_sr_installation_info 已处理

## 1.coss_dm.dm_srs_daily_sr_wl_qty_item_di 数据更新

```sql
-- drop table if exists coss_dm.dm_srs_daily_sr_wl_qty_item_di;

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

-- update region code
update coss_dm.dm_srs_daily_sr_wl_qty_item_di set region_code = 'HKI' where region_code = 'HK'

-- coss_dm.dm_srs_daily_sr_wl_qty_item_di
-- update subregion code 
update coss_dm.dm_srs_daily_sr_wl_qty_item_di set sub_region = concat(region_code,'(',sub_region,')') where sub_region is not null




```





