-- add log file 
sqlldr venba/venba control=C:\Users\shrio\Desktop\bhav_files\Source_code\bhav_master.txt data=C:\Users\shrio\Desktop\bhav_files\Source_code\Bhav_Master.csv

-- control file used
OPTIONS (SKIP=1)
LOAD DATA
APPEND
INTO TABLE VENBA.BHAV_MASTER
FIELDS TERMINATED BY ',' 
TRAILING NULLCOLS
(
SYMBOL, SERIES, DATE1, PREV_CLOSE, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, LAST_PRICE, CLOSE_PRICE, AVG_PRICE, TTL_TRD_QNTY, TURNOVER_LACS, NO_OF_TRADES, DELIV_QTY, DELIV_PER
--HIREDATE DATE "dd/mm/yyyy",
)


create or replace directory BHAV_COPY as 'C:\Users\shrio\Desktop\bhav_files\';
GRANT READ ON DIRECTORY BHAV_COPY TO venba;
GRANT WRITE ON DIRECTORY BHAV_COPY TO venba;
 

drop table venba.bhav_ext purge;

drop table venba.bhav_master purge;

CREATE  TABLE venba.bhav_ext
  (
     symbol        VARCHAR2(50),
     series        VARCHAR2(5),
     date1         DATE,
     prev_close    NUMBER,
     open_price    NUMBER,
     high_price    NUMBER,
     low_price     NUMBER,
     last_price    NUMBER,
     close_price   NUMBER,
     avg_price     NUMBER,
     ttl_trd_qnty  NUMBER,
     turnover_lacs NUMBER,
     no_of_trades  NUMBER,
     deliv_qty     VARCHAR2(50),
     deliv_per     VARCHAR2(50)
  )  
ORGANIZATION EXTERNAL      ( DEFAULT DIRECTORY BHAV_COPY LOCATION ('sec_bhavdata_full_31032021.csv'))
PARALLEL 25
REJECT LIMIT UNLIMITED ;

CREATE  TABLE venba.bhav_master
  (
     symbol        VARCHAR2(50),
     series        VARCHAR2(5),
     date1         DATE,
     prev_close    NUMBER,
     open_price    NUMBER,
     high_price    NUMBER,
     low_price     NUMBER,
     last_price    NUMBER,
     close_price   NUMBER,
     avg_price     NUMBER,
     ttl_trd_qnty  NUMBER,
     turnover_lacs NUMBER,
     no_of_trades  NUMBER,
     deliv_qty     VARCHAR2(50),
     deliv_per     VARCHAR2(50)
  )  ; 