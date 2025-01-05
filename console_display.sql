

-- creating data to pass to python for further processing the data here comes from ADFI subset tickers from DS or disposition

create table ru.console_display as
select a.*, afidtc, round(cosine) as cosine, sctestcd, scgrpid,  round(fistresn*100) as fistres,   round( (chg*100)::numeric, 2)  as chgn
        from 
            ( select * from ru.adfi where subjid in (select distinct subjid from ru.ds where dsterm = 'SELECTED'))  as a
        left join
            ( select fidtc, afidtc, aval*100 as cosine, subjid from ru.adcd where param = 'FISTRESN') as b 
        on a.subjid = b.subjid
        and a.fidtc = b.fidtc
        left JOIN
            ( select distinct scgrpid, scgrp, sctest, sctestcd  from ru.sc) as c 
        on a.ficat = c.scgrp
        and a.fitest = c.sctest


-------------------------------------- SELECTING TICKERS FROM DS ----------------------------------------------------------------------

create table ru.console_display as
select a.*, sctestcd, scgrpid,  round(fistresn*100) as fistres,   round( (chg*100)::numeric, 2)  as chgn
        from 
            ( select * from ru.adfi where subjid in (select distinct subjid from ru.ds where dsterm = 'SELECTED'))  as a
        left JOIN
            ( select distinct scgrpid, scgrp, sctest, sctestcd  from ru.sc) as c 
        on a.ficat = c.scgrp
        and a.fitest = c.sctest


drop table ru.console_display

select distinct * from ru.console_display where chgn is not null

