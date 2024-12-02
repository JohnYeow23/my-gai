---------------------------------------------------------------------------------------------------------
SELECT
	collection_id,
	document,
	cmetadata,
	custom_id,
	uuid
FROM langchain_pg_embedding;

SELECT DISTINCT custom_id
FROM langchain_pg_embedding;

SELECT *
FROM langchain_pg_collection;

-- Checking the information
SELECT 
    COUNT(*)
FROM langchain_pg_embedding;

-- Removing the values within the langchain_pg_embedding
TRUNCATE TABLE langchain_pg_embedding;

-- Connecting the data together to make sure the data is uniquely
SELECT 
	embed.document,
	collect.name,
	collect.cmetadata
FROM langchain_pg_embedding AS embed
LEFT JOIN langchain_pg_collection AS collect
			 ON embed.collection_id = collect.uuid;
---------------------------------------------------------------------------------------------------------

-- ALTER TABLE langchain_pg_embedding
-- ADD COLUMN IF NOT EXISTS created_datetime TIMESTAMP;

-- UPDATE langchain_pg_embedding
-- SET created_datetime = NOW();

---------------------------------------------------------------------------------------------------------

-- Change the connection to the other database

SELECT document
FROM langchain_pg_embedding
LIMIT 1;

-- TRUNCATE TABLE langchain_pg_embedding;