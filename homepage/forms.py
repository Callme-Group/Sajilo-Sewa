from .models import Profile
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user', 'username', 'email', 'created_date']
