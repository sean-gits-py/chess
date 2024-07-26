CREATE TABLE games (
    game_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    white_player_id UUID NOT NULL REFERENCES players(uuid),
    black_player_id UUID NOT NULL REFERENCES players(uuid),
    result VARCHAR(10) NOT NULL,  -- '1-0', '0-1', '1/2-1/2'
    date_played DATE
);
