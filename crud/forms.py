from django import forms
from .models import ServiceUser


class ServiceRegisterForm(forms.ModelForm):
    class Meta:
        model = ServiceUser
        fields = ['name','email','password']
