from django.db import models

from football_analysis.models.stadium_models import Stadium

class Club(models.Model):
    name = models.CharField(max_length=75)
    home_stadium = models.OneToOneField(Stadium, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    