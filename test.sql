SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;
SELECT * FROM levelupapi_game;
SELECT * FROM levelupapi_event;

SELECT * FROM levelupapi_game;

SELECT 
    g.id,
    g.name,
    g.description,
    g.number_of_players,
    g.maker,
    g.game_type_id,
FROM levelupapi_game g
WHERE g.id = 1;