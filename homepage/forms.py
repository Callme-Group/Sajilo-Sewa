from dashboard.models import Profile
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    district = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']