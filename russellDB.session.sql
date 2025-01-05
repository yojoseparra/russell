
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