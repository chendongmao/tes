# ods

## ods_sttss_extract_raw_water_supply_asset_day（调度任务）

调度任务前置任务节点名称

```tex
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_ir_df_all
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_ir_group_df_all
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_measurement_df_all
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_ps_di_add
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_region_df_all
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_rw_df_all
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_rw_type_df_all
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_sr_di_add
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_w_type_df_all
ods_sttss_extract_raw_water_supply_asset_day_sql_ods_sttss_rws_water_usage_df_all
ods_sttss_extract_raw_water_supply_day_sql_ods_sttss_rws_wtw_df_all
```

### 1.coss_ods.ods_sttss_rws_ir_df

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_ir_df;

create table if not exists coss_ods.ods_sttss_rws_ir_df (
    "ir_id"           varchar(20),
    "ig_id"           varchar(20),
    "i_code"          varchar(10),
    "rlabel"          varchar(400),
    "level_type"      varchar(2),
    "level_unit"      varchar(2),
    "dead_storage"    decimal(12, 4),
    "twl"             decimal(12, 4),
    "capacity"        decimal(12, 4),
    "min_storage"     decimal(12, 4),
    "limit_m"         decimal(12, 4),
    "last_upd_user"   varchar(120),
    "last_upd_post"   varchar(52),
    "last_upd_dt"     timestamp(6),
    "ir_name"         varchar(200),
    "ir_cname"        varchar(300),
    ods_update_time   timestamp(6) default current_timestamp,
    ods_load_time     timestamp(6) default current_timestamp,
    primary key ("ir_id")
) ;

comment on table coss_ods.ods_sttss_rws_ir_df is 'Impounding Reservoir Information';
comment on column coss_ods.ods_sttss_rws_ir_df."ir_id"          is 'Impounding Reservoir ID With Format IRNNNNNNNN';
comment on column coss_ods.ods_sttss_rws_ir_df."ig_id"          is 'Impounding Reservoir Group Being Referenced';
comment on column coss_ods.ods_sttss_rws_ir_df."i_code"         is 'Installation Code Of Impounding Reservoir';
comment on column coss_ods.ods_sttss_rws_ir_df."rlabel"         is 'Labels Used In Reports';
comment on column coss_ods.ods_sttss_rws_ir_df."level_type"     is 'Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}';
comment on column coss_ods.ods_sttss_rws_ir_df."level_unit"     is 'Possible Values:{"F" - Feet / Inch, "M" - Meter}';
comment on column coss_ods.ods_sttss_rws_ir_df."dead_storage"   is 'Dead Storage Of An Impounding Reservoir.  Unit Is In Mcm';
comment on column coss_ods.ods_sttss_rws_ir_df."twl"            is 'TWL';
comment on column coss_ods.ods_sttss_rws_ir_df."capacity"       is 'Capacity Of IR.  Unit Is In Mcm';
comment on column coss_ods.ods_sttss_rws_ir_df."min_storage"    is 'Allowable Minimum Storage.  Unit Is In Mcm';
comment on column coss_ods.ods_sttss_rws_ir_df."limit_m"        is 'Preset Limit For Water Level.  Unit Is In M';
comment on column coss_ods.ods_sttss_rws_ir_df."last_upd_user"  is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_ir_df."last_upd_post"  is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_ir_df."last_upd_dt"    is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_ir_df."ir_name"        is 'Impounding Reservoir Name';
comment on column coss_ods.ods_sttss_rws_ir_df."ir_cname"       is 'Impounding Reservoir Chinese Name';
comment on column coss_ods.ods_sttss_rws_ir_df.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_ir_df.ods_load_time    is 'Data Loading Time';

```

#### datax sql

```sql
select
    ir_id,                                 -- Impounding Reservoir ID with format IRNNNNNNNN
    ig_id,                                -- Impounding Reservoir Group being referenced
    i_code,                               -- Installation Code of Impounding Reservoir
    rlabel,                               -- Labels used in reports
    level_type,                           -- Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}
    level_unit,                           -- Possible Values:{"F" - Feet / Inch, "M" - Meter}
    dead_storage,                         -- Dead Storage of an Impounding Reservoir.  Unit is in mcm
    twl,                                  -- TWL
    capacity,                             -- Capacity of IR.  Unit is in mcm
    min_storage,                          -- Allowable Minimum Storage.  Unit is in mcm
    limit_m,                              -- Preset Limit for Water Level.  Unit is in m
    last_upd_user,                        -- Last Update By (Username)
    last_upd_post,                        -- Last Update By (Post)
    last_upd_dt,                          -- Last Update Date
    ir_name,                              -- Impounding reservoir name
    ir_cname,                             -- Impounding Reservoir Chinese Name
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.ir
```



#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Impounding Reservoir Information
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.ir
-- Target Table:  coss_ods.ods_sttss_rws_ir_df
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_ir_df (
    "ir_id",
    "ig_id",
    "i_code",
    "rlabel",
    "level_type",
    "level_unit",
    "dead_storage",
    "twl",
    "capacity",
    "min_storage",
    "limit_m",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    "ir_name",
    "ir_cname",
    ods_update_time,
    ods_load_time
)
select
    ir_id,                                 -- Impounding Reservoir ID with format IRNNNNNNNN
    ig_id,                                -- Impounding Reservoir Group being referenced
    i_code,                               -- Installation Code of Impounding Reservoir
    rlabel,                               -- Labels used in reports
    level_type,                           -- Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}
    level_unit,                           -- Possible Values:{"F" - Feet / Inch, "M" - Meter}
    dead_storage,                         -- Dead Storage of an Impounding Reservoir.  Unit is in mcm
    twl,                                  -- TWL
    capacity,                             -- Capacity of IR.  Unit is in mcm
    min_storage,                          -- Allowable Minimum Storage.  Unit is in mcm
    limit_m,                              -- Preset Limit for Water Level.  Unit is in m
    last_upd_user,                        -- Last Update By (Username)
    last_upd_post,                        -- Last Update By (Post)
    last_upd_dt,                          -- Last Update Date
    ir_name,                              -- Impounding reservoir name
    ir_cname,                             -- Impounding Reservoir Chinese Name
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_ir_df_tmp
on duplicate key update
    "ig_id" = values("ig_id"),
    "i_code" = values("i_code"),
    "rlabel" = values("rlabel"),
    "level_type" = values("level_type"),
    "level_unit" = values("level_unit"),
    "dead_storage" = values("dead_storage"),
    "twl" = values("twl"),
    "capacity" = values("capacity"),
    "min_storage" = values("min_storage"),
    "limit_m" = values("limit_m"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    "ir_name" = values("ir_name"),
    "ir_cname" = values("ir_cname"),
    ods_update_time = values(ods_update_time)
    
    

```

### 2.coss_ods.ods_sttss_rws_ir_group_df

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_ir_group_df;

