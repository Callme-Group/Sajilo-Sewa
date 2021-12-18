from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.core import validators


class RegisterUserFrom(UserCreationForm):
    """Form for creating Users"""

    class Meta:
        model = User
        first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        email = forms.EmailField(validators=[validators.EmailValidator])
        username = forms.CharField(validators=[validators.MinLengthValidator(3)])
        fields = ['first_name', 'last_name', 'email', 'username','password1','password2']


