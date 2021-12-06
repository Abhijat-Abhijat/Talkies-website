from django.core.checks import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.core.validators import EmailValidator, validate_email
from .models import moviefiles, moviefiles2, moviedata, feedbackModel
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def home(request):                          # View for hone page
    data = moviefiles2.objects.all()
    nav = moviedata.objects.all()
    movie = moviefiles.objects.all().order_by('-views')[:10]
    action = moviefiles.objects.filter(genre__icontains="Action")
    comedy = moviefiles.objects.filter(genre__icontains="Comedy")
    drama = moviefiles.objects.filter(genre__icontains="Drama")
    animation = moviefiles.objects.filter(genre__icontains="Animation")
    thriller = moviefiles.objects.filter(genre__icontains="Thriller")
    horror = moviefiles.objects.filter(genre__icontains="Horror")
    book1 = moviefiles2.objects.all().order_by('-views')[:5]
    book2 = moviefiles2.objects.all().order_by('views')[:5]
    context = {
        'data': data,
        'nav': nav,
        'movie': movie,
        'action': action,
        'comedy': comedy,
        'drama': drama,
        'animation': animation,
        'thriller': thriller,
        'horror': horror,
        'book1': book1,
        'book2': book2
    }
    return render(request, "index.html", context)


def about(request):                     # View for about page 
    nav = moviedata.objects.all()
    context = {
        "nav":nav
    }
    return render(request, "About.html", context)


def faq(request):                       # View for FAQ page 
    nav = moviedata.objects.all()
    context = {
        "nav" : nav
    }
    return render(request, "FAQ.html", context)


def feedback(request):                  # View for feedback page 
    nav = moviedata.objects.all()
    context = {
        "nav" : nav
    }
    if request.method == "POST":                        
        '''
            If the method is POST, then we will take the data the user entered and then save them to the backend. 
            Also applied a email validator using the default django validation engine to make sure that the user 
            enters a valid email. 
            This is a very basic implementation made to give an idea about the implementation. Here the user only needs to add a "@"
            symbol to get past the validation. More secure validation can be added later which checks for validation checks like gmail, 
            yahoo etc. 
        '''
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

def search(request):                        # Function to provide the website search functionality. 
    query = request.GET['query']
    nav = moviedata.objects.all()
    if query == "":         # If the user enters a blank query then show 404 page. 
        return render(request, "search_page_nomov.html")
    elif moviefiles.objects.filter(name__icontains=query):          
        '''
            The user entered data is checked. If the data matches that of a movie title, then the movie is returned. 
        '''
        allmovies = moviefiles.objects.filter(name__icontains=query) 
        if not allmovies:
            return render(request, "search_page_nomov.html", {"nav": nav})
        else:
            return render(request, "search_page.html", {"allmovies": allmovies, "nav": nav })
    elif moviefiles.objects.filter(genre__icontains=query):
        '''
            Checking if the data user entered matches a genre. If yes, then the genre is returned. 
        '''
        allmovies = moviefiles.objects.filter(genre__icontains = query)
        if not allmovies:
            return render(request, "search_page_nomov.html", {"nav":  nav})
        else:
            '''
                All the above search methods implement a functionality that if the data user entered does not match any records, 
                then we return them a 404 page. 
            '''
    else:
        return render(request, "search_page_nomov.html", {"nav": nav})



def movieabout(request, slug):                      # The about movie page function 
    data = moviefiles.objects.filter(slug=slug)
    nav = moviedata.objects.all()
    movie = moviefiles.objects.all().order_by('-views')[:5]
    stuff = get_object_or_404(moviefiles, slug=slug)
    total_likes = stuff.total_likes()
    liked = False
    if stuff.liked.filter(id=request.user.id).exists(): # If user has already liked them unlike it.
        liked = True
    
    context = {
        "data" : data,
        "nav" : nav,
        "movie" : movie,
        "total_likes" : total_likes,
        "liked" : liked,
    }
    return render(request, "movabout.html", context)


def moviewatch(request, slug):                              # Page to watch the movie 
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


def cat_year(request, year):                            # Year nav bar 
    y = {"year": year}
    if moviefiles.objects.filter(year__icontains = y['year']):
        allmovies = moviefiles.objects.filter(year__icontains = y['year'])
        return render(request, "search_page.html", {"allmovies": allmovies})
    else: 
        return render(request, "search_page_nomov.html")


def cat_genre(request, genre):                          # Genre nav bar 
    g = {"genre": genre}
    if moviefiles.objects.filter(genre__icontains = g['genre']):
        allmovies = moviefiles.objects.filter(genre__icontains = g['genre'])
        return render(request, "search_page.html", {"allmovies":allmovies})
    else:
        return render(request, "search_page_nomov.html")


def cat_quality(request, quality):                          # Quality nav bar 
    q = {"quality" : quality }
    if moviefiles.objects.filter(quality__icontains = q['quality']):
        allmovies = moviefiles.objects.filter(quality__icontains = q['quality'])
        return render(request, "search_page.html", {"quality": quality})
    else:
        return render(request, "search_page_nomov.html")


def movieLike(request, slug):                           # Function to implement the like functionality
    user = request.user
    if user.is_authenticated:
        post = get_object_or_404(moviefiles, slug=request.POST.get('post_id'))  # Get the current post 
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
        return redirect('/user/signup') # If a user tries to like but is not logged in the send them to login page
        
