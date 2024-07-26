CREATE TABLE players (
    uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    player_id SERIAL UNIQUE,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
