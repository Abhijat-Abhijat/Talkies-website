from django.core.checks import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.core.validators import EmailValidator, validate_email
from .models import moviefiles, moviefiles2, moviedata, feedbackModel
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def home(request):
    data = moviefiles2.objects.all()
    nav = moviedata.objects.all()
    movie = moviefiles.objects.all().order_by('-views')[:10]
    action = moviefiles.objects.filter(genre__icontains="Action")
    comedy = moviefiles.objects.filter(genre__icontains="Comedy")
    drama = moviefiles.objects.filter(genre__icontains="Drama")
    animation = moviefiles.objects.filter(genre__icontains="Animation")
    thriller = moviefiles.objects.filter(genre__icontains="Thriller")
    horror = moviefiles.objects.filter(genre__icontains="Horror")
    context = {
        'data': data,
        'nav': nav,
        'movie': movie,
        'action': action,
        'comedy': comedy,
        'drama': drama,
        'animation': animation,
        'thriller': thriller,
        'horror': horror
    }
    return render(request, "index.html", context)


def about(request):
    nav = moviedata.objects.all()
    context = {
        "nav":nav
    }
    return render(request, "About.html", context)


def faq(request):
    nav = moviedata.objects.all()
    context = {
        "nav" : nav
    }
    return render(request, "FAQ.html", context)


def feedback(request):
    nav = moviedata.objects.all()
    context = {
        "nav" : nav
    }
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        message = request.POST.get("message")
        try: 
            validate_email(email)
        except ValidationError as e:
            print("Bad Email", e)
        else:
            print("Valid mail")
        data = feedbackModel(name=name, email=email, contact=contact, message=message)
        data.save()
        return render(request, "Feedback-FAQ.html")
    else:  
        return render(request, "Feedback-FAQ.html", context)

def search(request):
    query = request.GET['query']
    nav = moviedata.objects.all()
    if query == "":
        return render(request, "search_page_nomov.html")
    elif moviefiles.objects.filter(name__icontains=query):
        allmovies = moviefiles.objects.filter(name__icontains=query) 
        if not allmovies:
            return render(request, "search_page_nomov.html", {"nav": nav})
        else:
            return render(request, "search_page.html", {"allmovies": allmovies, "nav": nav })
    elif moviefiles.objects.filter(genre__icontains=query):
        allmovies = moviefiles.objects.filter(genre__icontains = query)
        if not allmovies:
            return render(request, "search_page_nomov.html", {"nav":  nav})
        else:
            return render(request, "search_page.html",  {"allmovies": allmovies, "nav": nav})
    else:
        return render(request, "search_page_nomov.html", {"nav": nav})



def movieabout(request, slug):
    data = moviefiles.objects.filter(slug=slug)
    print(data[0])
    nav = moviedata.objects.all()
    movie = moviefiles.objects.all().order_by('-views')[:5]
    # data2 = moviefiles.objects.filter(id=moviefiles.id)
    # comments = MovieComment.objects.filter(no=movie)
    # comments = MovieComment.objects.filter(movie=data)
    # comments = MovieComment.objects.filter(tag__id__in=data.all())
    comments = MovieComment.objects.filter(movie_id=data)
    # print(comments[0])
    stuff = get_object_or_404(moviefiles, slug=slug)
    total_likes = stuff.total_likes()
    liked = False
    if stuff.liked.filter(id=request.user.id).exists():
        liked = True
    
    context = {
        "data" : data,
        "nav" : nav,
        "movie" : movie,
        "total_likes" : total_likes,
        "liked" : liked,
        "comments": comments,
    }
    return render(request, "movabout.html", context)


def moviewatch(request, slug):
    nav = moviedata.objects.all()
    data = moviefiles.objects.filter(slug=slug)
    movie = moviefiles.objects.all().order_by('-views')[:5]
    movie2 = moviefiles.objects.all().order_by('-imdb_rating')[:10]
    context = {
        "nav" : nav,
        "data" : data,
        "movie" : movie,
        "movie2" : movie2
    }
    return render(request, 'movwatch.html', context)


def cat_year(request, year):
    y = {"year": year}
    if moviefiles.objects.filter(year__icontains = y['year']):
        allmovies = moviefiles.objects.filter(year__icontains = y['year'])
        return render(request, "search_page.html", {"allmovies": allmovies})
    else: 
        return render(request, "search_page_nomov.html")


def cat_genre(request, genre):
    g = {"genre": genre}
    if moviefiles.objects.filter(genre__icontains = g['genre']):
        allmovies = moviefiles.objects.filter(genre__icontains = g['genre'])
        return render(request, "search_page.html", {"allmovies":allmovies})
    else:
        return render(request, "search_page_nomov.html")


def cat_quality(request, quality):
    q = {"quality" : quality }
    if moviefiles.objects.filter(quality__icontains = q['quality']):
        allmovies = moviefiles.objects.filter(quality__icontains = q['quality'])
        return render(request, "search_page.html", {"quality": quality})
    else:
        return render(request, "search_page_nomov.html")


def movieLike(request, slug):
    user = request.user
    if user.is_authenticated:
        post = get_object_or_404(moviefiles, slug=request.POST.get('post_id'))
        liked = False  
        if post.liked.filter(id=request.user.id).exists():
            post.liked.remove(request.user)
            liked = False 
            return HttpResponseRedirect(reverse('movie-about', args=[str(slug)]))
        else:
            post.liked.add(request.user)
            liked = True
            return HttpResponseRedirect(reverse('movie-about', args=[str(slug)]))
    else: 
        return redirect('/user/signup')
        

# def movieComment(request):
#     if request.method == "POST":
#         print("POST")
#         comment = request.POST.get('comments')
#         user = request.user
#         movieid = request.POST.get('movieid')
#         print(movieid)
#         # movie = moviefiles.objects.get(id=movieid)
#         # movie = moviefiles.objects.get(id=movieid)
#         movie = moviefiles.objects.get(id=movieid)
#         print(movie)
#         comment = MovieComment(comment=comment, user=user, movie=movie)
#         comment.save() 
#         messages.Info("Comment saved.")
#     # return render(f'/movie-about/{movie.slug}')
#     return redirect('/')