from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        help_texts = {
            'username': None,
            'email': None, 
        }
        fields = ['username', 'email']