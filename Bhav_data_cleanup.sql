--- data cleanup
CREATE TABLE bhav
    AS
        SELECT  /*+  parallel 10  */
            TRIM(symbol)                 symbol,
            TRIM(series)                 series,
            date1,
            to_number(prev_close)        prev_close,
            to_number(open_price)        open_price,
            to_number(high_price)        high_price,
            to_number(low_price)        low_price,
            to_number(last_price)        last_price,
            to_number(close_price)       close_price,
            to_number(avg_price)         avg_price,
            to_number(ttl_trd_qnty)      ttl_trd_qnty,
            to_number(turnover_lacs)     turnover_lacs,
            to_number(no_of_trades)      no_of_trades,
            TRIM(deliv_qty)              deliv_qty,
            TRIM(deliv_per)              deliv_per
        FROM
            bhav_master
        WHERE
            TRIM(series) = 'EQ';
            
-- delete records which is not EQ


select * from bhav

select * from (
select symbol,week,traded_qnt,DENSE_RANK() OVER (PARTITION BY symbol order by traded_qnt desc) as rankk from (
select symbol,trunc(date1, 'IW') as week, sum(TTL_TRD_QNTY)  AS traded_qnt
from bhav --where symbol ='TTKHLTCARE'
group by trunc(date1, 'IW') ,symbol  ) ranking_tab ) temp_tab where week   between '01-May-21' and '31-May-21' and rankk =1;


select * from (
select symbol,week,turnover,DENSE_RANK() OVER (PARTITION BY symbol order by turnover desc) as rankk from (
select symbol,trunc(date1, 'IW') as week, sum(TURNOVER_LACS)  AS turnover
from bhav --where symbol ='TTKHLTCARE'
group by trunc(date1, 'IW') ,symbol  ) ranking_tab ) temp_tab where week   between '24-MAY-21' and '31-May-21' and rankk =1 order by turnover desc




select * from (
select symbol,date1, TURNOVER_LACS   ,DENSE_RANK() OVER (PARTITION BY symbol order by TURNOVER_LACS desc) as rankk from bhav   
)where date1 between '27-MAY-21' and '31-May-21' and rankk =1 order by TURNOVER_LACS desc

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
