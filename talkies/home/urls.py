from django.urls import path 
from . import views

# app_name = 'home'


urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('faq/', views.faq, name="faq"),
    path('feedback/', views.feedback, name="feedback"),
    path('search/',views.search, name ="search"),
    path('movie-about/<slug:slug>', views.movieabout, name="movie-about"),
    path('watch/<slug:slug>', views.moviewatch, name="movie-watch"),
    path('year/<int:year>', views.cat_year, name="year"),
    path('genre/<str:genre>', views.cat_genre, name="genre"),
    path('quality/<str:quality>', views.cat_quality, name="quality"),
    path('like/', views.movieLike, name="like-movie")
]