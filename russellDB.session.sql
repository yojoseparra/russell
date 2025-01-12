
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





