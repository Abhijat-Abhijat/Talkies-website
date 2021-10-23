from typing import NewType
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User

# from talkies.home.models import moviedata
from home.models import moviedata
from .forms import UserUpdateForm
from .models import UserLogin

# Create your views here.

def signup(request):
    nav = moviedata.objects.all()
    if request.method == "POST": 
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, "login.html", {'error': "Username already taken. "})
        except User.DoesNotExist:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            facebook = request.POST.get('facebook')
            twitter = request.POST.get('twitter')
            instagram = request.POST.get('instagram')
            if (User.objects.filter(email=email).exists()) or (User.objects.filter(username=username).exists()):
                messages.info(request, "Email exists.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                userlogin = UserLogin(facebook=facebook, twitter=twitter, instagram=instagram, user=user)
                userlogin.save()
                return redirect("/user/login")
    else:
        return render(request, "signin_up.html", {"nav": nav})


def signin(request):
    nav = moviedata.objects.all()
    if request.method == "POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # data = User.objects.get(id=user.pk)
            print("User logged in")
            # return render(request, "user_profile.html", {"data":data})
            return redirect("/user/profile")
        else:
            print("User not logged in.")
            # return render(request, "index.html")
            return redirect("/user/signup/")
    else:
        return render(request, "signin.html", {"nav": nav})


def logoutuser(request):
    auth.logout(request)
    return redirect("/")
    print("User logged out. ")


def userprofile(request):
    if request.user.is_authenticated:
        data = request.user
        nav = moviedata.objects.all()
        return render(request, "user_profile.html", {"data": data, "nav": nav})
    else:
        return redirect('/user/login')


def userEdit(request):
    nav = moviedata.objects.all()
    if request.method == "POST":
        update_form = UserUpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        'user_form' : user_form,
        'nav' : nav
    }

    return render(request, 'user_edit.html', context)


def deactivateUser(request):
    user = request.user
    user.is_active = False
    user.save()
    messages.success(request, 'User deactivated successfully! ')
    return redirect('/')
    