SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;
SELECT * FROM levelupapi_game;
SELECT * FROM levelupapi_event;

SELECT * FROM levelupapi_game;

SELECT 
    id,
    name,
    description,
    number_of_players,
    maker,
    game_type_id
FROM levelupapi_game;