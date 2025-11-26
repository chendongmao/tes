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

