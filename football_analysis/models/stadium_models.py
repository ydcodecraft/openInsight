from django.db import models

class Stadium(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.name} in {self.city}, {self.country}"