from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('faq/', views.faq, name="faq"),
    path('feedback/', views.feedback, name="feedback"),
]