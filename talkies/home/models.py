from django.db import models
from django.db.models.fields import DurationField

# Create your models here.

class feedbackModel(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    contact = models.BigIntegerField()
    message = models.TextField()
    

class moviefiles(models.Model):
    name = models.CharField(max_length=50)
    download = models.URLField()
    duration = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    imdb_rating = models.DecimalField(decimal_places=1,max_digits=10)
    poster = models.URLField()
    stream = models.URLField()
    trailer = models.URLField()
    user_rating = models.DecimalField(decimal_places=1, max_digits=10)
    views = models.IntegerField()
    year = models.IntegerField()
    summary = models.TextField(max_length=500)
    movie_id = models.IntegerField(default=1)


class moviefiles2(models.Model):
    name = models.CharField(max_length=50)
    download = models.URLField()
    duration = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    imdb_rating = models.DecimalField(decimal_places=1,max_digits=10)
    poster = models.URLField()
    stream = models.URLField()
    trailer = models.URLField()
    user_rating = models.DecimalField(decimal_places=1, max_digits=10)
    views = models.IntegerField()
    year = models.IntegerField()
    summary = models.TextField(max_length=500)
    movie_id = models.IntegerField(default=1)