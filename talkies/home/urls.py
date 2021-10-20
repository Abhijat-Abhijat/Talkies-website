from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('faq/', views.faq, name="faq"),
    path('feedback/', views.feedback, name="feedback"),
    path('search/',views.search, name ="search"),
    # path('page/', views.home2, name="home2"),
    path('movie-about/<slug:slug>', views.movieabout, name="movie-about"),
    path('watch/<slug:slug>', views.moviewatch, name="movie-watch"),
]