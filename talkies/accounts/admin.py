from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserLogin
from .models import newUser
# Register your models here.
admin.site.register(UserLogin)

admin.site.register(newUser)