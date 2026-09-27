```tex
251231 :添加水塘单位转换
```



# 1.dm_rws_etl_raw_water_supply_day（调度任务）

前置任务节点

```tex
dm_rws_etl_raw_water_supply_day_sql_dm_rws_annual_rw_yield_di_add
dm_rws_etl_raw_water_supply_day_sql_dm_rws_daily_ir_storage_yield_di_add
dm_rws_etl_raw_water_supply_day_sql_dm_rws_daily_ir_level_storage_di_add
dm_rws_etl_raw_water_supply_day_sql_dm_rws_region_day_kpi_dip_add
dm_rws_etl_raw_water_supply_day_sql_dm_rws_region_month_kpi_dip_add
dm_rws_etl_raw_water_supply_day_sql_dm_rws_region_year_kpi_dip_add
dm_rws_etl_raw_water_supply_day_sql_dm_rws_rw_supply_hist_dip_add
```

数据表

```tex
coss_dm.dm_rws_daily_ir_storage_yield_di
coss_dm.dm_rws_daily_ir_level_storage_di
coss_dm.dm_rws_region_day_kpi_dip
coss_dm.dm_rws_region_month_kpi_dip
coss_dm.dm_rws_region_year_kpi_dip
coss_dm.dm_rws_rw_supply_hist_dip
```



## 1.coss_dm.dm_rws_daily_rw_yield_di+ID

### create table 

```sql
drop table if exists coss_dm.dm_rws_daily_rw_yield_di;
create table if not exists coss_dm.dm_rws_daily_rw_yield_di(
    id                            varchar(50),
    statistical_day               decimal(20,0),
    island_change_storage         decimal(20,5),
    mainland_change_storage       decimal(20,5),
    total_change_storage          decimal(20,5),
    island_current_storage        decimal(20,5),
    island_design_storage         decimal(20,5),
    mainland_current_storage      decimal(20,5),
    mainland_design_storage       decimal(20,5),
    total_current_storage         decimal(20,5),
    total_design_storage          decimal(20,5),
    island_yield                  decimal(20,5),
    mainland_yield                decimal(20,5),
    total_local_yield             decimal(20,5),
    dj_yield                      decimal(20,5),
    total_yield                   decimal(20,5),
    dm_update_time  timestamp(6)       default current_timestamp,
    dm_load_time    timestamp(6)       default current_timestamp,
    primary key(statistical_day)
);

comment on table coss_dm.dm_rws_daily_rw_yield_di is 'Daily Raw Yield';
comment on column coss_dm.dm_rws_daily_rw_yield_di.id                       is 'ID';
comment on column coss_dm.dm_rws_daily_rw_yield_di.statistical_day          is 'Statistical Day';
comment on column coss_dm.dm_rws_daily_rw_yield_di.island_change_storage    is 'Island Change Storage';
comment on column coss_dm.dm_rws_daily_rw_yield_di.mainland_change_storage  is 'Mainland Change Storage';
comment on column coss_dm.dm_rws_daily_rw_yield_di.total_change_storage     is 'Total Change Storage';
comment on column coss_dm.dm_rws_daily_rw_yield_di.island_current_storage   is 'Island Current Storage';
comment on column coss_dm.dm_rws_daily_rw_yield_di.island_design_storage    is 'Island Design Storage';
comment on column coss_dm.dm_rws_daily_rw_yield_di.mainland_current_storage is 'Mainland Current Storage';
comment on column coss_dm.dm_rws_daily_rw_yield_di.mainland_design_storage  is 'Mainland Design Storage';
comment on column coss_dm.dm_rws_daily_rw_yield_di.total_current_storage    is 'Total Current Storage';
comment on column coss_dm.dm_rws_daily_rw_yield_di.total_design_storage     is 'Total Design Storage';
comment on column coss_dm.dm_rws_daily_rw_yield_di.island_yield             is 'Island Yield';
comment on column coss_dm.dm_rws_daily_rw_yield_di.mainland_yield           is 'Mainland Yield';
comment on column coss_dm.dm_rws_daily_rw_yield_di.total_local_yield        is 'Total Local Yield';
comment on column coss_dm.dm_rws_daily_rw_yield_di.dj_yield                 is 'Dj Yield';
comment on column coss_dm.dm_rws_daily_rw_yield_di.total_yield              is 'Total Yield';
comment on column coss_dm.dm_rws_daily_rw_yield_di.dm_update_time            is 'Dm Update Time';
comment on column coss_dm.dm_rws_daily_rw_yield_di.dm_load_time              is 'Dm Load Time';
```

### select sql

```sql

```



## 2.coss_dm.dm_rws_monthly_rw_yield_di+ID

### create table

```sql
drop table if exists coss_dm.dm_rws_monthly_rw_yield_di; 
create table if not exists coss_dm.dm_rws_monthly_rw_yield_di (
    id varchar(50),
    statistical_month numeric(20) null,
    island_yield numeric(20, 5) null,
    mainland_yield numeric(20, 5) null,
    total_local_yield numeric(20, 5) null,
    dj_yield numeric(20, 5) null,
    total_yield numeric(20, 5) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key(statistical_month)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_dm.dm_rws_monthly_rw_yield_di is 'Raw Water Yield';
comment on column coss_dm.dm_rws_monthly_rw_yield_di.id                   is 'ID';
comment on column coss_dm.dm_rws_monthly_rw_yield_di.statistical_month    is 'Statistical Month';
comment on column coss_dm.dm_rws_monthly_rw_yield_di.island_yield         is 'Island Yield';
comment on column coss_dm.dm_rws_monthly_rw_yield_di.mainland_yield       is 'Mainland Yield';
comment on column coss_dm.dm_rws_monthly_rw_yield_di.total_local_yield    is 'Total Local Yield';
comment on column coss_dm.dm_rws_monthly_rw_yield_di.dj_yield             is 'Dj Yield';
comment on column coss_dm.dm_rws_monthly_rw_yield_di.total_yield          is 'Total Yield';
comment on column coss_dm.dm_rws_monthly_rw_yield_di.dm_update_time       is 'Data Update Time';
comment on column coss_dm.dm_rws_monthly_rw_yield_di.dm_load_time         is 'Data Loading Time';
```

### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Raw Water Monthly Yield
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dm.dm_rws_daily_rw_yield_di
-- Target Table:
-- coss_dm.dm_rws_monthly_rw_yield_di
-- ****************************************************************************************
insert into coss_dm.dm_rws_monthly_rw_yield_di
select
    uuid() id,
    round(statistical_day / 100) as statistical_month,
    sum(island_yield) as island_yield,
    sum(mainland_yield) as mainland_yield,
    sum(total_local_yield) as total_local_yield,
    sum(dj_yield) as dj_yield,
    sum(total_yield) as total_yield,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_rw_yield_di
where island_yield is not null
  and mainland_yield is not null
  and total_local_yield is not null
  and dj_yield is not null
  and total_yield is not null
  and statistical_day >=${statistical_day}
group by
    statistical_month
on duplicate key update
    id = values(id),
    island_yield = values(island_yield),
    mainland_yield = values(mainland_yield),
    total_local_yield = values(total_local_yield),
    dj_yield = values(dj_yield),
    total_yield = values(total_yield),
    dm_update_time = values(dm_update_time);
```

## 3.coss_dm.dm_rws_annual_rw_yield_di+ID

### create table

```sql
drop table if exists coss_dm.dm_rws_annual_rw_yield_di;

