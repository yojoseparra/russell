-- Financials Domain FI
-- Dates are not standardized in the database where are taking from the database financials only dates with the same format

drop table portfolio.fi;


create table portfolio.fi as 
select *, to_date(fidtc, 'YYYY-MM-DD') as fidt
from portfolio.financials 
where fidtc in  (
    '2007-09-30'
'2009-02-28',
'2015-12-31',
'2016-09-30',
'2017-09-30',
'2017-12-31',
'2018-12-31',
'2019-03-31',
'2019-04-30',
'2019-05-31',
'2019-06-30',
'2019-07-31',
'2019-09-30',
'2019-10-31',
'2019-12-31',
'2020-01-31',
'2020-02-29',
'2020-03-31',
'2020-04-30',
'2020-05-31',
'2020-06-30',
'2020-07-31',
'2020-08-31',
'2020-09-30',
'2020-10-31',
'2020-11-30',
'2020-12-31',
'2021-01-31',
'2021-02-28',
'2021-03-31',
'2021-04-30',
'2021-05-31',
'2021-06-30',
'2021-07-31',
'2021-08-31',
'2021-09-30',
'2021-10-31',
'2021-11-30',
'2021-12-31',
'2022-01-31',
'2022-02-28',
'2022-03-31',
'2022-04-30',
'2022-05-31',
'2022-06-30',
'2022-07-31',
'2022-08-31',
'2022-09-30',
'2022-10-31',
'2022-11-30',
'2022-12-31',
'2023-01-31',
'2023-02-28',
'2023-03-31',
'2023-04-30',
'2023-05-31',
'2023-06-30',
'2023-07-31',
'2023-08-31',
'2023-09-30',
'2023-10-31',
'2023-11-30',
'2023-12-31',
'2024-01-31',
'2024-02-29',
'2024-03-31',
'2024-04-30',
'2024-05-31',
'2024-06-30',
'2024-07-31',
'2024-08-31',
'2024-09-30',
'2024-10-31'
);

-- In total we have 1446 subjects in 2019 up to 1658 in 2023. This data is taken from the tickers of russell 2000 index taken from yahoo finance
select distinct subjid from portfolio.fi where fidtc in ( '2019-12-31', '2020-12-31', '2021-12-31', '2022-12-31' , '2023-12-31' );

---------------------------------------------- standardize the data by dividing everything by EBIT

-- Doing it in 2 steps as in one step does not work
create table portfolio.a as
select subjid, fiorres from portfolio.fi where  fitest in ('totalRevenue') and fidtc ='2019-12-31'  

create table portfolio.b as
select subjid, fiorres from portfolio.fi where  fitest in ('totalRevenue') and fidtc ='2020-12-31'  

create table portfolio.c as
select subjid, fiorres from portfolio.fi where  fitest in ('totalRevenue') and fidtc ='2021-12-31'  

create table portfolio.d as
select subjid, fiorres from portfolio.fi where  fitest in ('totalRevenue') and fidtc ='2022-12-31'  


create table portfolio.e as
select subjid, fiorres from portfolio.fi where  fitest in ('totalRevenue') and fidtc ='2023-12-31'  

drop table portfolio.f 
create table portfolio.f as
    select z.* ,a.fiorres as fa, b.fiorres as fb, c.fiorres as fc, d.fiorres as fd, e.fiorres as fe
                , coalesce(a.fiorres, b.fiorres, c.fiorres, d.fiorres, e.fiorres) as revenue
    from  portfolio.fi as z
    left join portfolio.a as a
        on z.subjid = a.subjid
    left join portfolio.b as b
        on z.subjid = b.subjid
    left join portfolio.c as c
        on z.subjid = c.subjid
    left join portfolio.d as d        on z.subjid = d.subjid
    left join portfolio.e as e
        on z.subjid = e.subjid
order by subjid, fidtc
;

---- fa has many missng values in 2019 so we are using the year 2020

drop table portfolio.g;

create table portfolio.adfi as 
select a.*, case when revenue > 0 then fiorres/revenue else NULL end as fistnrlo,
        case when fidtc ='2019-12-31'  and fa > 0  then fiorres / fa
             when fidtc ='2020-12-31' and fb > 0      then fiorres /fb
            when fidtc ='2021-12-31'  and fc > 0     then fiorres / fc
            when fidtc ='2022-12-31'  and fd > 0     then fiorres / fd
            when fidtc ='2023-12-31'  and fe > 0     then fiorres /fe    
        else NULL end as fistresn
from (select * from portfolio.f where fidtc in ('2019-12-31'  ,'2020-12-31'  ,'2021-12-31'  ,'2022-12-31'  ,'2023-12-31'  ) ) as a
;

select distinct subjid from portfolio.g


 -- 1506 not bad as there might be biotechs without any revenue               
select distinct subjid from portfolio.f where revenue is not NULL

