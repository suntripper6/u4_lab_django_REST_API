from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    wins = models.IntegerField()
    losses = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    age = models.IntegerField()
    injured_reserve_list = models.BooleanField()
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="player")

    def __str__(self):
        return self.name
