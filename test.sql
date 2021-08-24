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

SELECT *
FROM levelupapi_gamer;

SELECT g.user_id AS gamer_id, g.bio AS bio, e.id, e.date, e.time, gm.name AS game_name
FROM levelupapi_gamer AS g, levelupapi_eventgamer AS eg, levelupapi_event AS e, levelupapi_game AS gm
WHERE g.user_id = eg.gamer_id AND eg.event_id = e.id AND e.game_id = gm.id
ORDER BY g.user_id ASC;