
https://wiki.sis2.wsd.gov/ems/webresources/reports?loc_id=24&from=2023-01-01&to=2023-02-28
(conn=43276) Table 'mysql2.report_pump' doesn't exist Query: SELECT LEFT(Report_Id,LENGTH(Report_Id)-6) AS asset_id, RIGHT(Report_Id,6) as ym, Hours_Run_This_Month, Pump_Number, Water_Pumped_This_Month, pd.Name as drive, pc.Name as category, del.Name as destination, del.ID AS dest_id, Average_Head_Suct, Average_Head_Del FROM report_pump rp INNER JOIN pump_delivery_to del ON rp.Delivery_To_Id=del.ID INNER JOIN pump_category pc ON rp.Category_Id = pc.ID INNER JOIN pump_drive pd ON rp.Drive_Id = pd.ID HAVING asset_id = ? AND ym BETWEEN ? AND ? ORDER BY ym,Pump_Number Parameters: [24, 202301, 202302]

https://wiki.sis2.wsd.gov/ems/webresources/bills?from=2023-01-01&to=2023-01-31

{"exception":{"class":"SQLException","message":"(conn=43276) Table 'mysql2.billing' doesn't exist Query: SELECT b.Date, a.Name, t.Name , b.kWh_On_Peak, b.kWh_Off_Peak, b.kVA_On_Peak, b.kVA_Off_Peak, b.Payout, t.Description, a.ID  FROM billing b INNER JOIN asset a ON b.Location_Code_Id=a.ID INNER JOIN tariff t ON b.Tariff_Id=t.ID WHERE b.Date >= ? AND b.Date<= ? ORDER BY a.Name, b.Date Parameters: [2023-01-01, 2023-01-31]"}}







https://wiki.sis2.wsd.gov/ems/webresources/reports?loc_id=24&from=2023-01-01&to=2023-02-28

https://wiki.sis2/wsd.gov/ems/webresources/bills?from=2023-01-01&to=2023-01-31


https://wiki.sis2.wsd.gov/ems/webresources/assets?id=1&id=2


https://wiki.sis2.wsd.gov/ems/webresources/pumps?equip-number=M503-10905&equip-number=M524-11325
https://wiki.sis2.wsd.gov/ems/webresources/tagnames?id=4&id=55


API_URL = 'http://10.66.169.58:8001/iot3/rest/api/v1/realtime.json'
