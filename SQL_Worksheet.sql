select * from bhav_master where symbol ='TIDEWATER';
 
select symbol, round(avg(last_price),2) avg_price,round( avg(deliv_per),2) avg_deliv_per from bhav_master  group by symbol;
select symbol, round(avg(last_price),2), (select last_price from bhav_master where date1 =(select max(date1) from bhav_master  )) LTP,round( avg(deliv_per),2) from bhav_master  group by symbol, LTP
;

delete from bhav_master where trim(series) <> 'EQ';
commit;
update bhav_master set SYMBOL= trim(SYMBOL) , SERIES=trim(SERIES),  DELIV_QTY=trim(DELIV_QTY) , DELIV_PER=trim(DELIV_PER);
commit;

select symbol , avg_price, avg_deliv_per , (select last_price from bhav_master b where date1 =(select max(date1) from bhav_master where a.symbol = b.symbol )) LTP
from  (
select symbol, round(avg(last_price),2) avg_price,round( avg(deliv_per),2) avg_deliv_per from bhav_master where to_date(date1,'DD-MON-YY') between   '01-MAY-21' and '30-MAY-21' group by symbol ) a ;
