from django.db import models
from django.db.models.fields import DurationField
from django.db.models.signals import pre_save
from talkies.utils import unique_slug_generator
from django.contrib.auth.models import User 

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
    slug = models.CharField(max_length=130, null=True, blank=True)
    liked = models.ManyToManyField(User, related_name='movie_like')

    @property
    def num_likes(self):
        return self.liked.all().count() 


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
    slug = models.CharField(max_length=130, null=True, blank=True)
  


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator, sender=moviefiles2)


class moviedata(models.Model):
    year = models.IntegerField()
    genre = models.CharField(max_length=20)
    quality = models.CharField(max_length=25)

class Like(models.Model):
    Like_choices = (
        ("Like", "Like"),
        ("Unlike", "Unlike")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(moviefiles, default="Like", max_length=10, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movie)