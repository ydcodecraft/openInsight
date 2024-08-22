from django.db import models

from football_analysis.models.club_models import Club
from football_analysis.models.stadium_models import Stadium

class Match(models.Model):
    date_time = models.DateTimeField("Date When the Match Took Place")
    stadium = models.OneToOneField(Stadium, on_delete=models.PROTECT)
    home_team = models.OneToOneField(Club, on_delete=models.PROTECT, related_name="home_team")
    away_team = models.OneToOneField(Club, on_delete=models.PROTECT, related_name="away_team")
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.home_team} v {self.away_team} on {self.date_time} at {self.stadium}"