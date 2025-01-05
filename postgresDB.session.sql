

create database russell
create user jose with password 'sfgdsfg';
GRANT ALL PRIVILEGES ON DATABASE russell TO jose;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO jose;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO jose;

SELECT schema_name, schema_owner FROM information_schema.schemata WHERE schema_name = 'public';



--ALTER SCHEMA public OWNER TO jose;
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA public TO jose;

SELECT schema_name, schema_owner FROM information_schema.schemata WHERE schema_name = 'public';


ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO jose;


GRANT CREATE ON SCHEMA public TO jose;

SHOW search_path;

ALTER ROLE jose SET search_path TO schema_name, public;
GRANT USAGE ON SCHEMA public TO jose;

ALTER SCHEMA public OWNER TO jose;

grant all on all tables in schema public to jose

GRANT admins TO jose;

drop table portfolio.russell

-- Vector Embeddings

SELECT rolname, rolsuper FROM pg_roles WHERE rolname = 'jose';
CREATE EXTENSION vector;
GRANT CREATE ON DATABASE russell TO jose;

create extension if not exists vector;
SELECT * FROM pg_available_extensions WHERE name = 'vector';

ALTER EXTENSION vector OWNER TO jose;
-- i have an issue, i cannot chante the owner to jose and it looks like the vector extension is too old
SELECT version();
drop extension vector;

SELECT 
    objid::regclass AS dependent_object, 
    classid::regclass AS object_type 
FROM 
    pg_depend 
WHERE 
    refobjid = (SELECT oid FROM pg_extension WHERE extname = 'vector');
