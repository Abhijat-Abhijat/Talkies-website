from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from .models import UserLogin, UserProfile
# Create your views here.

def signup(request):
    if request.method == "POST": 
        if HttpResponse == "None":
            print("Enter valid data")
            return render(request, "signin_up.html")
        else:
            # print("POST")
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if (User.objects.filter(email=email).exists()) or (User.objects.filter(username=username).exists()):
                messages.info(request, "Email exists.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("/user/login")
    elif request.method == "GET":
        print("GET")
        print(request.GET.get("switch_btn"))
        if request.GET.get("switch_btn") == "switch_btn":
            print("button clicked")
            # return redirect("/login")
        return render(request, "signin_up.html")


def signin(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        # print(user)

        if user is not None:
            login(request, user)
            data = User.objects.get(id=user.pk)
            print("User logged in")
            # return render(request, "user_profile.html", {"data":data})
            return redirect("/")
        else:
            print("User not logged in.")
            # return render(request, "index.html")
            return redirect("/login")
    else:
        return render(request, "signin.html")


def logoutuser(request):
    auth.logout(request)
    return redirect("/")
    print("User logged out. ")


def userprofile(request):
    data = request.user
    return render(request, "user_profile.html", {"data": data})