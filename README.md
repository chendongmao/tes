drop table if exists coss_tmp.dm_psr_daily_ps_running_item_di01 ;
create table coss_tmp.dm_psr_daily_ps_running_item_di01 as 
SELECT * FROM coss_dm.dm_psr_daily_ps_running_item_di ;

-- create table sql



insert into  coss_dm.dm_psr_daily_ps_running_item_di
select
    asset_id,
    region,
    sub_region,
    installation_no,
    offical_eng_name,
    offical_chi_name,
    address_eng,
    address_chi,
    kwh_ml,
    running_pumps,
    total_pumps,
    mh
from (
    select
        *,
        -- 按 asset_id + mh 分组，对 running_pumps 降序排序，取排名第1的记录
        row_number() over (
            partition by asset_id, mh 
            order by running_pumps desc
        ) as rn
    from coss_tmp.dm_psr_daily_ps_running_item_di01
) t
where rn = 1;
