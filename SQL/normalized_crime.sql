CREATE TABLE normalized_crime (
    state TEXT,
    category TEXT,
    value INTEGER
);


INSERT INTO normalized_crime (state, category, value)
SELECT state, 'total_all_classes', total_all_classes FROM crime
UNION ALL
SELECT state, 'violent_crime', violent_crime FROM crime
UNION ALL
SELECT state, 'property_crime', property_crime FROM crime
UNION ALL
SELECT state, 'murder_nonnegligent', murder_nonnegligent FROM crime
UNION ALL
SELECT state, 'rape', rape FROM crime
UNION ALL
SELECT state, 'robbery', robbery FROM crime
UNION ALL
SELECT state, 'aggravated_assault', aggravated_assault FROM crime
UNION ALL
SELECT state, 'burglary', burglary FROM crime
UNION ALL
SELECT state, 'larceny_theft', larceny_theft FROM crime
UNION ALL
SELECT state, 'motor_vehicle_theft', motor_vehicle_theft FROM crime
UNION ALL
SELECT state, 'arson', arson FROM crime
UNION ALL
SELECT state, 'other_assaults', other_assaults FROM crime
UNION ALL
SELECT state, 'forgery_counterfeiting', forgery_counterfeiting FROM crime
UNION ALL
SELECT state, 'fraud', fraud FROM crime
UNION ALL
SELECT state, 'embezzlement', embezzlement FROM crime
UNION ALL
SELECT state, 'stolen_property', stolen_property FROM crime
UNION ALL
SELECT state, 'vandalism', vandalism FROM crime
UNION ALL
SELECT state, 'weapons_possession', weapons_possession FROM crime
UNION ALL
SELECT state, 'prostitution_vice', prostitution_vice FROM crime
UNION ALL
SELECT state, 'sex_offenses', sex_offenses FROM crime
UNION ALL
SELECT state, 'drug_abuse_violations', drug_abuse_violations FROM crime
UNION ALL
SELECT state, 'gambling', gambling FROM crime
UNION ALL
SELECT state, 'family_offenses', family_offenses FROM crime
UNION ALL
SELECT state, 'dui', dui FROM crime
UNION ALL
SELECT state, 'liquor_laws', liquor_laws FROM crime
UNION ALL
SELECT state, 'drunkenness', drunkenness FROM crime
UNION ALL
SELECT state, 'disorderly_conduct', disorderly_conduct FROM crime
UNION ALL
SELECT state, 'vagrancy', vagrancy FROM crime
UNION ALL
SELECT state, 'other_offenses', other_offenses FROM crime
UNION ALL
SELECT state, 'suspicion', suspicion FROM crime
UNION ALL
SELECT state, 'curfew_loitering', curfew_loitering FROM crime;
