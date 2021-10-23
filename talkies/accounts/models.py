from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class UserLogin(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    # email = models.EmailField()
    # password = models.CharField(max_length=120)
    # login_count = models.PositiveBigIntegerField(default=0)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
     




# class extenduser(models.Model):
#     user = models.OneToOneField(User, on_delete=CASCADE)
#     facebook = models.URLField()
#     twitter = models.URLField()
#     instagram = models.URLField()

class newUser(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
