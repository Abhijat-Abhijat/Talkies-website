from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import feedbackModel
from django.core.validators import EmailValidator, validate_email
# Create your views here.

def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "About.html")


def faq(request):
    return render(request, "FAQ.html")


def feedback(request):
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
        return render(request, "Feedback-FAQ.html")