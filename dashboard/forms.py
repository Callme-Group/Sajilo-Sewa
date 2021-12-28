from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.core import validators
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class RegisterUserFrom(UserCreationForm):
    """Form for creating Users"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp','placeholder':'Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp','placeholder':'lastname'}))
    email = forms.EmailField(validators=[validators.EmailValidator], widget=forms.TextInput(attrs={'class': 'inp','placeholder':'email'}))
    username = forms.CharField(validators=[validators.MinLengthValidator(3)], widget=forms.TextInput(attrs={'class': 'inp','placeholder':'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'inp','placeholder':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'inp','placeholder':'Confirm password'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

