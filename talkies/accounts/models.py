from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class UserLogin(models.Model):                                     
    user = models.OneToOneField(User, on_delete=CASCADE)
    # facebook = models.URLField(null=True, blank=True)
    # twitter = models.URLField(null=True, blank=True)
    # instagram = models.URLField(null=True, blank=True)
     
     
# class newUser(models.Model):
#     user = models.OneToOneField(User, on_delete=CASCADE)
#     facebook = models.URLField()
#     twitter = models.URLField()
#     instagram = models.URLField()
