from django.db import models


class World(models.Model):
    world_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.world_text


class Race(models.Model):
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    race_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.race_text