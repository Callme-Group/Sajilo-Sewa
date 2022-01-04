from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.core import validators
from .models import Category
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class RegisterUserFrom(UserCreationForm):
    """Form for creating Users"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(validators=[validators.EmailValidator], widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(validators=[validators.MinLengthValidator(3)], widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name','image','description']