create table if not exists coss_ods.ods_sttss_rws_ir_group_df (
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

comment on table coss_ods.ods_sttss_rws_ir_group_df is 'Impounding Reservoir Group Information';
comment on column coss_ods.ods_sttss_rws_ir_group_df.ig_id            is 'Impounding Reservoir Group ID With Format IGNNNNNNNN';
comment on column coss_ods.ods_sttss_rws_ir_group_df.ig_name          is 'Name Of Impounding Reservoir Group';
comment on column coss_ods.ods_sttss_rws_ir_group_df.ig_cname         is 'Chinese Name Of Impounding Reservoir Group';
comment on column coss_ods.ods_sttss_rws_ir_group_df.rlabel           is 'Labels Used In Reports';
comment on column coss_ods.ods_sttss_rws_ir_group_df.region           is 'Region';
comment on column coss_ods.ods_sttss_rws_ir_group_df.old_ind          is 'Indicates If Impounding Reservoir Group Is Old Or New. Possible Values: {"Y" - Old, "N" - New} ';
comment on column coss_ods.ods_sttss_rws_ir_group_df.last_upd_user    is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_ir_group_df.last_upd_post    is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_ir_group_df.last_upd_dt      is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_ir_group_df.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_ir_group_df.ods_load_time    is 'Data Loading Time';

```

#### datax sql

```sql
select
    ig_id,                                 -- Impounding Reservoir Group ID with format IGNNNNNNNN
    ig_name,                               -- Name of Impounding Reservoir Group
    ig_cname,                              -- Chinese Name of Impounding Reservoir Group
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    old_ind,                               -- Indicates if Impounding Reservoir Group is old or new. Possible Values: {"Y" - Old, "N" - New}
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.ir_group
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Impounding Reservoir Group Information
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.ir_group
-- Target Table:  coss_ods.ods_sttss_rws_ir_group_df
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_ir_group_df (
    ig_id,
    ig_name,
    ig_cname,
    rlabel,
    region,
    old_ind,
    last_upd_user,
    last_upd_post,
    last_upd_dt,
    ods_update_time,
    ods_load_time
)
select
    ig_id,                                 -- Impounding Reservoir Group ID with format IGNNNNNNNN
    ig_name,                               -- Name of Impounding Reservoir Group
    ig_cname,                              -- Chinese Name of Impounding Reservoir Group
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    old_ind,                               -- Indicates if Impounding Reservoir Group is old or new. Possible Values: {"Y" - Old, "N" - New}
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_ir_group_df_tmp
on duplicate key update
    ig_name = values(ig_name),
    ig_cname = values(ig_cname),
    rlabel = values(rlabel),
    region = values(region),
    old_ind = values(old_ind),
    last_upd_user = values(last_upd_user),
    last_upd_post = values(last_upd_post),
    last_upd_dt = values(last_upd_dt),
    ods_update_time = values(ods_update_time)
    
    

```

### 3.coss_ods.ods_sttss_rws_measurement_df

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_measurement_df;

create table if not exists coss_ods.ods_sttss_rws_measurement_df (
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

comment on table coss_ods.ods_sttss_rws_measurement_df is 'Measurement Type';
comment on column coss_ods.ods_sttss_rws_measurement_df."code"             is 'Defines How Water Level Are Measured';
comment on column coss_ods.ods_sttss_rws_measurement_df."descrip"          is 'Description Of Measurement';
comment on column coss_ods.ods_sttss_rws_measurement_df."cdescrip"         is 'Chinese Description Of Measurement Type';
comment on column coss_ods.ods_sttss_rws_measurement_df."last_upd_user"    is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_measurement_df."last_upd_post"    is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_measurement_df."last_upd_dt"      is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_measurement_df.ods_update_time    is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_measurement_df.ods_load_time      is 'Data Loading Time';

```

#### datax sql

```sql
select
    code,                                 -- Defines how water level are measured
    descrip,                              -- Description of Measurement
    cdescrip,                             -- Chinese Description of Measurement Type
    last_upd_user,                        -- Last Update By (Username)
    last_upd_post,                        -- Last Update By (Post)
    last_upd_dt,                          -- Last Update Date
    current_timestamp as ods_update_time, -- Data Warehouse update Time
    current_timestamp as ods_load_time    -- Data Warehouse load Time
from sttss.measurement

```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Measurement Type
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.measurement
-- Target Table:  coss_ods.ods_sttss_rws_measurement_df
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_measurement_df (
    "code",
    "descrip",
    "cdescrip",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    ods_update_time,
    ods_load_time
)
select
    code,                                 -- Defines how water level are measured
    descrip,                              -- Description of Measurement
    cdescrip,                             -- Chinese Description of Measurement Type
    last_upd_user,                        -- Last Update By (Username)
    last_upd_post,                        -- Last Update By (Post)
    last_upd_dt,                          -- Last Update Date
    current_timestamp as ods_update_time, -- Data Warehouse update Time
    current_timestamp as ods_load_time    -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_measurement_df_tmp
on duplicate key update
    "descrip" = values("descrip"),
    "cdescrip" = values("cdescrip"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    ods_update_time = values(ods_update_time)
    

```

### 4.coss_ods.ods_sttss_rws_ps_di

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_ps_di;

create table if not exists coss_ods.ods_sttss_rws_ps_di (
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

comment on table coss_ods.ods_sttss_rws_ps_di is 'Pumping Station';
comment on column coss_ods.ods_sttss_rws_ps_di."ps_id"          is 'Pumping Station ID With Format PSNNNNNNNN';
comment on column coss_ods.ods_sttss_rws_ps_di."i_code"         is 'Installation Code Of Pumping Station';
comment on column coss_ods.ods_sttss_rws_ps_di."rlabel"         is 'Labels Used In Reports';
comment on column coss_ods.ods_sttss_rws_ps_di."region"         is 'Region';
comment on column coss_ods.ods_sttss_rws_ps_di."w_type"         is 'Type Of Water Maintained In The Pumping Station';
comment on column coss_ods.ods_sttss_rws_ps_di."repumping"      is 'Repumping';
comment on column coss_ods.ods_sttss_rws_ps_di."last_upd_user"  is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_ps_di."last_upd_post"  is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_ps_di."last_upd_dt"    is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_ps_di."remark"         is 'Remarks';
comment on column coss_ods.ods_sttss_rws_ps_di."ps_name"        is 'Pumping Station Name';
comment on column coss_ods.ods_sttss_rws_ps_di."ps_cname"       is 'Pumping Station Chinese Name';
comment on column coss_ods.ods_sttss_rws_ps_di.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_ps_di.ods_load_time    is 'Data Loading Time';

```

#### datax sql

```sql
select
    ps_id,                                 -- Pumping Station ID with format PSNNNNNNNN
    i_code,                                -- Installation Code of Pumping Station
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    w_type,                                -- Type of water maintained in the pumping station
    repumping,                             -- Repumping
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    remark,                                -- Remarks
    ps_name,                               -- Pumping station name
    ps_cname,                              -- Pumping Station Chinese Name
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.ps
where last_upd_dt >= '${last_upd_dt}'
```



#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Pumping Station
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.ps
-- Target Table:  coss_ods.ods_sttss_rws_ps_di
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_ps_di (
    "ps_id",
    "i_code",
    "rlabel",
    "region",
    "w_type",
    "repumping",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    "remark",
    "ps_name",
    "ps_cname",
    ods_update_time,
    ods_load_time
)
select
    ps_id,                                 -- Pumping Station ID with format PSNNNNNNNN
    i_code,                                -- Installation Code of Pumping Station
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    w_type,                                -- Type of water maintained in the pumping station
    repumping,                             -- Repumping
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    remark,                                -- Remarks
    ps_name,                               -- Pumping station name
    ps_cname,                              -- Pumping Station Chinese Name
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_ps_di_tmp
on duplicate key update
    "i_code" = values("i_code"),
    "rlabel" = values("rlabel"),
    "region" = values("region"),
    "w_type" = values("w_type"),
    "repumping" = values("repumping"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    "remark" = values("remark"),
    "ps_name" = values("ps_name"),
    "ps_cname" = values("ps_cname"),
    ods_update_time = values(ods_update_time)

```

### 5.coss_ods.ods_sttss_rws_region_df

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_region_df;

create table if not exists coss_ods.ods_sttss_rws_region_df (
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

comment on table coss_ods.ods_sttss_rws_region_df is 'Region';
comment on column coss_ods.ods_sttss_rws_region_df."code"           is 'Possible Values: {"HK" - HK Island, "K" - Kowloon, "NTE" -  New Territories East, "NTW" - New Territories West}';
comment on column coss_ods.ods_sttss_rws_region_df."descrip"        is 'Description Of Region';
comment on column coss_ods.ods_sttss_rws_region_df."cdescrip"       is 'Chinese Description Of Region';
comment on column coss_ods.ods_sttss_rws_region_df."indicator"      is 'Possible Values: {"I" - HK Island, "M" - Mainland} ';
comment on column coss_ods.ods_sttss_rws_region_df."last_upd_user"  is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_region_df."last_upd_post"  is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_region_df."last_upd_dt"    is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_region_df.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_region_df.ods_load_time    is 'Data Loading Time';

```

#### datax sql

```sql
select
    code,                                  -- Possible Values: {"HK" - HK Island, "K" - Kowloon, "NTE" -  New Territories East, "NTW" - New Territories West}
    descrip,                               -- Description of Region
    cdescrip,                              -- Chinese Description of Region
    indicator,                             -- Possible Values: {"I" - HK Island, "M" - Mainland} 
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.region
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Region
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.region
-- Target Table:  coss_ods.ods_sttss_rws_region_df
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_region_df (
    "code",
    "descrip",
    "cdescrip",
    "indicator",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    ods_update_time,
    ods_load_time
)
select
    code,                                  -- Possible Values: {"HK" - HK Island, "K" - Kowloon, "NTE" -  New Territories East, "NTW" - New Territories West}
    descrip,                               -- Description of Region
    cdescrip,                              -- Chinese Description of Region
    indicator,                             -- Possible Values: {"I" - HK Island, "M" - Mainland} 
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_region_df_tmp
on duplicate key update
    "descrip" = values("descrip"),
    "cdescrip" = values("cdescrip"),
    "indicator" = values("indicator"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    ods_update_time = values(ods_update_time)
    
    

```

### 6.coss_ods.ods_sttss_rws_rw_df

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_rw_df;

create table if not exists coss_ods.ods_sttss_rws_rw_df (
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

comment on table coss_ods.ods_sttss_rws_rw_df is 'Raw Water Source';
comment on column coss_ods.ods_sttss_rws_rw_df."rw_id"          is 'Raw Water Source ID With Format RWNNNNNNNN';
comment on column coss_ods.ods_sttss_rws_rw_df."rw_name"        is 'Name Of Raw Water';
comment on column coss_ods.ods_sttss_rws_rw_df."rw_cname"       is 'Chinese Name Of Raw Water';
comment on column coss_ods.ods_sttss_rws_rw_df."rlabel"         is 'Labels Used In Reports';
comment on column coss_ods.ods_sttss_rws_rw_df."region"         is 'Region';
comment on column coss_ods.ods_sttss_rws_rw_df."source"         is 'Source Of Raw Water';
comment on column coss_ods.ods_sttss_rws_rw_df."last_upd_user"  is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_rw_df."last_upd_post"  is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_rw_df."last_upd_dt"    is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_rw_df.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_rw_df.ods_load_time    is 'Data Loading Time';

```

#### datax sql

```sql
select
    rw_id,                                 -- Raw Water Source ID with format RWNNNNNNNN
    rw_name,                               -- Name of Raw Water
    rw_cname,                              -- Chinese Name of Raw Water
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    source,                                -- Source of raw water
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.rw
```



#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Raw Water Source
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.rw
-- Target Table:  coss_ods.ods_sttss_rws_rw_df
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_rw_df (
    "rw_id",
    "rw_name",
    "rw_cname",
    "rlabel",
    "region",
    "source",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    ods_update_time,
    ods_load_time
)
select
    rw_id,                                 -- Raw Water Source ID with format RWNNNNNNNN
    rw_name,                               -- Name of Raw Water
    rw_cname,                              -- Chinese Name of Raw Water
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    source,                                -- Source of raw water
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_rw_df_tmp
on duplicate key update
    "rw_name" = values("rw_name"),
    "rw_cname" = values("rw_cname"),
    "rlabel" = values("rlabel"),
    "region" = values("region"),
    "source" = values("source"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    ods_update_time = values(ods_update_time)



```

### 7.coss_ods.ods_sttss_rws_rw_type_df

#### create table  

```sql
drop table if exists coss_ods.ods_sttss_rws_rw_type_df;

create table if not exists coss_ods.ods_sttss_rws_rw_type_df (
    "code"           varchar(4),     -- Possible Values:{"G" - Guangdong, "R" - River, "O" - Others}
    "descrip"        varchar(90),    -- Description of Raw Water Source
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("code")
);

comment on table coss_ods.ods_sttss_rws_rw_type_df is 'Raw Water Type';
comment on column coss_ods.ods_sttss_rws_rw_type_df."code"           is 'Possible Values:{"G" - Guangdong, "R" - River, "O" - Others}';
comment on column coss_ods.ods_sttss_rws_rw_type_df."descrip"        is 'Description Of Raw Water Source';
comment on column coss_ods.ods_sttss_rws_rw_type_df.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_rw_type_df.ods_load_time    is 'Data Loading Time';

```

#### datax sql

```sql
select
    code,                                  -- Possible Values:{"G" - Guangdong, "R" - River, "O" - Others}
    descrip,                               -- Description of Raw Water Source
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.rw_type
```



#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Raw Water Type
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.rw_type
-- Target Table:  coss_ods.ods_sttss_rws_rw_type_df
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_rw_type_df (
    "code",
    "descrip",
    ods_update_time,
    ods_load_time
)
select
    code,                                  -- Possible Values:{"G" - Guangdong, "R" - River, "O" - Others}
    descrip,                               -- Description of Raw Water Source
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_rw_type_df_tmp
on duplicate key update
    "descrip" = values("descrip"),
    ods_update_time = values(ods_update_time)




```

### 8.coss_ods.ods_sttss_rws_sr_di

#### create table 

```sql
drop table if exists coss_ods.ods_sttss_rws_sr_di;

create table if not exists coss_ods.ods_sttss_rws_sr_di (
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

comment on table coss_ods.ods_sttss_rws_sr_di is 'Service Reservoir';
comment on column coss_ods.ods_sttss_rws_sr_di."sr_id"           is 'Service Reservoir ID With Format SRNNNNNNNN';
comment on column coss_ods.ods_sttss_rws_sr_di."i_code"          is 'Installation Code Of Service Reservoir';
comment on column coss_ods.ods_sttss_rws_sr_di."rlabel"          is 'Labels Used In Reports';
comment on column coss_ods.ods_sttss_rws_sr_di."region"          is 'Region';
comment on column coss_ods.ods_sttss_rws_sr_di."w_type"          is 'Type Of Water Maintained By The Service Reservoir';
comment on column coss_ods.ods_sttss_rws_sr_di."div_height"      is 'Height Of Division Wall.  Unit Is In M';
comment on column coss_ods.ods_sttss_rws_sr_di."capacity"        is 'Capacity Of Service Reservoir.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_rws_sr_di."limit"           is 'Preset Limit For Water Level Above Division Wall.  Unit Is In M';
comment on column coss_ods.ods_sttss_rws_sr_di."num_of_storage"  is 'No. Of Storage/Compartment';
comment on column coss_ods.ods_sttss_rws_sr_di."last_upd_user"   is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_sr_di."last_upd_post"   is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_sr_di."last_upd_dt"     is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_sr_di."sr_name"         is 'Service Reservoir Name ';
comment on column coss_ods.ods_sttss_rws_sr_di."sr_cname"        is 'Service Reservoir Chinese Name';
comment on column coss_ods.ods_sttss_rws_sr_di.ods_update_time   is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_sr_di.ods_load_time     is 'Data Loading Time';

```

#### datax sql

```sql
select
    sr_id,                                 -- Service Reservoir ID with format SRNNNNNNNN
    i_code,                                -- Installation Code of Service Reservoir
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    w_type,                                -- Type of water maintained by the service reservoir
    div_height,                            -- Height of Division Wall.  Unit is in m
    capacity,                              -- Capacity of Service Reservoir.  Unit is in cu m
    0 as "limit",                          -- Preset Limit for Water Level above division wall.  Unit is in m
    num_of_storage,                        -- No. of Storage/Compartment
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    sr_name,                               -- Service Reservoir Name 
    sr_cname,                              -- Service Reservoir Chinese Name
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.sr
where last_upd_dt >= '${last_upd_dt}'
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Service Reservoir
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.sr
-- Target Table:  coss_ods.ods_sttss_rws_sr_di
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_sr_di (
    "sr_id",
    "i_code",
    "rlabel",
    "region",
    "w_type",
    "div_height",
    "capacity",
    "limit",
    "num_of_storage",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    "sr_name",
    "sr_cname",
    ods_update_time,
    ods_load_time
)
select
    sr_id,                                 -- Service Reservoir ID with format SRNNNNNNNN
    i_code,                                -- Installation Code of Service Reservoir
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    w_type,                                -- Type of water maintained by the service reservoir
    div_height,                            -- Height of Division Wall.  Unit is in m
    capacity,                              -- Capacity of Service Reservoir.  Unit is in cu m
    0 as "limit",                          -- Preset Limit for Water Level above division wall.  Unit is in m
    num_of_storage,                        -- No. of Storage/Compartment
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    sr_name,                               -- Service Reservoir Name 
    sr_cname,                              -- Service Reservoir Chinese Name
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_sr_di_tmp
on duplicate key update
    "i_code" = values("i_code"),
    "rlabel" = values("rlabel"),
    "region" = values("region"),
    "w_type" = values("w_type"),
    "div_height" = values("div_height"),
    "capacity" = values("capacity"),
    "limit" = values("limit"),
    "num_of_storage" = values("num_of_storage"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    "sr_name" = values("sr_name"),
    "sr_cname" = values("sr_cname"),
    ods_update_time = values(ods_update_time)
```

### 9.coss_ods.ods_sttss_rws_w_type_df

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_w_type_df;

create table if not exists coss_ods.ods_sttss_rws_w_type_df (
    code             varchar(4),             -- Possible Values{G - Guangdong, R - River, O - Others}
    descrip          varchar(90),            -- Description of Raw Water Source
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key (code)
);

comment on table coss_ods.ods_sttss_rws_w_type_df is 'Raw Water Type';
comment on column coss_ods.ods_sttss_rws_w_type_df.code             is 'Possible Values{G - Guangdong, R - River, O - Others}';
comment on column coss_ods.ods_sttss_rws_w_type_df.descrip          is 'Description Of Raw Water Source';
comment on column coss_ods.ods_sttss_rws_w_type_df.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_w_type_df.ods_load_time    is 'Data Loading Time';

```

#### datax sql

```sql
select
    code,                                  -- Possible Values{G - Guangdong, R - River, O - Others}
    descrip,                               -- Description of Raw Water Source
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.w_type
```



#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Raw Water Type
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.w_type
-- Target Table:  coss_ods.ods_sttss_rws_w_type_df
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_w_type_df (
    code,
    descrip,
    ods_update_time,
    ods_load_time
)
select
    code,                                  -- Possible Values{G - Guangdong, R - River, O - Others}
    descrip,                               -- Description of Raw Water Source
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_w_type_df_tmp
on duplicate key update
    descrip = values(descrip),
    ods_update_time = values(ods_update_time)



```



### 10.coss_ods.ods_sttss_rws_water_usage_df

#### create table 

```sql
drop table if exists coss_ods.ods_sttss_rws_water_usage_df;

create table if not exists coss_ods.ods_sttss_rws_water_usage_df (
    "code"           decimal(3),        -- Code
    "descrip"        varchar(200),      -- Possible Values: {"Commissioning Test to Waste", "Commissioning Test to be Returned to System", "Augmented Supply for Flushing", Commission Test to be Used for Consumption}
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("code")
);

comment on table coss_ods.ods_sttss_rws_water_usage_df is 'Water Usage';
comment on column coss_ods.ods_sttss_rws_water_usage_df."code"           is 'Code';
comment on column coss_ods.ods_sttss_rws_water_usage_df."descrip"        is 'Possible Values: {"Commissioning Test to Waste", "Commissioning Test to be Returned to System", "Augmented Supply for Flushing", Commission Test to be Used for Consumption}';
comment on column coss_ods.ods_sttss_rws_water_usage_df.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_water_usage_df.ods_load_time    is 'Data Loading Time';

```

#### datax sql

```sql
select
    code,                                  -- Code
    descrip,                               -- Possible Values: {"Commissioning Test to Waste", "Commissioning Test to be Returned to System", "Augmented Supply for Flushing", Commission Test to be Used for Consumption}
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.water_usage
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Water Usage
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.water_usage
-- Target Table:  coss_ods.ods_sttss_rws_water_usage_df
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_water_usage_df (
    "code",
    "descrip",
    ods_update_time,
    ods_load_time
)
select
    code,                                  -- Code
    descrip,                               -- Possible Values: {"Commissioning Test to Waste", "Commissioning Test to be Returned to System", "Augmented Supply for Flushing", Commission Test to be Used for Consumption}
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_water_usage_df_tmp
on duplicate key update
    "descrip" = values("descrip"),
    ods_update_time = values(ods_update_time)



```

### 11.coss_ods.ods_sttss_rws_wtw_df

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_wtw_df;

create table if not exists coss_ods.ods_sttss_rws_wtw_df (
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

comment on table coss_ods.ods_sttss_rws_wtw_df is 'Water Treatment Works';
comment on column coss_ods.ods_sttss_rws_wtw_df."tw_id"          is 'Water Treatment Woks ID With Format TWNNNNNNNN';
comment on column coss_ods.ods_sttss_rws_wtw_df."i_code"         is 'Installation Code Of Water Treatment Works';
comment on column coss_ods.ods_sttss_rws_wtw_df."rlabel"         is 'Labels Used In Reports';
comment on column coss_ods.ods_sttss_rws_wtw_df."region"         is 'Region';
comment on column coss_ods.ods_sttss_rws_wtw_df."capacity"       is 'Capacity Of WTW.  Unit Is In Mld';
comment on column coss_ods.ods_sttss_rws_wtw_df."last_upd_user"  is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_wtw_df."last_upd_post"  is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_wtw_df."last_upd_dt"    is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_wtw_df."tw_name"        is 'Water Treatment Works Name';
comment on column coss_ods.ods_sttss_rws_wtw_df."tw_cname"       is 'Water Treatment Works Chinese Name';
comment on column coss_ods.ods_sttss_rws_wtw_df.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_wtw_df.ods_load_time    is 'Data Loading Time';

```

#### datax sql

```sql
select
    tw_id,                                 -- Water Treatment Woks ID with format TWNNNNNNNN
    i_code,                                -- Installation Code of Water Treatment Works
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    capacity,                              -- Capacity of WTW.  Unit is in Mld
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    tw_name,                               -- Water Treatment Works Name
    tw_cname,                              -- Water Treatment Works Chinese Name
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.wtw
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Water Treatment Works
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.wtw
-- Target Table:  coss_ods.ods_sttss_rws_wtw_df
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_wtw_df (
    "tw_id",
    "i_code",
    "rlabel",
    "region",
    "capacity",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    "tw_name",
    "tw_cname",
    ods_update_time,
    ods_load_time
)
select
    tw_id,                                 -- Water Treatment Woks ID with format TWNNNNNNNN
    i_code,                                -- Installation Code of Water Treatment Works
    rlabel,                                -- Labels used in reports
    region,                                -- Region
    capacity,                              -- Capacity of WTW.  Unit is in Mld
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    tw_name,                               -- Water Treatment Works Name
    tw_cname,                              -- Water Treatment Works Chinese Name
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_wtw_df_tmp
on duplicate key update
    "i_code"  = values("i_code"),
    "rlabel"  = values("rlabel"),
    "region"  = values("region"),
    "capacity"  = values("capacity"),
    "last_upd_user"  = values("last_upd_user"),
    "last_upd_post"  = values("last_upd_post"),
    "last_upd_dt"  = values("last_upd_dt"),
    "tw_name"  = values("tw_name"),
    "tw_cname"  = values("tw_cname"),
    ods_update_time  = values(ods_update_time)

```



## ods_sttss_extract_raw_water_supply_records_day（调度任务）

调度任务前置任务节点名称

```
ods_sttss_extract_raw_water_supply_records_day_sql_ods_sttss_rws_calc_di_add
ods_sttss_extract_raw_water_supply_records_day_sql_ods_sttss_rws_channel_di_add
ods_sttss_extract_raw_water_supply_records_day_sql_ods_sttss_rws_channel_flow_di_year_add
ods_sttss_extract_raw_water_supply_records_day_sql_ods_sttss_rws_ir_storage_di_year_add
ods_sttss_extract_raw_water_supply_records_day_sql_ods_sttss_rws_pqty_detail_di_year_add
ods_sttss_extract_raw_water_supply_records_day_sql_ods_sttss_rws_pqty_di_add
ods_sttss_extract_raw_water_supply_records_day_sql_ods_sttss_rws_gd_agr_supply_di_year_add
```



### 1.coss_ods.ods_sttss_rws_calc_di

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_calc_di;

create table if not exists coss_ods.ods_sttss_rws_calc_di (
    calc_id         decimal(10) not null,  -- Calculation ID
    ref_id          varchar(20) not null,  -- Referenced Channel or Internal Circulation
    usage           varchar(2),            -- Determines if the referenced Channel or Internal Circulation is used as summation or difference. Possible Values:{"S" - Sum, "D" - Difference}
    last_upd_user   varchar(120),          -- Last Update By (Username)
    last_upd_post   varchar(52),           -- Last Update By (Post)
    last_upd_dt     timestamp(6),          -- Last Update Date
    ods_update_time timestamp(6) default current_timestamp,  -- Data Update Time
    ods_load_time   timestamp(6) default current_timestamp,  -- Data Loading Time
    primary key (calc_id, ref_id)
) with (
    orientation=row,
    compression=no,
    storage_type=ustore,
    segment=off
);

-- Table And Column Comments (Comply With Water Affairs Department Specification)
comment on table coss_ods.ods_sttss_rws_calc_di                   is 'Calculation Lookup';
comment on column coss_ods.ods_sttss_rws_calc_di.calc_id         is 'Calculation ID';
comment on column coss_ods.ods_sttss_rws_calc_di.ref_id          is 'Referenced Channel or Internal Circulation';
comment on column coss_ods.ods_sttss_rws_calc_di.usage           is 'Determines if the referenced Channel or Internal Circulation is used as summation or difference. Possible Values:{"S" - Sum, "D" - Difference}';
comment on column coss_ods.ods_sttss_rws_calc_di.last_upd_user   is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_calc_di.last_upd_post   is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_calc_di.last_upd_dt     is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_calc_di.ods_update_time is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_calc_di.ods_load_time   is 'Data Loading Time';
```

#### datax sql

```sql
select
    calc_id                               -- Calculation ID
    ,ref_id                               -- Referenced Channel or Internal Circulation
    ,usage                                -- Determines if the referenced Channel or Internal Circulation is used as summation or difference. Possible Values:{"S" - Sum, "D" - Difference}
    ,last_upd_user                        -- Last Update By (Username)
    ,last_upd_post                        -- Last Update By (Post)
    ,last_upd_dt                          -- Last Update Date
    ,current_timestamp as ods_update_time    -- Data Warehouse Update Time
    ,current_timestamp as ods_load_time      -- Data Warehouse Load Time
from sttss.calc
where last_upd_dt >= '${last_upd_dt}'


```



#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Calculation Lookup
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table: sttss.calc
-- Target Table: coss_ods.ods_sttss_rws_calc_df
-- Note: This Script Is Used For Creating ODS Layer Table And Full Load Data From STTSS System
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_calc_di (
    calc_id,
    ref_id,
    usage,
    last_upd_user,
    last_upd_post,
    last_upd_dt,
    ods_update_time,
    ods_load_time
)
select
    calc_id                               -- Calculation ID
    ,ref_id                               -- Referenced Channel or Internal Circulation
    ,usage                                -- Determines if the referenced Channel or Internal Circulation is used as summation or difference. Possible Values:{"S" - Sum, "D" - Difference}
    ,last_upd_user                        -- Last Update By (Username)
    ,last_upd_post                        -- Last Update By (Post)
    ,last_upd_dt                          -- Last Update Date
    ,current_timestamp as ods_update_time    -- Data Warehouse Update Time
    ,current_timestamp as ods_load_time      -- Data Warehouse Load Time
from coss_ods.ods_sttss_rws_calc_di_tmp
on duplicate key update
    usage = values(usage),
    last_upd_user = values(last_upd_user),
    last_upd_post = values(last_upd_post),
    last_upd_dt = values(last_upd_dt),
    ods_update_time = values(ods_update_time)

```





### 2.coss_ods.ods_sttss_rws_channel_di（N）

> 多加了主键

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_channel_di;

create table if not exists coss_ods.ods_sttss_rws_channel_di (
    "option_no"       decimal(10),         -- Option No.
    "ch_id"           varchar(20),         -- System generated ID of a water transfer channel
    "src_id"          varchar(20),         -- Source of Water Inflow
    "dest_id"         varchar(20),         -- Destination of Water outflow
    "rlabel"          varchar(2000),       -- Labels used in reports
    "water_usage"     decimal(3),          -- Water Usage
    "w_type"          varchar(2),          -- Type of water maintained by the installation
    "calc_id"         decimal(10),         -- Calculation logic being referenced by daily water transfer volume of channels
    "m_code"          varchar(20),         -- Measured By
    "last_upd_user"   varchar(120),        -- Last Update By (Username)
    "last_upd_post"   varchar(52),         -- Last Update By (Post)
    "last_upd_dt"     timestamp(6),        -- Last Update Date
    "rlabelc"         varchar(200),        -- Labels used in reports
    ods_update_time   timestamp(6) default current_timestamp,
    ods_load_time     timestamp(6) default current_timestamp,
    primary key ("option_no", "ch_id")
);

comment on table coss_ods.ods_sttss_rws_channel_di is 'Water Transfer Channels';
comment on column coss_ods.ods_sttss_rws_channel_di."option_no"     is 'Option No.';
comment on column coss_ods.ods_sttss_rws_channel_di."ch_id"         is 'System Generated ID Of A Water Transfer Channel';
comment on column coss_ods.ods_sttss_rws_channel_di."src_id"        is 'Source Of Water Inflow';
comment on column coss_ods.ods_sttss_rws_channel_di."dest_id"       is 'Destination Of Water Outflow';
comment on column coss_ods.ods_sttss_rws_channel_di."rlabel"        is 'Labels Used In Reports';
comment on column coss_ods.ods_sttss_rws_channel_di."water_usage"   is 'Water Usage';
comment on column coss_ods.ods_sttss_rws_channel_di."w_type"        is 'Type Of Water Maintained By The Installation';
comment on column coss_ods.ods_sttss_rws_channel_di."calc_id"       is 'Calculation Logic Being Referenced By Daily Water Transfer Volume Of Channels';
comment on column coss_ods.ods_sttss_rws_channel_di."m_code"        is 'Measured By';
comment on column coss_ods.ods_sttss_rws_channel_di."last_upd_user" is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_channel_di."last_upd_post" is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_channel_di."last_upd_dt"   is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_channel_di."rlabelc"       is 'Labels Used In Reports';
comment on column coss_ods.ods_sttss_rws_channel_di.ods_update_time is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_channel_di.ods_load_time   is 'Data Loading Time';


```

#### datax sql

```sql
select
    option_no,                              -- Option No.
    ch_id,                                 -- System generated ID of a water transfer channel
    src_id,                                -- Source of Water Inflow
    dest_id,                               -- Destination of Water outflow
    rlabel,                                -- Labels used in reports
    water_usage,                           -- Water Usage
    w_type,                                -- Type of water maintained by the installation
    calc_id,                               -- Calculation logic being referenced by daily water transfer volume of channels
    m_code,                                -- Measured By
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    rlabelc,                               -- Labels used in reports
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from sttss.channel
where last_upd_dt >= '${last_upd_dt}'
```



#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Water Transfer Channels
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.channel
-- Target Table:  coss_ods.ods_sttss_rws_channel_df
-- ****************************************************************************************

insert into coss_ods.ods_sttss_rws_channel_di (
    "option_no",
    "ch_id",
    "src_id",
    "dest_id",
    "rlabel",
    "water_usage",
    "w_type",
    "calc_id",
    "m_code",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    "rlabelc",
    ods_update_time,
    ods_load_time
)
select
    option_no,                              -- Option No.
    ch_id,                                 -- System generated ID of a water transfer channel
    src_id,                                -- Source of Water Inflow
    dest_id,                               -- Destination of Water outflow
    rlabel,                                -- Labels used in reports
    water_usage,                           -- Water Usage
    w_type,                                -- Type of water maintained by the installation
    calc_id,                               -- Calculation logic being referenced by daily water transfer volume of channels
    m_code,                                -- Measured By
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    rlabelc,                               -- Labels used in reports
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_channel_di_tmp
on duplicate key update
    "src_id" = values("src_id"),
    "rlabel" = values("rlabel"),
    "dest_id" = values("dest_id"),
    "water_usage" = values("water_usage"),
    "w_type" = values("w_type"),
    "calc_id" = values("calc_id"),
    "m_code" = values("m_code"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    "rlabelc" = values("rlabelc"),
    ods_update_time = values(ods_update_time)
```



### 3.coss_ods.ods_sttss_rws_channel_flow_di_year（N）

> 问题还没找到

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_channel_flow_di_year;

create table if not exists coss_ods.ods_sttss_rws_channel_flow_di_year (
    "option_no"       decimal(10),           -- Option No. of Water Transfer Channel being referenced
    "ch_id"           varchar(20),           -- Water Transfer Channels being referenced
    "qty_del"         decimal(12, 4),        -- Quantity delivered of "Water transfer channel. Unit is in Mld
    "scada_qty_del"   decimal(12, 4),        -- Quantity delivered of "Water transfer channel. Unit is in Mld (SCADA)
    "m_code"          varchar(20),           -- Defines how the channel water flow is measured
    "rec_dt"          timestamp(6),          -- Date of Record
    "remarks"         varchar(2000),         -- Remarks
    "submit_dt"       timestamp(6),          -- Submission Date
    "last_upd_user"   varchar(120),          -- Last Update By (Username)
    "last_upd_post"   varchar(52),           -- Last Update By (Post)
    "last_upd_dt"     timestamp(6),          -- Last Update Date
    "wl_m"            decimal(12, 4),        -- Water Level reading in meter
    "wl_mpd"          decimal(13, 6),        -- Water Level in mPD
    ods_update_time   timestamp(6) default current_timestamp,
    ods_load_time     timestamp(6) default current_timestamp,
    "dt"              decimal(10),           -- Daily Partitions
    primary key (option_no, ch_id, rec_dt)
) partition by range (rec_dt) (
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

comment on table coss_ods.ods_sttss_rws_channel_flow_di_year is 'Water Transfer Channels Daily Flow';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."option_no"     is 'Option No. of Water Transfer Channel being referenced';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."ch_id"         is 'Water Transfer Channels being referenced';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."qty_del"       is 'Quantity delivered of "Water transfer channel. Unit is in Mld';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."scada_qty_del" is 'Quantity delivered of "Water transfer channel. Unit is in Mld (SCADA)';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."m_code"        is 'Defines how the channel water flow is measured';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."rec_dt"        is 'Date of Record';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."remarks"       is 'Remarks';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."submit_dt"     is 'Submission Date';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."last_upd_user" is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."last_upd_post" is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."last_upd_dt"   is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."wl_m"          is 'Water Level reading in meter';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."wl_mpd"        is 'Water Level in mPD';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year.ods_update_time is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year.ods_load_time   is 'Data Loading Time';
comment on column coss_ods.ods_sttss_rws_channel_flow_di_year."dt"            is 'Daily Partitions';

```

#### datax sql

```sql
 select
    option_no,                              -- Option No. of Water Transfer Channel being referenced
    ch_id,                                 -- Water Transfer Channels being referenced
    qty_del,                               -- Quantity delivered of "Water transfer channel. Unit is in Mld
    scada_qty_del,                         -- Quantity delivered of "Water transfer channel. Unit is in Mld (SCADA)
    m_code,                                -- Defines how the channel water flow is measured
    rec_dt,                                -- Date of Record
    remarks,                               -- Remarks
    submit_dt,                             -- Submission Date
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    0 as wl_m,                             -- Water Level reading in meter
    0 as wl_mpd,                           -- Water Level in mPD
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(rec_dt, 'yyyymmdd')::decimal(10) as "dt"  -- Daily Partitions
from sttss.channel_flow
where last_upd_dt >= ${last_upd_dt}
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Water Transfer Channels Daily Flow
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.channel_flow
-- Target Table:  coss_ods.ods_sttss_rws_channel_flow_di_year
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_channel_flow_di_year (
    "option_no",
    "ch_id",
    "qty_del",
    "scada_qty_del",
    "m_code",
    "rec_dt",
    "remarks",
    "submit_dt",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    "wl_m",
    "wl_mpd",
    ods_update_time,
    ods_load_time,
    "dt"
)
select
    option_no,                              -- Option No. of Water Transfer Channel being referenced
    ch_id,                                 -- Water Transfer Channels being referenced
    qty_del,                               -- Quantity delivered of "Water transfer channel. Unit is in Mld
    scada_qty_del,                         -- Quantity delivered of "Water transfer channel. Unit is in Mld (SCADA)
    m_code,                                -- Defines how the channel water flow is measured
    rec_dt,                                -- Date of Record
    remarks,                               -- Remarks
    submit_dt,                             -- Submission Date
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    0 as wl_m,                             -- Water Level reading in meter
    0 as wl_mpd,                           -- Water Level in mPD
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(rec_dt, 'yyyymmdd')::decimal(10) as "dt"  -- Daily Partitions
from coss_ods.ods_sttss_rws_channel_flow_di_year_tmp
on duplicate key update
    "qty_del" = values("qty_del"),
    "scada_qty_del" = values("scada_qty_del"),
    "m_code" = values("m_code"),
    "remarks" = values("remarks"),
    "submit_dt" = values("submit_dt"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    "wl_m" = values("wl_m"),
    "wl_mpd" = values("wl_mpd"),
    ods_update_time = values(ods_update_time)
```







### 4.coss_ods.ods_sttss_rws_ir_storage_di_year

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_ir_storage_di_year;

create table if not exists coss_ods.ods_sttss_rws_ir_storage_di_year (
    "ir_id"           varchar(20),              -- Impounding Reservior being referenced
    "wl_ft"           decimal(12, 4),           -- Water Level reading in feet
    "wl_in"           decimal(12, 4),           -- Water Level reading in inch
    "wl_m"            decimal(12, 4),           -- Water Level reading in meter
    "wl_mpd"          decimal(13, 6),           -- Waler Level in mPD
    "scada_wl_mpd"    decimal(13, 6),           -- Waler Level in mPD (SCADA)
    "storage"         decimal(16, 8),           -- Storage of water in IR.  Unit is in mcm
    "remarks"         varchar(2000),            -- Remarks
    "rec_dt"          timestamp(6),             -- Date of record
    "submit_dt"       timestamp(6),             -- Submission Date
    "last_upd_user"   varchar(120),             -- Last Update By (Username)
    "last_upd_post"   varchar(52),              -- Last Update By (Post)
    "last_upd_dt"     timestamp(6),             -- Last Update Date
    ods_update_time   timestamp(6) default current_timestamp,
    ods_load_time     timestamp(6) default current_timestamp,
    "dt"              decimal(10),              -- Daily Partitions
    primary key ("ir_id", "rec_dt")
) 
partition by range ("rec_dt") (
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

comment on table coss_ods.ods_sttss_rws_ir_storage_di_year is 'Daily Impounding Reservoir Storage Details';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."ir_id"          is 'Impounding Reservior Being Referenced';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."wl_ft"          is 'Water Level Reading In Feet';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."wl_in"          is 'Water Level Reading In Inch';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."wl_m"           is 'Water Level Reading In Meter';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."wl_mpd"         is 'Waler Level In MPD';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."scada_wl_mpd"   is 'Waler Level In MPD (SCADA)';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."storage"        is 'Storage Of Water In IR.  Unit Is In Mcm';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."remarks"        is 'Remarks';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."rec_dt"         is 'Date Of Record';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."submit_dt"      is 'Submission Date';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."last_upd_user"  is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."last_upd_post"  is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."last_upd_dt"    is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year.ods_load_time    is 'Data Loading Time';
comment on column coss_ods.ods_sttss_rws_ir_storage_di_year."dt"             is 'Daily Partitions';
```

#### datax sql

```sql
    
select
    ir_id,                                 -- Impounding Reservior being referenced
    wl_ft,                                 -- Water Level reading in feet
    wl_in,                                 -- Water Level reading in inch
    wl_m,                                  -- Water Level reading in meter
    wl_mpd,                                -- Waler Level in mPD
    scada_wl_mpd,                          -- Waler Level in mPD (SCADA)
    storage,                               -- Storage of water in IR.  Unit is in mcm
    remarks,                               -- Remarks
    rec_dt,                                -- Date of record
    submit_dt,                             -- Submission Date
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(rec_dt, 'yyyymmdd')::decimal(10) as "dt"  -- Daily Partitions
from sttss.ir_storage
where last_upd_dt >= '${last_upd_dt}'
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Daily Impounding Reservoir Storage Details
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.ir_storage
-- Target Table:  coss_ods.ods_sttss_rws_ir_storage_di_year
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_ir_storage_di_year (
    "ir_id",
    "wl_ft",
    "wl_in",
    "wl_m",
    "wl_mpd",
    "scada_wl_mpd",
    "storage",
    "remarks",
    "rec_dt",
    "submit_dt",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    ods_update_time,
    ods_load_time,
    "dt"
)
select
    ir_id,                                 -- Impounding Reservior being referenced
    wl_ft,                                 -- Water Level reading in feet
    wl_in,                                 -- Water Level reading in inch
    wl_m,                                  -- Water Level reading in meter
    wl_mpd,                                -- Waler Level in mPD
    scada_wl_mpd,                          -- Waler Level in mPD (SCADA)
    storage,                               -- Storage of water in IR.  Unit is in mcm
    remarks,                               -- Remarks
    rec_dt,                                -- Date of record
    submit_dt,                             -- Submission Date
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(rec_dt, 'yyyymmdd')::decimal(10) as "dt"  -- Daily Partitions
from coss_ods.ods_sttss_rws_ir_storage_di_year_tmp
on duplicate key update
    "wl_ft" = values("wl_ft"),
    "wl_in" = values("wl_in"),
    "wl_m" = values("wl_m"),
    "wl_mpd" = values("wl_mpd"),
    "scada_wl_mpd" = values("scada_wl_mpd"),
    "storage" = values("storage"),
    "remarks" = values("remarks"),
    "submit_dt" = values("submit_dt"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    ods_update_time = values(ods_update_time)
    

```



### 5.coss_ods.ods_sttss_rws_pqty_detail_di_year

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_pqty_detail_di_year;

create table if not exists coss_ods.ods_sttss_rws_pqty_detail_di_year (
    "prop_qty_id"    decimal(10),
    "ref_entity"     varchar(100),
    "ref_id"         varchar(20),
    "item_no"        decimal(10),
    "p_qty"          decimal(12, 4),
    "last_upd_user"  varchar(120),
    "last_upd_post"  varchar(52),
    "last_upd_dt"    timestamp(6),
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    "mh"             decimal(10),
    primary key ("prop_qty_id", "ref_id", "item_no")
) 
partition by range ("last_upd_dt") (
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

comment on table coss_ods.ods_sttss_rws_pqty_detail_di_year is 'Proposed Quantity Details';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year."prop_qty_id"    is 'Proposed Quantity ID';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year."ref_entity"     is 'Referenced Entity';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year."ref_id"         is 'Installations Being Referenced';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year."item_no"        is 'Item No.  To Be Used For Key Delivery';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year."p_qty"          is 'Proposed Quantity.  Unit Is Mld';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year."last_upd_user"  is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year."last_upd_post"  is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year."last_upd_dt"    is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year.ods_load_time    is 'Data Loading Time';
comment on column coss_ods.ods_sttss_rws_pqty_detail_di_year."mh"             is 'Daily Partitions';

```

#### datax sql

```sql
    
select
    prop_qty_id,
    ref_entity,
    ref_id,
    item_no,
    p_qty,
    last_upd_user,
    last_upd_post,
    last_upd_dt,
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(last_upd_dt, 'yyyymm')::decimal(10) as "mh"  -- Daily Partitions
from sttss.pqty_detail
where last_upd_dt >= '${last_upd_dt}'
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Proposed Quantity Details
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.pqty_detail
-- Target Table:  coss_ods.ods_sttss_rws_pqty_detail_di_year
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_pqty_detail_di_year (
    "prop_qty_id",
    "ref_entity",
    "ref_id",
    "item_no",
    "p_qty",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    ods_update_time,
    ods_load_time,
    "mh"
)
select
    prop_qty_id,
    ref_entity,
    ref_id,
    item_no,
    p_qty,
    last_upd_user,
    last_upd_post,
    last_upd_dt,
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(last_upd_dt, 'yyyymm')::decimal(10) as "mh"  -- Daily Partitions
from coss_ods.ods_sttss_rws_pqty_detail_di_year_tmp
on duplicate key update
    "ref_entity" = values("ref_entity"),
    "p_qty" = values("p_qty"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    ods_update_time = values(ods_update_time),
    "mh" = values("mh")

```

### 6.coss_ods.ods_sttss_rws_pqty_di

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_pqty_di;

create table if not exists coss_ods.ods_sttss_rws_pqty_di (
    "prop_qty_id"    decimal(10),      -- Proposed Quantity ID
    "start_dt"       timestamp(6),     -- Effective Start Date
    "end_dt"         timestamp(6),     -- Effective End Date
    "create_dt"      timestamp(6),     -- Created Date
    "create_by"      varchar(40),      -- Created By
    "last_upd_user"  varchar(120),     -- Last Update By (Username)
    "last_upd_post"  varchar(52),      -- Last Update By (Post)
    "last_upd_dt"    timestamp(6),     -- Last Update Date
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    primary key ("prop_qty_id")
);

comment on table coss_ods.ods_sttss_rws_pqty_di is 'Proposed Quantity';
comment on column coss_ods.ods_sttss_rws_pqty_di."prop_qty_id"    is 'Proposed Quantity ID';
comment on column coss_ods.ods_sttss_rws_pqty_di."start_dt"       is 'Effective Start Date';
comment on column coss_ods.ods_sttss_rws_pqty_di."end_dt"         is 'Effective End Date';
comment on column coss_ods.ods_sttss_rws_pqty_di."create_dt"      is 'Created Date';
comment on column coss_ods.ods_sttss_rws_pqty_di."create_by"      is 'Created By';
comment on column coss_ods.ods_sttss_rws_pqty_di."last_upd_user"  is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_pqty_di."last_upd_post"  is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_pqty_di."last_upd_dt"    is 'Last Update Date';
comment on column coss_ods.ods_sttss_rws_pqty_di.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_pqty_di.ods_load_time    is 'Data Loading Time';
```

#### datax sql

```sql
select
    prop_qty_id,                          -- Proposed Quantity ID
    start_dt,                            -- Effective Start Date
    end_dt,                              -- Effective End Date
    create_dt,                           -- Created Date
    create_by,                           -- Created By
    last_upd_user,                       -- Last Update By (Username)
    last_upd_post,                       -- Last Update By (Post)
    last_upd_dt,                         -- Last Update Date
    current_timestamp as ods_update_time,-- Data Warehouse update Time
    current_timestamp as ods_load_time   -- Data Warehouse load Time
from sttss.pqty
where last_upd_dt >= '${last_upd_dt}'
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Proposed Quantity
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.pqty
-- Target Table:  coss_ods.ods_sttss_rws_pqty_di
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_pqty_di (
    "prop_qty_id",
    "start_dt",
    "end_dt",
    "create_dt",
    "create_by",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    ods_update_time,
    ods_load_time
)
select
    prop_qty_id,                          -- Proposed Quantity ID
    start_dt,                            -- Effective Start Date
    end_dt,                              -- Effective End Date
    create_dt,                           -- Created Date
    create_by,                           -- Created By
    last_upd_user,                       -- Last Update By (Username)
    last_upd_post,                       -- Last Update By (Post)
    last_upd_dt,                         -- Last Update Date
    current_timestamp as ods_update_time,-- Data Warehouse update Time
    current_timestamp as ods_load_time   -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_pqty_di_tmp
on duplicate key update
    "start_dt" = values("start_dt"),
    "end_dt" = values("end_dt"),
    "create_dt" = values("create_dt"),
    "create_by" = values("create_by"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    "last_upd_dt" = values("last_upd_dt"),
    ods_update_time = values(ods_update_time)
      

```

### 7.coss_ods.ods_sttss_rws_gd_agr_supply_di_year（N）

> 缺少主键

#### create table

```sql
drop table if exists coss_ods.ods_sttss_rws_gd_agr_supply_di_year;

create table if not exists coss_ods.ods_sttss_rws_gd_agr_supply_di_year (
    rw_id            varchar(20),         -- Raw water Source being referenced
    hk_vol           numeric(14, 6),      -- Volume at HK Side.  Unit is in mcm
    gd_vol           numeric(14, 6),      -- Volume at GD Side. Unit is in mcm
    agr_vol          numeric(14, 6),      -- Agreed volume.  Unit is in mcm
    dis_vol          numeric(14, 6),      -- Discharged volume.  Unit is in mcm
    sz_wlevel        numeric(12, 4),      -- Shen Zhen Water Level.  Unit is in m
    dis_ind          varchar(3),          -- Possible Values:Y - Yes,N - No
    rec_dt           date,                -- Date of record
    submit_dt        timestamp(6),        -- Submission Date
    last_upd_user    varchar(100),        -- Last Update By (Username)
    last_upd_post    varchar(50),         -- Last Update By (Post)
    last_upd_dt      timestamp(6),       -- Last Update_Date
    ods_update_time  timestamp(6) default current_timestamp,
    ods_load_time    timestamp(6) default current_timestamp,
    "dt"             decimal(10),         -- Daily Partitions
    primary key(rw_id,rec_dt)
) partition by range (rec_dt) (
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

comment on table coss_ods.ods_sttss_rws_gd_agr_supply_di_year is 'Daily GD Water Supply';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.rw_id            is 'Raw Water Source Being Referenced';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.hk_vol           is 'Volume At HK Side.  Unit Is In Mcm';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.gd_vol           is 'Volume At GD Side. Unit Is In Mcm';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.agr_vol          is 'Agreed Volume.  Unit Is In Mcm';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.dis_vol          is 'Discharged Volume.  Unit Is In Mcm';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.sz_wlevel        is 'Shen Zhen Water Level.  Unit Is In M';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.dis_ind          is 'Possible Values:Y - Yes,N - No';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.rec_dt           is 'Date Of Record';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.submit_dt        is 'Submission Date';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.last_upd_user    is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.last_upd_post    is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.last_upd_dt    is 'Last Update_Date';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.ods_update_time  is 'Data Update Time';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year.ods_load_time    is 'Data Loading Time';
comment on column coss_ods.ods_sttss_rws_gd_agr_supply_di_year."dt"             is 'Daily Partitions';

```

#### datax sql

```sql
select
    rw_id,                                 -- Raw water Source being referenced
    hk_vol,                                -- Volume at HK Side.  Unit is in mcm
    gd_vol,                                -- Volume at GD Side. Unit is in mcm
    agr_vol,                               -- Agreed volume.  Unit is in mcm
    dis_vol,                               -- Discharged volume.  Unit is in mcm
    sz_wlevel,                             -- Shen Zhen Water Level.  Unit is in m
    dis_ind,                               -- Possible Values:Y - Yes,N - No
    rec_dt,                                -- Date of record
    submit_dt,                             -- Submission Date
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt                            -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(rec_dt, 'yyyymmdd')::decimal(10) as "dt"  -- Daily Partitions
from sttss.gd_agr_supply
where last_upd_dt >= '${last_upd_dt}'
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Daily GD Water Supply
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.gd_agr_supply
-- Target Table:  coss_ods.ods_sttss_rws_gd_agr_supply_di_year
-- ****************************************************************************************
insert into coss_ods.ods_sttss_rws_gd_agr_supply_di_year (
    rw_id,
    hk_vol,
    gd_vol,
    agr_vol,
    dis_vol,
    sz_wlevel,
    dis_ind,
    rec_dt,
    submit_dt,
    last_upd_user,
    last_upd_post,
    last_upd_dt,
    ods_update_time,
    ods_load_time,
    "dt"
)
select
    rw_id,                                 -- Raw water Source being referenced
    hk_vol,                                -- Volume at HK Side.  Unit is in mcm
    gd_vol,                                -- Volume at GD Side. Unit is in mcm
    agr_vol,                               -- Agreed volume.  Unit is in mcm
    dis_vol,                               -- Discharged volume.  Unit is in mcm
    sz_wlevel,                             -- Shen Zhen Water Level.  Unit is in m
    dis_ind,                               -- Possible Values:Y - Yes,N - No
    rec_dt,                                -- Date of record
    submit_dt,                             -- Submission Date
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(rec_dt, 'yyyymmdd')::decimal(10) as "dt"  -- Daily Partitions
from coss_ods.ods_sttss_rws_gd_agr_supply_di_year_tmp
on duplicate key update
    hk_vol = values(hk_vol),
    gd_vol = values(gd_vol),
    agr_vol = values(agr_vol),
    dis_vol = values(dis_vol),
    sz_wlevel = values(sz_wlevel),
    dis_ind = values(dis_ind),
    submit_dt = values(submit_dt),
    last_upd_user = values(last_upd_user),
    last_upd_post = values(last_upd_post),
    last_upd_dt = values(last_upd_dt),
    ods_update_time = values(ods_update_time)

```

## ods_sttss_extract_sr_water_supply_records_day（调度任务）

调度任务前置任务节点名称

```tex
ods_sttss_extract_raw_water_supply_day_sql_ods_sttss_rws_sr_storage_di_year_add
```



### 15.coss_ods.ods_sttss_rws_sr_storage_di_year(N)

> 缺少主键

#### create table

```sql
drop table if exists coss_ods.ods_sttss_srs_sr_storage_di_year;

create table if not exists coss_ods.ods_sttss_srs_sr_storage_di_year (
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
) partition by range ("rec_dt") (
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

comment on table coss_ods.ods_sttss_srs_sr_storage_di_year is 'Daily SR Storage Details';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."sr_id"           is 'Service Reservior Being Referenced';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."a_wlevel"        is 'A Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."b_wlevel"        is 'B Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."c_wlevel"        is 'C Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."d_wlevel"        is 'D Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."e_wlevel"        is 'E Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."f_wlevel"        is 'F Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."g_wlevel"        is 'G Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."h_wlevel"        is 'H Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."i_wlevel"        is 'I Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."j_wlevel"        is 'J Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."k_wlevel"        is 'K Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."l_wlevel"        is 'L Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."m_wlevel"        is 'M Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."n_wlevel"        is 'N Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."o_wlevel"        is 'O Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."p_wlevel"        is 'P Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."q_wlevel"        is 'Q Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."r_wlevel"        is 'R Compartment Water Level';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_a_wlevel"  is 'A Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_b_wlevel"  is 'B Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_c_wlevel"  is 'C Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_d_wlevel"  is 'D Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_e_wlevel"  is 'E Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_f_wlevel"  is 'F Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_g_wlevel"  is 'G Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_h_wlevel"  is 'H Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_i_wlevel"  is 'I Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_j_wlevel"  is 'J Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_k_wlevel"  is 'K Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_l_wlevel"  is 'L Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_m_wlevel"  is 'M Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_n_wlevel"  is 'N Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_o_wlevel"  is 'O Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_p_wlevel"  is 'P Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_q_wlevel"  is 'Q Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."scada_r_wlevel"  is 'R Compartment Water Level (SCADA)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."a_storage"       is 'Volume Of Water In A Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."b_storage"       is 'Volume Of Water In B Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."c_storage"       is 'Volume Of Water In C Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."d_storage"       is 'Volume Of Water In D Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."e_storage"       is 'Volume Of Water In E Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."f_storage"       is 'Volume Of Water In F Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."g_storage"       is 'Volume Of Water In G Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."h_storage"       is 'Volume Of Water In H Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."i_storage"       is 'Volume Of Water In I Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."j_storage"       is 'Volume Of Water In J Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."k_storage"       is 'Volume Of Water In K Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."l_storage"       is 'Volume Of Water In L Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."m_storage"       is 'Volume Of Water In M Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."n_storage"       is 'Volume Of Water In N Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."o_storage"       is 'Volume Of Water In O Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."p_storage"       is 'Volume Of Water In P Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."q_storage"       is 'Volume Of Water In Q Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."r_storage"       is 'Volume Of Water In R Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."tot_storage"     is 'Total Volume Of Water In A+ B+..+R.  Unit Is In Cu M';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."remarks"         is 'Remarks';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."rec_dt"          is 'Date Of Record';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."submit_dt"       is 'Submission Date';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."last_upd_user"   is 'Last Update By (Username)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."last_upd_post"   is 'Last Update By (Post)';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."last_upd_dt"     is 'Last Update Date';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year.ods_update_time   is 'Data Update Time';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year.ods_load_time     is 'Data Loading Time';
comment on column coss_ods.ods_sttss_srs_sr_storage_di_year."dt"              is 'Daily Partitions';

```

#### datax sql

```sql
select
    sr_id,                                 -- Service Reservior being referenced
    a_wlevel,                              -- A Compartment Water Level
    b_wlevel,                              -- B Compartment Water Level
    c_wlevel,                              -- C Compartment Water Level
    d_wlevel,                              -- D Compartment Water Level
    e_wlevel,                              -- E Compartment Water Level
    f_wlevel,                              -- F Compartment Water Level
    g_wlevel,                              -- G Compartment Water Level
    h_wlevel,                              -- H Compartment Water Level
    i_wlevel,                              -- I Compartment Water Level
    j_wlevel,                              -- J Compartment Water Level
    k_wlevel,                              -- K Compartment Water Level
    l_wlevel,                              -- L Compartment Water Level
    m_wlevel,                              -- M Compartment Water Level
    n_wlevel,                              -- N Compartment Water Level
    o_wlevel,                              -- O Compartment Water Level
    p_wlevel,                              -- P Compartment Water Level
    q_wlevel,                              -- Q Compartment Water Level
    r_wlevel,                              -- R Compartment Water Level
    scada_a_wlevel,                        -- A Compartment Water Level (SCADA)
    scada_b_wlevel,                        -- B Compartment Water Level (SCADA)
    scada_c_wlevel,                        -- C Compartment Water Level (SCADA)
    scada_d_wlevel,                        -- D Compartment Water Level (SCADA)
    scada_e_wlevel,                        -- E Compartment Water Level (SCADA)
    scada_f_wlevel,                        -- F Compartment Water Level (SCADA)
    scada_g_wlevel,                        -- G Compartment Water Level (SCADA)
    scada_h_wlevel,                        -- H Compartment Water Level (SCADA)
    scada_i_wlevel,                        -- I Compartment Water Level (SCADA)
    scada_j_wlevel,                        -- J Compartment Water Level (SCADA)
    scada_k_wlevel,                        -- K Compartment Water Level (SCADA)
    scada_l_wlevel,                        -- L Compartment Water Level (SCADA)
    scada_m_wlevel,                        -- M Compartment Water Level (SCADA)
    scada_n_wlevel,                        -- N Compartment Water Level (SCADA)
    scada_o_wlevel,                        -- O Compartment Water Level (SCADA)
    scada_p_wlevel,                        -- P Compartment Water Level (SCADA)
    scada_q_wlevel,                        -- Q Compartment Water Level (SCADA)
    scada_r_wlevel,                        -- R Compartment Water Level (SCADA)
    a_storage,                             -- Volume of water in A compartment of an SR.  Unit is in cu m
    b_storage,                             -- Volume of water in B compartment of an SR.  Unit is in cu m
    c_storage,                             -- Volume of water in C compartment of an SR.  Unit is in cu m
    d_storage,                             -- Volume of water in D compartment of an SR.  Unit is in cu m
    e_storage,                             -- Volume of water in E compartment of an SR.  Unit is in cu m
    f_storage,                             -- Volume of water in F compartment of an SR.  Unit is in cu m
    g_storage,                             -- Volume of water in G compartment of an SR.  Unit is in cu m
    h_storage,                             -- Volume of water in H compartment of an SR.  Unit is in cu m
    i_storage,                             -- Volume of water in I compartment of an SR.  Unit is in cu m
    j_storage,                             -- Volume of water in J compartment of an SR.  Unit is in cu m
    k_storage,                             -- Volume of water in K compartment of an SR.  Unit is in cu m
    l_storage,                             -- Volume of water in L compartment of an SR.  Unit is in cu m
    m_storage,                             -- Volume of water in M compartment of an SR.  Unit is in cu m
    n_storage,                             -- Volume of water in N compartment of an SR.  Unit is in cu m
    o_storage,                             -- Volume of water in O compartment of an SR.  Unit is in cu m
    p_storage,                             -- Volume of water in P compartment of an SR.  Unit is in cu m
    q_storage,                             -- Volume of water in Q compartment of an SR.  Unit is in cu m
    r_storage,                             -- Volume of water in R compartment of an SR.  Unit is in cu m
    tot_storage,                           -- Total volume of water in A+ B+..+R.  Unit is in cu m
    remarks,                               -- Remarks
    rec_dt,                                -- Date of record
    submit_dt,                             -- Submission Date
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(rec_dt, 'yyyymmdd')::decimal(10) as "dt"  -- Daily Partitions
from sttss.sr_storage
where last_upd_dt >= '${last_upd_dt}'
```

#### select sql

```sql
-- ****************************************************************************************
-- Source     System: STTSS(Smart Trunk Transfer Support System)
-- Function Describe: Daily SR Storage Details
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  sttss.sr_storage
-- Target Table:  coss_ods.ods_sttss_srs_sr_storage_di_year
-- ****************************************************************************************
insert into coss_ods.ods_sttss_srs_sr_storage_di_year (
    "sr_id",
    "a_wlevel",
    "b_wlevel",
    "c_wlevel",
    "d_wlevel",
    "e_wlevel",
    "f_wlevel",
    "g_wlevel",
    "h_wlevel",
    "i_wlevel",
    "j_wlevel",
    "k_wlevel",
    "l_wlevel",
    "m_wlevel",
    "n_wlevel",
    "o_wlevel",
    "p_wlevel",
    "q_wlevel",
    "r_wlevel",
    "scada_a_wlevel",
    "scada_b_wlevel",
    "scada_c_wlevel",
    "scada_d_wlevel",
    "scada_e_wlevel",
    "scada_f_wlevel",
    "scada_g_wlevel",
    "scada_h_wlevel",
    "scada_i_wlevel",
    "scada_j_wlevel",
    "scada_k_wlevel",
    "scada_l_wlevel",
    "scada_m_wlevel",
    "scada_n_wlevel",
    "scada_o_wlevel",
    "scada_p_wlevel",
    "scada_q_wlevel",
    "scada_r_wlevel",
    "a_storage",
    "b_storage",
    "c_storage",
    "d_storage",
    "e_storage",
    "f_storage",
    "g_storage",
    "h_storage",
    "i_storage",
    "j_storage",
    "k_storage",
    "l_storage",
    "m_storage",
    "n_storage",
    "o_storage",
    "p_storage",
    "q_storage",
    "r_storage",
    "tot_storage",
    "remarks",
    "rec_dt",
    "submit_dt",
    "last_upd_user",
    "last_upd_post",
    "last_upd_dt",
    ods_update_time,
    ods_load_time,
    "dt"
)
select
    sr_id,                                 -- Service Reservior being referenced
    a_wlevel,                              -- A Compartment Water Level
    b_wlevel,                              -- B Compartment Water Level
    c_wlevel,                              -- C Compartment Water Level
    d_wlevel,                              -- D Compartment Water Level
    e_wlevel,                              -- E Compartment Water Level
    f_wlevel,                              -- F Compartment Water Level
    g_wlevel,                              -- G Compartment Water Level
    h_wlevel,                              -- H Compartment Water Level
    i_wlevel,                              -- I Compartment Water Level
    j_wlevel,                              -- J Compartment Water Level
    k_wlevel,                              -- K Compartment Water Level
    l_wlevel,                              -- L Compartment Water Level
    m_wlevel,                              -- M Compartment Water Level
    n_wlevel,                              -- N Compartment Water Level
    o_wlevel,                              -- O Compartment Water Level
    p_wlevel,                              -- P Compartment Water Level
    q_wlevel,                              -- Q Compartment Water Level
    r_wlevel,                              -- R Compartment Water Level
    scada_a_wlevel,                        -- A Compartment Water Level (SCADA)
    scada_b_wlevel,                        -- B Compartment Water Level (SCADA)
    scada_c_wlevel,                        -- C Compartment Water Level (SCADA)
    scada_d_wlevel,                        -- D Compartment Water Level (SCADA)
    scada_e_wlevel,                        -- E Compartment Water Level (SCADA)
    scada_f_wlevel,                        -- F Compartment Water Level (SCADA)
    scada_g_wlevel,                        -- G Compartment Water Level (SCADA)
    scada_h_wlevel,                        -- H Compartment Water Level (SCADA)
    scada_i_wlevel,                        -- I Compartment Water Level (SCADA)
    scada_j_wlevel,                        -- J Compartment Water Level (SCADA)
    scada_k_wlevel,                        -- K Compartment Water Level (SCADA)
    scada_l_wlevel,                        -- L Compartment Water Level (SCADA)
    scada_m_wlevel,                        -- M Compartment Water Level (SCADA)
    scada_n_wlevel,                        -- N Compartment Water Level (SCADA)
    scada_o_wlevel,                        -- O Compartment Water Level (SCADA)
    scada_p_wlevel,                        -- P Compartment Water Level (SCADA)
    scada_q_wlevel,                        -- Q Compartment Water Level (SCADA)
    scada_r_wlevel,                        -- R Compartment Water Level (SCADA)
    a_storage,                             -- Volume of water in A compartment of an SR.  Unit is in cu m
    b_storage,                             -- Volume of water in B compartment of an SR.  Unit is in cu m
    c_storage,                             -- Volume of water in C compartment of an SR.  Unit is in cu m
    d_storage,                             -- Volume of water in D compartment of an SR.  Unit is in cu m
    e_storage,                             -- Volume of water in E compartment of an SR.  Unit is in cu m
    f_storage,                             -- Volume of water in F compartment of an SR.  Unit is in cu m
    g_storage,                             -- Volume of water in G compartment of an SR.  Unit is in cu m
    h_storage,                             -- Volume of water in H compartment of an SR.  Unit is in cu m
    i_storage,                             -- Volume of water in I compartment of an SR.  Unit is in cu m
    j_storage,                             -- Volume of water in J compartment of an SR.  Unit is in cu m
    k_storage,                             -- Volume of water in K compartment of an SR.  Unit is in cu m
    l_storage,                             -- Volume of water in L compartment of an SR.  Unit is in cu m
    m_storage,                             -- Volume of water in M compartment of an SR.  Unit is in cu m
    n_storage,                             -- Volume of water in N compartment of an SR.  Unit is in cu m
    o_storage,                             -- Volume of water in O compartment of an SR.  Unit is in cu m
    p_storage,                             -- Volume of water in P compartment of an SR.  Unit is in cu m
    q_storage,                             -- Volume of water in Q compartment of an SR.  Unit is in cu m
    r_storage,                             -- Volume of water in R compartment of an SR.  Unit is in cu m
    tot_storage,                           -- Total volume of water in A+ B+..+R.  Unit is in cu m
    remarks,                               -- Remarks
    rec_dt,                                -- Date of record
    submit_dt,                             -- Submission Date
    last_upd_user,                         -- Last Update By (Username)
    last_upd_post,                         -- Last Update By (Post)
    last_upd_dt,                           -- Last Update Date
    current_timestamp as ods_update_time,  -- Data Warehouse update Time
    current_timestamp as ods_load_time,    -- Data Warehouse load Time
    to_char(rec_dt, 'yyyymmdd')::decimal(10) as "dt"  -- Daily Partitions
from coss_ods.ods_sttss_srs_sr_storage_di_year_tmp
on duplicate key update
    "a_wlevel" = values("a_wlevel"),
    "b_wlevel" = values("b_wlevel"),
    "c_wlevel" = values("c_wlevel"),
    "d_wlevel" = values("d_wlevel"),
    "e_wlevel" = values("e_wlevel"),
    "f_wlevel" = values("f_wlevel"),
    "g_wlevel" = values("g_wlevel"),
    "h_wlevel" = values("h_wlevel"),
    "i_wlevel" = values("i_wlevel"),
    "j_wlevel" = values("j_wlevel"),
    "k_wlevel" = values("k_wlevel"),
    "l_wlevel" = values("l_wlevel"),
    "m_wlevel" = values("m_wlevel"),
    "n_wlevel" = values("n_wlevel"),
    "o_wlevel" = values("o_wlevel"),
    "p_wlevel" = values("p_wlevel"),
    "q_wlevel" = values("q_wlevel"),
    "r_wlevel" = values("r_wlevel"),
    "scada_a_wlevel" = values("scada_a_wlevel"),
    "scada_b_wlevel" = values("scada_b_wlevel"),
    "scada_c_wlevel" = values("scada_c_wlevel"),
    "scada_d_wlevel" = values("scada_d_wlevel"),
    "scada_e_wlevel" = values("scada_e_wlevel"),
    "scada_f_wlevel" = values("scada_f_wlevel"),
    "scada_g_wlevel" = values("scada_g_wlevel"),
    "scada_h_wlevel" = values("scada_h_wlevel"),
    "scada_i_wlevel" = values("scada_i_wlevel"),
    "scada_j_wlevel" = values("scada_j_wlevel"),
    "scada_k_wlevel" = values("scada_k_wlevel"),
    "scada_l_wlevel" = values("scada_l_wlevel"),
    "scada_m_wlevel" = values("scada_m_wlevel"),
    "scada_n_wlevel" = values("scada_n_wlevel"),
    "scada_o_wlevel" = values("scada_o_wlevel"),
    "scada_p_wlevel" = values("scada_p_wlevel"),
    "scada_q_wlevel" = values("scada_q_wlevel"),
    "scada_r_wlevel" = values("scada_r_wlevel"),
    "a_storage" = values("a_storage"),
    "b_storage" = values("b_storage"),
    "c_storage" = values("c_storage"),
    "d_storage" = values("d_storage"),
    "e_storage" = values("e_storage"),
    "f_storage" = values("f_storage"),
    "g_storage" = values("g_storage"),
    "h_storage" = values("h_storage"),
    "i_storage" = values("i_storage"),
    "j_storage" = values("j_storage"),
    "k_storage" = values("k_storage"),
    "l_storage" = values("l_storage"),
    "m_storage" = values("m_storage"),
    "n_storage" = values("n_storage"),
    "o_storage" = values("o_storage"),
    "p_storage" = values("p_storage"),
    "q_storage" = values("q_storage"),
    "r_storage" = values("r_storage"),
    "tot_storage" = values("tot_storage"),
    "remarks" = values("remarks"),
    "submit_dt" = values("submit_dt"),
    "last_upd_user" = values("last_upd_user"),
    "last_upd_post" = values("last_upd_post"),
    ods_update_time = values(ods_update_time)
```



# dwd

## dwd_rws_etl_raw_water_supply_asset_day（调度任务）

调度任务前置任务节点名称

```tex
dwd_rws_etl_raw_water_supply_asset_day_sql_dwd_ass_channels_df_all
dwd_rws_etl_raw_water_supply_asset_day_sql_dwd_ass_ir_df_all
dwd_rws_etl_raw_water_supply_asset_day_sql_dwd_ass_ps_df_all
dwd_rws_etl_raw_water_supply_asset_day_sql_dwd_ass_rw_src_df_all
dwd_rws_etl_raw_water_supply_asset_day_sql_dwd_ass_sr_df_all
dwd_rws_etl_raw_water_supply_asset_day_sql_dwd_ass_wtw_df_all
```



### 1.coss_dwd.dwd_ass_channels_df

#### create table 

```sql
drop table if exists coss_dwd.dwd_ass_channels_df;

create table if not exists coss_dwd.dwd_ass_channels_df (
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

comment on table coss_dwd.dwd_ass_channels_df is 'Water Transfer Channels Information';
comment on column coss_dwd.dwd_ass_channels_df.option_no        is 'Option No.';
comment on column coss_dwd.dwd_ass_channels_df.ch_id            is 'System Generated ID of a Water Transfer Channel';
comment on column coss_dwd.dwd_ass_channels_df.src_id           is 'Source of Water Inflow';
comment on column coss_dwd.dwd_ass_channels_df.dest_id          is 'Destination of Water Outflow';
comment on column coss_dwd.dwd_ass_channels_df.rlabel           is 'Labels Used In Reports';
comment on column coss_dwd.dwd_ass_channels_df.w_usage          is 'Water Usage';
comment on column coss_dwd.dwd_ass_channels_df.w_usage_desc     is 'Possible Values: {"Commissioning Test to Waste", "Commissioning Test to be Returned to System", "Augmented Supply for Flushing", Commission Test to be Used for Consumption}';
comment on column coss_dwd.dwd_ass_channels_df.w_type           is 'Type of Water Maintained by the Installation';
comment on column coss_dwd.dwd_ass_channels_df.w_type_desc      is 'Description of Water Type';
comment on column coss_dwd.dwd_ass_channels_df.calc_id          is 'Calculation Logic Being Referenced by Daily Water Transfer Volume of Channels';
comment on column coss_dwd.dwd_ass_channels_df.calc_usage       is 'Determines if the Referenced Channel or Internal Circulation is Used as Summation or Difference Possible Values:{"S" - Sum, "D" - Difference}';
comment on column coss_dwd.dwd_ass_channels_df.meas_code        is 'Measured By';
comment on column coss_dwd.dwd_ass_channels_df.meas_desc        is 'Description of Measurement';
comment on column coss_dwd.dwd_ass_channels_df.meas_cdesc       is 'Chinese Description of Measurement Type';
comment on column coss_dwd.dwd_ass_channels_df.dwd_update_time  is 'Data Update Time';
comment on column coss_dwd.dwd_ass_channels_df.dwd_load_time    is 'Data Loading Time';

```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Assets
-- Function Describe: Water Transfer Channels Information
-- Create         By: dongmaochen
-- Create       Date: 2025-04-24
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:
-- coss_ods.ods_sttss_rws_water_usage_df
-- coss_ods.ods_sttss_rws_w_type_df
-- coss_ods.ods_sttss_rws_calc_di
-- coss_ods.ods_sttss_rws_measurement_df
-- coss_ods.ods_sttss_rws_channel_di
-- Target Table:  coss_dwd.dwd_ass_channels_df
-- ****************************************************************************************
drop table if exists coss_tmp.tmp_dwd_ass_channels_df_1;
create table if not exists coss_tmp.tmp_dwd_ass_channels_df_1 as
select
    t.option_no      as option_no,        -- Option No.
    t.ch_id         as ch_id,             -- System generated ID of a water transfer channel
    t.src_id        as src_id,            -- Source of Water Inflow
    t.dest_id       as dest_id,           -- Destination of Water outflow
    t.rlabel        as rlabel,            -- Labels used in reports
    t.water_usage   as w_usage,           -- Water Usage
    t1.descrip      as w_usage_desc,      -- Possible Values: {"Commissioning Test to Waste", "Commissioning Test to be Returned to System", "Augmented Supply for Flushing", Commission Test to be Used for Consumption}
    t.w_type        as w_type,            -- Type of water maintained by the installation
    t2.descrip      as w_type_desc,       -- Description of Water Type
    t.calc_id       as calc_id,           -- Calculation logic being referenced by daily water transfer volume of channels
    t.m_code        as meas_code          -- Measured By
from coss_ods.ods_sttss_rws_channel_di t
left join coss_ods.ods_sttss_rws_water_usage_df t1
    on t.water_usage = t1.code
left join coss_ods.ods_sttss_rws_w_type_df t2
    on t.w_type = t2.code;

-- Step 2: Load data to target dimension table (full refresh)
insert into coss_dwd.dwd_ass_channels_df (
    option_no,
    ch_id,
    src_id,
    dest_id,
    rlabel,
    w_usage,
    w_usage_desc,
    w_type,
    w_type_desc,
    calc_id,
    calc_usage,
    meas_code,
    meas_desc,
    meas_cdesc,
    dwd_update_time,
    dwd_load_time
)
select
    t.option_no      as option_no,        -- Option No.
    t.ch_id         as ch_id,             -- System generated ID of a water transfer channel
    t.src_id        as src_id,            -- Source of Water Inflow
    t.dest_id       as dest_id,           -- Destination of Water outflow
    t.rlabel        as rlabel,            -- Labels used in reports
    t.w_usage       as w_usage,           -- Water Usage
    t.w_usage_desc  as w_usage_desc,      -- Possible Values: {"Commissioning Test to Waste", "Commissioning Test to be Returned to System", "Augmented Supply for Flushing", Commission Test to be Used for Consumption}
    t.w_type        as w_type,            -- Type of water maintained by the installation
    t.w_type_desc   as w_type_desc,       -- Description of Water Type
    t.calc_id       as calc_id,           -- Calculation logic being referenced by daily water transfer volume of channels
    t2.usage        as calc_usage,        -- Determines if the referenced Channel or Internal Circulation is used as summation or difference Possible Values:{"S" - Sum, "D" - Difference}
    t.meas_code     as meas_code,         -- Measured By
    t3.descrip      as meas_desc,         -- Description of Measurement
    t3.cdescrip     as meas_cdesc,        -- Chinese Description of Measurement Type
    current_timestamp as dwd_update_time, -- Data Warehouse update Time
    current_timestamp as dwd_load_time    -- Data Warehouse load Time
from coss_tmp.tmp_dwd_ass_channels_df_1 t
left join coss_ods.ods_sttss_rws_calc_di t2
    on t.calc_id = t2.calc_id
    and t.ch_id = t2.ref_id  -- Join by calculation ID and channel reference ID
left join coss_ods.ods_sttss_rws_measurement_df t3
    on t.meas_code = t3.code  -- Join by measurement code
on duplicate key update
  rlabel = values(rlabel),
  w_usage = values(w_usage),
  w_usage_desc = values(w_usage_desc),
  w_type = values(w_type),
  w_type_desc = values(w_type_desc),
  calc_id = values(calc_id),
  calc_usage = values(calc_usage),
  meas_code = values(meas_code),
  meas_desc = values(meas_desc),
  meas_cdesc = values(meas_cdesc),
  dwd_update_time = values(dwd_update_time)
```

### 2.coss_dwd.dwd_ass_ir_df

#### create table

```sql
drop table if exists coss_dwd.dwd_ass_ir_df;

create table if not exists coss_dwd.dwd_ass_ir_df (
    ig_id             varchar(20),        -- Impounding Reservoir Group ID with format IGNNNNNNNN
    ig_name           varchar(200),       -- Name of Impounding Reservoir Group
    ig_cname          varchar(300),       -- Chinese Name of Impounding Reservoir Group
    ig_rpt_label      varchar(400),       -- Labels used in reports
    region_code       varchar(10),        -- Region
    region_name       varchar(60),        -- Description of Region
    region_cname      varchar(300),       -- Chinese Description of Region
    region_ind        varchar(2),         -- Possible Values: {"I" - HK Island, "M" - Mainland}
    ig_ind            varchar(2),         -- Indicates if Impounding Reservoir Group is old or new. Possible Values: {"Y" - Old, "N" - New}
    ir_id             varchar(20),        -- Impounding Reservoir ID with format IRNNNNNNNN
    i_code            varchar(10),        -- Installation Code of Impounding Reservoir
    ir_rpt_label      varchar(400),       -- Labels used in reports
    ir_name           varchar(200),       -- Impounding reservoir name
    ir_cname          varchar(300),       -- Impounding Reservoir Chinese Name
    level_type        varchar(2),         -- Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}
    level_unit        varchar(2),         -- Possible Values:{"F" - Feet / Inch, "M" - Meter}
    dead_storage      decimal(12, 4),     -- Dead Storage of an Impounding Reservoir.  Unit is in mcm
    twl               decimal(12, 4),     -- TWL
    capacity          decimal(12, 4),     -- Capacity of IR.  Unit is in mcm
    min_storage       decimal(12, 4),     -- Allowable Minimum Storage.  Unit is in mcm
    limit_m           decimal(12, 4),     -- Preset Limit for Water Level.  Unit is in m
    dwd_update_time   timestamp(6) default current_timestamp,
    dwd_load_time     timestamp(6) default current_timestamp,
    primary key (ig_id, ir_id)
) ;

comment on table coss_dwd.dwd_ass_ir_df is 'Impounding Reservoir Information';
comment on column coss_dwd.dwd_ass_ir_df.ig_id            is 'Impounding Reservoir Group ID with format IGNNNNNNNN';
comment on column coss_dwd.dwd_ass_ir_df.ig_name          is 'Name of Impounding Reservoir Group';
comment on column coss_dwd.dwd_ass_ir_df.ig_cname         is 'Chinese Name of Impounding Reservoir Group';
comment on column coss_dwd.dwd_ass_ir_df.ig_rpt_label     is 'Labels Used In Reports';
comment on column coss_dwd.dwd_ass_ir_df.region_code      is 'Region';
comment on column coss_dwd.dwd_ass_ir_df.region_name      is 'Description of Region';
comment on column coss_dwd.dwd_ass_ir_df.region_cname     is 'Chinese Description of Region';
comment on column coss_dwd.dwd_ass_ir_df.region_ind       is 'Possible Values: {"I" - HK Island, "M" - Mainland}';
comment on column coss_dwd.dwd_ass_ir_df.ig_ind           is 'Indicates if Impounding Reservoir Group is Old or New. Possible Values: {"Y" - Old, "N" - New}';
comment on column coss_dwd.dwd_ass_ir_df.ir_id            is 'Impounding Reservoir ID with format IRNNNNNNNN';
comment on column coss_dwd.dwd_ass_ir_df.i_code           is 'Installation Code of Impounding Reservoir';
comment on column coss_dwd.dwd_ass_ir_df.ir_rpt_label     is 'Labels Used In Reports';
comment on column coss_dwd.dwd_ass_ir_df.ir_name          is 'Impounding Reservoir Name';
comment on column coss_dwd.dwd_ass_ir_df.ir_cname         is 'Impounding Reservoir Chinese Name';
comment on column coss_dwd.dwd_ass_ir_df.level_type       is 'Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}';
comment on column coss_dwd.dwd_ass_ir_df.level_unit       is 'Possible Values:{"F" - Feet / Inch, "M" - Meter}';
comment on column coss_dwd.dwd_ass_ir_df.dead_storage     is 'Dead Storage of an Impounding Reservoir.  Unit is in mcm';
comment on column coss_dwd.dwd_ass_ir_df.twl              is 'TWL (Top Water Level)';
comment on column coss_dwd.dwd_ass_ir_df.capacity         is 'Capacity of Impounding Reservoir.  Unit is in mcm';
comment on column coss_dwd.dwd_ass_ir_df.min_storage      is 'Allowable Minimum Storage of Impounding Reservoir.  Unit is in mcm';
comment on column coss_dwd.dwd_ass_ir_df.limit_m          is 'Preset Limit for Water Level.  Unit is in m';
comment on column coss_dwd.dwd_ass_ir_df.dwd_update_time  is 'Data Update Time';
comment on column coss_dwd.dwd_ass_ir_df.dwd_load_time    is 'Data Loading Time';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Assets
-- Function Describe: Impounding Reservoir Information
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_rws_ir_df
-- coss_ods.ods_sttss_rws_ir_group_df
-- coss_ods.ods_sttss_rws_region_df
-- Target Table:  
-- coss_dwd.dwd_ass_ir_df
-- ****************************************************************************************
-- Step: Full refresh target dimension table (delete old data then insert new data)
insert into coss_dwd.dwd_ass_ir_df (
    ig_id,
    ig_name,
    ig_cname,
    ig_rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    ig_ind,
    ir_id,
    i_code,
    ir_rpt_label,
    ir_name,
    ir_cname,
    level_type,
    level_unit,
    dead_storage,
    twl,
    capacity,
    min_storage,
    limit_m,
    dwd_update_time,
    dwd_load_time
)
select
    t1.ig_id           as ig_id,            -- Impounding Reservoir Group ID with format IGNNNNNNNN
    t1.ig_name         as ig_name,          -- Name of Impounding Reservoir Group
    t1.ig_cname        as ig_cname,         -- Chinese Name of Impounding Reservoir Group
    t1.rlabel          as ig_rpt_label,     -- Labels used in reports
    -- Convert region code: Map 'HK' to 'HKI' (HK Island) for consistency with region dimension
    case
        when t1.region = 'HK' then 'HKI'
        else t1.region
    end as region_code,                     -- Region
    t2.descrip         as region_name,      -- Description of Region
    t2.cdescrip        as region_cname,     -- Chinese Description of Region
    t2.indicator       as region_ind,       -- Possible Values: {"I" - HK Island, "M" - Mainland}
    t1.old_ind         as ig_ind,           -- Indicates if Impounding Reservoir Group is old or new. Possible Values: {"Y" - Old, "N" - New}
    t.ir_id            as ir_id,            -- Impounding Reservoir ID with format IRNNNNNNNN
    t.i_code           as i_code,           -- Installation Code of Impounding Reservoir
    t.rlabel           as ir_rpt_label,     -- Labels used in reports
    t.ir_name          as ir_name,          -- Impounding reservoir name
    t.ir_cname         as ir_cname,         -- Impounding Reservoir Chinese Name
    t.level_type       as level_type,       -- Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}
    t.level_unit       as level_unit,       -- Possible Values:{"F" - Feet / Inch, "M" - Meter}
    t.dead_storage     as dead_storage,     -- Dead Storage of an Impounding Reservoir.  Unit is in mcm
    t.twl              as twl,              -- TWL
    t.capacity         as capacity,         -- Capacity of IR.  Unit is in mcm
    t.min_storage      as min_storage,      -- Allowable Minimum Storage.  Unit is in mcm
    t.limit_m          as limit_m,          -- Preset Limit for Water Level.  Unit is in m
    current_timestamp  as dwd_update_time,  -- Data Warehouse update Time
    current_timestamp  as dwd_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_ir_df t  -- Main table: Impounding Reservoir base info
left join coss_ods.ods_sttss_rws_ir_group_df t1  -- Join: Reservoir Group dimension
    on t.ig_id = t1.ig_id
left join coss_ods.ods_sttss_rws_region_df t2  -- Join: Region dimension
    on t1.region = t2.code
on duplicate key update
    ig_name = values(ig_name),
    ig_cname = values(ig_cname),
    ig_rpt_label = values(ig_rpt_label),
    region_code = values(region_code),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    ig_ind = values(ig_ind),
    i_code = values(i_code),
    ir_rpt_label = values(ir_rpt_label),
    ir_name = values(ir_name),
    ir_cname = values(ir_cname),
    level_type = values(level_type),
    level_unit = values(level_unit),
    dead_storage = values(dead_storage),
    twl = values(twl),
    capacity = values(capacity),
    min_storage = values(min_storage),
    limit_m = values(limit_m),
    dwd_update_time = values(dwd_update_time)
```

### 3.coss_dwd.dwd_ass_ps_df

#### create table

```sql
drop table if exists coss_dwd.dwd_ass_ps_df;

create table if not exists coss_dwd.dwd_ass_ps_df (
    ps_id             varchar(20),        -- Pumping Station ID with format PSNNNNNNNN
    i_code            varchar(10),        -- Installation Code of Pumping Station
    ps_name           varchar(200),       -- Pumping Station Name
    ps_cname          varchar(300),       -- Pumping Station Chinese Name
    rpt_label         varchar(400),       -- Labels used in reports
    region_code       varchar(10),        -- Region
    region_name       varchar(60),        -- Description of Region
    region_cname      varchar(300),       -- Chinese Description of Region
    region_ind        varchar(2),         -- Possible Values: {"I" - HK Island, "M" - Mainland}
    w_type            varchar(2),         -- Type of water maintained in the pumping station
    w_type_desc       varchar(200),       -- Description of Water Type
    repumping         varchar(2),         -- Repumping (Indicator for repumping function)
    remarks           varchar(200),       -- Remarks
    dwd_update_time   timestamp(6) default current_timestamp,
    dwd_load_time     timestamp(6) default current_timestamp,
    primary key (ps_id)
) ;

comment on table coss_dwd.dwd_ass_ps_df is 'Pumping Station Information';
comment on column coss_dwd.dwd_ass_ps_df.ps_id            is 'Pumping Station ID with format PSNNNNNNNN (System-generated unique ID)';
comment on column coss_dwd.dwd_ass_ps_df.i_code           is 'Installation Code of Pumping Station (Unique operational code)';
comment on column coss_dwd.dwd_ass_ps_df.ps_name          is 'Pumping Station Name (English name for operational reference)';
comment on column coss_dwd.dwd_ass_ps_df.ps_cname         is 'Pumping Station Chinese Name (Chinese name for reporting)';
comment on column coss_dwd.dwd_ass_ps_df.rpt_label        is 'Labels used in reports (Custom labels for report display)';
comment on column coss_dwd.dwd_ass_ps_df.region_code      is 'Region (Standardized region code)';
comment on column coss_dwd.dwd_ass_ps_df.region_name      is 'Description of Region (English name of the region)';
comment on column coss_dwd.dwd_ass_ps_df.region_cname     is 'Chinese Description of Region (Chinese name of the region)';
comment on column coss_dwd.dwd_ass_ps_df.region_ind       is 'Possible Values: {"I" - HK Island, "M" - Mainland} (Region category indicator)';
comment on column coss_dwd.dwd_ass_ps_df.w_type           is 'Type of water maintained in the pumping station (Water type code)';
comment on column coss_dwd.dwd_ass_ps_df.w_type_desc      is 'Description of Water Type (English description of water type)';
comment on column coss_dwd.dwd_ass_ps_df.repumping        is 'Repumping (Indicator: e.g., "Y" = Has repumping function, "N" = No repumping function)';
comment on column coss_dwd.dwd_ass_ps_df.remarks          is 'Remarks (Additional operational notes)';
comment on column coss_dwd.dwd_ass_ps_df.dwd_update_time  is 'Data Update Time (Timestamp of last data update)';
comment on column coss_dwd.dwd_ass_ps_df.dwd_load_time    is 'Data Loading Time (Timestamp of initial data load)';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Assets
-- Function Describe: Pumping Station Information
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_rws_ps_di
-- coss_ods.ods_sttss_rws_region_df
-- coss_ods.ods_sttss_rws_w_type_df
-- Target Table:  
-- coss_dwd.dwd_ass_ps_df
-- ****************************************************************************************
-- Step: Full refresh target dimension table (delete old data first, then insert new data)
insert into coss_dwd.dwd_ass_ps_df (
    ps_id,
    i_code,
    ps_name,
    ps_cname,
    rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    w_type,
    w_type_desc,
    repumping,
    remarks,
    dwd_update_time,
    dwd_load_time
)
select
    t.ps_id            as ps_id,              -- Pumping Station ID with format PSNNNNNNNN
    t.i_code           as i_code,             -- Installation Code of Pumping Station
    t.ps_name          as ps_name,            -- Pumping Station Name
    t.ps_cname         as ps_cname,           -- Pumping Station Chinese Name
    t.rlabel           as rpt_label,          -- Labels used in reports
    -- Standardize region code: Map "HK" to "HKI" (HK Island) to align with region dimension table
    case
        when t.region = 'HK' then 'HKI'
        else t.region
    end as region_code,                     -- Region
    t1.descrip         as region_name,        -- Description of Region
    t1.cdescrip        as region_cname,       -- Chinese Description of Region
    t1.indicator       as region_ind,         -- Possible Values: {"I" - HK Island, "M" - Mainland}
    t.w_type           as w_type,             -- Type of water maintained in the pumping station
    t2.descrip         as w_type_desc,        -- Description of Water Type
    t.repumping        as repumping,          -- Repumping
    t.remark           as remarks,            -- Remarks (Map source "remark" to target "remarks" for consistency)
    current_timestamp  as dwd_update_time,    -- Data Warehouse update Time
    current_timestamp  as dwd_load_time       -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_ps_di t  -- Main source: Pumping Station base information table
left join coss_ods.ods_sttss_rws_region_df t1  -- Join 1: Region dimension table (for region attributes)
    on t.region = t1.code  -- Join condition: Match pumping station's region code with region dimension code
left join coss_ods.ods_sttss_rws_w_type_df t2  -- Join 2: Water type dimension table (for water type description)
    on t.w_type = t2.code -- Join condition: Match pumping station's water type code with water type dimension code
on duplicate key update
    i_code = values(i_code),
    ps_name = values(ps_name),
    ps_cname = values(ps_cname),
    rpt_label = values(rpt_label),
    region_code = values(region_code),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    w_type = values(w_type),
    w_type_desc = values(w_type_desc),
    repumping = values(repumping),
    remarks = values(remarks),
    dwd_update_time = values(dwd_update_time)
```

### 4.coss_dwd.dwd_ass_rw_src_df

#### create table

```sql
drop table if exists coss_dwd.dwd_ass_rw_src_df;

create table if not exists coss_dwd.dwd_ass_rw_src_df (
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

comment on table coss_dwd.dwd_ass_rw_src_df is 'Raw Water Source Information';
comment on column coss_dwd.dwd_ass_rw_src_df.rw_id            is 'Raw Water Source ID with format RWNNNNNNNN (System-generated unique ID)';
comment on column coss_dwd.dwd_ass_rw_src_df.rw_name          is 'Name of Raw Water (English name of the raw water source)';
comment on column coss_dwd.dwd_ass_rw_src_df.rw_cname         is 'Chinese Name of Raw Water (Chinese name of the raw water source)';
comment on column coss_dwd.dwd_ass_rw_src_df.rpt_label        is 'Labels used in reports (Custom labels for report display)';
comment on column coss_dwd.dwd_ass_rw_src_df.region_code      is 'Region Code (Standardized region code aligned with region dimension)';
comment on column coss_dwd.dwd_ass_rw_src_df.region_name      is 'Description of Region (English name of the region)';
comment on column coss_dwd.dwd_ass_rw_src_df.region_cname     is 'Chinese Description of Region (Chinese name of the region)';
comment on column coss_dwd.dwd_ass_rw_src_df.region_ind       is 'Possible Values: {"I" - HK Island, "M" - Mainland} (Region category indicator)';
comment on column coss_dwd.dwd_ass_rw_src_df.ig_ind           is 'Indicates if Impounding Reservoir Group is old or new. Possible Values: {"Y" - Old, "N" - New} (Null for non-reservoir sources)';
comment on column coss_dwd.dwd_ass_rw_src_df.source_rw        is 'Source of raw water (Source type code: e.g., "O" = Others, "G" = Guangdong)';
comment on column coss_dwd.dwd_ass_rw_src_df.source_desc      is 'Description of Raw Water Source (Text description of the source type)';
comment on column coss_dwd.dwd_ass_rw_src_df.dwd_update_time  is 'Data Update Time (Timestamp of last data update)';
comment on column coss_dwd.dwd_ass_rw_src_df.dwd_load_time    is 'Data Loading Time (Timestamp of initial data load)';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Assets
-- Function Describe: Raw Water Source Information
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_rws_ir_group_df
-- coss_ods.ods_sttss_rws_region_df
-- coss_ods.ods_sttss_rws_rw_df
-- coss_ods.ods_sttss_rws_rw_type_df
-- Target Table:  
-- coss_dwd.dwd_ass_rw_src_df
-- ****************************************************************************************
-- Step 1: Create temporary table 1 - Extract raw water sources from Impounding Reservoir Group
drop table if exists coss_tmp.tmp_dwd_ass_rw_src_df_1;
create table if not exists coss_tmp.tmp_dwd_ass_rw_src_df_1 as
select
    t.ig_id               as rw_id,               -- Map Reservoir Group ID (ig_id) to Raw Water Source ID (rw_id)
    t.ig_name             as rw_name,             -- Map Reservoir Group Name to Raw Water Name
    t.ig_cname            as rw_cname,            -- Map Reservoir Group Chinese Name to Raw Water Chinese Name
    t.rlabel              as rpt_label,           -- Labels used in reports
    t.region              as region_code,         -- Region Code (to be standardized later)
    t1.descrip            as region_name,         -- Description of Region (from region dimension)
    t1.cdescrip           as region_cname,        -- Chinese Description of Region (from region dimension)
    t1.indicator          as region_ind,          -- Possible Values: {"I" - HK Island, "M" - Mainland}
    t.old_ind             as ig_ind,              -- Reservoir Group old/new indicator (unique to reservoir sources)
    'O'                   as source_rw,           -- Hardcode source type: "O" = Others (reservoir group as raw water source)
    'Others'              as source_desc          -- Hardcode source description: "Others"
from coss_ods.ods_sttss_rws_ir_group_df t  -- Source 1: Impounding Reservoir Group table
left join coss_ods.ods_sttss_rws_region_df t1
    on t.region = t1.code;  -- Join with region dimension to get region attributes


-- Step 2: Create temporary table 2 - Extract raw water sources from Raw Water base table
drop table if exists coss_tmp.tmp_dwd_ass_rw_src_df_2;
create table if not exists coss_tmp.tmp_dwd_ass_rw_src_df_2 as
select
    t.rw_id               as rw_id,               -- Raw Water Source ID (direct from base table)
    t.rw_name             as rw_name,             -- Name of Raw Water (direct from base table)
    t.rw_cname            as rw_cname,            -- Chinese Name of Raw Water (direct from base table)
    t.rlabel              as rpt_label,           -- Labels used in reports (direct from base table)
    t.region              as region_code,         -- Region Code (to be standardized later)
    t1.descrip            as region_name,         -- Description of Region (from region dimension)
    t1.cdescrip           as region_cname,        -- Chinese Description of Region (from region dimension)
    t1.indicator          as region_ind,          -- Possible Values: {"I" - HK Island, "M" - Mainland}
    ' '                   as ig_ind,              -- Empty for non-reservoir sources (no reservoir group attribute)
    t.source              as source_rw,           -- Source of raw water (code from base table)
    t2.descrip            as source_desc          -- Source description (from raw water type dimension)
from coss_ods.ods_sttss_rws_rw_df t  -- Source 2: Raw Water base table
left join coss_ods.ods_sttss_rws_region_df t1
    on t.region = t1.code  -- Join with region dimension to get region attributes
left join coss_ods.ods_sttss_rws_rw_type_df t2
    on t.source = t2.code;  -- Join with raw water type dimension to get source description


-- Step 3: Full refresh target dimension table (union two temp tables + standardize region code)
insert into coss_dwd.dwd_ass_rw_src_df (
    rw_id,
    rw_name,
    rw_cname,
    rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    ig_ind,
    source_rw,
    source_desc,
    dwd_update_time,
    dwd_load_time
)
select
    rw_id,                               -- Raw Water Source ID with format RWNNNNNNNN
    rw_name,                              -- Name of Raw Water
    rw_cname,                             -- Chinese Name of Raw Water
    rpt_label,                            -- Labels used in reports
    -- Standardize region code: Map "HK" to "HKI" (HK Island) to align with region dimension table
    case
        when region_code = 'HK' then 'HKI'
        else region_code
    end as region_code,                   -- Region Code
    region_name,                          -- Description of Region
    region_cname,                         -- Chinese Description of Region
    region_ind,                           -- Possible Values: {"I" - HK Island, "M" - Mainland}
    ig_ind,                               -- Indicates if Impounding Reservoir Group is old or new
    source_rw,                            -- Source of raw water
    source_desc,                          -- Description of Raw Water Source
    current_timestamp as dwd_update_time, -- Data Warehouse update Time
    current_timestamp as dwd_load_time    -- Data Warehouse load Time
from (
    -- Union two temporary tables: Combine reservoir group sources and base raw water sources
    select * from coss_tmp.tmp_dwd_ass_rw_src_df_1
    union all
    select * from coss_tmp.tmp_dwd_ass_rw_src_df_2
) as unioned_data  -- Alias for unioned result set
on duplicate key update
    rw_name = values(rw_name),
    rw_cname = values(rw_cname),
    rpt_label = values(rpt_label),
    region_code = values(region_code),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    ig_ind = values(ig_ind),
    source_rw = values(source_rw),
    source_desc = values(source_desc),
    dwd_update_time = values(dwd_update_time)
```

### 5.coss_dwd.dwd_ass_sr_df

#### create table

```sql
drop table if exists coss_dwd.dwd_ass_sr_df;

create table if not exists coss_dwd.dwd_ass_sr_df (
    sr_id             varchar(20),        -- Service Reservoir ID with format SRNNNNNNNN
    i_code            varchar(10),        -- Installation Code of Service Reservoir
    sr_name           varchar(200),       -- Service Reservoir Name
    sr_cname          varchar(300),       -- Service Reservoir Chinese Name
    rpt_label         varchar(400),       -- Labels used in reports
    region_code       varchar(5),         -- Region (Standardized code)
    region_name       varchar(60),        -- Description of Region
    region_cname      varchar(300),       -- Chinese Description of Region
    region_ind        varchar(2),         -- Possible Values: {"I" - HK Island, "M" - Mainland}
    w_type            varchar(2),         -- Type of water maintained by the service reservoir
    w_type_desc       varchar(200),       -- Description of Water Type
    div_height        decimal(12, 4),     -- Height of Division Wall.  Unit is in m
    capacity          decimal(12, 4),     -- Capacity of Service Reservoir.  Unit is in cu m
    w_lim             decimal(12, 4),     -- Preset Limit for Water Level above division wall.  Unit is in m
    num_of_storage    decimal(10),        -- No. of Storage/Compartment
    dwd_update_time   timestamp(6) default current_timestamp,
    dwd_load_time     timestamp(6) default current_timestamp,
    primary key (sr_id)
);

comment on table coss_dwd.dwd_ass_sr_df is 'Service Reservoir Information';
comment on column coss_dwd.dwd_ass_sr_df.sr_id             is 'Service Reservoir ID with format SRNNNNNNNN (System-generated unique ID)';
comment on column coss_dwd.dwd_ass_sr_df.i_code            is 'Installation Code of Service Reservoir (Unique operational code)';
comment on column coss_dwd.dwd_ass_sr_df.sr_name           is 'Service Reservoir Name (English name for operational reference)';
comment on column coss_dwd.dwd_ass_sr_df.sr_cname          is 'Service Reservoir Chinese Name (Chinese name for reporting and management)';
comment on column coss_dwd.dwd_ass_sr_df.rpt_label         is 'Labels used in reports (Custom labels for report display, e.g., abbreviations)';
comment on column coss_dwd.dwd_ass_sr_df.region_code       is 'Region (Standardized code aligned with region dimension table, e.g., "HKI" for HK Island)';
comment on column coss_dwd.dwd_ass_sr_df.region_name       is 'Description of Region (English name of the region, from region dimension table)';
comment on column coss_dwd.dwd_ass_sr_df.region_cname      is 'Chinese Description of Region (Chinese name of the region, from region dimension table)';
comment on column coss_dwd.dwd_ass_sr_df.region_ind        is 'Possible Values: {"I" - HK Island, "M" - Mainland} (Region category indicator)';
comment on column coss_dwd.dwd_ass_sr_df.w_type            is 'Type of water maintained by the service reservoir (Water type code, e.g., "R" for Raw Water)';
comment on column coss_dwd.dwd_ass_sr_df.w_type_desc       is 'Description of Water Type (English description of water type, from water type dimension table)';
comment on column coss_dwd.dwd_ass_sr_df.div_height        is 'Height of Division Wall.  Unit is in m (Structural parameter of the reservoir)';
comment on column coss_dwd.dwd_ass_sr_df.capacity          is 'Capacity of Service Reservoir.  Unit is in cu m (Total storage volume of the reservoir)';
comment on column coss_dwd.dwd_ass_sr_df.w_lim             is 'Preset Limit for Water Level above division wall.  Unit is in m (Safety control threshold)';
comment on column coss_dwd.dwd_ass_sr_df.num_of_storage    is 'No. of Storage/Compartment (Number of independent storage compartments in the reservoir)';
comment on column coss_dwd.dwd_ass_sr_df.dwd_update_time   is 'Data Update Time (Timestamp of last data modification in the warehouse)';
comment on column coss_dwd.dwd_ass_sr_df.dwd_load_time     is 'Data Loading Time (Timestamp of initial data loading into the warehouse)';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Assets
-- Function Describe: Service Reservoir Information
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_rws_sr_di
-- coss_ods.ods_sttss_rws_region_df
-- coss_ods.ods_sttss_rws_w_type_df
-- Target Table:  
-- coss_dwd.dwd_ass_sr_df
-- ****************************************************************************************

-- Step: Full refresh target dimension table (delete old data first, then insert integrated new data)
delete from coss_dwd.dwd_ass_sr_df;
insert into coss_dwd.dwd_ass_sr_df (
    sr_id,
    i_code,
    sr_name,
    sr_cname,
    rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    w_type,
    w_type_desc,
    div_height,
    capacity,
    w_lim,
    num_of_storage,
    dwd_update_time,
    dwd_load_time
)
select
    t.sr_id             as sr_id,            -- Service Reservoir ID with format SRNNNNNNNN
    t.i_code            as i_code,           -- Installation Code of Service Reservoir
    t.sr_name           as sr_name,          -- Service Reservoir Name
    t.sr_cname          as sr_cname,         -- Service Reservoir Chinese Name
    t.rlabel            as rpt_label,        -- Labels used in reports
    -- Standardize region code: Map "HK" to "HKI" (HK Island) to align with region dimension table's coding rule
    case
        when t.region = 'HK' then 'HKI'
        else t.region
    end as region_code,                     -- Region Code
    t1.descrip          as region_name,      -- Description of Region (from region dimension)
    t1.cdescrip         as region_cname,     -- Chinese Description of Region (from region dimension)
    t1.indicator        as region_ind,       -- Possible Values: {"I" - HK Island, "M" - Mainland}
    t.w_type            as w_type,           -- Type of water maintained by the service reservoir
    t2.descrip          as w_type_desc,      -- Description of Water Type (from water type dimension)
    t.div_height        as div_height,       -- Height of Division Wall.  Unit is in m
    t.capacity          as capacity,         -- Capacity of Service Reservoir.  Unit is in cu m
    t.limit             as w_lim,            -- Map source "limit" to target "w_lim" (water level limit) for semantic consistency
    t.num_of_storage    as num_of_storage,   -- No. of Storage/Compartment (fix original typo: "num_of_storag" → "num_of_storage")
    current_timestamp   as dwd_update_time,  -- Data Warehouse update Time
    current_timestamp   as dwd_load_time     -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_sr_di t  -- Main source: Service Reservoir base information table
left join coss_ods.ods_sttss_rws_region_df t1  -- Join 1: Region dimension table (for region attributes)
    on t.region = t1.code  -- Join condition: Match service reservoir's region code with region dimension code
left join coss_ods.ods_sttss_rws_w_type_df t2  -- Join 2: Water type dimension table (for water type description)
    on t.w_type = t2.code -- Join condition: Match service reservoir's water type code with water type dimension code
on duplicate key update
    i_code = values(i_code),
    sr_name = values(sr_name),
    sr_cname = values(sr_cname),
    rpt_label = values(rpt_label),
    region_code = values(region_code),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    w_type = values(w_type),
    w_type_desc = values(w_type_desc),
    div_height = values(div_height),
    capacity = values(capacity),
    w_lim = values(w_lim),
    num_of_storage = values(num_of_storage),
    dwd_update_time = values(dwd_update_time)
```

### 6.coss_dwd.dwd_ass_wtw_df

#### create table

```sql
-- Fix 1: Correct field comments (original comments were misaligned with field semantics)
drop table if exists coss_dwd.dwd_ass_wtw_df;

create table if not exists coss_dwd.dwd_ass_wtw_df (
    tw_id           varchar(20),         -- Water Treatment Works ID with format TWNNNNNNNN
    i_code          varchar(10),         -- Installation Code of Water Treatment Works
    tw_name         varchar(200),        -- Water Treatment Works Name
    tw_cname        varchar(300),        -- Water Treatment Works Chinese Name
    rpt_label       varchar(400),        -- Labels used in reports
    region_code     varchar(10),         -- Region (Standardized code)
    region_name     varchar(60),         -- Description of Region
    region_cname    varchar(300),        -- Chinese Description of Region
    region_ind      varchar(2),          -- Possible Values: {"I" - HK Island, "M" - Mainland}
    capacity        decimal(12, 4),      -- Capacity of WTW.  Unit is in Mld (Million liters per day)
    dwd_update_time timestamp(6) default current_timestamp,
    dwd_load_time   timestamp(6) default current_timestamp,
    primary key (tw_id)
) ;

comment on table coss_dwd.dwd_ass_wtw_df is 'Water Treatment Works Information';
comment on column coss_dwd.dwd_ass_wtw_df.tw_id            is 'Water Treatment Works ID with format TWNNNNNNNN (System-generated unique ID)';
comment on column coss_dwd.dwd_ass_wtw_df.i_code           is 'Installation Code of Water Treatment Works (Unique operational code for on-site management)';
comment on column coss_dwd.dwd_ass_wtw_df.tw_name          is 'Water Treatment Works Name (English name for operational and reporting reference)';
comment on column coss_dwd.dwd_ass_wtw_df.tw_cname         is 'Water Treatment Works Chinese Name (Chinese name for local management and reporting)';
comment on column coss_dwd.dwd_ass_wtw_df.rpt_label        is 'Labels used in reports (Custom labels for report display, e.g., abbreviations or full names)';
comment on column coss_dwd.dwd_ass_wtw_df.region_code      is 'Region (Standardized code aligned with region dimension table, e.g., "HKI" for HK Island)';
comment on column coss_dwd.dwd_ass_wtw_df.region_name      is 'Description of Region (English name of the region, from region dimension table)';
comment on column coss_dwd.dwd_ass_wtw_df.region_cname     is 'Chinese Description of Region (Chinese name of the region, from region dimension table)';
comment on column coss_dwd.dwd_ass_wtw_df.region_ind       is 'Possible Values: {"I" - HK Island, "M" - Mainland} (Indicator for region category)';
comment on column coss_dwd.dwd_ass_wtw_df.capacity         is 'Capacity of WTW.  Unit is in Mld (Million liters per day, design capacity of water treatment)';
comment on column coss_dwd.dwd_ass_wtw_df.dwd_update_time  is 'Data Update Time (Timestamp of last data modification in the data warehouse)';
comment on column coss_dwd.dwd_ass_wtw_df.dwd_load_time    is 'Data Loading Time (Timestamp of initial data loading into the data warehouse)';

```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Water Assets
-- Function Describe: Water Treatment Works Information
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_rws_wtw_df
-- coss_ods.ods_sttss_rws_region_df
-- Target Table:  
-- coss_dwd.dwd_ass_wtw_df
-- ****************************************************************************************
insert into coss_dwd.dwd_ass_wtw_df (
    tw_id,
    i_code,
    tw_name,
    tw_cname,
    rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    capacity,
    dwd_update_time,
    dwd_load_time
)
select
    t.tw_id            as tw_id,              -- Water Treatment Works ID with format TWNNNNNNNN
    t.i_code           as i_code,             -- Installation Code of Water Treatment Works
    t.tw_name          as tw_name,            -- Water Treatment Works Name
    t.tw_cname         as tw_cname,           -- Water Treatment Works Chinese Name
    t.rlabel           as rpt_label,          -- Labels used in reports
    -- Standardize region code: Map "HK" to "HKI" (HK Island) to align with region dimension table's coding rule
    case
        when t.region = 'HK' then 'HKI'
        else t.region
    end as region_code,                     -- Region (Standardized code)
    t1.descrip         as region_name,        -- Description of Region (from region dimension)
    t1.cdescrip        as region_cname,       -- Chinese Description of Region (from region dimension)
    t1.indicator       as region_ind,         -- Possible Values: {"I" - HK Island, "M" - Mainland}
    t.capacity         as capacity,           -- Capacity of WTW.  Unit is in Mld
    current_timestamp  as dwd_update_time,    -- Data Warehouse update Time
    current_timestamp  as dwd_load_time       -- Data Warehouse load Time
from coss_ods.ods_sttss_rws_wtw_df t  -- Main source: Water Treatment Works base information table
left join coss_ods.ods_sttss_rws_region_df t1  -- Join: Region dimension table (for region attributes)
    on t.region = t1.code  -- Join condition: Match WTW's region code with region dimension code
on duplicate key update
    i_code = values(i_code),
    tw_name = values(tw_name),
    tw_cname = values(tw_cname),
    rpt_label = values(rpt_label),
    region_code = values(region_code),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    capacity = values(capacity),
    dwd_update_time = values(dwd_update_time)
```

## dwd_rws_etl_raw_water_supply_records_day（调度任务）

调度任务前置任务节点名称

```sql
dwd_rws_etl_raw_water_supply_records_day_sql_dwd_rws_channel_flow_detail_di_year_add
dwd_rws_etl_raw_water_supply_records_day_sql_dwd_rws_ir_storage_detail_di_year_add
dwd_rws_etl_raw_water_supply_records_day_sql_dwd_rws_pqty_detail_di_year_add
dwd_rws_etl_raw_water_supply_records_day_sql_dwd_rws_gd_agr_supply_di_year_add
```



### 1.coss_dwd.dwd_rws_channel_flow_detail_di_year

#### create table 

```sql
-- 1. Delete target table if it exists to avoid table structure conflict
drop table if exists coss_dwd.dwd_rws_channel_flow_detail_di_year;

-- 2. Create target table: Daily flow detail of water transfer channels (partitioned by year, distributed by channel ID)
create table if not exists coss_dwd.dwd_rws_channel_flow_detail_di_year (
    option_no          decimal(20),          -- Option No. of Water Transfer Channel being referenced
    ch_id              varchar(20),          -- Water Transfer Channels being referenced
    src_id             varchar(20),          -- Source of Water Inflow
    dest_id            varchar(20),          -- Destination of Water outflow
    qty_del            decimal(12, 4),       -- Quantity delivered of Water transfer channel. Unit is in Mld
    scada_qty_del      decimal(12, 4),       -- Quantity delivered of Water transfer channel. Unit is in Mld (SCADA)
    meas_code          varchar(20),          -- Defines how the channel water flow is measured
    meas_desc          varchar(200),         -- Description of Measurement
    meas_cdesc         varchar(300),         -- Chinese Description of Measurement Type
    remarks            varchar(2000),        -- Remarks
    wl_m               decimal(12, 4),       -- Water Level reading in meter
    wl_mpd             decimal(13, 6),       -- Water Level in mPD (fix original typo: "Waler" → "Water")
    rec_dt             timestamp(6),         -- Date of Record
    dwd_update_time    timestamp(6) default current_timestamp,
    dwd_load_time      timestamp(6) default current_timestamp,
    dt                 decimal(10),          -- Daily Partitions
    primary key (option_no, ch_id, src_id, dest_id, rec_dt)  -- Composite primary key for data uniqueness
) 
partition by range (rec_dt) (  -- Partition data by record date (yearly partition)
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

-- 3. Table comment: Explain business meaning of the table
comment on table coss_dwd.dwd_rws_channel_flow_detail_di_year is 'Water Transfer Channels Daily Flow Detail';

-- 4. Column comments: Clarify each field's business meaning (first letter uppercase)
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.option_no        is 'Option No. of Water Transfer Channel being referenced';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.ch_id            is 'Water Transfer Channels being referenced';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.src_id           is 'Source of Water Inflow';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.dest_id          is 'Destination of Water Outflow';  -- Fix: "outflow" → "Outflow" for capitalization
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.qty_del          is 'Quantity Delivered of Water Transfer Channel. Unit Is In Mld';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.scada_qty_del    is 'Quantity Delivered of Water Transfer Channel. Unit Is In Mld (SCADA)';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.meas_code        is 'Defines How the Channel Water Flow Is Measured';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.meas_desc        is 'Description of Measurement';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.meas_cdesc       is 'Chinese Description of Measurement Type';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.remarks          is 'Remarks';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.wl_m             is 'Water Level Reading In Meter';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.wl_mpd           is 'Water Level In mPD (fix original typo: "Waler" → "Water")';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.rec_dt           is 'Date of Record';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.dwd_update_time  is 'Data Update Time';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.dwd_load_time    is 'Data Loading Time';
comment on column coss_dwd.dwd_rws_channel_flow_detail_di_year.dt               is 'Daily Partitions';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Water Transfer Channels Daily Flow Detail
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_rws_channel_flow_di_year
-- coss_ods.ods_sttss_rws_channel_di
-- coss_ods.ods_sttss_rws_measurement_df
-- Target Table:  
-- coss_dwd.dwd_rws_channel_flow_detail_di_year
-- ****************************************************************************************

insert into coss_dwd.dwd_rws_channel_flow_detail_di_year (
    option_no,
    ch_id,
    src_id,
    dest_id,
    qty_del,
    scada_qty_del,
    meas_code,
    meas_desc,
    meas_cdesc,
    remarks,
    wl_m,
    wl_mpd,
    rec_dt,
    dwd_update_time,
    dwd_load_time,
    dt
)
select
    t.option_no                     as option_no,       -- Option No. of Water Transfer Channel being referenced
    t.ch_id                        as ch_id,           -- Water Transfer Channels being referenced
    t1.src_id                      as src_id,          -- Source of Water Inflow (from channel base table)
    t1.dest_id                     as dest_id,         -- Destination of Water outflow (from channel base table)
    t.qty_del                      as qty_del,         -- Quantity delivered of Water transfer channel. Unit is in Mld
    t.scada_qty_del                as scada_qty_del,   -- Quantity delivered of Water transfer channel. Unit is in Mld (SCADA)
    t.m_code                       as meas_code,       -- Defines how the channel water flow is measured
    t2.descrip                     as meas_desc,       -- Description of Measurement (from measurement dimension table)
    t2.cdescrip                    as meas_cdesc,      -- Chinese Description of Measurement Type (from measurement dimension table)
    t.remarks                      as remarks,         -- Remarks
    t.wl_m                         as wl_m,            -- Water Level reading in meter
    t.wl_mpd                       as wl_mpd,          -- Water Level in mPD (fix original typo: "Waler" → "Water")
    t.rec_dt                       as rec_dt,          -- Date of Record
    current_timestamp              as dwd_update_time, -- Replace localtimestamp with current_timestamp
    current_timestamp              as dwd_load_time,   -- Replace localtimestamp with current_timestamp
    to_char(t.rec_dt, 'yyyymmdd')::decimal(10) as dt  -- Convert date to decimal(10) for daily partition (type match)
from coss_ods.ods_sttss_rws_channel_flow_di_year t  -- Main source: Channel daily flow table
inner join coss_ods.ods_sttss_rws_channel_di t1  -- Inner join: Get channel source/destination (must match)
    on t.option_no = t1.option_no
    and t.ch_id = t1.ch_id  -- Composite join condition: Ensure unique channel matching
left join coss_ods.ods_sttss_rws_measurement_df t2  -- Left join: Get measurement description (allow null)
    on t.m_code = t2.code
where t.ods_update_time >= '${dwd_update_time}'
on duplicate key update
    qty_del = values(qty_del),
    scada_qty_del = values(scada_qty_del),
    meas_code = values(meas_code),
    meas_desc = values(meas_desc),
    meas_cdesc = values(meas_cdesc),
    remarks = values(remarks),
    wl_m = values(wl_m),
    wl_mpd = values(wl_mpd),
    dwd_update_time = values(dwd_update_time),
    dt = values(dt)

```

### 2.coss_dwd.dwd_rws_ir_storage_detail_di_year

#### create table

```sql
-- 1. Delete target table if it exists to avoid table structure conflict
drop table if exists coss_dwd.dwd_rws_ir_storage_detail_di_year;

-- 2. Create target table: Daily storage details of impounding reservoir (yearly partition, distributed by reservoir ID)
create table if not exists coss_dwd.dwd_rws_ir_storage_detail_di_year (
    ig_id             varchar(20),      -- Impounding Reservoir Group being referenced
    ir_id             varchar(20),      -- Impounding Reservoir being referenced
    wl_ft             decimal(12, 4),   -- Water Level reading in feet
    wl_in             decimal(12, 4),   -- Water Level reading in inch
    wl_m              decimal(12, 4),   -- Water Level reading in meter
    wl_mpd            decimal(13, 6),   -- Water Level in mPD (fix original typo: "Waler" → "Water")
    present_storage   decimal(16, 8),   -- Storage of water in IR.  Unit is in mcm
    remarks           varchar(2000),    -- Remarks
    rec_dt            timestamp(6),     -- Date of record
    dwd_update_time   timestamp(6) default current_timestamp,
    dwd_load_time     timestamp(6) default current_timestamp,
    dt                decimal(10),      -- Daily Partitions
    primary key (ig_id, ir_id, rec_dt)  -- Composite primary key: Ensure unique record per reservoir-group-date
)
partition by range (rec_dt) (  -- Yearly partition by record date for efficient data management
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

-- 3. Table comment: Standardize comment format (first letter uppercase)
comment on table coss_dwd.dwd_rws_ir_storage_detail_di_year is 'Daily Impounding Reservoir Storage Details';

-- 4. Column comments: Clarify business meaning + standardize first letter uppercase
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.ig_id            is 'Impounding Reservoir Group being referenced';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.ir_id            is 'Impounding Reservoir being referenced';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.wl_ft            is 'Water Level Reading In Feet';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.wl_in            is 'Water Level Reading In Inch';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.wl_m             is 'Water Level Reading In Meter';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.wl_mpd           is 'Water Level In mPD (fix original typo: "Waler" → "Water")';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.present_storage  is 'Storage Of Water In IR.  Unit Is In mcm';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.remarks          is 'Remarks';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.rec_dt           is 'Date Of Record';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.dwd_update_time  is 'Data Update Time';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.dwd_load_time    is 'Data Loading Time';
comment on column coss_dwd.dwd_rws_ir_storage_detail_di_year.dt               is 'Daily Partitions';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Impounding Reservoir Storage Details
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_rws_ir_storage_di_year
-- coss_ods.ods_sttss_rws_ir_df
-- Target Table:  
-- coss_dwd.dwd_rws_ir_storage_detail_di_year
-- ****************************************************************************************
-- 6. Insert data: Join source tables + filter non-system data + replace time function
insert into coss_dwd.dwd_rws_ir_storage_detail_di_year (
    ig_id,
    ir_id,
    wl_ft,
    wl_in,
    wl_m,
    wl_mpd,
    present_storage,
    remarks,
    rec_dt,
    dwd_update_time,
    dwd_load_time,
    dt
)
select
    t1.ig_id                      as ig_id,            -- Impounding Reservoir Group being referenced (from reservoir base table)
    t.ir_id                       as ir_id,            -- Impounding Reservoir being referenced (from storage fact table)
    t.wl_ft                       as wl_ft,            -- Water Level reading in feet
    t.wl_in                       as wl_in,            -- Water Level reading in inch
    t.wl_m                        as wl_m,             -- Water Level reading in meter
    t.wl_mpd                      as wl_mpd,           -- Water Level in mPD (fix original typo: "Waler" → "Water")
    t.storage                     as present_storage,  -- Storage of water in IR.  Unit is in mcm
    t.remarks                     as remarks,          -- Remarks
    t.rec_dt                      as rec_dt,           -- Date of record
    current_timestamp              as dwd_update_time,  -- Replace localtimestamp with current_timestamp (standardize time function)
    current_timestamp              as dwd_load_time,    -- Replace localtimestamp with current_timestamp
    to_char(t.rec_dt, 'yyyymmdd')::decimal(10) as dt  -- Convert date string to decimal(10) to match target field type
from coss_ods.ods_sttss_rws_ir_storage_di_year t  -- Main source: Reservoir daily storage fact table
left join coss_ods.ods_sttss_rws_ir_df t1  -- Left join: Get reservoir group ID (allow reservoir without group info)
    on t.ir_id = t1.ir_id  -- Join condition: Match reservoir ID
where t.last_upd_user != 'system'  -- Filter condition: Exclude system-generated records
  and t.ods_update_time >= '${dwd_update_time}'
on duplicate key update
    wl_ft = values(wl_ft),
    wl_in = values(wl_in),
    wl_m = values(wl_m),
    wl_mpd = values(wl_mpd),
    present_storage = values(present_storage),
    remarks = values(remarks),
    dwd_update_time = values(dwd_update_time),
    dt = values(dt)
```

### 3.coss_dwd.dwd_rws_pqty_detail_di_year

#### create table

```sql
-- 1. Delete target table if exists to avoid table structure conflict
drop table if exists coss_dwd.dwd_rws_pqty_detail_di_year;

-- 2. Create target table: Proposed quantity details (yearly partition, distributed by proposed quantity ID)
create table if not exists coss_dwd.dwd_rws_pqty_detail_di_year (
    prop_qty_id       decimal(10),       -- Proposed Quantity ID
    ref_entity        varchar(100),      -- Referenced Entity
    ref_id            varchar(20),       -- Installations being referenced
    item_no           decimal(10),       -- Item No. To be used for Key Delivery
    p_qty             decimal(12, 4),    -- Proposed Quantity.  Unit is Mld
    start_dt          timestamp(6),      -- Effective Start Date
    end_dt            timestamp(6),      -- Effective End Date
    dwd_update_time   timestamp(6) default current_timestamp,
    dwd_load_time     timestamp(6) default current_timestamp,
    mh                decimal(10),       -- Monthly Partitions
    primary key (prop_qty_id, ref_id, item_no)  -- Composite PK: Ensure unique proposed quantity record
)
partition by range (start_dt) (     -- Yearly partition by effective start date for data management
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

-- 3. Table comment: Standardize first letter uppercase
comment on table coss_dwd.dwd_rws_pqty_detail_di_year is 'Proposed Quantity Details';

-- 4. Column comments: Clarify business meaning + standardize first letter uppercase
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.prop_qty_id      is 'Proposed Quantity ID';
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.ref_entity       is 'Referenced Entity';
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.ref_id           is 'Installations Being Referenced';
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.item_no          is 'Item No. To Be Used for Key Delivery';
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.p_qty            is 'Proposed Quantity.  Unit Is Mld';
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.start_dt         is 'Effective Start Date';
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.end_dt           is 'Effective End Date';
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.dwd_update_time  is 'Data Update Time';
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.dwd_load_time    is 'Data Loading Time';
comment on column coss_dwd.dwd_rws_pqty_detail_di_year.mh               is 'Monthly Partitions';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Proposed Quantity Details
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_rws_pqty_detail_di_year
-- coss_ods.ods_sttss_rws_pqty_di
-- Target Table:  
-- coss_dwd.dwd_rws_pqty_detail_di_year
-- ****************************************************************************************

-- 6. Insert data: Inner join source tables + replace time function + type conversion
insert into coss_dwd.dwd_rws_pqty_detail_di_year (
    prop_qty_id,
    ref_entity,
    ref_id,
    item_no,
    p_qty,
    start_dt,
    end_dt,
    dwd_update_time,
    dwd_load_time,
    mh
)
select
    t1.prop_qty_id                   as prop_qty_id,  -- Proposed Quantity ID (from proposed quantity base table)
    t.ref_entity                     as ref_entity,   -- Referenced Entity (from proposed quantity detail table)
    t.ref_id                         as ref_id,       -- Installations being referenced
    t.item_no                        as item_no,      -- Item No. To be used for Key Delivery
    t.p_qty                          as p_qty,        -- Proposed Quantity.  Unit is Mld
    t1.start_dt                      as start_dt,     -- Effective Start Date (from proposed quantity base table)
    t1.end_dt                        as end_dt,       -- Effective End Date (from proposed quantity base table)
    current_timestamp                as dwd_update_time,  -- Replace localtimestamp with current_timestamp
    current_timestamp                as dwd_load_time,    -- Replace localtimestamp with current_timestamp
    to_char(t1.start_dt, 'yyyymm')::decimal(10) as mh  -- Convert date string to decimal(10) for monthly partition
from coss_ods.ods_sttss_rws_pqty_detail_di_year t  -- Main source: Proposed quantity detail fact table
inner join coss_ods.ods_sttss_rws_pqty_di t1  -- Inner join: Get start/end date (must match proposed quantity ID)
    on t.prop_qty_id = t1.prop_qty_id  -- Composite join condition: Match proposed quantity ID
where t1.start_dt is not null  -- Filter condition: Exclude records with null effective start date
and t.ods_update_time >= '${dwd_update_time}'
on duplicate key update
ref_entity = values(ref_entity),
p_qty = values(p_qty),
start_dt = values(start_dt),
end_dt = values(end_dt),
dwd_update_time = values(dwd_update_time),
mh = values(mh)
```



### 4.coss_dwd.dwd_rws_gd_agr_supply_di_year

#### create table

```sql
-- 1. Delete target table if exists to avoid table structure conflict
drop table if exists coss_dwd.dwd_rws_gd_agr_supply_di_year;

-- 2. Create target table: Daily GD agreed water supply details (yearly partition, row-oriented storage)
create table if not exists coss_dwd.dwd_rws_gd_agr_supply_di_year (
    rw_id            varchar(20),         -- Raw water Source being referenced
    hk_vol           numeric(14, 6),      -- Volume at HK Side.  Unit is in mcm
    gd_vol           numeric(14, 6),      -- Volume at GD Side. Unit is in mcm
    agr_vol          numeric(14, 6),      -- Agreed volume.  Unit is in mcm
    dis_vol          numeric(14, 6),      -- Discharged volume.  Unit is in mcm
    sz_wlevel        numeric(12, 4),      -- Shen Zhen Water Level.  Unit is in m
    dis_ind          varchar(3),          -- Possible Values:Y - Yes,N - No
    rec_dt           date,                -- Date of record
    submit_dt        timestamp(6),        -- Submission Date
    dwd_update_time  timestamp(6) default pg_systimestamp(),  -- Data Update Time (PostgreSQL-specific function)
    dwd_load_time    timestamp(6) default pg_systimestamp(),  -- Data Loading Time (PostgreSQL-specific function)
    primary key (rw_id, rec_dt)  -- Composite PK: Ensure unique supply record per raw water source-date
)
with (
    orientation = row,          -- Row-oriented storage (suitable for transactional queries)
    compression = no,           -- No compression (ensure data read efficiency for critical supply data)
    storage_type = ustore,      -- Use USTORE storage engine (for high write performance)
    segment = off               -- Disable segment management (simplify storage structure)
)
partition by range (rec_dt) (  -- Yearly partition by record date for long-term data management
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

-- 3. Table comment: Standardize first letter uppercase + clarify business scope
comment on table coss_dwd.dwd_rws_gd_agr_supply_di_year is 'Daily GD Water Supply (Guangdong Daily Agreed Water Supply Details)';

-- 4. Column comments: Standardize first letter uppercase + retain business semantics
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.rw_id            is 'Raw Water Source Being Referenced';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.hk_vol           is 'Volume At HK Side.  Unit Is In Mcm';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.gd_vol           is 'Volume At GD Side. Unit Is In Mcm';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.agr_vol          is 'Agreed Volume.  Unit Is In Mcm';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.dis_vol          is 'Discharged Volume.  Unit Is In Mcm';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.sz_wlevel        is 'Shen Zhen Water Level.  Unit Is In M';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.dis_ind          is 'Possible Values:Y - Yes,N - No';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.rec_dt           is 'Date Of Record';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.submit_dt        is 'Submission Date';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.dwd_update_time  is 'Data Update Time (PostgreSQL-specific: pg_systimestamp())';
comment on column coss_dwd.dwd_rws_gd_agr_supply_di_year.dwd_load_time    is 'Data Loading Time (PostgreSQL-specific: pg_systimestamp())';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Daily GD Water Supply (Guangdong Daily Agreed Water Supply Details)
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14 (Consistent with similar DWD layer table standards)
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_rws_gd_agr_supply_di_year (Inferred from table business logic)
-- Target Table:  
-- coss_dwd.dwd_rws_gd_agr_supply_di_year
-- ****************************************************************************************
-- Insert data: Map ODS layer data to DWD layer (retain all business fields)
insert into coss_dwd.dwd_rws_gd_agr_supply_di_year (
    rw_id,
    hk_vol,
    gd_vol,
    agr_vol,
    dis_vol,
    sz_wlevel,
    dis_ind,
    rec_dt,
    submit_dt,
    dwd_update_time,
    dwd_load_time
)
select
    t.rw_id            as rw_id,            -- Raw water Source being referenced
    t.hk_vol           as hk_vol,           -- Volume at HK Side.  Unit is in mcm
    t.gd_vol           as gd_vol,           -- Volume at GD Side. Unit is in mcm
    t.agr_vol          as agr_vol,          -- Agreed volume.  Unit is in mcm
    t.dis_vol          as dis_vol,          -- Discharged volume.  Unit is in mcm
    t.sz_wlevel        as sz_wlevel,        -- Shen Zhen Water Level.  Unit is in m
    t.dis_ind          as dis_ind,          -- Possible Values:Y - Yes,N - No
    t.rec_dt           as rec_dt,           -- Date of record
    t.submit_dt        as submit_dt,        -- Submission Date
    current_timestamp  as dwd_update_time,  -- Use PostgreSQL-specific function for time consistency
    current_timestamp  as dwd_load_time     -- Use PostgreSQL-specific function for time consistency
from coss_ods.ods_sttss_rws_gd_agr_supply_di_year t  -- Source: ODS layer GD agreed supply table
where t.ods_update_time >= '${dwd_update_time}'
on duplicate key update
    hk_vol = values(hk_vol),
    gd_vol = values(gd_vol),
    agr_vol = values(agr_vol),
    dis_vol = values(dis_vol),
    sz_wlevel = values(sz_wlevel),
    dis_ind = values(dis_ind),
    submit_dt = values(submit_dt),
    dwd_update_time = values(dwd_update_time)
```

## dwd_srs_etl_sr_water_supply_records_day(调度任务)

调度任务前置任务节点名称

```sql
dwd_srs_etl_sr_water_supply_records_day_sql_dwd_srs_sr_storage_detail_di_year_add
```



### 1.coss_dwd.dwd_srs_sr_storage_detail_di_year

#### create table

```sql
-- 1. Delete target table if exists to avoid table structure conflict
drop table if exists coss_dwd.dwd_srs_sr_storage_detail_di_year;

-- 2. Create target table: Daily storage details of service reservoir (yearly partition, distributed by reservoir ID)
create table if not exists coss_dwd.dwd_srs_sr_storage_detail_di_year (
    sr_id            varchar(20),          -- Service Reservoir being referenced
    a_wl             decimal(9, 2),        -- A Compartment Water Level
    b_wl             decimal(9, 2),        -- B Compartment Water Level
    a_storage        decimal(12, 4),       -- Volume of water in A compartment of an SR.  Unit is in cu m
    b_storage        decimal(12, 4),       -- Volume of water in B compartment of an SR.  Unit is in cu m
    tot_storage      decimal(12, 4),       -- Total volume of water in A+ B+..+R.  Unit is in cu m
    remarks          varchar(2000),        -- Remarks
    rec_dt           timestamp(6),         -- Date of record
    dwd_update_time  timestamp(6) default current_timestamp,
    dwd_load_time    timestamp(6) default current_timestamp,
    dt               decimal(10),          -- Daily Partitions
    primary key (sr_id, rec_dt)  -- Composite PK: Ensure unique storage record per reservoir-date
)
partition by range (rec_dt) (  -- Yearly partition by record date for efficient data query
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

-- 3. Table comment: Keep business meaning consistent
comment on table coss_dwd.dwd_srs_sr_storage_detail_di_year is 'Daily SR Storage Details';

-- 4. Column comments: Standardize first letter uppercase + clarify business meaning
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.sr_id            is 'Service Reservoir Being Referenced';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.a_wl             is 'A Compartment Water Level';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.b_wl             is 'B Compartment Water Level';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.a_storage        is 'Volume Of Water In A Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.b_storage        is 'Volume Of Water In B Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.tot_storage      is 'Total Volume Of Water In A+ B+..+R.  Unit Is In Cu M';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.remarks          is 'Remarks';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.rec_dt           is 'Date Of Record';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.dwd_update_time  is 'Data Update Time';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.dwd_load_time    is 'Data Loading Time';
comment on column coss_dwd.dwd_srs_sr_storage_detail_di_year.dt               is 'Daily Partitions';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Service Reservoir Supply
-- Function Describe: Daily SR Storage Details
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_ods.ods_sttss_srs_sr_storage_di_year
-- Target Table:  
-- coss_dwd.dwd_srs_sr_storage_detail_di_year
-- ****************************************************************************************
-- 6. Insert data: Fix field mapping error + replace time function + type conversion
insert into coss_dwd.dwd_srs_sr_storage_detail_di_year (
    sr_id,
    a_wl,
    b_wl,
    a_storage,
    b_storage,
    tot_storage,
    remarks,
    rec_dt,
    dwd_update_time,
    dwd_load_time,
    dt
)
select
    t.sr_id                         as sr_id,            -- Service Reservoir being referenced
    t.a_wlevel                      as a_wl,             -- A Compartment Water Level (map source "a_wlevel" to target "a_wl")
    t.b_wlevel                      as b_wl,             -- B Compartment Water Level (map source "b_wlevel" to target "b_wl")
    t.a_storage                     as a_storage,        -- Volume of water in A compartment of an SR.  Unit is in cu m
    t.b_storage                     as b_storage,        -- Volume of water in B compartment of an SR.  Unit is in cu m
    t.tot_storage                   as tot_storage,      -- Fix original error: Map "tot_storage" to "tot_storage" (not "b_storage")
    t.remarks                       as remarks,          -- Remarks
    t.rec_dt                        as rec_dt,           -- Date of record
    current_timestamp               as dwd_update_time,  -- Replace localtimestamp with current_timestamp
    current_timestamp               as dwd_load_time,    -- Replace localtimestamp with current_timestamp
    to_char(t.rec_dt, 'yyyymmdd')::decimal(10) as dt    -- Convert date string to decimal(10) to match target field type
from coss_ods.ods_sttss_srs_sr_storage_di_year t  -- Source: ODS layer service reservoir daily storage table
where t.ods_update_time >= '${dwd_update_time}'
on duplicate key update
    a_wl = values(a_wl),
    b_wl = values(b_wl),
    a_storage = values(a_storage),
    b_storage = values(b_storage),
    tot_storage = values(tot_storage),
    remarks = values(remarks),
    dwd_update_time = values(dwd_update_time),
    dt = values(dt)
```



# dws

## dws_rws_etl_raw_water_supply_day(调度任务)

调度任务前置任务节点名称

```sql
dws_rws_etl_raw_water_supply_day_sql_dws_rws_ir_storage_detail_di_year_add
dws_rws_etl_raw_water_supply_day_sql_dws_rws_rw_supply_detail_di_year_add
```



### 1.coss_dws.dws_rws_ir_storage_detail_di_year

#### create table

```sql
-- 1. Delete target table if exists to avoid table structure conflict
drop table if exists coss_dws.dws_rws_ir_storage_detail_di_year;

-- 2. Create target table: Integrated daily storage details of impounding reservoir (DWS layer, yearly partition)
create table if not exists coss_dws.dws_rws_ir_storage_detail_di_year (
    ig_id             varchar(20),         -- Impounding Reservoir Group ID with format IGNNNNNNNN
    ig_name           varchar(200),        -- Name of Impounding Reservoir Group
    ig_cname          varchar(300),        -- Chinese Name of Impounding Reservoir Group
    ig_rpt_label      varchar(400),        -- Labels used in reports
    region_code       varchar(10),         -- Region
    region_name       varchar(60),         -- Description of Region
    region_cname      varchar(300),        -- Chinese Description of Region
    region_ind        varchar(2),          -- Possible Values: {"I" - HK Island, "M" - Mainland} (fix original quote missing)
    ig_ind            varchar(2),          -- Indicates if Impounding Reservoir Group is old or new. Possible Values: {"Y" - Old, "N" - New} (fix original quote missing)
    ir_id             varchar(20),         -- Impounding Reservoir ID with format IRNNNNNNNN
    i_code            varchar(10),         -- Installation Code of Impounding Reservoir
    ir_rpt_label      varchar(400),        -- Labels used in reports
    ir_name           varchar(200),        -- Impounding Reservoir Name
    ir_cname          varchar(300),        -- Impounding Reservoir Chinese Name
    level_type        varchar(2),          -- Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}
    level_unit        varchar(2),          -- Possible Values:{"F" - Feet / Inch, "M" - Meter}
    dead_storage      decimal(12, 4),      -- Dead Storage of an Impounding Reservoir.  Unit is in mcm
    twl               decimal(12, 4),      -- TWL (Top Water Level)
    capacity          decimal(12, 4),      -- Capacity of IR.  Unit is in mcm
    min_storage       decimal(12, 4),      -- Allowable Minimum Storage.  Unit is in mcm
    limit_m           decimal(12, 4),      -- Preset Limit for Water Level.  Unit is in m
    wl_ft             decimal(12, 4),      -- Water Level reading in feet
    wl_in             decimal(12, 4),      -- Water Level reading in inch
    wl_m              decimal(12, 4),      -- Water Level reading in meter
    wl_mpd            decimal(13, 6),      -- Water Level in mPD (fix original typo: "Waler" → "Water")
    present_storage   decimal(16, 8),      -- Storage of water in IR.  Unit is Mld (converted from mcm)
    remarks           varchar(2000),       -- Remarks
    rec_dt            timestamp(6),        -- Date of record
    dws_update_time   timestamp(6) default current_timestamp,
    dws_load_time     timestamp(6) default current_timestamp,
    dt                decimal(10),         -- Daily Partitions
    primary key (ir_id, rec_dt)  -- Composite PK: Ensure unique record per reservoir-date
)  
partition by range (rec_dt) (  -- Yearly partition by record date for efficient data query
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

-- 3. Table comment: Standardize first letter uppercase
comment on table coss_dws.dws_rws_ir_storage_detail_di_year is 'Daily Impounding Reservoir Storage Details';

-- 4. Column comments: Fix format errors + standardize first letter uppercase
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.ig_id              is 'Impounding Reservoir Group ID With Format IGNNNNNNNN';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.ig_name            is 'Name Of Impounding Reservoir Group';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.ig_cname           is 'Chinese Name Of Impounding Reservoir Group';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.ig_rpt_label       is 'Labels Used In Reports';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.region_code        is 'Region';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.region_name        is 'Description Of Region';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.region_cname       is 'Chinese Description Of Region';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.region_ind         is 'Possible Values: {"I" - HK Island, "M" - Mainland} (fix original missing double quote)';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.ig_ind             is 'Indicates If Impounding Reservoir Group Is Old Or New. Possible Values: {"Y" - Old, "N" - New} (fix original missing double quote)';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.ir_id              is 'Impounding Reservoir ID With Format IRNNNNNNNN';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.i_code             is 'Installation Code Of Impounding Reservoir';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.ir_rpt_label       is 'Labels Used In Reports';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.ir_name            is 'Impounding Reservoir Name';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.ir_cname           is 'Impounding Reservoir Chinese Name';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.level_type         is 'Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD}';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.level_unit         is 'Possible Values:{"F" - Feet / Inch, "M" - Meter}';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.dead_storage       is 'Dead Storage Of An Impounding Reservoir.  Unit Is In Mcm';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.twl                is 'TWL (Top Water Level)';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.capacity           is 'Capacity Of IR.  Unit Is In Mcm';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.min_storage        is 'Allowable Minimum Storage.  Unit Is In Mcm';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.limit_m            is 'Preset Limit For Water Level.  Unit Is In M';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.wl_ft              is 'Water Level Reading In Feet';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.wl_in              is 'Water Level Reading In Inch';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.wl_m               is 'Water Level Reading In Meter';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.wl_mpd             is 'Water Level In mPD (fix original typo: "Waler" → "Water")';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.present_storage    is 'Storage Of Water In IR.  Unit Is Mld (converted from mcm by ×1000)';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.remarks            is 'Remarks';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.rec_dt             is 'Date Of Record';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.dws_update_time    is 'Data Update Time';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.dws_load_time      is 'Data Loading Time';
comment on column coss_dws.dws_rws_ir_storage_detail_di_year.dt                 is 'Daily Partitions';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Impounding Reservoir Storage Details
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_dwd.dwd_rws_ir_storage_detail_di_year
-- coss_dwd.dwd_ass_ir_df
-- Target Table:  coss_dws.dws_rws_ir_storage_detail_di_year
-- ****************************************************************************************
insert into coss_dws.dws_rws_ir_storage_detail_di_year (
    ig_id,
    ig_name,
    ig_cname,
    ig_rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    ig_ind,
    ir_id,
    i_code,
    ir_rpt_label,
    ir_name,
    ir_cname,
    level_type,
    level_unit,
    dead_storage,
    twl,
    capacity,
    min_storage,
    limit_m,
    wl_ft,
    wl_in,
    wl_m,
    wl_mpd,
    present_storage,
    remarks,
    rec_dt,
    dws_update_time,
    dws_load_time,
    dt
)
select
    t1.ig_id                         as ig_id,              -- Impounding Reservoir Group ID with format IGNNNNNNNN (from DIM table)
    t1.ig_name                      as ig_name,            -- Name of Impounding Reservoir Group (from DIM table)
    t1.ig_cname                     as ig_cname,           -- Chinese Name of Impounding Reservoir Group (from DIM table)
    t1.ig_rpt_label                 as ig_rpt_label,       -- Labels used in reports (from DIM table)
    t1.region_code                  as region_code,        -- Region (from DIM table)
    t1.region_name                  as region_name,        -- Description of Region (from DIM table)
    t1.region_cname                 as region_cname,       -- Chinese Description of Region (from DIM table)
    t1.region_ind                   as region_ind,         -- Possible Values: {"I" - HK Island, "M" - Mainland}
    t1.ig_ind                       as ig_ind,             -- Indicates if Impounding Reservoir Group is old or new
    t1.ir_id                        as ir_id,              -- Impounding Reservoir ID with format IRNNNNNNNN (from DIM table)
    t1.i_code                       as i_code,             -- Installation Code of Impounding Reservoir (from DIM table)
    t1.ir_rpt_label                 as ir_rpt_label,       -- Labels used in reports (from DIM table)
    t1.ir_name                      as ir_name,            -- Impounding Reservoir Name (from DIM table)
    t1.ir_cname                     as ir_cname,           -- Impounding Reservoir Chinese Name (from DIM table)
    t1.level_type                   as level_type,         -- Possible Values: {"A" - Above TWL, "B" - Below TWL, "P" - APD} (from DIM table)
    t1.level_unit                   as level_unit,         -- Possible Values:{"F" - Feet / Inch, "M" - Meter} (from DIM table)
    t1.dead_storage                 as dead_storage,       -- Dead Storage of an Impounding Reservoir.  Unit is in mcm (from DIM table)
    t1.twl                          as twl,                -- TWL (from DIM table)
    t1.capacity                     as capacity,           -- Capacity of IR.  Unit is in mcm (from DIM table)
    t1.min_storage                  as min_storage,        -- Allowable Minimum Storage.  Unit is in mcm (from DIM table)
    t1.limit_m                      as limit_m,            -- Preset Limit for Water Level.  Unit is in m (from DIM table)
    t.wl_ft                         as wl_ft,              -- Water Level reading in feet (from DWD fact table)
    t.wl_in                         as wl_in,              -- Water Level reading in inch (from DWD fact table)
    t.wl_m                          as wl_m,               -- Water Level reading in meter (from DWD fact table)
    t.wl_mpd                        as wl_mpd,             -- Water Level in mPD (fix typo: "Waler" → "Water")
    t.present_storage * 1000        as present_storage,    -- Unit conversion: mcm → Mld (1 mcm = 1000 Mld)
    t.remarks                       as remarks,            -- Remarks (from DWD fact table)
    t.rec_dt                        as rec_dt,             -- Date of record (from DWD fact table)
    current_timestamp                as dws_update_time,    -- Replace localtimestamp with current_timestamp (standardize time function)
    current_timestamp                as dws_load_time,      -- Replace localtimestamp with current_timestamp
    to_char(t.rec_dt, 'yyyymmdd')::decimal(10) as dt       -- Convert date string to decimal(10) for daily partition (type match)
from coss_dwd.dwd_rws_ir_storage_detail_di_year t  -- Main source: DWD layer reservoir storage fact table
inner join coss_dwd.dwd_ass_ir_df t1  -- Inner join: Get reservoir dimension info (must match reservoir ID)
    on t.ir_id = t1.ir_id  -- Join condition: Match impounding reservoir ID
where  t.dwd_update_time >= '${dws_update_time}'
on duplicate key update
    ig_id = values(ig_id),
    ig_name = values(ig_name),
    ig_cname = values(ig_cname),
    ig_rpt_label = values(ig_rpt_label),
    region_code = values(region_code),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    ig_ind = values(ig_ind),
    i_code = values(i_code),
    ir_rpt_label = values(ir_rpt_label),
    ir_name = values(ir_name),
    ir_cname = values(ir_cname),
    level_type = values(level_type),
    level_unit = values(level_unit),
    dead_storage = values(dead_storage),
    twl = values(twl),
    capacity = values(capacity),
    min_storage = values(min_storage),
    limit_m = values(limit_m),
    wl_ft = values(wl_ft),
    wl_in = values(wl_in),
    wl_m = values(wl_m),
    wl_mpd = values(wl_mpd),
    present_storage = values(present_storage),
    remarks = values(remarks),
    dws_update_time = values(dws_update_time),
    dt = values(dt)
```

### 2.coss_dws.dws_rws_rw_supply_detail_di_year

#### create table

```sql
-- 1. Delete target table if exists to avoid table structure conflict
drop table if exists coss_dws.dws_rws_rw_supply_detail_di_year;

-- 2. Create target table: Integrated daily raw water supply volume detail (DWS layer, yearly partition)
create table if not exists coss_dws.dws_rws_rw_supply_detail_di_year (
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
)
partition by range (rec_dt) (  -- Yearly partition by record date for efficient data query
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

-- 3. Table comment: Keep business meaning consistent
comment on table coss_dws.dws_rws_rw_supply_detail_di_year is 'Raw Water Supply Daily Volume Detail';

-- 4. Column comments: Standardize first letter uppercase + clarify business semantics
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.rw_id             is 'Raw Water Source ID With Format RWNNNNNNNN';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.rw_name           is 'Name Of Raw Water';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.rw_cname          is 'Chinese Name Of Raw Water';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.rpt_label         is 'Labels Used In Reports';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.region_code       is 'Region Code';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.region_name       is 'Description Of Region';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.region_cname      is 'Chinese Description Of Region';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.region_ind        is 'Possible Values: {"I" - HK Island, "M" - Mainland}';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.ig_ind            is 'Indicates If Impounding Reservoir Group Is Old Or New. Possible Values: {"Y" - Old, "N" - New}';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.source_rw         is 'Source Of Raw Water';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.source_desc       is 'Description Of Raw Water Source';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.p_qty             is 'Proposed Quantity.  Unit Is Mld';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.qty_del           is 'Quantity Delivered Of Water Transfer Channel. Unit Is In Mld';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.present_storage   is 'Storage Of Water In IR At Present.  Unit Is Mld';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.capacity          is 'Capacity Of IR.  Unit Is Mld';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.min_storage       is 'Allowable Minimum Storage.  Unit Is Mld';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.rec_dt            is 'Date Of Record';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.dws_update_time   is 'Data Update Time';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.dws_load_time     is 'Data Loading Time';
comment on column coss_dws.dws_rws_rw_supply_detail_di_year.dt                is 'Daily Partitions';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Raw Water Supply
-- Function Describe: Raw Water Supply Daily Volume Detail
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_dwd.dwd_rws_channel_flow_detail_di_year
-- coss_dwd.dwd_rws_ir_storage_detail_di_year
-- coss_dwd.dwd_rws_pqty_detail_di_year
-- coss_dwd.dwd_ass_ir_df 
-- coss_dwd.dwd_ass_rw_src_df
-- Target Table:  
-- coss_dws.dws_rws_rw_supply_detail_di_year
-- ****************************************************************************************

drop table if exists coss_tmp.tmp_dws_rws_rw_supply_detail_di_year_1;
create table if not exists coss_tmp.tmp_dws_rws_rw_supply_detail_di_year_1 as
select
    t_a.rw_id                            as rw_id,
    -- t_a.p_qty is reserved for later join with proposed quantity table (tmp_dws_rws_rw_supply_detail_di_year_2)
    t_a.qty_del                         as qty_del,
    -- Unit conversion: mcm → Mld (1 mcm = 1000 Mld), replace null with 0
    ifnull(t_b.present_storage, 0) * 1000 as present_storage,
    ifnull(t_c.capacity, 0) * 1000        as capacity,
    ifnull(t_c.min_storage, 0) * 1000     as min_storage,
    t_a.rec_dt                          as rec_dt,
    t_a.dt                              as dt
from (
    -- Subquery A: Calculate total raw water delivery quantity from channel flow data
    select
        t.src_id                 as rw_id,  -- Map channel source ID to raw water source ID
        t.rec_dt                 as rec_dt,
        t.dt                     as dt,
        sum(ifnull(t.qty_del, 0)) as qty_del  -- Sum delivery quantity, replace null with 0
    from coss_dwd.dwd_rws_channel_flow_detail_di_year t
    where 
        -- Filter valid raw water sources: Reservoir Group (IG) or Raw Water Source (RW)
        (left(t.src_id, 2) = 'IG' or left(t.src_id, 2) = 'RW')
        -- Exclude delivery to Reservoir Group (avoid circular calculation)
        and left(t.dest_id, 2) != 'IG'
		and t.rec_dt >= '${rec_dt}'
    group by
        t.src_id,
        t.rec_dt,
        t.dt
) t_a
left join (
    -- Subquery B: Calculate total present storage of impounding reservoir group
    select
        t.ig_id               as ig_id,  -- Map reservoir group ID to raw water source ID
        t.rec_dt              as rec_dt,
        sum(t.present_storage) as present_storage  -- Sum storage quantity
    from coss_dwd.dwd_rws_ir_storage_detail_di_year t
    where t.rec_dt >= '${rec_dt}'
    group by
        t.ig_id,
        t.rec_dt
) t_b 
    on t_a.rw_id = t_b.ig_id  -- Join by raw water source ID (IG)
    and t_a.rec_dt = t_b.rec_dt  -- Join by record date (ensure time consistency)
left join (
    -- Subquery C: Calculate total capacity and minimum storage of impounding reservoir group
    select
        t.ig_id           as ig_id,  -- Map reservoir group ID to raw water source ID
        sum(t.capacity)   as capacity,  -- Sum total capacity of reservoir group
        sum(t.min_storage) as min_storage  -- Sum minimum storage of reservoir group
    from coss_dwd.dwd_ass_ir_df t
    group by
        t.ig_id
) t_c 
    on t_a.rw_id = t_c.ig_id;  -- Join by raw water source ID (IG)


-- ****************************************************************************************
-- Step 2: Create temporary table 2 - Join proposed quantity data to temporary table 1
-- ****************************************************************************************
drop table if exists coss_tmp.tmp_dws_rws_rw_supply_detail_di_year_2;
create table if not exists coss_tmp.tmp_dws_rws_rw_supply_detail_di_year_2 as
select
    t.rw_id                            as rw_id,
    ifnull(t1.p_qty, 0)                as p_qty,  -- Replace null proposed quantity with 0
    t.qty_del                         as qty_del,
    t.present_storage                 as present_storage,
    t.capacity                        as capacity,
    t.min_storage                     as min_storage,
    t.rec_dt                          as rec_dt
from coss_tmp.tmp_dws_rws_rw_supply_detail_di_year_1 t
left join (
    -- Subquery: Filter valid proposed quantity data (raw water/reservoir group)
    select
        t.ref_id,       -- Map reference ID to raw water source ID
        t.ref_entity,   -- Filter entity type: Raw Water (RW) or Reservoir Group (IR_GROUP)
        t.p_qty,        -- Proposed quantity
        t.start_dt,     -- Effective start date of proposed quantity
        t.end_dt        -- Effective end date of proposed quantity
    from coss_dwd.dwd_rws_pqty_detail_di_year t
    where 
        t.ref_entity in ('RW', 'IR_GROUP')
) t1 
    on t.rw_id = t1.ref_id  -- Join by raw water source ID
    and t.rec_dt >= t1.start_dt  -- Ensure record date is within proposed quantity's effective period
    and t.rec_dt <= t1.end_dt;


-- Insert integrated data: Join temporary table 2 with raw water source dimension table
insert into coss_dws.dws_rws_rw_supply_detail_di_year (
    rw_id,
    rw_name,
    rw_cname,
    rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    ig_ind,
    source_rw,
    source_desc,
    p_qty,
    qty_del,
    present_storage,
    capacity,
    min_storage,
    rec_dt,
    dws_update_time,
    dws_load_time,
    dt
)
select
    t1.rw_id                       as rw_id,            -- Raw Water Source ID with format RWNNNNNNNN (from DIM table)
    t1.rw_name                     as rw_name,          -- Name of Raw Water (from DIM table)
    t1.rw_cname                    as rw_cname,         -- Chinese Name of Raw Water (from DIM table)
    t1.rpt_label                   as rpt_label,        -- Labels used in reports (from DIM table)
    t1.region_code                 as region_code,      -- Region Code (from DIM table)
    t1.region_name                 as region_name,      -- Description of Region (from DIM table)
    t1.region_cname                as region_cname,     -- Chinese Description of Region (from DIM table)
    t1.region_ind                  as region_ind,       -- Possible Values: {"I" - HK Island, "M" - Mainland} (from DIM table)
    t1.ig_ind                      as ig_ind,           -- Reservoir group old/new indicator (from DIM table)
    t1.source_rw                   as source_rw,        -- Source of raw water (from DIM table)
    t1.source_desc                 as source_desc,      -- Description of Raw Water Source (from DIM table)
    t.p_qty                        as p_qty,            -- Proposed Quantity.  Unit is Mld (from temporary table 2)
    t.qty_del                      as qty_del,          -- Quantity delivered of Water transfer channel. Unit is in Mld (from temporary table 2)
    t.present_storage              as present_storage,  -- Storage of water in IR At Present.  Unit is Mld (from temporary table 2)
    t.capacity                     as capacity,         -- Capacity of IR.  Unit is Mld (from temporary table 2)
    t.min_storage                  as min_storage,      -- Allowable Minimum Storage.  Unit is Mld (from temporary table 2)
    t.rec_dt                       as rec_dt,           -- Date of Record (from temporary table 2)
    current_timestamp              as dws_update_time,  -- Replace localtimestamp with current_timestamp (standardize time function)
    current_timestamp              as dws_load_time,    -- Replace localtimestamp with current_timestamp
    to_char(t.rec_dt, 'yyyymmdd')::decimal(10) as dt    -- Convert date string to decimal(10) for daily partition (type match)
from coss_tmp.tmp_dws_rws_rw_supply_detail_di_year_2 t  -- Main source: Integrated temporary table
inner join coss_dwd.dwd_ass_rw_src_df t1  -- Inner join: Get raw water source dimension info (must match)
    on t.rw_id = t1.rw_id  -- Join condition: Match raw water source ID
on duplicate key update
    rw_name = values(rw_name),
    rw_cname = values(rw_cname),
    rpt_label = values(rpt_label),
    region_code = values(region_code),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    ig_ind = values(ig_ind),
    source_rw = values(source_rw),
    source_desc = values(source_desc),
    p_qty = values(p_qty),
    qty_del = values(qty_del),
    present_storage = values(present_storage),
    capacity = values(capacity),
    min_storage = values(min_storage),
    dws_update_time = values(dws_update_time),
    dt = values(dt)
```

## dws_srs_etl_sr_water_supply_day（调度任务）

调度任务前置任务节点名称

```sql
dws_srs_etl_sr_water_supply_day_sql_dws_srs_sr_storage_detail_di_year_add
```

### 1.coss_dws.dws_srs_sr_storage_detail_di_year

#### create table

```sql
-- 1. Delete target table if exists to avoid table structure conflict
drop table if exists coss_dws.dws_srs_sr_storage_detail_di_year;

-- 2. Create target table: Integrated service reservoir storage details (DWS layer, yearly partition)
create table if not exists coss_dws.dws_srs_sr_storage_detail_di_year (
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
)
partition by range (rec_dt) (  -- Yearly partition by record date for efficient data query
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

-- 3. Table comment: Standardize first letter uppercase
comment on table coss_dws.dws_srs_sr_storage_detail_di_year is 'Service Reservoir Storage Details';

-- 4. Column comments: Standardize first letter uppercase + clarify business semantics
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.sr_id             is 'Service Reservoir ID With Format SRNNNNNNNN';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.i_code            is 'Installation Code Of Service Reservoir';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.sr_name           is 'Service Reservoir Name';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.sr_cname          is 'Service Reservoir Chinese Name';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.rpt_label         is 'Labels Used In Reports';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.region_code       is 'Region';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.region_name       is 'Description Of Region';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.region_cname      is 'Chinese Description Of Region';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.region_ind        is 'Possible Values: {"I" - HK Island, "M" - Mainland}';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.w_type            is 'Type Of Water Maintained By The Service Reservoir';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.w_type_desc       is 'Description Of Water Type';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.div_height        is 'Height Of Division Wall.  Unit Is In M';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.capacity          is 'Capacity Of Service Reservoir.  Unit Is In Cum';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.w_lim             is 'Preset Limit For Water Level Above Division Wall.  Unit Is In M';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.num_of_storage    is 'No. Of Storage/Compartment';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.a_wl              is 'A Compartment Water Level';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.b_wl              is 'B Compartment Water Level';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.a_storage         is 'Volume Of Water In A Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.b_storage         is 'Volume Of Water In B Compartment Of An SR.  Unit Is In Cu M';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.tot_storage       is 'Total Volume Of Water In A+ B+..+R.  Unit Is In Cu M';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.qty_del           is 'Quantity Delivered Of Water Transfer Channel. Unit Is In Mld';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.p_qty             is 'Proposed Quantity.  Unit Is In Mld';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.remarks           is 'Remarks';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.rec_dt            is 'Date Of Record';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.dws_update_time   is 'Data Update Time';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.dws_load_time     is 'Data Loading Time';
comment on column coss_dws.dws_srs_sr_storage_detail_di_year.dt                is 'Daily Partitions';
```

#### select sql

```sql
-- ****************************************************************************************
-- Subject     Areas: Service Reservoir Supply
-- Function Describe: Service Reservoir Storage Details
-- Create         By: dongmaochen
-- Create       Date: 2025-04-14
-- Modify Date                Modify By                    Modify Content
-- None                       None                         None
-- Source Table:  
-- coss_dwd.dwd_srs_sr_storage_detail_di_year
-- coss_dwd.dwd_rws_channel_flow_detail_di_year
-- coss_dwd.dwd_rws_pqty_detail_di_year
-- coss_dwd.dwd_ass_sr_df
-- Target Table:  
-- coss_dws.dws_srs_sr_storage_detail_di_year
-- ****************************************************************************************
-- ****************************************************************************************
-- Step 1: Create temporary table 1 - Aggregate storage, delivery and proposed quantity data
-- ****************************************************************************************
drop table if exists coss_tmp.tmp_dws_srs_sr_storage_detail_di_year_1;
create table if not exists coss_tmp.tmp_dws_srs_sr_storage_detail_di_year_1 as 
select
    t.sr_id,
    t.a_wl,
    t.b_wl,
    t.a_storage,
    t.b_storage,
    t.tot_storage,
    ifnull(t1.qty_del, 0) as qty_del,  -- Replace null delivery quantity with 0
    ifnull(t2.p_qty, 0) as p_qty,      -- Replace null proposed quantity with 0
    t.remarks,
    t.rec_dt,
    t.dt  -- Retain daily partition field for target table
from (
    -- Subquery A: Extract base storage data from DWD layer service reservoir storage table
    select
        sr_id                         as sr_id,
        a_wl                         as a_wl,
        b_wl                         as b_wl,
        a_storage                    as a_storage,
        b_storage                    as b_storage,
        tot_storage                  as tot_storage,
        remarks                      as remarks,
        rec_dt                       as rec_dt,
        to_char(rec_dt, 'yyyymmdd')  as dt  -- Generate daily partition field
    from coss_dwd.dwd_srs_sr_storage_detail_di_year t
    where  t.dwd_update_time >= '${dws_update_time}'
) t
left join (
    -- Subquery B: Calculate total delivery quantity from channel flow data (filter service reservoir sources)
    select
        src_id,
        rec_dt,
        sum(ifnull(qty_del, 0)) as qty_del  -- Sum delivery quantity, replace null with 0
    from coss_dwd.dwd_rws_channel_flow_detail_di_year t
    where left(t.src_id, 2) = 'SR'  -- Filter sources: Service Reservoir (SR)
    group by
        src_id,
        rec_dt
) t1 
    on t.sr_id = t1.src_id  -- Join by service reservoir ID
    and t.rec_dt = t1.rec_dt  -- Join by record date (ensure time consistency)
left join (
    -- Subquery C: Filter proposed quantity data for service reservoirs
    select
        t.ref_id,
        t.p_qty,
        t.start_dt,
        t.end_dt
    from coss_dwd.dwd_rws_pqty_detail_di_year t
    where t.ref_entity = 'SR'  -- Filter entity type: Service Reservoir (SR)
) t2 
    on t.sr_id = t2.ref_id  -- Join by service reservoir ID
    and t.rec_dt >= t2.start_dt  -- Ensure record date is within proposed quantity's effective period
    and t.rec_dt <= t2.end_dt;


-- Insert integrated data: Join temporary table 1 with service reservoir dimension table
insert into coss_dws.dws_srs_sr_storage_detail_di_year (
    sr_id,
    i_code,
    sr_name,
    sr_cname,
    rpt_label,
    region_code,
    region_name,
    region_cname,
    region_ind,
    w_type,
    w_type_desc,
    div_height,
    capacity,
    w_lim,
    num_of_storage,
    a_wl,
    b_wl,
    a_storage,
    b_storage,
    tot_storage,
    qty_del,
    p_qty,
    remarks,
    rec_dt,
    dws_update_time,
    dws_load_time,
    dt
)
select
    t.sr_id                         as sr_id,             -- Service Reservoir ID with format SRNNNNNNNN (from temporary table 1)
    t1.i_code                       as i_code,            -- Installation Code of Service Reservoir (from DIM table)
    t1.sr_name                      as sr_name,           -- Service Reservoir Name (from DIM table)
    t1.sr_cname                     as sr_cname,          -- Service Reservoir Chinese Name (from DIM table)
    t1.rpt_label                    as rpt_label,         -- Labels used in reports (from DIM table)
    t1.region_code                  as region_code,       -- Region (from DIM table)
    t1.region_name                  as region_name,       -- Description of Region (from DIM table)
    t1.region_cname                 as region_cname,      -- Chinese Description of Region (from DIM table)
    t1.region_ind                   as region_ind,        -- Possible Values: {"I" - HK Island, "M" - Mainland} (from DIM table)
    t1.w_type                       as w_type,            -- Type of water maintained by the service reservoir (from DIM table)
    t1.w_type_desc                  as w_type_desc,       -- Description of Water Type (from DIM table)
    t1.div_height                   as div_height,        -- Height of Division Wall.  Unit is in m (from DIM table)
    t1.capacity                     as capacity,          -- Capacity of Service Reservoir.  Unit is in cum (from DIM table)
    t1.w_lim                        as w_lim,             -- Preset Limit for Water Level above division wall.  Unit is in m (from DIM table)
    t1.num_of_storage               as num_of_storage,    -- No. of Storage/Compartment (from DIM table)
    t.a_wl                          as a_wl,              -- A Compartment Water Level (from temporary table 1)
    t.b_wl                          as b_wl,              -- B Compartment Water Level (from temporary table 1)
    t.a_storage                     as a_storage,         -- Volume of water in A compartment of an SR.  Unit is in cu m (from temporary table 1)
    t.b_storage                     as b_storage,         -- Volume of water in B compartment of an SR.  Unit is in cu m (from temporary table 1)
    t.tot_storage                   as tot_storage,       -- Total volume of water in A+ B+..+R.  Unit is in cu m (from temporary table 1)
    t.qty_del                       as qty_del,           -- Quantity delivered of Water transfer channel. Unit is in Mld (from temporary table 1)
    t.p_qty                         as p_qty,             -- Proposed Quantity.  Unit is in Mld (from temporary table 1)
    t.remarks                       as remarks,           -- Remarks (from temporary table 1)
    t.rec_dt                        as rec_dt,            -- Date of record (from temporary table 1)
    current_timestamp               as dws_update_time,   -- Replace localtimestamp with current_timestamp (standardize time function)
    current_timestamp               as dws_load_time,     -- Replace localtimestamp with current_timestamp
    t.dt::decimal(10)               as dt                 -- Daily Partitions (convert to decimal(10) to match target field type)
from coss_tmp.tmp_dws_srs_sr_storage_detail_di_year_1 t  -- Main source: Integrated temporary table
inner join coss_dwd.dwd_ass_sr_df t1  -- Inner join: Get service reservoir dimension info (must match)
    on t.sr_id = t1.sr_id  -- Join condition: Match service reservoir ID
on duplicate key update
    i_code = values(i_code),
    sr_name = values(sr_name),
    sr_cname = values(sr_cname),
    rpt_label = values(rpt_label),
    region_code = values(region_code),
    region_name = values(region_name),
    region_cname = values(region_cname),
    region_ind = values(region_ind),
    w_type = values(w_type),
    w_type_desc = values(w_type_desc),
    div_height = values(div_height),
    capacity = values(capacity),
    w_lim = values(w_lim),
    num_of_storage = values(num_of_storage),
    a_wl = values(a_wl),
    b_wl = values(b_wl),
    a_storage = values(a_storage),
    b_storage = values(b_storage),
    tot_storage = values(tot_storage),
    qty_del = values(qty_del),
    p_qty = values(p_qty),
    remarks = values(remarks),
    dws_update_time = values(dws_update_time),
    dt = values(dt)
```



















# template

## 获取最大更新时间的最小业务时间

```sql
-- Get the business time of the latest update record, return the default date when the table is empty
select
    coalesce(
        (
            select rec_dt  -- Business time
            from (
                select
                    rec_dt,  -- Business time
                    row_number() over (
                        order by dws_update_time desc, rec_dt asc
                    ) as row_num  -- Row number sorted by update time and business time
                from coss_dws.dws_srs_sr_storage_detail_di_year
            ) t
            where t.row_num = 1  -- Filter the first row of sorted results
        ),
        '1900-01-01 00:00:00'  -- Default date when the table is empty
    ) as rec_dt;  -- Business time, return default value if the table is empty
```



```sql
  ,ods_update_time timestamp(6) default current_timestamp
  ,ods_load_time timestamp(6) default current_timestamp

partition by range (==)
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
)


;comment on column coss_ods.ods_update_time  is 'Data Update Time'
;comment on column coss_ods.ods_load_time    is 'Data Loading Time'


  ,localtimestamp    -- Data Warehouse update Time
  ,localtimestamp    -- Data Warehouse load Time
```







```sql
drop table if exists coss_dwd.dwd_wqm_sample_result_di_year;
create table if not exists coss_dwd.dwd_wqm_sample_result_di_year(
	sample_code varchar(21) not null,
	analysis_code varchar(72) not null,
	analysis_name varchar(300),
	result_modify_date timestamp(6),
	raw_result float8,
	local_code varchar(24),
	point_code varchar(12),
	water_type_code varchar(12),
	water_nature varchar(20),
	region_abbr varchar(5),
	admin_division_code varchar(12),
	collection_date timestamp(6),
	dwd_update_time timestamp(6) default current_timestamp,
	dwd_load_time timestamp(6) default current_timestamp,
	primary key (analysis_code, analysis_name, sample_code)
)
with (orientation = row, compression = no)
distribute by hash (analysis_code, analysis_name, sample_code)
partition by range (collection_date)
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
comment on table coss_dwd.dwd_wqm_sample_result_di_year is 'Sample Inspection Result';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.sample_code is 'Sample ID';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.analysis_code is 'Analysis Code';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.analysis_name is 'Analysis Name';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.result_modify_date is 'Result Modified Date';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.raw_result is 'Raw Result';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.local_code is 'Sample Point Code';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.point_code is 'Sample Point Code';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.water_type_code is 'Water Type Code';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.water_nature is 'Water Nature';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.region_abbr is 'Regional Abbreviation';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.admin_division_code is 'Administrative Division Code';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.collection_date is 'Sample Collection Date';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.dwd_update_time is 'Data Update Time';
comment on column coss_dwd.dwd_wqm_sample_result_di_year.dwd_load_time is 'Data Loading Time';

drop table if exists coss_dwd.dwd_wqm_sample_local_info_df;
create table if not exists coss_dwd.dwd_wqm_sample_local_info_df(
	point_code varchar(12),
	local_code varchar(72),
	local_description varchar(180),
	region_abbr varchar(5),
	admin_division_code varchar(12),
	dwd_update_time timestamp(6) default current_timestamp,
	dwd_load_time timestamp(6) default current_timestamp,
	primary key (local_code)
)
with (orientation = row, compression = no)
distribute by replication;
comment on table coss_dwd.dwd_wqm_sample_local_info_df is 'Location Information of Sampling Points';
comment on column coss_dwd.dwd_wqm_sample_local_info_df.point_code is 'Sample Point Code';
comment on column coss_dwd.dwd_wqm_sample_local_info_df.local_code is 'Sample Point Code';
comment on column coss_dwd.dwd_wqm_sample_local_info_df.local_description is 'Sample Point Description';
comment on column coss_dwd.dwd_wqm_sample_local_info_df.region_abbr is 'Regional Abbreviation';
comment on column coss_dwd.dwd_wqm_sample_local_info_df.admin_division_code is 'Administrative Division Code';
comment on column coss_dwd.dwd_wqm_sample_local_info_df.dwd_update_time is 'Data Update Time';
comment on column coss_dwd.dwd_wqm_sample_local_info_df.dwd_load_time is 'Data Loading Time';
```

