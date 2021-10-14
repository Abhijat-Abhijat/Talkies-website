from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
# Create your models here.

class UserLogin(models.Model):
    username = models.CharField(max_length=35)
    email = models.EmailField()
    password = models.CharField(max_length=120)
    login_count = models.PositiveBigIntegerField(default=0)