from django.db import models

from football_analysis.models.club_models import Club


class Player(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    age = models.IntegerField(default=0)
    height = models.FloatField(default=0)
    club = models.OneToOneField(Club, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    
