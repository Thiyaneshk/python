--- data cleanup

-- delete records which is not EQ

delete from bhav_master where trim(series) <> 'EQ';
commit;
update bhav_master set SYMBOL= trim(SYMBOL) , SERIES=trim(SERIES),  DELIV_QTY=trim(DELIV_QTY) , DELIV_PER=trim(DELIV_PER);
commit;

select SYMBOL, count(1) from bhav_master group by SYMBOL order by 2;

/*
select SYMBOL , count(1) from bhav_master group by symbol
select series , count(1)  
from bhav_master where trim(DELIV_PER) ='-' group by SERIES order by 2;
select SERIES, count(1) from bhav_master group by SERIES order by 2

*/