order by subjid, fitest, fidtc
;

select distinct subjid from portfolio.fi


drop table portfolio.f;
create table portfolio.f as
    select a.* 
                , g.fiorres as oltd
                , b.fiorres as otd 
                , c.fiorres as oebit
                , d.fiorres as ocfo
                , e.fiorres as ofcf
                , f.fiorres as ocapex
                , h.fiorres as oequity
                 ,i.fiorres as oequityc        
                 ,j.fiorres as ocash    
                , g.fistresn as ltd
                , b.fistresn as td
                , c.fistresn as ebit
                , d.fistresn as cfo
                , e.fistresn as fcf
                , f.fistresn as capex
                , h.fistresn as equity
                 ,i.fistresn as equityc        
                 ,j.fistresn as cash      
                 , to_char( (c.fiorres*0.75 / ( h.fiorres + b.fiorres - j.fiorres))*100, '990D99%') as proic
                 , (c.fiorres*0.75 / ( h.fiorres + b.fiorres - j.fiorres)) as roic
    from (select * from portfolio.adfi) as a
    left join (  select * from portfolio.adfi where  fitest in ('longTermDebt')  ) as g
        on a.subjid = g.subjid
        and 
            a.fidtc = g.fidtc
    left join (
            select * from portfolio.adfi where  fitest in ('totalDebt')    ) as b
        on a.subjid = b.subjid
        and 
            a.fidtc = b.fidtc
     left join (
            select * from portfolio.adfi where  fitest in ('ebit')    ) as c
        on a.subjid = c.subjid
        and 
            a.fidtc = c.fidtc       
     left join (
            select * from portfolio.adfi where  fitest in ('cashFlowFromContinuingOperatingActivities')   ) as d
        on a.subjid = d.subjid
        and 
            a.fidtc = d.fidtc       
     left join (
            select * from portfolio.adfi where  fitest in ('freeCashFlow')    ) as e
        on a.subjid = e.subjid
        and 
            a.fidtc = e.fidtc     
     left join (
            select * from portfolio.adfi where  fitest in ('capitalExpenditure')   ) as f
        on a.subjid = f.subjid
        and 
            a.fidtc = f.fidtc    
     left join (
            select * from portfolio.adfi where  fitest in ('stockholdersEquity')   ) as h
        on a.subjid = h.subjid
        and 
            a.fidtc = h.fidtc    
     left join (
            select * from portfolio.adfi where  fitest in ('commonStockEquity')   ) as i
        on a.subjid = i.subjid
        and 
            a.fidtc = i.fidtc    
     left join (
            select * from portfolio.adfi where  fitest in ('cashAndCashEquivalents')   ) as j
        on a.subjid = j.subjid
        and 
            a.fidtc = j.fidtc    
order by subjid, fidtc
;


drop table portfolio.h;
create table portfolio.h as 
select * from portfolio.f 
        where subjid in (select distinct subjid from portfolio.f where (ebit is NOT NULL) and roic > 0.15)
        and subjid in (select distinct subjid from portfolio.f where ltd < 2) 
        ;


select distinct subjid from portfolio.h


drop table portfolio.i;
create table portfolio.i as 
    select a.*, ticker, name from (  select * from portfolio.h where fitest in  ('ebit','cashFlowFromContinuingOperatingActivities',   'freeCashFlow','stockholdersEquity','cashAndCashEquivalents')  ) as a
    left join portfolio.russell as b
    on a.subjid = b.company
order by subjid, fitest, fidtc


-- Finnally we choose 50 companies out of the about 1.600 from the Russell 2000. Many of these companies were house builders.

alter table portfolio.adfi drop column fa, drop column fb ,drop column fc ,drop column fd, drop column fe;
alter table portfolio.adfi drop column revenue;


drop table ru.selected;
create table ru.selected as
select * from ru.adfi where subjid in ('ATMU', 'BBSI', 'BCC', 'BDC', 'BTU', 'BXC', 'CCOI', 'CEIX', 'COCO',
       'CVLG', 'DENN', 'DIOD', 'ELA', 'EVRI', 'EVTC', 'FTDR', 'FWRD',
       'GOLF', 'GRBK', 'HCC', 'HCKT', 'HDSN', 'HLF', 'IBP', 'IDCC',
       'IMXI', 'INVA', 'IPAR', 'JBI', 'KAI', 'KRT', 'KTB', 'LEGH', 'LEU',
       'LGIH', 'MATX', 'MCRI', 'METCB', 'MHO', 'MTH', 'MYE', 'NRC',
       'PMTS', 'PRKS', 'RYI', 'SHLS', 'STC', 'STRL', 'TEX', 'TH', 'TWI',
       'UHG', 'VC', 'WNC', 'XPEL', 'ZYXI')
       order by subjid, ficat, fidtc;

ALTER SCHEMA ad RENAME TO ru;

