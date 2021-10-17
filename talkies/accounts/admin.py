from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserLogin
# Register your models here.
admin.site.register(UserLogin)