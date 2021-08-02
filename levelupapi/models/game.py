from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):
    name = models.CharField(max_length=100)
    game_type = models.ForeignKey("GameType", on_delete=CASCADE)
    description = models.CharField(max_length=255)
    number_of_players = models.IntegerField()
    maker = models.CharField(max_length=100)