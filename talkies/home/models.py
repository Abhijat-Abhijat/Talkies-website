from django.db import models
from django.db.models.fields import DurationField
from django.db.models.signals import pre_save
from talkies.utils import unique_slug_generator
from django.contrib.auth.models import User 
from django.utils.timezone import now

# Create your models here.

class feedbackModel(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    contact = models.BigIntegerField()
    message = models.TextField()
    

class moviefiles(models.Model):                     # The main movie database 
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
    id = models.IntegerField(primary_key=True)
    slug = models.CharField(max_length=130, null=True, blank=True)
    liked = models.ManyToManyField(User, related_name='movie_like')
    rt = models.IntegerField(default=1)

    def total_likes(self):
        return self.liked.count()


class moviefiles2(models.Model):                    # Database for swiper 
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
    rt = models.IntegerField(default=1)
    
class moviedata(models.Model):                          # For the nav bar
    year = models.IntegerField()
    genre = models.CharField(max_length=20)
    quality = models.CharField(max_length=25)


# class MovieComment(models.Model):
#     no = models.AutoField(primary_key= True)
#     comment = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     movie = models.ForeignKey(moviefiles, on_delete=models.CASCADE, related_name='movie_name')
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
#     date = models.DateTimeField(default=now)

#     def __str__(self):
#         return self.comment[0:15] + "..." + "by " + self.user.username