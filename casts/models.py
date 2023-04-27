from django.db import models
from movies.models import Movie

# Create your models here.



class Casts(models.Model):
    character = models.CharField(max_length=255)
    actor = models.CharField(max_length=255)
    movie = models.ManyToManyField(Movie, blank=True, related_name="movies")
    actor_age = models.IntegerField()
    deceased = models.BooleanField()
    image = models.ImageField(upload_to='character/cast')
    actor_image = models.ImageField(upload_to='character/cast')
    