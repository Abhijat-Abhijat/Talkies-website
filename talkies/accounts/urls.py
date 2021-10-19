from django.urls import path 
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signin"),
    path('login/', views.signin, name="signin"),
    path('profile/', views.userprofile, name="profile"),
    path('logout/', views.logoutuser, name="logout"),
]