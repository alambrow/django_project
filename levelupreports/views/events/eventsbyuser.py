import sqlite3
from levelupreports.views import Connection
from django.shortcuts import render
from levelupapi.models import Event

def userevent_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT g.user_id AS gamer_id, g.bio AS bio, e.id, e.date, e.time, gm.name AS game_name
                FROM levelupapi_gamer AS g, levelupapi_eventgamer AS eg, levelupapi_event AS e, levelupapi_game AS gm
                WHERE g.user_id = eg.gamer_id AND eg.event_id = e.id AND e.game_id = gm.id
                ORDER BY g.user_id ASC;
            """)

            dataset = db_cursor.fetchall()

            events_by_user = {}

            for row in dataset:
                event = Event()
                event.date = row["date"]
                event.time = row["time"]
                event.game_name = row["game_name"]
                uid = row["gamer_id"]

                if uid in events_by_user:
                    events_by_user[uid]["events"].append(event)
                else:
                    events_by_user[uid] = {}
                    events_by_user[uid]["id"] = uid
                    events_by_user[uid]["bio"] = row["bio"]
                    events_by_user[uid]["events"] = [event]
    
    userevents = events_by_user.values()

    template = 'views/events_by_user.html'
    context = {
        'userevent_list': userevents
    }

    return render(request, template, context)