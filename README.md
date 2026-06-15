
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
    "dt"               decimal(10)        -- Daily Partitions
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
    "dt"             decimal(10)         -- Daily Partitions
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




https://wiki.sis2.wsd.gov/ems/webresources/reports?loc_id=24&from=2023-01-01&to=2023-02-28

https://wiki.sis2/wsd.gov/ems/webresources/bills?from=2023-01-01&to=2023-01-31


https://wiki.sis2.wsd.gov/ems/webresources/assets?id=1&id=2


https://wiki.sis2.wsd.gov/ems/webresources/pumps?equip-number=M503-10905&equip-number=M524-11325
https://wiki.sis2.wsd.gov/ems/webresources/tagnames?id=4&id=55


API_URL = 'http://10.66.169.58:8001/iot3/rest/api/v1/realtime.json'
