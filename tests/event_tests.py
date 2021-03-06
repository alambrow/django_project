import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType, Event

class EventTests(APITestCase):
    def setUp(self):
        """
        Create a new account
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }

        # Initiate request and capture response
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        game_type = GameType()
        game_type.label = "Board game"
        game_type.save()
        
        new_url = "/games"
        data = {
            "name": "Clue",
            "game_type": 1,
            "description": "Who's the killer?",
            "number_of_players": 6,
            "maker": "Milton Bradley"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(new_url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["name"], "Clue")
        self.assertEqual(json_response["maker"], "Milton Bradley")
        self.assertEqual(json_response["description"], "Who's the killer?")
        self.assertEqual(json_response["number_of_players"], 6)
    
    def test_create_event(self):
        url = "/events"
        data = {
            "title": "My event",
            "date": "2021-08-28",
            "time": "11:00",
            "description": "My event",
            "host": 1,
            "game": 1
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["title"], data["title"])
    
    def test_get_event(self):
        data = {
            "title": "My event",
            "date": "2021-08-28",
            "time": "11:00:00",
            "description": "My event",
            "host": 1,
            "game": 1
        }
        event = Event()
        event.title = data["title"]
        event.date = data["date"]
        event.time = data["time"]
        event.description = data["description"]
        event.host_id = 1
        event.game_id = 1
        event.save()
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(f"/events/{event.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["title"], data["title"])
        self.assertEqual(json_response["date"], data["date"])
        self.assertEqual(json_response["time"], data["time"])
        self.assertEqual(json_response["description"], data["description"])
    
    def test_change_event(self):
        data = {
            "title": "My event",
            "date": "2021-08-28",
            "time": "11:00:00",
            "description": "My event",
            "host": 1,
            "game": 1
        }
        event = Event()
        event.title = data["title"]
        event.date = data["date"]
        event.time = data["time"]
        event.description = data["description"]
        event.host_id = 1
        event.game_id = 1
        event.save()

        new_data = {
            "id": event.id,
            "title": "My new event",
            "date": "2021-08-28",
            "time": "11:00:00",
            "description": "My new event",
            "game": 1,
            "host": 1
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(f"/events/{event.id}", new_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        response = self.client.get(f"/events/{event.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["title"], new_data["title"])
        self.assertEqual(json_response["date"], new_data["date"])
        self.assertEqual(json_response["time"], new_data["time"])
        self.assertEqual(json_response["description"], new_data["description"])

    def test_delete_event(self):
        data = {
            "title": "My event",
            "date": "2021-08-28",
            "time": "11:00:00",
            "description": "My event",
            "host": 1,
            "game": 1
        }
        event = Event()
        event.title = data["title"]
        event.date = data["date"]
        event.time = data["time"]
        event.description = data["description"]
        event.host_id = 1
        event.game_id = 1
        event.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.delete(f"/events/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/events/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # def test_join_event(self):
    #     data = {
    #         "title": "My event",
    #         "date": "2021-08-28",
    #         "time": "11:00:00",
    #         "description": "My event",
    #         "host": 1,
    #         "game": 1
    #     }
    #     event = Event()
    #     event.title = data["title"]
    #     event.date = data["date"]
    #     event.time = data["time"]
    #     event.description = data["description"]
    #     event.host_id = 1
    #     event.game_id = 1
    #     event.save()
        
    #     join_data = event.id
        
    #     new_url = "/events/{event.id}/signup"
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    #     response = self.client.post(new_url)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
