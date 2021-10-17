from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import UserLogin
from django.http import HttpResponseRedirect
# Create your views here.

def signup(request):
    if request.method == "POST": 
        if HttpResponse == "None":
            print("Enter valid data")
            return render(request, "signin_up.html")
        else:
            print("POST")
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email exists")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
            # return redirect(request, "/")
                return HttpResponseRedirect('/')
    elif request.method == "GET":
        print("GET")
        return render(request, "signin_up.html")


def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        



    return render(request, "signin_up.html")