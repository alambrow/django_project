from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)