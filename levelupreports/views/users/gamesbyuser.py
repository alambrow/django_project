"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Game
from levelupreports.views import Connection


def usergame_list(request):
    """Function to build an HTML report of games by user"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all games, with related user info.
            db_cursor.execute("""
                SELECT 
                    id,
                    name,
                    description,
                    number_of_players,
                    maker,
                    game_type_id
                FROM levelupapi_game;
            """)

            dataset = db_cursor.fetchall()

            # Take the flat data from the database, and build the
            # following data structure for each gamer.
            #
            # {
            #     1: {
            #         "id": 1,
            #         "full_name": "Admina Straytor",
            #         "games": [
            #             {
            #                 "id": 1,
            #                 "title": "Foo",
            #                 "maker": "Bar Games",
            #                 "skill_level": 3,
            #                 "number_of_players": 4,
            #                 "game_type_id": 2
            #             }
            #         ]
            #     }
            # }

            games = []

            for row in dataset:
                # Crete a Game instance and set its properties
                game = Game()
                game.name = row["name"]
                game.maker = row["maker"]
                game.number_of_players = row["number_of_players"]
                games.append(game)
 

        # Specify the Django template and provide data context
        template = '/root/workspace/python/levelup/levelupreports/templates/views/list_with_games.html'
        context = {
            'game_list': games
        }

        return render(request, template, context)