create table if not exists coss_dm.dm_rws_annual_rw_yield_di (
    id varchar(50),
    statistical_year numeric(20) null,
    island_yield numeric(20, 5) null,
    mainland_yield numeric(20, 5) null,
    total_local_yield numeric(20, 5) null,
    dj_yield numeric(20, 5) null,
    total_yield numeric(20, 5) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key(statistical_year)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_dm.dm_rws_annual_rw_yield_di is 'Annual Raw Water Yield';
comment on column coss_dm.dm_rws_annual_rw_yield_di.id                   is 'ID';
comment on column coss_dm.dm_rws_annual_rw_yield_di.statistical_year   is 'Statistical Year';
comment on column coss_dm.dm_rws_annual_rw_yield_di.island_yield       is 'Island Yield';
comment on column coss_dm.dm_rws_annual_rw_yield_di.mainland_yield     is 'Mainland Yield';
comment on column coss_dm.dm_rws_annual_rw_yield_di.total_local_yield  is 'Total Local Yield';
comment on column coss_dm.dm_rws_annual_rw_yield_di.dj_yield           is 'Dj Yield';
comment on column coss_dm.dm_rws_annual_rw_yield_di.total_yield        is 'Total Yield';
comment on column coss_dm.dm_rws_annual_rw_yield_di.dm_update_time     is 'Update Time';
comment on column coss_dm.dm_rws_annual_rw_yield_di.dm_load_time       is 'Load Time';
```

### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Raw Water Annual Yield
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dm.dm_rws_daily_rw_yield_di
-- Target Table:
-- coss_dm.dm_rws_annual_rw_yield_di
-- ****************************************************************************************
insert into coss_dm.dm_rws_annual_rw_yield_di
select
    uuid() id,
    round(statistical_day / 10000) as statistical_year,
    sum(island_yield) as island_yield,
    sum(mainland_yield) as mainland_yield,
    sum(total_local_yield) as total_local_yield,
    sum(dj_yield) as dj_yield,
    sum(total_yield) as total_yield,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_rw_yield_di
where island_yield is not null
  and mainland_yield is not null
  and total_local_yield is not null
  and dj_yield is not null
  and total_yield is not null
  and statistical_day >= ${statistical_day}
group by
    statistical_year
on duplicate key update
    id = values(id),
    island_yield = values(island_yield),
    mainland_yield = values(mainland_yield),
    total_local_yield = values(total_local_yield),
    dj_yield = values(dj_yield),
    total_yield = values(total_yield),
    dm_update_time = values(dm_update_time);
```

## 4.coss_dm.dm_rws_daily_ir_storage_yield_di+ID

### create table 

```sql
drop table if exists coss_dm.dm_rws_daily_ir_storage_yield_di;

create table if not exists coss_dm.dm_rws_daily_ir_storage_yield_di (
    id varchar(50) null,
    rw_id varchar(50) null,
    rw_name varchar(50) null,
    rw_cname varchar(50) null,
    rpt_label varchar(50) null,
    region_code varchar(50) null,
    region_name varchar(100) null,
    region_cname varchar(200) null,
    region_ind varchar(50) null,
    ig_ind varchar(50) null,
    yield numeric(20, 5) null,
    current_storage numeric(20, 5) null,
    design_storage numeric(20, 5) null,
    change_storage numeric(20, 5) null,
    dt numeric(10) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key (rw_id, dt)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

comment on table coss_dm.dm_rws_daily_ir_storage_yield_di is 'Daily Impounding Reservoir Storage And Yield';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.id                 is 'ID';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.rw_id              is 'Raw Water ID';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.rw_name            is 'Raw Water Name';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.rw_cname           is 'Raw Water TC Name';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.rpt_label          is 'Report Label';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.region_code        is 'Region Code';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.region_name        is 'Region Name';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.region_cname       is 'Region Cname';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.region_ind         is 'Region Ind';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.ig_ind             is 'Impounding Reservoir Group Index';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.yield              is 'Yield';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.current_storage    is 'Current Storage';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.design_storage     is 'Design Storage';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.change_storage     is 'Change Storage';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.dt                 is 'Date';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.dm_update_time     is 'Update Time';
comment on column coss_dm.dm_rws_daily_ir_storage_yield_di.dm_load_time       is 'Load Time';
```

### select sql

```sql
create table if not exists coss_dm.dm_rws_daily_ir_storage_yield_stg_di (
    id varchar(50) null,
    rw_id varchar(50) null,
    rw_name varchar(50) null,
    rw_cname varchar(50) null,
    rpt_label varchar(50) null,
    region_code varchar(50) null,
    region_name varchar(100) null,
    region_cname varchar(200) null,
    region_ind varchar(50) null,
    ig_ind varchar(50) null,
    yield numeric(20, 5) null,
    current_storage numeric(20, 5) null,
    design_storage numeric(20, 5) null,
    change_storage numeric(20, 5) null,
    dt numeric(10) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key (rw_id, dt)
);


-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Raw Water Impounding Reservoir Yield
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dwd.dwd_rws_channel_flow_detail_di_year
-- coss_dws.dws_rws_rw_supply_detail_di_year
-- coss_dwd.dwd_ass_channels_df
-- coss_dwd.dwd_ass_rw_src_df
-- Target Table:
-- coss_dm.dm_rws_daily_ir_storage_yield_di
-- ****************************************************************************************
with dm_rws_daily_ir_storage_yield_di_01 as
(-- Delivery volume
select
    dt,
    t1.src_id as ig_id,
    if(sum(if(left(t1.src_id, 2) = 'IG' and t.qty_del >= 0, t.qty_del, 0)) < 0, 0, sum(if(left(t1.src_id, 2) = 'IG' and t.qty_del >= 0, t.qty_del, 0))) as to_wtc
from
(
select
    option_no,
    ch_id,
    qty_del,
    dt,
    rec_dt
from coss_dwd.dwd_rws_channel_flow_detail_di_year
 where rec_dt>= '${rec_dt}'
) t
inner join coss_dwd.dwd_ass_channels_df t1 on t.option_no = t1.option_no and t.ch_id = t1.ch_id
where left(t1.src_id, 2) = 'IG'
group by
    dt,
    ig_id),
    
dm_rws_daily_ir_storage_yield_di_02 as
(select
    dt,
    t1.dest_id as ig_id,
    if(sum(if(left(t1.dest_id, 2) = 'IG' and t.qty_del >= 0, t.qty_del, 0)) < 0, 0, sum(if(left(t1.dest_id, 2) = 'IG' and t.qty_del >= 0, t.qty_del, 0))) as from_wtc
from
(select
    option_no,
    ch_id,
    qty_del,
    dt,
    rec_dt
from coss_dwd.dwd_rws_channel_flow_detail_di_year
 where rec_dt>= '${rec_dt}'
) t
inner join coss_dwd.dwd_ass_channels_df t1 on t.option_no = t1.option_no and t.ch_id = t1.ch_id
where left(t1.dest_id, 2) = 'IG'
group by
    dt,
    ig_id),

 dm_rws_daily_ir_storage_yield_di_03 as
(select
    rw_id,
    dt,
    rw_name,
    rw_cname,
    present_storage,
    capacity
from coss_dws.dws_rws_rw_supply_detail_di_year
where left(rw_id, 2) = 'IG'
 and rec_dt>= '${rec_dt}'),

dm_rws_daily_ir_storage_yield_di_04 as
(select
    rw_id,
    dt,
    rw_name,
    rw_cname,
    present_storage,
    capacity
from coss_dws.dws_rws_rw_supply_detail_di_year
where left(rw_id, 2) = 'IG'
 and rec_dt>= '${rec_dt}'),

dm_rws_daily_ir_storage_yield_di_05 as
(select
    ig_id,
    dt,
    rw_name,
    rw_cname,
    to_wtc,
    from_wtc,
    delivery
from
(select
    t.dt,
    t.ig_id,
    t.to_wtc,
    t1.from_wtc,
    t.to_wtc - ifnull(t1.from_wtc, 0) as delivery
from
 dm_rws_daily_ir_storage_yield_di_01 t
left join  dm_rws_daily_ir_storage_yield_di_02 t1 on t.dt = t1.dt and t.ig_id = t1.ig_id) t
left join coss_dwd.dwd_ass_rw_src_df t1 on t.ig_id = t1.rw_id),

dm_rws_daily_ir_storage_yield_di_06 as
(select
    t.rw_id as ig_id,
    t.dt,
    t.rw_name,
    t.rw_cname,
    t.present_storage,
    t.capacity,
    (t1.present_storage - t.present_storage) change_storage
from  dm_rws_daily_ir_storage_yield_di_03 t
left join  dm_rws_daily_ir_storage_yield_di_04 t1 on t.dt = to_char(to_date(t1.dt, 'yyyymmdd') + integer '-1', 'yyyymmdd')
and t.rw_id = t1.rw_id and t1.present_storage != 0)

insert into coss_dm.dm_rws_daily_ir_storage_yield_stg_di
-- IR supply
select
    uuid() id,
    t.ig_id rw_id,
    t2.rw_name,
    t2.rw_cname,
    t2.rpt_label,
    t2.region_code,
    t2.region_name,
    t2.region_cname,
    t2.region_ind,
    t2.ig_ind,
    t.delivery + t1.change_storage as yield,
    t1.present_storage current_storage,
    t1.capacity design_storage,
    t1.change_storage change_storage,
    t.dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from
 dm_rws_daily_ir_storage_yield_di_05 t
left join
 dm_rws_daily_ir_storage_yield_di_06 t1 on t.ig_id = t1.ig_id and t.dt = t1.dt
left join coss_dwd.dwd_ass_rw_src_df t2 on t.ig_id = t2.rw_id
where t1.present_storage != 0
;






insert into coss_dm.dm_rws_daily_ir_storage_yield_di (
    id,
    rw_name,
    rw_cname,
    rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    ig_ind,
    yield,
    current_storage,
    design_storage,
    change_storage,
    dm_update_time,
    rw_id,
    dt
)
select
    id,
    rw_name,
    rw_cname,
    rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    ig_ind,
    yield,
    current_storage,
    design_storage,
    change_storage,
    dm_update_time,
    rw_id,
    dt
from coss_dm.dm_rws_daily_ir_storage_yield_stg_di
on duplicate key update
    id = values(id),
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
    dm_update_time = values(dm_update_time);
    
    
    
    
    -- 后续需要把逻辑下沉到DW层
    
    with dm_rws_daily_ir_storage_yield_di_01 as
(-- Delivery volume
select
    rec_dt,
    t1.src_id as ig_id,
    if(sum(if(left(t1.src_id, 2) = 'IG' and t.qty_del >= 0, t.qty_del, 0)) < 0, 0, sum(if(left(t1.src_id, 2) = 'IG' and t.qty_del >= 0, t.qty_del, 0))) as to_wtc
from
(
select
    option_no,
    ch_id,
    qty_del,
    rec_dt
from coss_dwd.dwd_rws_channel_flow_detail_di_year
 where rec_dt>= '${rec_dt}'
) t
inner join coss_dwd.dwd_ass_channels_df t1 on t.option_no = t1.option_no and t.ch_id = t1.ch_id
where left(t1.src_id, 2) = 'IG'
group by
    rec_dt,
    ig_id),
    
dm_rws_daily_ir_storage_yield_di_02 as
(select
    rec_dt,
    t1.dest_id as ig_id,
    if(sum(if(left(t1.dest_id, 2) = 'IG' and t.qty_del >= 0, t.qty_del, 0)) < 0, 0, sum(if(left(t1.dest_id, 2) = 'IG' and t.qty_del >= 0, t.qty_del, 0))) as from_wtc
from
(select
    option_no,
    ch_id,
    qty_del,
    rec_dt
from coss_dwd.dwd_rws_channel_flow_detail_di_year
 where rec_dt>= '${rec_dt}'
) t
inner join coss_dwd.dwd_ass_channels_df t1 on t.option_no = t1.option_no and t.ch_id = t1.ch_id
where left(t1.dest_id, 2) = 'IG'
group by
    rec_dt,
    ig_id),

dm_rws_daily_ir_storage_yield_di_03 as
(
select
    ig_id rw_id,
    rec_dt,
    present_storage * 1000 present_storage  -- Unit MCM To ML
from coss_dwd.dwd_rws_ir_storage_detail_di_year
 where  rec_dt>= '${rec_dt}'
 ),

dm_rws_daily_ir_storage_yield_di_04 as
(
select
    ig_id rw_id,
    rec_dt,
    present_storage * 1000 present_storage  -- Unit MCM To ML
from coss_dwd.dwd_rws_ir_storage_detail_di_year
where rec_dt>= '${rec_dt}'
),

dm_rws_daily_ir_storage_yield_di_05 as
(
select
    t.rec_dt,
    t.ig_id,
    t.to_wtc,
    t1.from_wtc,
    t.to_wtc - ifnull(t1.from_wtc, 0) as delivery
from
 dm_rws_daily_ir_storage_yield_di_01 t
left join  dm_rws_daily_ir_storage_yield_di_02 t1 on t.rec_dt = t1.rec_dt and t.ig_id = t1.ig_id
),

dm_rws_daily_ir_storage_yield_di_06 as
(select
    t.rw_id as ig_id,
    t.rec_dt,
    t.present_storage,
    (t1.present_storage - t.present_storage) change_storage
from  dm_rws_daily_ir_storage_yield_di_03 t
left join  dm_rws_daily_ir_storage_yield_di_04 t1 on t.rec_dt = to_char(t1.rec_dt + integer '-1', 'yyyymmdd')
and t.rw_id = t1.rw_id)


select
    uuid() id,
    t.ig_id rw_id,
    t2.rw_name,
    t2.rw_cname,
    t2.rpt_label,
    t2.region_code,
    t2.region_name,
    t2.region_cname,
    t2.region_ind,
    t2.ig_ind,
    t.delivery + t1.change_storage as yield,
    t1.present_storage current_storage,
    t1.change_storage change_storage,
    t.rec_dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from
 dm_rws_daily_ir_storage_yield_di_05 t
left join
 dm_rws_daily_ir_storage_yield_di_06 t1 on t.ig_id = t1.ig_id and t.rec_dt = t1.rec_dt
left join coss_dwd.dwd_ass_rw_src_df t2 on t.ig_id = t2.rw_id

   
```

## 5.coss_dm.dm_rws_daily_ir_level_storage_di+ID

### create table

```sql
drop table if exists coss_dm.dm_rws_daily_ir_level_storage_di;
create table if not exists coss_dm.dm_rws_daily_ir_level_storage_di(
    id               varchar(50),
    ir_id            varchar(50),
    i_code           varchar(50),
    ir_rpt_label     varchar(100),
    ir_name          varchar(100),
    ir_cname         varchar(100),
    region_code      varchar(100),
    region_name      varchar(100),
    region_cname     varchar(100),
    region_ind       varchar(50),
    level_type       varchar(50),
    level_unit       varchar(50),
    dead_storage     decimal(20, 5),
    twl              decimal(20, 5),
    capacity         decimal(20, 5),
    min_storage      decimal(20, 5),
    limit_m          decimal(20, 5),
    wl_mpd           decimal(20, 5),
    storage          decimal(20, 5),
    avg_7_mpd        decimal(20, 5),
    avg_7_storage    decimal(20, 5),
    avg_28_mpd       decimal(20, 5),
    avg_28_storage   decimal(20, 5),
    rec_dt           timestamp(6),
    dm_update_time   timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time     timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key(ir_id, rec_dt)
);

comment on table coss_dm.dm_rws_daily_ir_level_storage_di is 'Impounding Reservoir Level And Storage';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.id                  is 'ID';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.ir_id               is 'Impounding Reservoir ID';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.i_code              is 'Installation Code';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.ir_rpt_label        is 'Impounding Reservoir Report Label';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.ir_name             is 'Impounding Reservoir Name';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.ir_cname            is 'Impounding Reservoir Cname';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.region_code         is 'Region Code';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.region_name         is 'Region Name';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.region_cname        is 'Region Cname';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.region_ind          is 'Region Ind';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.level_type          is 'Level Type';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.level_unit          is 'Level Unit';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.dead_storage        is 'Dead Storage';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.twl                 is 'TWL';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.capacity            is 'Capacity';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.min_storage         is 'Min Storage';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.limit_m             is 'Limit M';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.wl_mpd              is 'WL MPD';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.storage             is 'Storage';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.avg_7_mpd           is 'Avg 7 MPD';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.avg_7_storage       is 'Avg 7 Storage';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.avg_28_mpd          is 'Avg 28 MPD';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.avg_28_storage      is 'Avg 28 Storage';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.rec_dt              is 'Rec DT';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.dm_update_time      is 'DM Update Time';
comment on column coss_dm.dm_rws_daily_ir_level_storage_di.dm_load_time        is 'DM Load Time';
```

### select sql

```sql
create table if not exists coss_dm.dm_rws_daily_ir_level_storage_stg_di(
    id               varchar(50),
    ir_id            varchar(50),
    i_code           varchar(50),
    ir_rpt_label     varchar(100),
    ir_name          varchar(100),
    ir_cname         varchar(100),
    region_code      varchar(100),
    region_name      varchar(100),
    region_cname     varchar(100),
    region_ind       varchar(50),
    level_type       varchar(50),
    level_unit       varchar(50),
    dead_storage     decimal(20, 5),
    twl              decimal(20, 5),
    capacity         decimal(20, 5),
    min_storage      decimal(20, 5),
    limit_m          decimal(20, 5),
    wl_mpd           decimal(20, 5),
    storage          decimal(20, 5),
    avg_7_mpd        decimal(20, 5),
    avg_7_storage    decimal(20, 5),
    avg_28_mpd       decimal(20, 5),
    avg_28_storage   decimal(20, 5),
    rec_dt           timestamp(6),
    dm_update_time   timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time     timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key(ir_id, rec_dt)
);



-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Raw Water Impounding Reservoir Level And Storage
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dws.dws_rws_ir_storage_detail_di_year
-- coss_dwd.dwd_ass_ir_df
-- Target Table:
-- coss_dm.dm_rws_daily_ir_level_storage_di
-- ****************************************************************************************
with dm_rws_daily_ir_level_storage_di_01 as
(
select
    ir_id,
    rec_dt,
    wl_mpd,
    present_storage,
    sum(wl_mpd) over(
        partition by ir_id
        order by rec_dt desc
        rows between current row and 6 following
    ) / 7 as avg_7_mpd,
    sum(present_storage) over(
        partition by ir_id
        order by rec_dt desc
        rows between current row and 6 following
    ) / 7 as avg_7_storage,
    sum(wl_mpd) over(
        partition by ir_id
        order by rec_dt desc
        rows between current row and 27 following
    ) / 28 as avg_28_mpd,
    sum(present_storage) over(
        partition by ir_id
        order by rec_dt desc
        rows between current row and 27 following
    ) / 28 as avg_28_storage
from coss_dws.dws_rws_ir_storage_detail_di_year
where wl_mpd is not null
  and present_storage is not null
   and rec_dt >= '${rec_dt}'
order by rec_dt
),

dm_rws_daily_ir_level_storage_di_02 as
(select
    t.ig_id as ig_id,            -- Impounding Reservoir Group ID with format IGNNNNNNNN
    t.ig_name as ig_name,          -- Name of Impounding Reservoir Group
    t.ig_cname as ig_cname,         -- Chinese Name of Impounding Reservoir Group
    t.region_code as region_code,      -- Region
    t.region_name as region_name,      -- Description of Region
    t.region_cname as region_cname,     -- Chinese Description of Region
    t.region_ind as region_ind,       -- Possible Values: {"I" - HK Island, "M" - Mainland}
    t.ir_id as ir_id,            -- Impounding Reservoir ID with format IRNNNNNNNN
    t.i_code as i_code,           -- Installation Code of Impounding Reservoir
    t.ir_rpt_label as ir_rpt_label,     -- Labels used in reports
    t.ir_name as ir_name,          -- Impounding reservoir name
    t.ir_cname as ir_cname,         -- Impounding Reservoir Chinese Name
    t.level_type as level_type,       -- Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}
    t.level_unit as level_unit,       -- Possible Values:{"F" - Feet / Inch, "M" - Meter}
    t.dead_storage as dead_storage,     -- Dead Storage of an Impounding Reservoir.  Unit is in mcm
    t.twl as twl,              -- TWL
    t.capacity*1000 as capacity,         -- Unit mcm change to ML
    t.min_storage as min_storage,      -- Allowable Minimum Storage.  Unit is in mcm
    t.limit_m as limit_m,          -- Preset Limit for Water Level.  Unit is in m
    current_timestamp as dw_etl_time      -- Data Warehouse ETL Time
from coss_dwd.dwd_ass_ir_df t)

insert into coss_dm.dm_rws_daily_ir_level_storage_stg_di
select
    uuid() id,
    t1.ir_id,
    t1.i_code,
    t1.ir_rpt_label,
    t1.ir_name,
    t1.ir_cname,
    t1.region_code,
    t1.region_name,
    t1.region_cname,
    t1.region_ind,
    t1.level_type,
    t1.level_unit,
    t1.dead_storage,
    t1.twl,
    t1.capacity,
    t1.min_storage,
    t1.limit_m,
    t.wl_mpd,
    t.present_storage / t1.capacity * 100 as storage,
    t.avg_7_mpd,
    t.avg_7_storage / t1.capacity * 100 as avg_7_storage,
    t.avg_28_mpd,
    t.avg_28_storage / t1.capacity * 100 as avg_28_storage,
    t.rec_dt,
    current_timestamp dm_load_time,
    current_timestamp dm_update_time
from dm_rws_daily_ir_level_storage_di_01 t
left join dm_rws_daily_ir_level_storage_di_02 t1 on t.ir_id = t1.ir_id

   
insert into coss_dm.dm_rws_daily_ir_level_storage_di
select
    id,
    ir_id,
    i_code,
    ir_rpt_label,
    ir_name,
    ir_cname,
    region_code,
    region_name,
    region_cname,
    region_ind,
    level_type,
    level_unit,
    dead_storage,
    twl,
    capacity,
    min_storage,
    limit_m,
    wl_mpd,
    storage,
    avg_7_mpd,
    avg_7_storage,
    avg_28_mpd,
    avg_28_storage,
    rec_dt,
    current_timestamp dm_load_time,
    current_timestamp dm_update_time
from coss_dm.dm_rws_daily_ir_level_storage_stg_di 
on duplicate key update
    id = values(id),
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
    dm_update_time = values(dm_update_time);
    
    
    
    
```

## 6.coss_dm.dm_rws_region_day_kpi_dip(STG) 

### create table

> Detail: Key (region, item_code, dt)=(HKSAR, bi_p_224, 20091030) already exists.

```sql
drop table if exists coss_dm.dm_rws_region_day_kpi_dip;
create table if not exists coss_dm.dm_rws_region_day_kpi_dip (
    id varchar(42) null,
    region varchar(200) null,
    item_code varchar(200) null,
    item_name varchar(300) null,
    item_value numeric(20, 5) null,
    "unit" varchar(50) null,
    etl_time timestamp(6) null,
    dt numeric(10) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time	
    primary key(region, item_code, dt)
)
with (
    orientation=row,
    compression=no
);

comment on table coss_dm.dm_rws_region_day_kpi_dip is 'Raw Water Supply Daily KPI';
comment on column coss_dm.dm_rws_region_day_kpi_dip.id is 'ID';
comment on column coss_dm.dm_rws_region_day_kpi_dip.region is 'Region';
comment on column coss_dm.dm_rws_region_day_kpi_dip.item_code is 'Item Code';
comment on column coss_dm.dm_rws_region_day_kpi_dip.item_name is 'Item Name';
comment on column coss_dm.dm_rws_region_day_kpi_dip.item_value is 'Item Value';
comment on column coss_dm.dm_rws_region_day_kpi_dip.unit is 'Unit';
comment on column coss_dm.dm_rws_region_day_kpi_dip.etl_time is 'ETL Time';
comment on column coss_dm.dm_rws_region_day_kpi_dip.dt is 'Statistical Day';
comment on column coss_dm.dm_rws_region_day_kpi_dip.dm_update_time is 'Update Time';
comment on column coss_dm.dm_rws_region_day_kpi_dip.dm_load_time is 'Load Time';
```

### select sql(G)

```sql
create table if not exists coss_dm.dm_rws_region_day_kpi_stg_dip (
    id varchar(42) null,
    region varchar(200) null,
    item_code varchar(200) null,
    item_name varchar(300) null,
    item_value numeric(20, 5) null,
    "unit" varchar(50) null,
    etl_time timestamp(6) null,
    dt numeric(10) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp() -- Data Loading Time	
)
with (
    orientation=row,
    compression=no
);


-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Raw Water Daily KPI
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dws.dws_rws_rw_supply_detail_di_year
-- Target Table:
-- coss_dm.dm_rws_region_day_kpi_dip
-- ****************************************************************************************
-- Precomputation Metrics of propose and actual supply
with dm_rws_region_day_kpi_dip_01 as
(select
    region_code as region,
    sum(p_qty) as p_qty,
    sum(qty_del) as qty_del,
    dt
from coss_dws.dws_rws_rw_supply_detail_di_year
 where rec_dt >= '${rec_dt}'
group by
    region_code,
    dt),
 
dm_rws_region_day_kpi_dip_02 as
(select
    'HKSAR' as region,
    sum(p_qty) as p_qty,
    sum(qty_del) as qty_del,
    dt
from coss_dws.dws_rws_rw_supply_detail_di_year
 where rec_dt >= '${rec_dt}'
group by
    dt)
    
insert into coss_dm.dm_rws_region_day_kpi_stg_dip
-- HKSAR Raw Water Actual Supply Volume
select
    uuid() as id,
    region as region,
    'bi_p_224' as item_code,
    'Raw Water Actual Supply Volume' as item_name,
    qty_del as item_value,
    'Ml' as unit,
    current_timestamp as etl_time, 
    t.dt as dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_day_kpi_dip_02 t

union all
-- Region Raw Water Actual Supply Volume
select
    uuid() as id,
    region as region,
    'bi_p_225' as item_code,
    'Raw Water Actual Supply Volume' as item_name,
    qty_del as item_value,
    'Ml' as unit,
    current_timestamp as etl_time, 
    t.dt as dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_day_kpi_dip_01 t

union all
-- HKSAR Raw Water Propose Supply Volume
select
    uuid() as id,
    region as region,
    'bi_p_226' as item_code,
    'Raw Water Propose Supply Volume' as item_name,
    p_qty as item_value,
    'Ml' as unit,
    current_timestamp as etl_time, 
    t.dt as dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_day_kpi_dip_02 t

union all
-- Region Raw Water Propose Supply Volume
select
    uuid() as id,
    region as region,
    'bi_p_227' as item_code,
    'Raw Water Propose Supply Volume' as item_name,
    p_qty as item_value,
    'Ml' as unit,
    current_timestamp as etl_time,  
    t.dt as dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_day_kpi_dip_01 t;




insert into coss_dm.dm_rws_region_day_kpi_dip (
    id,
    region,
    item_code,
    item_name,
    item_value,
    unit,
    etl_time,
    dt,
    dm_update_time,
    dm_load_time
)
select
    id,
    region,
    item_code,
    item_name,
    item_value,
    unit,
    etl_time,
    dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_region_day_kpi_stg_dip
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    "unit" = values("unit"),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);
   
   
   
   
   
   
delete from coss_dm.dm_rws_region_day_kpi_dip where item_code in ('bi_p_224','bi_p_225','bi_p_226','bi_p_227')

delete from coss_dm.dm_rws_region_day_kpi_stg_dip



数据核对sqL

select rw_cname,p_qty, qty_del  from coss_dws.dws_rws_rw_supply_detail_di_year where dt= 20230430

select sum(p_qty), sum(qty_del)  from coss_dws.dws_rws_rw_supply_detail_di_year where dt= 20230430



-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- 水塘当前容量(天指标)
insert into coss_dm.dm_rws_region_day_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_253' as item_code,
    'Impounding Reservoir Current Storage ML' as item_name,
    sum(present_storage) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dws.dws_rws_ir_storage_detail_di_year
group by
dt,
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_253' as item_code,
    'Impounding Reservoir Current Storage ML' as item_name,
    sum(present_storage) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    dt, --
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  coss_dws.dws_rws_ir_storage_detail_di_year
group by
 dt
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);


-- 水塘产量(天指标)
insert into coss_dm.dm_rws_region_day_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
group by
dt,
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    dt, --
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
group by
 dt
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);


-- 东江水(天指标)
insert into coss_dm.dm_rws_region_day_kpi_dip
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_255' as item_code,
    'GD Water Actual Supply ML' as item_name,
    sum(agr_vol - dis_vol) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(to_char(rec_dt,'yyyymmdd') as int) dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_rws_gd_agr_supply_di_year
group by
cast(to_char(rec_dt,'yyyymmdd') as int)
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);
    
    

```

## 7.coss_dm.dm_rws_region_month_kpi_dip(STG)

### create table

```sql
drop table if exists coss_dm.dm_rws_region_month_kpi_dip;
create table if not exists coss_dm.dm_rws_region_month_kpi_dip (
    id varchar(42) null,
    region varchar(200) null,
    item_code varchar(200) null,
    item_name varchar(300) null,
    item_value numeric(20, 5) null,
    "unit" varchar(50) null,
    etl_time timestamp(6) null,
    mh numeric(10) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key(region, item_code, mh)
)
with (
    orientation=row,
    compression=no
);

comment on table coss_dm.dm_rws_region_month_kpi_dip is 'Raw Water Supply Region Monthly KPI';
comment on column coss_dm.dm_rws_region_month_kpi_dip.id  is 'ID';
comment on column coss_dm.dm_rws_region_month_kpi_dip.region  is 'Region';
comment on column coss_dm.dm_rws_region_month_kpi_dip.item_code  is 'Item Code';
comment on column coss_dm.dm_rws_region_month_kpi_dip.item_name  is 'Item Name';
comment on column coss_dm.dm_rws_region_month_kpi_dip.item_value  is 'Item Value';
comment on column coss_dm.dm_rws_region_month_kpi_dip.unit  is 'Unit';
comment on column coss_dm.dm_rws_region_month_kpi_dip.etl_time  is 'ETL Time';
comment on column coss_dm.dm_rws_region_month_kpi_dip.mh  is 'Statistical Month';
comment on column coss_dm.dm_rws_region_month_kpi_dip.dm_update_time is 'Update Time';
comment on column coss_dm.dm_rws_region_month_kpi_dip.dm_load_time  is 'Load Time';
```

### select sql(G)

```sql
create table if not exists coss_dm.dm_rws_region_month_kpi_stg_dip (
    id varchar(42) null,
    region varchar(200) null,
    item_code varchar(200) null,
    item_name varchar(300) null,
    item_value numeric(20, 5) null,
    "unit" varchar(50) null,
    etl_time timestamp(6) null,
    mh numeric(10) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key(region, item_code, mh)
)
with (
    orientation=row,
    compression=no
);


-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Raw Water Monthly KPI By Region 
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dws.dws_rws_rw_supply_detail_di_year
-- Target Table:
-- coss_dm.dm_rws_region_month_kpi_dip
-- ****************************************************************************************

-- Precomputation Metrics of propose and quantity delivery volume
with dm_rws_region_month_kpi_dip_01 as
(
select
    region_code as region,
    sum(p_qty) as p_qty,
    sum(qty_del) as qty_del,
    dt
from coss_dws.dws_rws_rw_supply_detail_di_year
  where rec_dt >= date_trunc('month', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) 
group by
    region_code,
    dt
    ),

dm_rws_region_month_kpi_dip_02 as
(
select
    'HKSAR' as region,
    sum(p_qty) as p_qty,
    sum(qty_del) as qty_del,
    dt
from coss_dws.dws_rws_rw_supply_detail_di_year
  where rec_dt >= date_trunc('month', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) 
group by
    dt
    )
insert into coss_dm.dm_rws_region_month_kpi_stg_dip
-- HKSAR Raw Water Actual Supply Volume
select
    uuid() as id,
    region as region,
    'bi_p_224' as item_code,
    'Raw Water Actual Supply Volume' as item_name,
    sum(qty_del) / count(distinct dt) as item_value,
    'Ml' as unit,
    current_timestamp as etl_time,  
    round(t.dt / 100) as mh,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_month_kpi_dip_02 t
group by
    region,
    round(t.dt / 100)  

union all
-- Region Raw Water Actual Supply Volume
select
    uuid() as id,
    region as region,
    'bi_p_225' as item_code,
    'Raw Water Actual Supply Volume' as item_name,
    sum(qty_del) / count(distinct dt) as item_value,
    'Ml' as unit,
    current_timestamp as etl_time, 
    round(t.dt / 100) as mh,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_month_kpi_dip_01 t
group by
    region,
    round(t.dt / 100) 

union all
-- HKSAR Raw Water Propose Supply Volume
select
    uuid() as id,
    region as region,
    'bi_p_226' as item_code,
    'Raw Water Propose Supply Volume' as item_name,
    sum(p_qty) / count(distinct dt) as item_value,
    'Ml' as unit,
    current_timestamp as etl_time, 
    round(t.dt / 100) as mh,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_month_kpi_dip_02 t
group by
    region,
    round(t.dt / 100) 

union all
-- Region Raw Water Propose Supply Volume
select
    uuid() as id,
    region as region,
    'bi_p_227' as item_code,
    'Raw Water Propose Supply Volume' as item_name,
    sum(p_qty) / count(distinct dt) as item_value,
    'Ml' as unit,
    current_timestamp as etl_time,  
    round(t.dt / 100) as mh,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_month_kpi_dip_01 t
group by
    region,
    round(t.dt / 100) 


--select date_trunc('month', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) 
   
insert into coss_dm.dm_rws_region_month_kpi_dip(
    id,
    region,
    item_code,
    item_name,
    item_value,
    unit,
    etl_time,
    mh,
    dm_update_time,
    dm_load_time
)
select 
    id,
    region,
    item_code,
    item_name,
    item_value,
    unit,
    etl_time,
    mh,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_region_month_kpi_stg_dip
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time)
    
    
delete from coss_dm.dm_rws_region_month_kpi_stg_dip   
delete from coss_dm.dm_rws_region_month_kpi_dip where item_code in ('bi_p_224','bi_p_225','bi_p_226','bi_p_227')




-- 水塘产量(月指标)

insert into coss_dm.dm_rws_region_month_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(dt/100 as int) mh ,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
where rec_dt >= date_trunc('month', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) 
group by
cast(dt/100  as int),
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(dt/100 as int) mh , --
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
where rec_dt >= date_trunc('month', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) 
group by
 cast(dt/100 as int)
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);

-- 东江水实际供应量（月指标）
insert into coss_dm.dm_rws_region_month_kpi_dip
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_255' as item_code,
    'GD Water Actual Supply ML' as item_name,
    sum(agr_vol - dis_vol) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(to_char(rec_dt,'yyyymm') as int) mh,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_rws_gd_agr_supply_di_year
where rec_dt >= date_trunc('month', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) 
group by
cast(to_char(rec_dt,'yyyymm') as int)
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);
   
```

## 8.coss_dm.dm_rws_region_year_kpi_dip(STG)

### create tbale 

```sql
drop table if exists coss_dm.dm_rws_region_year_kpi_dip;

create table if not exists coss_dm.dm_rws_region_year_kpi_dip (
    id varchar(42) null,
    region varchar(200) null,
    item_code varchar(200) null,
    item_name varchar(300) null,
    item_value numeric(20, 5) null,
    "unit" varchar(50) null,
    etl_time timestamp(6) null,
    yr numeric(10) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key(region, item_code, yr)
)
with (
    orientation=row,
    compression=no
);

comment on table coss_dm.dm_rws_region_year_kpi_dip is 'Raw Water Annual KPI';
comment on column coss_dm.dm_rws_region_year_kpi_dip.id is 'ID';
comment on column coss_dm.dm_rws_region_year_kpi_dip.region is 'Region';
comment on column coss_dm.dm_rws_region_year_kpi_dip.item_code is 'Item Code';
comment on column coss_dm.dm_rws_region_year_kpi_dip.item_name is 'Item Name';
comment on column coss_dm.dm_rws_region_year_kpi_dip.item_value is 'Item Value';
comment on column coss_dm.dm_rws_region_year_kpi_dip.unit is 'Unit';
comment on column coss_dm.dm_rws_region_year_kpi_dip.etl_time is 'ETL Time';
comment on column coss_dm.dm_rws_region_year_kpi_dip.yr is 'Statistical Year';
comment on column coss_dm.dm_rws_region_year_kpi_dip.dm_update_time is 'Update Time';
comment on column coss_dm.dm_rws_region_year_kpi_dip.dm_load_time is 'Load Time';
```

### select sql

```sql
create table if not exists coss_dm.dm_rws_region_year_kpi_stg_dip (
    id varchar(42) null,
    region varchar(200) null,
    item_code varchar(200) null,
    item_name varchar(300) null,
    item_value numeric(20, 5) null,
    "unit" varchar(50) null,
    etl_time timestamp(6) null,
    yr numeric(10) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key(region, item_code, yr)
);


-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Raw Water Supply Region Annual KPI
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dws.dws_rws_rw_supply_detail_di_year
-- Target Table:
-- coss_dm.dm_rws_region_year_kpi_dip
-- ****************************************************************************************

-- Precomputation Metrics of propose and quantity delivery volume
with dm_rws_region_year_kpi_dip_01 as
(select
    region_code as region,
    sum(p_qty) as p_qty,
    sum(qty_del) as qty_del,
    dt
from coss_dws.dws_rws_rw_supply_detail_di_year
 where rec_dt >= date_trunc('year', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) - interval '1 year'
group by
    region_code,
    dt),

dm_rws_region_year_kpi_dip_02 as
(select
    'HKSAR' as region,
    sum(p_qty) as p_qty,
    sum(qty_del) as qty_del,
    dt
from coss_dws.dws_rws_rw_supply_detail_di_year
 where rec_dt >= date_trunc('year', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) - interval '1 year'
group by
    dt),

dm_rws_region_year_kpi_dip_03 as
(select
    region as region,
    round(dt / 10000) as yr,
    sum(p_qty) / count(distinct dt) as p_qty,
    sum(qty_del) / count(distinct dt) as qty_del
from
(select
    region_code as region,
    sum(p_qty) as p_qty,
    sum(qty_del) as qty_del,
    dt
from coss_dws.dws_rws_rw_supply_detail_di_year
 where rec_dt >= date_trunc('year', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) - interval '1 year'
group by
    region_code,
    dt) t
group by
    region,
    yr),

dm_rws_region_year_kpi_dip_04 as
(
select
    region as region,
    round(dt / 10000) as yr,
    sum(p_qty) / count(distinct dt) as p_qty,
    sum(qty_del) / count(distinct dt) as qty_del
from
(select
    'HKSAR' as region,
    sum(p_qty) as p_qty,
    sum(qty_del) as qty_del,
    dt
from coss_dws.dws_rws_rw_supply_detail_di_year drrsddy 
 where rec_dt >= date_trunc('year', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) - interval '1 year'
group by
    dt
    ) t
group by
    region,
    yr
    )


 insert into coss_dm.dm_rws_region_year_kpi_stg_dip
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- HKSAR Raw Water Actual Supply Volume avg day
select
    uuid() as id,
    region as region,
    'bi_p_224' as item_code,
    'Raw Water Actual Supply Volume' as item_name,
    sum(qty_del) / count(distinct dt) as item_value,
    'Ml' as unit,
    current_timestamp as etl_time, 
    round(t.dt / 10000) as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_year_kpi_dip_02 t
group by
    region,
    round(t.dt / 10000) 

union all
-- Region Raw Water Actual Supply Volume avg day
select
    uuid() as id,
    region as region,
    'bi_p_225' as item_code,
    'Raw Water Actual Supply Volume' as item_name,
    sum(qty_del) / count(distinct dt) as item_value,
    'Ml' as unit,
    current_timestamp as etl_time, 
    round(t.dt / 10000) as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_year_kpi_dip_01 t
group by
    region,
    round(t.dt / 10000)  

union all
-- HKSAR Raw Water Propose Supply Volume avg day
select
    uuid() as id,
    region as region,
    'bi_p_226' as item_code,
    'Raw Water Propose Supply Volume' as item_name,
    sum(p_qty) / count(distinct dt) as item_value,
    'Ml' as unit,
    current_timestamp as etl_time,  
    round(t.dt / 10000) as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_year_kpi_dip_02 t
group by
    region,
    round(t.dt / 10000)  

union all
-- Region Raw Water Propose Supply Volume avg day
select
    uuid() as id,
    region as region,
    'bi_p_227' as item_code,
    'Raw Water Propose Supply Volume' as item_name,
    sum(p_qty) / count(distinct dt) as item_value,
    'Ml' as unit,
    current_timestamp as etl_time, 
    round(t.dt / 10000) as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_year_kpi_dip_01 t
group by
    region,
    round(t.dt / 10000)

union all
-- HKSAR Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water
select
    uuid() as id,
    t.region as region,
    'bi_p_230' as item_code,
    'Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water' as item_name,
    case
        when t1.qty_del is null or t1.qty_del = 0 then null
        else (t.qty_del - t1.qty_del) / t1.qty_del * 100
    end as item_value,
    '%' as unit,
    current_timestamp as etl_time,  
    t.yr as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_year_kpi_dip_04 t
left join  dm_rws_region_year_kpi_dip_04 t1 on t.yr = t1.yr + 1

union all
-- Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water
select
    uuid() as id,
    t.region as region,
    'bi_p_231' as item_code,
    'Year-On-Year Rises Of Average Actual Supply Volume Of Raw Water' as item_name,
    case
        when t1.qty_del is null or t1.qty_del = 0 then null
        else (t.qty_del - t1.qty_del) / t1.qty_del * 100
    end as item_value,
    '%' as unit,
    current_timestamp as etl_time, 
    t.yr as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_year_kpi_dip_03 t
left join  dm_rws_region_year_kpi_dip_03 t1 on t.region = t1.region and t.yr = t1.yr + 1

union all
-- HKSAR Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water
select
    uuid() as id,
    t.region as region,
    'bi_p_234' as item_code,
    'Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water' as item_name,
    case
        when t1.p_qty is null or t1.p_qty = 0 then null
        else (t.p_qty - t1.p_qty) / t1.p_qty * 100
    end as item_value,
    '%' as unit,
    current_timestamp as etl_time, 
    t.yr as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time  
from  dm_rws_region_year_kpi_dip_04 t
left join  dm_rws_region_year_kpi_dip_04 t1 on t.yr = t1.yr + 1


union all
-- Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water
select
    uuid() as id,
    t.region as region,
    'bi_p_235' as item_code,
    'Year-On-Year Rises Of Average Proposed Supply Volume Of Raw Water' as item_name,  
    case
        when t1.p_qty is null or t1.p_qty = 0 then null 
        else (t.p_qty - t1.p_qty) / t1.p_qty * 100
    end as item_value,
    '%' as unit,
    current_timestamp as etl_time, 
    t.yr as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  dm_rws_region_year_kpi_dip_03 t
left join  dm_rws_region_year_kpi_dip_03 t1 on t.region = t1.region and t.yr = t1.yr + 1



insert into coss_dm.dm_rws_region_year_kpi_dip(
	id,
	region,
	item_code,
	item_name,
	item_value,
	unit,
	etl_time,
	yr,
	dm_update_time,
	dm_load_time
)
select
	id,
	region,
	item_code,
	item_name,
	item_value,
	unit,
	etl_time,
	yr,
	dm_update_time,
	dm_load_time
from coss_dm.dm_rws_region_year_kpi_stg_dip
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time)
   
    ;
   
delete from coss_dm.dm_rws_region_year_kpi_stg_dip   

delete from coss_dm.dm_rws_region_year_kpi_dip where item_code in ('bi_p_224','bi_p_225','bi_p_226','bi_p_227','bi_p_230','bi_p_231','bi_p_234','bi_p_235')
 
 
 

   
-- 设计容量
insert into coss_dm.dm_rws_region_year_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_252' as item_code,
    'Impounding Reservoir Capacity mcm' as item_name,
    sum(capacity) as item_value,
    'mcm' as unit,
    current_timestamp as etl_time,
    to_char(current_timestamp, 'yyyy')  as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_ass_ir_df t
group by
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_252' as item_code,
    'Impounding Reservoir Capacity mcm' as item_name,
    sum(capacity) as item_value,
    'mcm' as unit,
    current_timestamp as etl_time,
    to_char(current_timestamp, 'yyyy')  as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_ass_ir_df t
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);
    

-- 水塘产量(年指标)
insert into coss_dm.dm_rws_region_year_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(dt/10000 as int) mh ,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
 where rec_dt >= date_trunc('year', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) 
group by
cast(dt/10000  as int),
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(dt/10000 as int) mh , --
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
 where rec_dt >= date_trunc('year', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) 
group by
 cast(dt/10000 as int)
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);


-- 东江水实际供应量（年指标）
insert into coss_dm.dm_rws_region_year_kpi_dip
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_255' as item_code,
    'GD Water Actual Supply ML' as item_name,
    sum(agr_vol - dis_vol) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(to_char(rec_dt,'yyyy') as int) yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_rws_gd_agr_supply_di_year
 where rec_dt >= date_trunc('year', to_date('${rec_dt}','YYYY-MM-DD HH24:MI:SS.FF3')) 
group by
cast(to_char(rec_dt,'yyyy') as int)
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);
```

## 9.coss_dm.dm_rws_rw_supply_hist_dip

### create table

```sql
drop table if exists coss_dm.dm_rws_rw_supply_hist_dip;
create table coss_dm.dm_rws_rw_supply_hist_dip (
    rw_id varchar(20) not null, -- Raw Water Source ID with format RWNNNNNNNN
    rw_name varchar(200) null, -- Name of Raw Water
    rw_cname varchar(300) null, -- Chinese Name of Raw Water
    region_code varchar(10) null, -- Region Code
    source_rw varchar(2) null, -- Source of Raw Water
    p_qty numeric(12, 4) null, -- Proposed Quantity.  Unit is Mld
    qty_del numeric(12, 4) null, -- Quantity delivered of Water transfer channel. Unit is in Mld
    present_storage numeric(16, 8) null, -- Storage of water in IR At Present.  Unit is Mld
    capacity numeric(12, 4) null, -- Capacity of IR.  Unit is Mld
    min_storage numeric(12, 4) null, -- Allowable Minimum Storage.  Unit is Mld
    rec_dt timestamp(6) not null, -- Date of Record
    dt numeric(10) null, -- Date time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- DM Load Time
    dm_update_time timestamp(6) null default pg_systimestamp(), -- DM Update Time
    primary key(rw_id,rec_dt)
)
with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

-- Add table comment
comment on table coss_dm.dm_rws_rw_supply_hist_dip is 'Raw Water Supply History';

-- Add column comments
comment on column coss_dm.dm_rws_rw_supply_hist_dip.rw_id is 'Raw Water Source ID with format RWNNNNNNNN';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.rw_name is 'Name of Raw Water';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.rw_cname is 'Chinese Name of Raw Water';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.region_code is 'Region Code';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.source_rw is 'Source of Raw Water';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.p_qty is 'Proposed Quantity.  Unit is Mld';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.qty_del is 'Quantity delivered of Water transfer channel. Unit is in Mld';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.present_storage is 'Storage of water in IR At Present.  Unit is Mld';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.capacity is 'Capacity of IR.  Unit is Mld';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.min_storage is 'Allowable Minimum Storage.  Unit is Mld';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.rec_dt is 'Date of Record';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.dt is 'Date time';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.dm_load_time is 'DM Load Time';
comment on column coss_dm.dm_rws_rw_supply_hist_dip.dm_update_time is 'DM Update Time';

```

### select sql(k 0)

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Raw Water Daily KPI
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dws.dws_rws_rw_supply_detail_di_year
-- Target Table:
-- coss_dm.dm_rws_rw_supply_hist_dip
-- ****************************************************************************************
insert into coss_dm.dm_rws_rw_supply_hist_dip (
    rw_id,
    rw_name,
    rw_cname,
    region_code,
    source_rw,
    p_qty,
    qty_del,
    present_storage,
    capacity,
    min_storage,
    rec_dt,
    dt,
    dm_load_time,
    dm_update_time
)
select
    rw_id,
    rw_name,
    rw_cname,
    region_code,
    source_rw,
    p_qty,
    qty_del,
    present_storage,
    capacity,
    min_storage,
    rec_dt,
    dt,
    current_timestamp dm_load_time,
    current_timestamp dm_update_time
from coss_dws.dws_rws_rw_supply_detail_di_year
where rec_dt >= '${rec_dt}'
on duplicate key update
    rw_name = values(rw_name),
    rw_cname = values(rw_cname),
    region_code = values(region_code),
    source_rw = values(source_rw),
    p_qty = values(p_qty),
    qty_del = values(qty_del),
    present_storage = values(present_storage),
    capacity = values(capacity),
    min_storage = values(min_storage),
    dt = values(dt),
    dm_update_time = values(dm_update_time);
```



# 2.dm_srs_etl_sr_water_supply_day（调度任务）

```
select * from coss_dm.dm_srs_daily_sr_wl_qty_item_di
select * from coss_dm.dm_srs_monthly_sr_qty_di
select * from coss_dm.dm_srs_annual_sr_pool_stopped_di
select * from coss_dm.dm_srs_region_year_kpi_dip
```



## 1.coss_dm.dm_srs_daily_sr_wl_qty_item_di(STG)[修改分区和主键]

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
    a_storage       numeric(20, 5) null,
    b_storage       numeric(20, 5) null,
    tot_storage     numeric(20, 5) null,
    qty_del         numeric(20, 5) null,
    rec_dt          timestamp(6) null,
    dm_update_time  timestamp(6) null default pg_systimestamp(),
    dm_load_time    timestamp(6) null default pg_systimestamp(),
    primary key (sr_id,i_code, rec_dt)
) with (
    orientation=row,
    compression=no
)
partition by range (rec_dt) (     -- Yearly partition by effective start date for data management
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
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.b_storage       is 'B Water Storage ';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.b_storage       is 'B Water Storage ';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.tot_storage     is 'Total Volume Of Water In A+ B+..+R.  Unit Is In Cu M';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.qty_del         is 'Qty Del';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.rec_dt          is 'Rec Date';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.dm_update_time  is 'Dm Update Time';
comment on column coss_dm.dm_srs_daily_sr_wl_qty_item_di.dm_load_time    is 'Dm Load Time';

```

### select sql

```sql
create table if not exists  coss_dm.dm_srs_daily_sr_wl_qty_item_stg_di (
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
    a_storage       numeric(20, 5) null,
    b_storage       numeric(20, 5) null,
  	tot_storage     numeric(20, 5) null,
    qty_del         numeric(20, 5) null,
    rec_dt          timestamp(6) null,
    dm_update_time  timestamp(6) null default pg_systimestamp(),
    dm_load_time    timestamp(6) null default pg_systimestamp()
);

-- ****************************************************************************************
-- Subject     Areas: Service Reservoir Supply
-- Function Describe: Service Reservoir Water Level And Quantity
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dwd.dwd_srs_sr_storage_detail_di_year
-- coss_dwd.dwd_rws_channel_flow_detail_di_year
-- coss_dim.dim_sr_installation_info
-- Target Table:
-- coss_dm.dm_srs_daily_sr_wl_qty_item_di
-- ****************************************************************************************

with t_b as (
    select
        t.sr_id,
        t.a_wl,
        t.b_wl,
        t.a_storage,
        t.b_storage,
  		t.tot_storage,
        t1.qty_del,
        t.rec_dt
    from (
        select
            sr_id,
            a_wl,
            b_wl,
            a_storage,
            b_storage,
  		    tot_storage,
            rec_dt
        from coss_dwd.dwd_srs_sr_storage_detail_di_year
          where rec_dt >= '${rec_dt}'
    ) t
    left join (
        select
            src_id,
            rec_dt,
            sum(qty_del) as qty_del
        from coss_dwd.dwd_rws_channel_flow_detail_di_year
        where left(src_id, 2) = 'SR'
          and qty_del is not null
          and qty_del > 0
         and rec_dt > '${rec_dt}'
        group by
            src_id,
            rec_dt
    ) t1 on t.sr_id = t1.src_id and t.rec_dt = t1.rec_dt
)
insert into  coss_dm.dm_srs_daily_sr_wl_qty_item_stg_di
(
	sr_id,
	i_code,
	sr_name,
	sr_cname,
	rpt_label,
	region_code,
	sub_region,
	region_name,
	region_cname,
	region_ind,
	w_type,
	w_type_desc,
	a_wl,
	b_wl,
	a_storage,
	b_storage,
	tot_storage,
	qty_del,
	rec_dt,
	dm_update_time,
	dm_load_time
)
select
    t1.sr_id,                     -- Service Reservoir Id
    t1.i_code,                     -- Installation Code
    t1.sr_name,                     -- Service Reservoir Name En
    t1.sr_cname,                     -- Service Reservoir Name Tc
    t1.rpt_label,                     -- Report Label
    t1.region_code,                     -- Region Code
    t1.sub_region,                     -- Sub Region
    t1.region_name,                     -- Region Name En
    t1.region_cname,                     -- Region Name Tc
    t1.region_ind,                     -- Region Ind
    t1.w_type,                     -- Water Type
    t1.w_type_desc,                     -- Water Type Describe
    t.a_wl,                      -- A Water Level
    t.b_wl,                      -- B Water level
    t.a_storage,                      -- A Water Storage
    t.b_storage,                      -- B Water Storage
    t.tot_storage,
    t.qty_del,                      -- Qty Del
    t.rec_dt,                      -- Rec Date
    current_timestamp dm_update_time,      -- Dm Update Time
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
    b_wl,                 -- B Water level
    a_storage,            -- A Water Storage
    b_storage,            -- B Water Storage
    tot_storage,          -- Total Volume Of Water In A+ B+..+R.  Unit Is In Cu M
    qty_del,              -- Qty Del
    rec_dt,               -- Rec Date
    dm_update_time,       -- Dm Update Time
    dm_load_time          -- Dm Load Time
from
     coss_dm.dm_srs_daily_sr_wl_qty_item_stg_di
on duplicate key update
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
    a_storage = values(a_storage),
    b_storage = values(b_storage),
    tot_storage = values(tot_storage),
    qty_del = values(qty_del),
    dm_update_time = values(dm_update_time);
```

## 2.coss_dm.dm_srs_monthly_sr_qty_di

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
-- Subject     Areas: Service Reservoir Supply
-- Function Describe: Service Reservoir Water Quantity
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dwd.dwd_rws_channel_flow_detail_di_year
-- coss_dim.dim_sr_installation_qty_info
-- Target Table:
-- coss_dm.dm_srs_monthly_sr_qty_di
-- ****************************************************************************************
insert into coss_dm.dm_srs_monthly_sr_qty_di
select
    round(t.dt / 100) as statistical_month,  -- Statistical Month
    t1.sr_id as sr_id,                        -- Service Reservoir Id
    t1.i_code as i_code,                      -- Installation Code
    t1.sr_name_en as sr_name_en,              -- Service Reservoir Name
    t1.sr_name_tc as sr_name_tc,              -- Service Reservoir Name Tc
    t1.rpt_label as rpt_label,                -- Report Label
    t1.region_abbr as region_abbr,            -- Region Abbr
    t1.sub_region as sub_region,              -- Sub Region
    ifnull(sum(t.qty_del), 0) as qty_del,     -- Quantity Deliver
    current_timestamp as dm_update_time,      -- Dm Update Time
    current_timestamp as dm_load_time         -- Dm Load Time
from coss_dwd.dwd_rws_channel_flow_detail_di_year t
inner join coss_dim.dim_sr_installation_qty_info t1 on t.src_id = t1.sr_id
  where rec_dt >= '${rec_dt}'
group by
    t1.sr_id,
    round(t.dt / 100)
on duplicate key update
    i_code = values(i_code),
    sr_name_en = values(sr_name_en),
    sr_name_tc = values(sr_name_tc),
    rpt_label = values(rpt_label),
    region_abbr = values(region_abbr),
    sub_region = values(sub_region),
    qty_del = values(qty_del),
    dm_update_time = values(dm_update_time);
```



## 3.coss_dm.dm_srs_annual_sr_pool_stopped_di(STG)

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
create table if not exists coss_dm.dm_srs_annual_sr_pool_stopped_stg_di (
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


-- ****************************************************************************************
-- Subject     Areas: Service Reservoir Supply
-- Function Describe: Service Reservoir Water Pool Stopped
-- Create         By: dongmaochen
-- Create       Date: 2025-11-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_dwd.dwd_srs_sr_storage_detail_di_year
-- coss_dim.dim_sr_installation_info
-- Target Table:
-- coss_dm.dm_srs_annual_sr_pool_stopped_di
-- ****************************************************************************************

with t_a as (
    select
        sr_id,
        round(dt / 10000) as yr, 
        count(distinct rec_dt) as days_num  
    from coss_dwd.dwd_srs_sr_storage_detail_di_year
    where a_wl = 0
      and a_wl is not null
      and rec_dt >= '${rec_dt}'
    group by
        sr_id,
        yr
), t_b as (
    select
        sr_id,
        round(dt / 10000) as yr,  
        count(distinct rec_dt) as days_num  
    from coss_dwd.dwd_srs_sr_storage_detail_di_year
    where b_wl = 0
      and b_wl is not null
      and rec_dt >= '${rec_dt}'
    group by
        sr_id,
        yr
)

insert into coss_dm.dm_srs_annual_sr_pool_stopped_stg_di
select
    t.yr as statistical_year,                       -- Statistical Year                                 
    t1.sr_id as sr_id,                             -- Service Reservoir Id    
    t1.i_code as i_code,                           -- Installation Code     
    t1.sr_name as sr_name_en,                      -- Service Reservoir Name EN                    
    t1.sr_cname as sr_name_tc,                     -- Service Reservoir Name Tc                     
    t1.rpt_label as rpt_label,                     -- Report Label        
    t1.region_code as region_abbr,                 -- Region Abbr                         
    t1.sub_region as sub_region,                   -- Sub Region          
    t.a_stoped as a_stoped,                        -- Number of Days When Pool A Is Stopped    
    t.b_stoped as b_stoped,                        -- Number of Days When Pool B Is Stopped    
    current_timestamp as dm_update_time,           -- Dm Update Time                               
    current_timestamp as dm_load_time              -- Dm Load Time                              
from
(
    select
        ifnull(t.sr_id, t1.sr_id) as sr_id,  
        ifnull(t.yr, t1.yr) as yr,          
        ifnull(t.days_num, 0) as a_stoped, 
        ifnull(t1.days_num, 0) as b_stoped 
    from t_a t
    full join t_b t1 on t.sr_id = t1.sr_id and t.yr = t1.yr
) as t
inner join coss_dim.dim_sr_installation_info t1 on t.sr_id = t1.sr_id;

insert into coss_dm.dm_srs_annual_sr_pool_stopped_di
select
    statistical_year,      -- Statistical Year                                 
    sr_id,                 -- Service Reservoir Id    
    i_code,                -- Installation Code     
    sr_name_en,            -- Service Reservoir Name EN                    
    sr_name_tc,            -- Service Reservoir Name Tc                     
    rpt_label,             -- Report Label        
    region_abbr,           -- Region Abbr                         
    sub_region,            -- Sub Region          
    a_stoped,              -- Number of Days When Pool A Is Stopped    
    b_stoped,              -- Number of Days When Pool B Is Stopped    
    dm_update_time,        -- Dm Update Time                               
    dm_load_time           -- Dm Load Time                              
from
    coss_dm.dm_srs_annual_sr_pool_stopped_stg_di
on duplicate key update
    i_code = values(i_code),
    sr_name_en = values(sr_name_en),
    sr_name_tc = values(sr_name_tc),
    rpt_label = values(rpt_label),
    region_abbr = values(region_abbr),
    sub_region = values(sub_region),
    a_stoped = values(a_stoped),
    b_stoped = values(b_stoped),
    dm_update_time = values(dm_update_time); 
```

## coss_dm.dm_srs_region_year_kpi_dip

> 还没上调度

### create table

```sql
drop table if exists coss_dm.dm_srs_region_year_kpi_dip;
CREATE TABLE if not exists coss_dm.dm_srs_region_year_kpi_dip (
	id varchar(42) NULL,
	region varchar(200) NULL,
	item_code varchar(200) NULL,
	item_name varchar(300) NULL,
	item_value numeric(20, 5) NULL,
	"unit" varchar(50) NULL,
	etl_time timestamp(6) NULL,
    dm_update_time  timestamp(6) default current_timestamp,
    dm_load_time  timestamp(6) default current_timestamp,
	yr numeric(10) NULL
)
WITH (
	orientation=row,
	compression=no
);

```

### select sql 

325.68



```sql
insert into  coss_dm.dm_srs_region_year_kpi_dip
select
  uuid()                               as id
  ,'HKSAR'                             as region
  ,'bi_p_216'                          as item_code
  ,'Service Reservoir Supply Volume'   as item_name
  ,qty_del                             as item_value
  ,'MCM'                               as unit
  ,current_timestamp                 as etl_time
  ,current_timestamp                 as dm_update_time
  ,current_timestamp                 as dm_load_time
  ,t.yr                                as yr
from (
select
  sum(qty_del)/1000     as qty_del,      -- convert Mld to mcm
  round(dt/10000,0)    as yr
from coss_dws.dws_srs_sr_storage_detail_di_year
where w_type = 'F' and qty_del is not null
group by
  yr) t
  
union all
select
  uuid()                             as id
  ,t.region                          as region
  ,'bi_p_217'                        as item_code
  ,'Service Reservoir Supply Volume' as item_name
  ,qty_del                           as item_value
  ,'MCM'                             as unit
  ,current_timestamp                 as etl_time
  ,current_timestamp                 as dm_update_time
  ,current_timestamp                 as dm_load_time
  ,t.yr                              as yr
from (
select
  region_code        as region,
  sum(qty_del)/1000 as qty_del,         -- convert Mld to mcm
  round(dt/10000,0) as yr
from coss_dws.dws_srs_sr_storage_detail_di_year
where w_type = 'F' and qty_del is not null
group by
  region_code,
  yr) t
on duplicate key update 
    item_value = values(item_value),
    dm_update_time = values(dm_update_time)
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
    is_qty           int null,
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
comment on column coss_dim.dim_sr_installation_info.is_qty          is 'Is Water Output Quantity 1 Is True 0 Is False';
comment on column coss_dim.dim_sr_installation_info.dim_update_time is 'Dim Update Time';
comment on column coss_dim.dim_sr_installation_info.dim_load_time   is 'Dim Load Time ';
```

## 2.coss_dim.dim_sr_installation_qty_info{这张维表先删除}

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



## 3.coss_dim.dim_ass_sr_qty_del_info

### create table

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Assets
-- Function Describe: Service Reservoir Information
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  coss_ods.ods_sttss_rws_sr_df, coss_ods.ods_sttss_rws_region_df, coss_ods.ods_sttss_rws_w_type_df
-- Target Table:  coss_dim.dim_ass_sr_qty_del_info
-- ****************************************************************************************
-- 1. Delete target table if it exists to avoid table structure conflict
drop table if exists coss_dim.dim_ass_sr_qty_del_info;

-- 2. Create target table: Store service reservoir quantity delivery info, including basic attributes, region/water type dimensions
create table if not exists coss_dim.dim_ass_sr_qty_del_info (
    sr_id             varchar(20),        -- Service Reservoir ID with format SRNNNNNNNN
    i_code            varchar(10),        -- Installation Code of Service Reservoir
    sr_name           varchar(200),       -- Service Reservoir Name
    sr_cname          varchar(300),       -- Service Reservoir Chinese Name
    rpt_label         varchar(400),       -- Labels used in reports
    region_code       varchar(5),         -- Region
    region_name       varchar(60),        -- Description of Region
    region_cname      varchar(300),       -- Chinese Description of Region
    region_ind        varchar(2),         -- Possible Values: {"I" - HK Island, "M" - Mainland}
    w_type            varchar(2),         -- Type of water maintained by the service reservoir
    w_type_desc       varchar(200),       -- Description of Water Type
    div_height        decimal(12, 4),     -- Height of Division Wall.  Unit is in m
    capacity          decimal(12, 4),     -- Capacity of Service Reservoir.  Unit is in cu m
    w_lim             decimal(12, 4),     -- Preset Limit for Water Level above division wall.  Unit is in m
    num_of_storage    decimal(10),        -- No. of Storage/Compartment
    dim_update_time   timestamp(6) default current_timestamp,
    dim_load_time     timestamp(6) default current_timestamp,
    primary key (sr_id)
);

-- 3. Table comment: Explain business meaning for maintenance
comment on table coss_dim.dim_ass_sr_qty_del_info is 'Service Reservoir Information';

-- 4. Column comments: Clarify each field's business meaning (first letter uppercase)
comment on column coss_dim.dim_ass_sr_qty_del_info.sr_id             is 'Service Reservoir ID With Format SRNNNNNNNN';
comment on column coss_dim.dim_ass_sr_qty_del_info.i_code            is 'Installation Code Of Service Reservoir';
comment on column coss_dim.dim_ass_sr_qty_del_info.sr_name           is 'Service Reservoir Name';  -- Fix extra space in original comment
comment on column coss_dim.dim_ass_sr_qty_del_info.sr_cname          is 'Service Reservoir Chinese Name';
comment on column coss_dim.dim_ass_sr_qty_del_info.rpt_label         is 'Labels Used In Reports';
comment on column coss_dim.dim_ass_sr_qty_del_info.region_code       is 'Region';
comment on column coss_dim.dim_ass_sr_qty_del_info.region_name       is 'Description Of Region';
comment on column coss_dim.dim_ass_sr_qty_del_info.region_cname      is 'Chinese Description Of Region';
comment on column coss_dim.dim_ass_sr_qty_del_info.region_ind        is 'Possible Values: {"I" - HK Island, "M" - Mainland}';
comment on column coss_dim.dim_ass_sr_qty_del_info.w_type            is 'Type Of Water Maintained By The Service Reservoir';
comment on column coss_dim.dim_ass_sr_qty_del_info.w_type_desc       is 'Description Of Water Type';
comment on column coss_dim.dim_ass_sr_qty_del_info.div_height        is 'Height Of Division Wall.  Unit Is In M';
comment on column coss_dim.dim_ass_sr_qty_del_info.capacity          is 'Capacity Of Service Reservoir.  Unit Is In Cu M';
comment on column coss_dim.dim_ass_sr_qty_del_info.w_lim             is 'Preset Limit For Water Level Above Division Wall.  Unit Is In M';
comment on column coss_dim.dim_ass_sr_qty_del_info.num_of_storage    is 'No. Of Storage/Compartment';
comment on column coss_dim.dim_ass_sr_qty_del_info.dim_update_time   is 'Data Update Time';
comment on column coss_dim.dim_ass_sr_qty_del_info.dim_load_time     is 'Data Loading Time';

```

### select sql

```sql
insert into coss_dim.dim_ass_sr_qty_del_info
select
*
from 
coss_dim.dim_ass_sr_df
where sr_id in (
'SR00000346',
'SR00000147',
'SR00000191',
'SR00000026',
'SR00000040',
'SR00000022',
'SR00000172',
'SR00000035',
'SR00000196',
'SR00000180',
'SR00000023',
'SR00000298',
'SR00000093',
'SR00000210',
'SR00000175',
'SR00000154',
'SR00000294',
'SR00000020',
'SR00000395',
'SR00000329',
'SR00000062',
'SR00000369',
'SR00000017',
'SR00000061',
'SR00000080',
'SR00000396',
'SR00000053',
'SR00000378',
'SR00000047',
'SR00000052',
'SR00000332',
'SR00000108'
)
```





### coss_dim.dim_ig_info

```sql
drop table if exists coss_dim.dim_ig_info;

create table if not exists coss_dim.dim_ig_info (
	ig_id varchar(20) not null, -- Impounding Reservoir Group Id With Format IGnnnnnnn
	region_abbr varchar(10) null, -- Region Abbr
	ig_name_en varchar(200) null, -- English Name Of Impounding Reservoir Group
	ig_name_cn varchar(300) null, -- Simplified Name Of Impounding Reservoir Group
	ig_name_tc varchar(300) null, -- Traditional Name Of Impounding Reservoir Group
	dim_update_time timestamp(6) null default current_timestamp, -- Data Update Time
	dim_load_time timestamp(6) null default current_timestamp, -- Data Loading Time
  primary key (ig_id)
)
with (
	orientation=row,
	compression=no
);

comment on table coss_dim.dim_ig_info is 'Impounding Reservoir Group Information';
comment on column coss_dim.dim_ig_info.ig_id is 'Impounding Reservoir Group Id With Format IGnnnnnnn';
comment on column coss_dim.dim_ig_info.region_abbr is 'Region Abbr';
comment on column coss_dim.dim_ig_info.ig_name_en is 'English Name Of Impounding Reservoir Group';
comment on column coss_dim.dim_ig_info.ig_name_cn is 'Simplified Name Of Impounding Reservoir Group';
comment on column coss_dim.dim_ig_info.ig_name_tc is 'Traditional Name Of Impounding Reservoir Group';
comment on column coss_dim.dim_ig_info.dim_update_time is 'Data Update Time';
comment on column coss_dim.dim_ig_info.dim_load_time is 'Data Loading Time';
```



### coss_dim.dim_ir_info

```sql
drop table if exists coss_dim.dim_ir_info;

create table coss_dim.dim_ir_info (
    ig_id                varchar(20) not null,        -- Impounding Reservoir Group Id With Format Ignnnnnnnn
    ig_name_en           varchar(200) null,           -- English Name Of Impounding Reservoir Group
    ig_name_cn           varchar(300) null,           -- Simplified Name Of Impounding Reservoir Group
    ig_name_tc           varchar(300) null,           -- Traditional Name Of Impounding Reservoir Group
    region_abbr          varchar(10) null,            -- Region Abbr
    ir_id                varchar(20) not null,        -- Impounding Reservoir Id With Format Irnnnnnnnn
    installation_id      varchar(10) null,            -- Installation Code Of Impounding Reservoir
    ir_name_en           varchar(200) null,           -- Impounding Reservoir English Name
    ir_name_cn           varchar(300) null,           -- Impounding Reservoir Simplified Name
    ir_name_tc           varchar(300) null,           -- Impounding Reservoir Traditional Name
    capacity             numeric(12, 4) null,         -- Capacity Of Impounding Reservoir.  Unit Is In Mcm
    min_storage          numeric(12, 4) null,         -- Allowable Minimum Storage Of Impounding Reservoir.  Unit Is In Mcm
    limit_m              numeric(12, 4) null,         -- Preset Limit For Water Level.  Unit Is In M
    dim_update_time      timestamp(6) null default pg_systimestamp(),  -- Data Update Time
    dim_load_time        timestamp(6) null default pg_systimestamp(),  -- Data Loading Time
    
    constraint dim_ir_info_pkey primary key (ig_id, ir_id)
)
with (
    orientation = row,
    compression = no
);
comment on table coss_dim.dim_ir_info is 'Impounding Reservoir Information';
comment on column coss_dim.dim_ir_info.ig_id is 'Impounding Reservoir Group Id With Format Ignnnnnnnn';
comment on column coss_dim.dim_ir_info.ig_name_en is 'English Name Of Impounding Reservoir Group';
comment on column coss_dim.dim_ir_info.ig_name_cn is 'Simplified Name Of Impounding Reservoir Group';
comment on column coss_dim.dim_ir_info.ig_name_tc is 'Traditional Name Of Impounding Reservoir Group';
comment on column coss_dim.dim_ir_info.region_abbr is 'Region Abbr';
comment on column coss_dim.dim_ir_info.ir_id is 'Impounding Reservoir Id With Format Irnnnnnnnn';
comment on column coss_dim.dim_ir_info.installation_id is 'Installation Code Of Impounding Reservoir';
comment on column coss_dim.dim_ir_info.ir_name_en is 'Impounding Reservoir English Name';
comment on column coss_dim.dim_ir_info.ir_name_cn is 'Impounding Reservoir Simplified Name';
comment on column coss_dim.dim_ir_info.ir_name_tc is 'Impounding Reservoir Traditional Name';
comment on column coss_dim.dim_ir_info.capacity is 'Capacity Of Impounding Reservoir.  Unit Is In Mcm';
comment on column coss_dim.dim_ir_info.min_storage is 'Allowable Minimum Storage Of Impounding Reservoir.  Unit Is In Mcm';
comment on column coss_dim.dim_ir_info.limit_m is 'Preset Limit For Water Level.  Unit Is In M';
comment on column coss_dim.dim_ir_info.dim_update_time is 'Data Update Time';
comment on column coss_dim.dim_ir_info.dim_load_time is 'Data Loading Time';
```

### dm_rws_daily_ig_flow_di

```sql
drop table if exists coss_dm.dm_rws_daily_ig_flow_di;
create table if not exists coss_dm.dm_rws_daily_ig_flow_di (
	ig_id varchar(20) not null, -- Impounding Reservoir Group Id With Format IGnnnnnnn
	region_abbr varchar(10) null, -- Region Abbr
	ig_name_en varchar(200) null, -- English Name Of Impounding Reservoir Group
	ig_name_cn varchar(300) null, -- Simplified Name Of Impounding Reservoir Group
	ig_name_tc varchar(300) null, -- Traditional Name Of Impounding Reservoir Group
	inflow numeric(12,4) null, -- Inflow  Unit: MLD
	outflow numeric(12,4) null, -- Outflow Unit: MLD
	rec_dt timestamp(6) not null, -- Record Date
	dm_load_time timestamp(6) null default current_timestamp, -- Load Time
	dm_update_time timestamp(6) null default current_timestamp, -- Update Time
	primary key (ig_id, rec_dt)
)
with (
	orientation=row,
	compression=no
);

comment on table coss_dm.dm_rws_daily_ig_flow_di is 'Daily Impounding Reservoir Group Flow Information';

comment on column coss_dm.dm_rws_daily_ig_flow_di.ig_id is 'Impounding Reservoir Group Id With Format IGnnnnnnn';
comment on column coss_dm.dm_rws_daily_ig_flow_di.region_abbr is 'Region Abbr';
comment on column coss_dm.dm_rws_daily_ig_flow_di.ig_name_en is 'English Name Of Impounding Reservoir Group';
comment on column coss_dm.dm_rws_daily_ig_flow_di.ig_name_cn is 'Simplified Name Of Impounding Reservoir Group';
comment on column coss_dm.dm_rws_daily_ig_flow_di.ig_name_tc is 'Traditional Name Of Impounding Reservoir Group';
comment on column coss_dm.dm_rws_daily_ig_flow_di.inflow is 'Inflow Unit: MLD';
comment on column coss_dm.dm_rws_daily_ig_flow_di.outflow is 'Outflow Unit: MLD';
comment on column coss_dm.dm_rws_daily_ig_flow_di.rec_dt is 'Record Date';
comment on column coss_dm.dm_rws_daily_ig_flow_di.dm_load_time is 'Load Time';
comment on column coss_dm.dm_rws_daily_ig_flow_di.dm_update_time is 'Update Time';

```











```
    where  t.dwd_update_time >= '${dws_update_time}'
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



# 中间表

```sql
create table if not exists coss_ods.ods_sttss_srs_sr_storage_stg_di(
    "sr_id"            varchar(20),       -- Service Reservior being referenced
    "a_wlevel"         decimal(9, 2),     -- A Compartment Water Level
    "b_wlevel"         decimal(9, 2),     -- B Compartment Water Level
    "c_wlevel"         decimal(9, 2),     -- C Compartment Water Level
    "d_wlevel"         decimal(9, 2),     -- D Compartment Water Level
    "e_wlevel"         decimal(9, 2),     -- E Compartment Water Level
    "f_wlevel"         decimal(9, 2),     -- F Compartment Water Level
    "g_wlevel"         decimal(9, 2),     -- G Compartment Water Level
    "h_wlevel"         decimal(9, 2),     -- H Compartment Water Level
    "i_wlevel"         decimal(9, 2),     -- I Compartment Water Level
    "j_wlevel"         decimal(9, 2),     -- J Compartment Water Level
    "k_wlevel"         decimal(9, 2),     -- K Compartment Water Level
    "l_wlevel"         decimal(9, 2),     -- L Compartment Water Level
    "m_wlevel"         decimal(9, 2),     -- M Compartment Water Level
    "n_wlevel"         decimal(9, 2),     -- N Compartment Water Level
    "o_wlevel"         decimal(9, 2),     -- O Compartment Water Level
    "p_wlevel"         decimal(9, 2),     -- P Compartment Water Level
    "q_wlevel"         decimal(9, 2),     -- Q Compartment Water Level
    "r_wlevel"         decimal(9, 2),     -- R Compartment Water Level
    "scada_a_wlevel"   decimal(9, 2),     -- A Compartment Water Level (SCADA)
    "scada_b_wlevel"   decimal(9, 2),     -- B Compartment Water Level (SCADA)
    "scada_c_wlevel"   decimal(9, 2),     -- C Compartment Water Level (SCADA)
    "scada_d_wlevel"   decimal(9, 2),     -- D Compartment Water Level (SCADA)
    "scada_e_wlevel"   decimal(9, 2),     -- E Compartment Water Level (SCADA)
    "scada_f_wlevel"   decimal(9, 2),     -- F Compartment Water Level (SCADA)
    "scada_g_wlevel"   decimal(9, 2),     -- G Compartment Water Level (SCADA)
    "scada_h_wlevel"   decimal(9, 2),     -- H Compartment Water Level (SCADA)
    "scada_i_wlevel"   decimal(9, 2),     -- I Compartment Water Level (SCADA)
    "scada_j_wlevel"   decimal(9, 2),     -- J Compartment Water Level (SCADA)
    "scada_k_wlevel"   decimal(9, 2),     -- K Compartment Water Level (SCADA)
    "scada_l_wlevel"   decimal(9, 2),     -- L Compartment Water Level (SCADA)
    "scada_m_wlevel"   decimal(9, 2),     -- M Compartment Water Level (SCADA)
    "scada_n_wlevel"   decimal(9, 2),     -- N Compartment Water Level (SCADA)
    "scada_o_wlevel"   decimal(9, 2),     -- O Compartment Water Level (SCADA)
    "scada_p_wlevel"   decimal(9, 2),     -- P Compartment Water Level (SCADA)
    "scada_q_wlevel"   decimal(9, 2),     -- Q Compartment Water Level (SCADA)
    "scada_r_wlevel"   decimal(9, 2),     -- R Compartment Water Level (SCADA)
    "a_storage"        decimal(12, 4),    -- Volume of water in A compartment of an SR.  Unit is in cu m
    "b_storage"        decimal(12, 4),    -- Volume of water in B compartment of an SR.  Unit is in cu m
    "c_storage"        decimal(12, 4),    -- Volume of water in C compartment of an SR.  Unit is in cu m
    "d_storage"        decimal(12, 4),    -- Volume of water in D compartment of an SR.  Unit is in cu m
    "e_storage"        decimal(12, 4),    -- Volume of water in E compartment of an SR.  Unit is in cu m
    "f_storage"        decimal(12, 4),    -- Volume of water in F compartment of an SR.  Unit is in cu m
    "g_storage"        decimal(12, 4),    -- Volume of water in G compartment of an SR.  Unit is in cu m
    "h_storage"        decimal(12, 4),    -- Volume of water in H compartment of an SR.  Unit is in cu m
    "i_storage"        decimal(12, 4),    -- Volume of water in I compartment of an SR.  Unit is in cu m
    "j_storage"        decimal(12, 4),    -- Volume of water in J compartment of an SR.  Unit is in cu m
    "k_storage"        decimal(12, 4),    -- Volume of water in K compartment of an SR.  Unit is in cu m
    "l_storage"        decimal(12, 4),    -- Volume of water in L compartment of an SR.  Unit is in cu m
    "m_storage"        decimal(12, 4),    -- Volume of water in M compartment of an SR.  Unit is in cu m
    "n_storage"        decimal(12, 4),    -- Volume of water in N compartment of an SR.  Unit is in cu m
    "o_storage"        decimal(12, 4),    -- Volume of water in O compartment of an SR.  Unit is in cu m
    "p_storage"        decimal(12, 4),    -- Volume of water in P compartment of an SR.  Unit is in cu m
    "q_storage"        decimal(12, 4),    -- Volume of water in Q compartment of an SR.  Unit is in cu m
    "r_storage"        decimal(12, 4),    -- Volume of water in R compartment of an SR.  Unit is in cu m
    "tot_storage"      decimal(12, 4),    -- Total volume of water in A+ B+..+R.  Unit is in cu m
    "remarks"          varchar(2000),     -- Remarks
    "rec_dt"           timestamp(6),      -- Date of record
    "submit_dt"        timestamp(6),      -- Submission Date
    "last_upd_user"    varchar(120),      -- Last Update By (Username)
    "last_upd_post"    varchar(52),       -- Last Update By (Post)
    "last_upd_dt"      timestamp(6),      -- Last Update Date
    ods_update_time    timestamp(6) default current_timestamp,
    ods_load_time      timestamp(6) default current_timestamp,
    "dt"               decimal(10),        -- Daily Partitions
    primary key(sr_id, rec_dt)
)




create table if not exists coss_ods.ods_sttss_rws_ir_group_stg_df (
    ig_id          varchar(20),         -- Impounding Reservoir Group ID with format IGNNNNNNNN
    ig_name        varchar(200),        -- Name of Impounding Reservoir Group
    ig_cname       varchar(300),        -- Chinese Name of Impounding Reservoir Group
    rlabel         varchar(400),        -- Labels used in reports
    region         varchar(10),         -- Region
    old_ind        varchar(2),          -- Indicates if Impounding Reservoir Group is old or new. Possible Values: {"Y" - Old, "N" - New}
    last_upd_user  varchar(120),        -- Last Update By (Username)
    last_upd_post  varchar(52),         -- Last Update By (Post)
    last_upd_dt    timestamp(6),        -- Last Update Date
    ods_update_time timestamp(6) default current_timestamp,
    ods_load_time   timestamp(6) default current_timestamp,
    primary key (ig_id)
);


create table if not exists coss_ods.ods_sttss_rws_measurement_stg_df (
    "code"           varchar(20),    -- Defines how water level are measured
    "descrip"        varchar(200),   -- Description of Measurement
    "cdescrip"       varchar(300),   -- Chinese Description of Measurement Type
    "last_upd_user"  varchar(120),   -- Last Update By (Username)
    "last_upd_post"  varchar(60),    -- Last Update By (Post)
    "last_upd_dt"    timestamp(6),   -- Last Update Date
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("code")
);



create table if not exists coss_ods.ods_sttss_rws_ps_stg_di (
    "ps_id"          varchar(20),       -- Pumping Station ID with format PSNNNNNNNN
    "i_code"         varchar(10),       -- Installation Code of Pumping Station
    "rlabel"         varchar(400),      -- Labels used in reports
    "region"         varchar(10),       -- Region
    "w_type"         varchar(2),        -- Type of water maintained in the pumping station
    "repumping"      varchar(2),        -- Repumping
    "last_upd_user"  varchar(120),      -- Last Update By (Username)
    "last_upd_post"  varchar(52),       -- Last Update By (Post)
    "last_upd_dt"    timestamp(6),      -- Last Update Date
    "remark"         varchar(200),      -- Remarks
    "ps_name"        varchar(200),      -- Pumping station name
    "ps_cname"       varchar(300),      -- Pumping Station Chinese Name
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("ps_id")
);



create table if not exists coss_ods.ods_sttss_rws_region_stg_df (
    "code"           varchar(10),     -- Possible Values: {"HK" - HK Island, "K" - Kowloon, "NTE" -  New Territories East, "NTW" - New Territories West}
    "descrip"        varchar(60),     -- Description of Region
    "cdescrip"       varchar(300),    -- Chinese Description of Region
    "indicator"      varchar(2),      -- Possible Values: {"I" - HK Island, "M" - Mainland}
    "last_upd_user"  varchar(120),    -- Last Update By (Username)
    "last_upd_post"  varchar(52),     -- Last Update By (Post)
    "last_upd_dt"    timestamp(6),    -- Last Update Date
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("code")
);

create table if not exists coss_ods.ods_sttss_rws_rw_stg_df (
    "rw_id"          varchar(20),      -- Raw Water Source ID with format RWNNNNNNNN
    "rw_name"        varchar(200),     -- Name of Raw Water
    "rw_cname"       varchar(300),     -- Chinese Name of Raw Water
    "rlabel"         varchar(400),     -- Labels used in reports
    "region"         varchar(10),      -- Region
    "source"         varchar(2),       -- Source of raw water
    "last_upd_user"  varchar(120),     -- Last Update By (Username)
    "last_upd_post"  varchar(52),      -- Last Update By (Post)
    "last_upd_dt"    timestamp(6),     -- Last Update Date
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("rw_id")
);

create table if not exists coss_ods.ods_sttss_rws_rw_type_stg_df (
    "code"           varchar(4),     -- Possible Values:{"G" - Guangdong, "R" - River, "O" - Others}
    "descrip"        varchar(90),    -- Description of Raw Water Source
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("code")
);


create table if not exists coss_ods.ods_sttss_rws_sr_stg_di (
    "sr_id"           varchar(20),        -- Service Reservoir ID with format SRNNNNNNNN
    "i_code"          varchar(10),        -- Installation Code of Service Reservoir
    "rlabel"          varchar(400),       -- Labels used in reports
    "region"          varchar(10),        -- Region
    "w_type"          varchar(2),         -- Type of water maintained by the service reservoir
    "div_height"      decimal(12, 4),     -- Height of Division Wall.  Unit is in m
    "capacity"        decimal(12, 4),     -- Capacity of Service Reservoir.  Unit is in cu m
    "limit"           decimal(12, 4),     -- Preset Limit for Water Level above division wall.  Unit is in m
    "num_of_storage"  decimal,            -- No. of Storage/Compartment
    "last_upd_user"   varchar(120),       -- Last Update By (Username)
    "last_upd_post"   varchar(52),        -- Last Update By (Post)
    "last_upd_dt"     timestamp(6),       -- Last Update Date
    "sr_name"         varchar(200),       -- Service Reservoir Name
    "sr_cname"        varchar(300),       -- Service Reservoir Chinese Name
    ods_update_time   timestamp(6) default current_timestamp,
    ods_load_time     timestamp(6) default current_timestamp,
    primary key ("sr_id")
);

create table if not exists coss_ods.ods_sttss_rws_w_type_stg_df (
    code             varchar(4),             -- Possible Values{G - Guangdong, R - River, O - Others}
    descrip          varchar(90),            -- Description of Raw Water Source
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key (code)
);


create table if not exists coss_ods.ods_sttss_rws_water_usage_stg_df (
    "code"           decimal(3),        -- Code
    "descrip"        varchar(200),      -- Possible Values: {"Commissioning Test to Waste", "Commissioning Test to be Returned to System", "Augmented Supply for Flushing", Commission Test to be Used for Consumption}
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("code")
);

create table if not exists coss_ods.ods_sttss_rws_wtw_stg_df (
    "tw_id"          varchar(20),       -- Water Treatment Woks ID with format TWNNNNNNNN
    "i_code"         varchar(10),       -- Installation Code of Water Treatment Works
    "rlabel"         varchar(400),      -- Labels used in reports
    "region"         varchar(10),       -- Region
    "capacity"       decimal(12, 4),    -- Capacity of WTW.  Unit is in Mld
    "last_upd_user"  varchar(120),      -- Last Update By (Username)
    "last_upd_post"  varchar(52),       -- Last Update By (Post)
    "last_upd_dt"    timestamp(6),      -- Last Update Date
    "tw_name"        varchar(200),      -- Water Treatment Works Name
    "tw_cname"       varchar(300),      -- Water Treatment Works Chinese Name
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("tw_id")
);


============================dwd==================================================================

create table if not exists coss_dwd.dwd_ass_channels_stg_df (
    option_no        decimal(10),         -- Option No.
    ch_id            varchar(20),         -- System generated ID of a water transfer channel
    src_id           varchar(20),         -- Source of Water Inflow
    dest_id          varchar(20),         -- Destination of Water outflow
    rlabel           varchar(2000),       -- Labels used in reports
    w_usage          decimal(3),          -- Water Usage
    w_usage_desc     varchar(200),        -- Possible Values: {"Commissioning Test to Waste", "Commissioning Test to be Returned to System", "Augmented Supply for Flushing", Commission Test to be Used for Consumption}
    w_type           varchar(2),          -- Type of water maintained by the installation
    w_type_desc      varchar(200),        -- Description of Water Type
    calc_id          decimal(10),         -- Calculation logic being referenced by daily water transfer volume of channels
    calc_usage       varchar(2),          -- Determines if the referenced Channel or Internal Circulation is used as summation or difference Possible Values:{"S" - Sum, "D" - Difference}
    meas_code        varchar(20),         -- Measured By
    meas_desc        varchar(200),        -- Description of Measurement
    meas_cdesc       varchar(300),        -- Chinese Description of Measurement Type
    dwd_update_time  timestamp(6) default current_timestamp,
    dwd_load_time    timestamp(6) default current_timestamp,
    primary key (option_no, ch_id, src_id, dest_id)
) ;



create table if not exists coss_dwd.dwd_ass_rw_src_stg_df (
    rw_id            varchar(20),         -- Raw Water Source ID with format RWNNNNNNNN
    rw_name          varchar(200),        -- Name of Raw Water
    rw_cname         varchar(300),        -- Chinese Name of Raw Water
    rpt_label        varchar(400),        -- Labels used in reports
    region_code      varchar(10),         -- Region Code
    region_name      varchar(60),         -- Description of Region
    region_cname     varchar(300),        -- Chinese Description of Region
    region_ind       varchar(2)   ,          -- Possible Values: {"I" - HK Island, "M" - Mainland}
    ig_ind           varchar(2),          -- Indicates if Impounding Reservoir Group is old or new. Possible Values: {"Y" - Old, "N" - New}
    source_rw        varchar(2),          -- Source of raw water
    source_desc      varchar(60),         -- Description of Raw Water Source
    dwd_update_time  timestamp(6) default current_timestamp,
    dwd_load_time    timestamp(6) default current_timestamp,
    primary key (rw_id)
) ;




create table if not exists coss_dws.dws_rws_rw_supply_detail_stg_di (
    rw_id                   varchar(20),         -- Raw Water Source ID with format RWNNNNNNNN
    rw_name                 varchar(200),        -- Name of Raw Water
    rw_cname                varchar(300),        -- Chinese Name of Raw Water
    rpt_label               varchar(400),        -- Labels used in reports
    region_code             varchar(10),         -- Region Code
    region_name             varchar(60),         -- Description of Region
    region_cname            varchar(300),        -- Chinese Description of Region
    region_ind              varchar(2),          -- Possible Values: {"I" - HK Island, "M" - Mainland}
    ig_ind                  varchar(2),          -- Indicates if Impounding Reservoir Group is old or new. Possible Values: {"Y" - Old, "N" - New}
    source_rw               varchar(2),          -- Source of raw water
    source_desc             varchar(60),         -- Description of Raw Water Source
    p_qty                   decimal(12, 4),      -- Proposed Quantity.  Unit is Mld
    qty_del                 decimal(12, 4),      -- Quantity delivered of Water transfer channel. Unit is in Mld
    present_storage         decimal(16, 8),      -- Storage of water in IR At Present.  Unit is Mld
    capacity                decimal(12, 4),      -- Capacity of IR.  Unit is Mld
    min_storage             decimal(12, 4),      -- Allowable Minimum Storage.  Unit is Mld
    rec_dt                  timestamp(6),        -- Date of Record
    dws_update_time         timestamp(6) default current_timestamp,
    dws_load_time           timestamp(6) default current_timestamp,
    dt                      decimal(10),         -- Daily Partitions
    primary key (rw_id, rec_dt)  -- Composite PK: Ensure unique supply record per raw water source-date
);



create table if not exists coss_dws.dws_srs_sr_storage_detail_stg_di (
    sr_id             varchar(20),        -- Service Reservoir ID with format SRNNNNNNNN
    i_code            varchar(10),        -- Installation Code of Service Reservoir
    sr_name           varchar(200),       -- Service Reservoir Name
    sr_cname          varchar(300),       -- Service Reservoir Chinese Name
    rpt_label         varchar(400),       -- Labels used in reports
    region_code       varchar(10),        -- Region
    region_name       varchar(60),        -- Description of Region
    region_cname      varchar(300),       -- Chinese Description of Region
    region_ind        varchar(2),         -- Possible Values: {"I" - HK Island, "M" - Mainland}
    w_type            varchar(2),         -- Type of water maintained by the service reservoir
    w_type_desc       varchar(200),       -- Description of Water Type
    div_height        decimal(12, 4),     -- Height of Division Wall.  Unit is in m
    capacity          decimal(12, 4),     -- Capacity of Service Reservoir.  Unit is in cum
    w_lim             decimal(12, 4),     -- Preset Limit for Water Level above division wall.  Unit is in m
    num_of_storage    decimal,            -- No. of Storage/Compartment (add length if needed: e.g., decimal(10))
    a_wl              decimal(9, 2),      -- A Compartment Water Level
    b_wl              decimal(9, 2),      -- B Compartment Water Level
    a_storage         decimal(12, 4),     -- Volume of water in A compartment of an SR.  Unit is in cu m
    b_storage         decimal(12, 4),     -- Volume of water in B compartment of an SR.  Unit is in cu m
    tot_storage       decimal(12, 4),     -- Total volume of water in A+ B+..+R.  Unit is in cu m
    qty_del           decimal(12, 4),     -- Quantity delivered of Water transfer channel. Unit is in Mld
    p_qty             decimal(12, 4),     -- Proposed Quantity.  Unit is in Mld
    remarks           varchar(1000),      -- Remarks
    rec_dt            timestamp(6),       -- Date of record
    dws_update_time   timestamp(6) default current_timestamp,
    dws_load_time     timestamp(6) default current_timestamp,
    dt                decimal(10),        -- Daily Partitions
    primary key (sr_id, rec_dt)  -- Composite PK: Ensure unique record per service reservoir-date
);





 DROP TABLE coss_dm.dm_rws_daily_rw_yield_stg_di;

CREATE TABLE coss_dm.dm_rws_daily_rw_yield_stg_di (
	id varchar(50) NULL,
	statistical_day numeric(20) NOT NULL,
	island_change_storage numeric(20, 5) NULL,
	mainland_change_storage numeric(20, 5) NULL,
	total_change_storage numeric(20, 5) NULL,
	island_current_storage numeric(20, 5) NULL,
	island_design_storage numeric(20, 5) NULL,
	mainland_current_storage numeric(20, 5) NULL,
	mainland_design_storage numeric(20, 5) NULL,
	total_current_storage numeric(20, 5) NULL,
	total_design_storage numeric(20, 5) NULL,
	island_yield numeric(20, 5) NULL,
	mainland_yield numeric(20, 5) NULL,
	total_local_yield numeric(20, 5) NULL,
	dj_yield numeric(20, 5) NULL,
	total_yield numeric(20, 5) NULL,
	PRIMARY KEY (statistical_day)
);




create table if not exists coss_dm.dm_rws_daily_ir_storage_yield_stg_di (
    id varchar(50) null,
    rw_id varchar(50) null,
    rw_name varchar(50) null,
    rw_cname varchar(50) null,
    rpt_label varchar(50) null,
    region_code varchar(50) null,
    region_name varchar(100) null,
    region_cname varchar(200) null,
    region_ind varchar(50) null,
    ig_ind varchar(50) null,
    yield numeric(20, 5) null,
    current_storage numeric(20, 5) null,
    design_storage numeric(20, 5) null,
    change_storage numeric(20, 5) null,
    dt numeric(10) null,
    dm_update_time timestamp(6) null default pg_systimestamp(), -- Data Update Time
    dm_load_time timestamp(6) null default pg_systimestamp(), -- Data Loading Time
    primary key (rw_id, dt)
);

```





# 新增指标：

```sql


-- 设计容量
insert into coss_dm.dm_rws_region_year_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_252' as item_code,
    'Impounding Reservoir Capacity mcm' as item_name,
    sum(capacity) as item_value,
    'mcm' as unit,
    current_timestamp as etl_time,
    to_char(current_timestamp, 'yyyy')  as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_ass_ir_df t
group by
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_252' as item_code,
    'Impounding Reservoir Capacity mcm' as item_name,
    sum(capacity) as item_value,
    'mcm' as unit,
    current_timestamp as etl_time,
    to_char(current_timestamp, 'yyyy')  as yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_ass_ir_df t
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);
    

-- 水塘产量(年指标)
insert into coss_dm.dm_rws_region_year_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(dt/10000 as int) mh ,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
group by
cast(dt/10000  as int),
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(dt/10000 as int) mh , --
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
group by
 cast(dt/10000 as int)
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);


-- 东江水实际供应量（年指标）
insert into coss_dm.dm_rws_region_year_kpi_dip
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_255' as item_code,
    'GD Water Actual Supply ML' as item_name,
    sum(agr_vol - dis_vol) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(to_char(rec_dt,'yyyy') as int) yr,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_rws_gd_agr_supply_di_year
group by
cast(to_char(rec_dt,'yyyy') as int)
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

-- 水塘产量(月指标)

insert into coss_dm.dm_rws_region_month_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(dt/100 as int) mh ,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
group by
cast(dt/100  as int),
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(dt/100 as int) mh , --
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
group by
 cast(dt/100 as int)

on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);

-- 东江水实际供应量（月指标）
insert into coss_dm.dm_rws_region_month_kpi_dip
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_255' as item_code,
    'GD Water Actual Supply ML' as item_name,
    sum(agr_vol - dis_vol) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(to_char(rec_dt,'yyyymm') as int) mh,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_rws_gd_agr_supply_di_year
group by
cast(to_char(rec_dt,'yyyymm') as int)
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);


-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- 水塘当前容量(天指标)
insert into coss_dm.dm_rws_region_day_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_253' as item_code,
    'Impounding Reservoir Current Storage ML' as item_name,
    sum(present_storage) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dws.dws_rws_ir_storage_detail_di_year
group by
dt,
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_253' as item_code,
    'Impounding Reservoir Current Storage ML' as item_name,
    sum(present_storage) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    dt, --
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from  coss_dws.dws_rws_ir_storage_detail_di_year
group by
 dt
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);


-- 水塘产量(天指标)
insert into coss_dm.dm_rws_region_day_kpi_dip
select
    uuid() as id,
    region_code  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
group by
dt,
region_code

union all
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_254' as item_code,
    'Impounding Reservoir Current Yield ML' as item_name,
    sum(yield) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    dt, --
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dm.dm_rws_daily_ir_storage_yield_di
group by
 dt
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);


-- 东江水(天指标)
insert into coss_dm.dm_rws_region_day_kpi_dip
select
    uuid() as id,
    'HKSAR'  as region,
    'bi_p_255' as item_code,
    'GD Water Actual Supply ML' as item_name,
    sum(agr_vol - dis_vol) as item_value,
    'ML' as unit,
    current_timestamp as etl_time,
    cast(to_char(rec_dt,'yyyymmdd') as int) dt,
    current_timestamp dm_update_time,
    current_timestamp dm_load_time
from coss_dwd.dwd_rws_gd_agr_supply_di_year
group by
cast(to_char(rec_dt,'yyyymmdd') as int)
on duplicate key update
    id = values(id),
    item_name = values(item_name),
    item_value = values(item_value),
    unit = values(unit),
    etl_time = values(etl_time),
    dm_update_time = values(dm_update_time);









```

