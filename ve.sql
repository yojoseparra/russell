-- Vector Embeddings

SELECT rolname, rolsuper FROM pg_roles WHERE rolname = 'jose';
CREATE EXTENSION vector;
GRANT CREATE ON DATABASE your_database TO your_username;

create extension if not exists vector;
SELECT * FROM pg_available_extensions WHERE name = 'vector';

ALTER EXTENSION vector OWNER TO your_username;

