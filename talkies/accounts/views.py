from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import UserLogin
# Create your views here.

def signup(request):
    if request.method == "POST": 
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.info("Email exists")
        else:
            user = User.objects.create_user(name=name, email=email, password=password)
            user.save()
            
def signin(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        user = authenticate(request, email=email, password=password)


    return render(request, "signin_up.html")