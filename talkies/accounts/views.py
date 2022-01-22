from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from home.models import moviedata, moviefiles
from .forms import UserUpdateForm
from django.shortcuts import get_object_or_404

# Create your views here.

def signup(request):                        # For creating new users 
    nav = moviedata.objects.all()
    if request.method == "POST": 
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, "lsignin_up.html", {'error': "Username already taken. "})
            '''
                Try block to check if the username exists or not. If it exists, it throws an error. Else the flow continues.
            '''
        except User.DoesNotExist:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if (User.objects.filter(email=email).exists()) or (User.objects.filter(username=username).exists()):
                messages.info(request, "Email exists or username exists.")
                # If email or username exists, then throws an error message. 
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                return redirect("/user/login")
                # Redirects user to login after creating an account.
    else:
        return render(request, "signin_up.html", {"nav": nav})


def signin(request):                        # For logging in users
    nav = moviedata.objects.all()
    if request.method == "POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) 
        '''
            Authenticating the entered username and password against the default django authentication system. No need to perform 
            input sanitisation since Django authenticate() converts text to clean data and uses it to authenticate the user entered
            information. 
        '''
        if user is not None:    # If user exists.
            login(request, user)    # Default django user login function
            return redirect("/user/profile")    # Redirecting user to their profile pages
        else:
            return redirect("/user/signup/")    # User does not exist. Redirecting the user to create an account. 
    else:
        return render(request, "signin.html", {"nav": nav})     # GET rendering 


def logoutuser(request):                        # To logout a currently logged in user
    auth.logout(request)                        # Default django logout function from auth
    return redirect("/")


def userprofile(request):                       # Show users their profiles
    if request.user.is_authenticated:
        data = request.user
        nav = moviedata.objects.all()           # Moview data to render on screen 
        return render(request, "user_profile.html", {"data": data, "nav": nav})         # Rendering data about the user and the movies on the screen 
    else:
        return redirect('/user/login')          # Do not show the user profile page is authenticated session is not found. Send the 
                                                # unauthenticated user to the login page.


def userEdit(request):                          # To enable user editing
    nav = moviedata.objects.all()
    if request.method == "POST":
        update_form = UserUpdateForm(request.POST, instance=request.user)           # Updating the user profile using the user update form
        if update_form.is_valid():                                                    # Input santisation
            update_form.save()
            return redirect('profile')                                              # Redirecting the user back to their profile after updating the profile

    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        'user_form' : user_form,
        'nav' : nav
    }

    return render(request, 'user_edit.html', context)


def deactivateUser(request):                        # To deactivate a user. Does not delete them from the current records. 
    user = request.user
    user.is_active = False
    user.save()
    messages.success(request, 'User deactivated successfully! ')
    return redirect('/')


