DROP TABLE IF EXISTS birds CASCADE;

CREATE TABLE birds (
    name TEXT,
    scientific_name TEXT,
    observation_count INTEGER,
    country_code TEXT,
    state TEXT,
    county TEXT,
    locality TEXT,
    observer_id TEXT,
    observation_type TEXT,
);

\copy birds(
    name, 
    scientific_name, 
    observation_count, 
    country_code, 
    state, 
    county, 
    locality, 
    observer_id, 
    observation_type) 
FROM 'birds.csv' with (format csv, HEADER true);