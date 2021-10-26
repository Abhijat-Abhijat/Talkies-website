from django.core.exceptions import ValidationError
from django.db.models.query_utils import refs_expression
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Like, feedbackModel
from django.core.validators import EmailValidator, validate_email
from django.http import HttpResponseRedirect
from django.urls import reverse 
# from .models import moviedata
from .models import moviefiles, moviefiles2, moviedata
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
    return render(request, "About.html", {"nav": nav})


def faq(request):
    nav = moviedata.objects.all()
    return render(request, "FAQ.html", {"nav": nav})


def feedback(request):
    nav = moviedata.objects.all()
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
        return render(request, "Feedback-FAQ.html", {"nav" : nav})

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
            # data = {'allmovies': allmovies}
            return render(request, "search_page.html", {"allmovies": allmovies, "nav": nav })
    elif moviefiles.objects.filter(genre__icontains=query):
        allmovies = moviefiles.objects.filter(genre__icontains = query)
        if not allmovies:
            return render(request, "search_page_nomov.html", {"nav":  nav})
        else:
            # data = {'allmovies': allmovies}
            return render(request, "search_page.html",  {"allmovies": allmovies, "nav": nav})
    else:
        return render(request, "search_page_nomov.html", {"nav": nav})



def movieabout(request, slug):
    data = moviefiles.objects.filter(slug=slug)
    nav = moviedata.objects.all()
    movie = moviefiles.objects.all().order_by('-views')[:5]
    return render(request, "movabout.html", {"data": data, "nav": nav, "movie": movie})


def moviewatch(request, slug):
    nav = moviedata.objects.all()
    data = moviefiles.objects.filter(slug=slug)
    return render(request, 'movwatch.html', {"data":  data, "nav": nav})


def cat_year(request, year):
    # y = request.GET['name']
    y = {"year": year}
    print(y['year'])
    if moviefiles.objects.filter(year__icontains = y['year']):
        allmovies = moviefiles.objects.filter(year__icontains = y['year'])
        print(allmovies)
        # {"yeardata":yeardata}
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


def movieLike(request):
    user = request.user
    if request.method == "POST":
        print("POST")
        movie_id = request.POST.get('home:movie_id')
        # print(movie_id)
        obj = moviefiles2.objects.get(id=movie_id)

        if user in obj.liked.all():
            obj.liked.remove(user)
            print("removed like")
        else:
            obj.liked.add(user)
            print("added like")
        like, created = Like.objects.get_or_create(user=user, movie_id=movie_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save() 
    else:
        print("GET")
    return redirect('home:movie-about/')
    