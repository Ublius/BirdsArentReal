DROP TABLE IF EXISTS crimes CASCADE;

CREATE TABLE crimes (
    state TEXT,
    total_all_classes INTEGER,
    violent_crime INTEGER,
    property_crime INTEGER,
    murder_nonnegligent INTEGER,
    rape INTEGER,
    robbery INTEGER,
    aggravated_assault INTEGER,
    burglary INTEGER,
    larceny_theft INTEGER,
    motor_vehicle_theft INTEGER,
    arson INTEGER,
    other_assaults INTEGER,
    forgery_counterfeiting INTEGER,
    fraud INTEGER,
    embezzlement INTEGER,
    stolen_property INTEGER,
    vandalism INTEGER,
    weapons_possession INTEGER,
    prostitution_vice INTEGER,
    sex_offenses INTEGER,
    drug_abuse_violations INTEGER,
    gambling INTEGER,
    family_offenses INTEGER,
    dui INTEGER,
    liquor_laws INTEGER,
    drunkenness INTEGER,
    disorderly_conduct INTEGER,
    vagrancy INTEGER,
    other_offenses INTEGER,
    suspicion INTEGER,
    curfew_loitering INTEGER,
    number_of_agencies INTEGER,
    population_2023 BIGINT
);

\copy crimes FROM 'CrimesState.csv' with (format csv, HEADER true);

