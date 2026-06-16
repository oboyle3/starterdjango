from django.db import models

# Create your models here.
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name="home_matches", on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name="away_matches", on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"