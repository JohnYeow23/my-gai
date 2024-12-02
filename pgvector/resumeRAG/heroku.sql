SELECT *
FROM public.covid19
LIMIT 10;

-- Let's find out which continent had the highest death 
SELECT 
	continent,
	SUM(total_cases) AS region_case
FROM public.covid19
GROUP BY 
	continent;
	
-- We found that the continent has null??
SELECT DISTINCT 
	continent,
	location
FROM public.covid19;