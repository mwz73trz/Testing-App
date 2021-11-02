from django.db import models
from django.contrib.auth.models import User

class Sport(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sports")

    def __str__(self):
        return f"{self.name}"

class Team(models.Model):
    name = models.CharField(max_length=200)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="teams")

    def __str__(self):
        return f"{self.name}"
