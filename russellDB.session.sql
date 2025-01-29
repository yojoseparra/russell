
--------- This code sets up the embeddings table with the id column from pgvector
# rol superuser
SELECT rolname, rolsuper FROM pg_roles;


create extension if not exists vector;

SELECT * FROM pg_available_extensions WHERE name = 'vector';
SELECT * FROM pg_extension WHERE extname = 'vector';


drop table public.em.em;create INDEX if not exists "idx" on em.em using hnsw("embedding", vector_cosine_ops);
--------------------------- ccreate schema embeddings -------------------------
create extension if not exists vector;
CREATE EXTENSION IF NOT EXISTS vector;


create schema em;
CREATE TABLE IF NOT EXISTS em.em (
    id SERIAL PRIMARY KEY,
    embedding VECTOR(1536),  -- Single column for vector data
    name TEXT,
    content TEXT, 
    dtm TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_embedding ON em.em USING hnsw (embedding vector_cosine_ops);

--CREATE INDEX IF NOT EXISTS idx_embedding ON em.em USING ivfflat (embedding vector_cosine_ops);
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'em.em';

select * from ru.pr where subjid in ('DIOD', 'XPEL')
select * from ru.pr where subjid = 'EVRI'


------------------- we have chosen handful companies
UPDATE ru.ds SET (dsterm, dsdecod) = ('', 'DISCARTED AFTER FURTHER ROUND OF ANALYSIS')
WHERE subjid not in ('TH','MATX', 'HDSN','MCRI','IDCC','SHLS','MTH','KAI','FWRD');

UPDATE ru.ds SET (dsterm, dsdecod) = ('SELECTED', 'SELECTED AS FINANCIALLY SOUND COMPANY')
WHERE subjid in ('XPEL');


------------------------------ Quarterly -----------------------------------------------------

CREATE TABLE ru.qfi (
    domain text,
    ficat text,
    subjid text,
    fitest text,
    fiorres double precision,    
    fiorresu text,
    fidtc text,
    fiperiod text
);

select * from ru.admo where subjid = 'MSFT'

select * from ru.cd where aval > 0.95 or aval < -0.95

select * from ru.cd where subjid = 'MSFT' and (aval < -0.9 or aval > 0.9)


drop table ru.pr;

CREATE TABLE ru.pr (
   index TEXT, 
   address1 TEXT, 
   address2 TEXT, 
   city TEXT, 
   zip TEXT, 
   country TEXT,
    phone  TEXT, 
    fax  TEXT,
    website TEXT, 
    industry TEXT, 
    industryKey TEXT, 
    industryDisp TEXT,
    sector TEXT, 
    sectorKey TEXT, 
    sectorDisp TEXT, 
    longBusinessSummary TEXT,
    fullTimeEmployees TEXT, 
    companyOfficers TEXT, 
    compensationAsOfEpochDate TEXT,
    maxAge TEXT, 
    state TEXT, 
    auditRisk TEXT, 
    boardRisk TEXT, 
    compensationRisk TEXT,
    shareHolderRightsRisk TEXT, 
    overallRisk TEXT, 
    governanceEpochDate TEXT,
    irWebsite TEXT, 
    executiveTeam TEXT, 
    address3 TEXT
);

--------------------- EBIT > 30% ------------------------------
select * from ru.cd where subjid in (select distinct subjid from ru.admo where fitest = 'EBIT' and fistresn > 0.30)


-------------------------------------------------------------------------- ROI calc --------------------------------
-- this code does not distinguish companies reporting in different currencies, it looks it s not important though
-- BABA is quoted in CNY and USD, for this company this query makes no sense
drop table ru.roi;
create table ru.roi as 
select a.subjid, a.fidtc, a.fiorresu, fcf, coalesce(sbc, 0) as sbc, tas, tde, tre, ((fcf - coalesce(sbc, 0))/ tas)*100  as roi 
        from 
        (select distinct subjid, fiorresu,fidtc::date AS fidtc from ru.admo) as a
        left join
        (select distinct subjid, fiorresu, fiorres/1000000 as fcf, fidtc::date AS fidtc from ru.admo where fitest = 'FreeCashFlow' ) as aa
        on a.subjid = aa.subjid
        and a.fidtc = aa.fidtc 
        and a.fiorresu = aa.fiorresu
        left join
        (select ficat, subjid, fiorresu,fiorres/1000000 as sbc, fidtc::date AS fidtc from ru.admo where fitest = 'StockBasedCompensation' ) as b
        on a.subjid = b.subjid
        and a.fidtc = b.fidtc 
        and a.fiorresu = b.fiorresu
        left join
        (select ficat, subjid, fiorresu,fiorres/1000000 as tas, fidtc::date AS fidtc from ru.admo where fitest = 'TotalAssets' ) as c
        on  a.subjid = c.subjid
        and a.fidtc = c.fidtc
        and a.fiorresu =c.fiorresu
        left join
        (select ficat, subjid, fiorresu, fiorres/1000000 as tde, fidtc::date AS fidtc from ru.admo where fitest = 'TotalDebt' ) as d
        on  a.subjid = d.subjid
        and a.fidtc = d.fidtc
        and a.fiorresu = d.fiorresu
        left join
        (select ficat, subjid, fiorresu, fiorres/1000000 as tre, fidtc::date AS fidtc from ru.admo where fitest = 'TotalRevenue' ) as e
        on  a.subjid = e.subjid
        and a.fidtc = e.fidtc
        and a.fiorresu = e.fiorresu

-------------------- Select a ROI > 30%

select distinct 
                subjid, fidtc, fiorresu, round(fcf) AS fcf, round(sbc) as sbc, round(tas) as tas, 
                round(tde) as tde, round(roi) as roi, round(tre) as tre 
from ru.roi where roi  > 15 
order by  subjid, tre, roi 

-------------------------------------------------------------------------- ROI/MarketCap calc --------------------------------

select a.*, round(cast(mc as numeric)/1000000) as mc,  
    CASE 
        WHEN fcf <> 0 THEN cast(mc as numeric)   / (1000000*fcf -  coalesce(1000000*sbc, 0) ) 
        ELSE NULL -- Or 0, or any default value you'd like
    END as fcf_times 
from (select * from ru.roi where fiorresu in ('USD', 'EUR', 'DKK') and fidtc > '2020-01-01') as a 
left join (select fiorres as mc, subjid from ru.ma where fitest = 'marketCap') as b 
on a.subjid = b.subjid


select * from ru.admo where subjid = 'NVO' and fitest = 'FreeCashFlow'





------------------------------------------------------------------------------------------------------------------
select subjid, avg(aval) as m  
from ru.cd group by (dtype, param, subjid)
having subjid in (select distinct subjid from ru.admo where fitest = 'EBIT' and fistresn > 0.30)


SELECT * from ru.admo where subjid = 'MSFT'

select subjid, fidtc, SPLIT_PART(afidtc, '_', 1) as subjid1, aval as cosine 
from ru.cd where subjid = 'DIOD' and (aval < -0.85 or aval > 0.85)", conn);


