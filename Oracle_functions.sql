
create or replace FUNCTION f_CLOSE_PRICE (symbol_in 
IN bhav.symbol%TYPE)
   RETURN bhav.CLOSE_PRICE%TYPE
   RESULT_CACHE RELIES_ON (bhav)
IS
    l_CLOSE_PRICE   bhav.CLOSE_PRICE%TYPE;
BEGIN
   SELECT CLOSE_PRICE
      INTO l_CLOSE_PRICE
      FROM bhav a
    WHERE symbol = symbol_in  and  date1 = ( select max(date1) from bhav b where a.symbol=b.symbol );
    RETURN l_CLOSE_PRICE;
EXCEPTION
    WHEN NO_DATA_FOUND
    THEN 
       RETURN l_CLOSE_PRICE;
END f_CLOSE_PRICE;

-- select f_close_price ('RELIANCE') from dual
