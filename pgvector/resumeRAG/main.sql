---------------------------------------------------------------------------------------------------------
SELECT *
FROM langchain_pg_embedding;

SELECT *
FROM langchain_pg_collection;

-- Checking the information
SELECT 
    COUNT(*)
FROM langchain_pg_embedding;

-- Removing the values within the langchain_pg_embedding
TRUNCATE TABLE langchain_pg_embedding;
---------------------------------------------------------------------------------------------------------