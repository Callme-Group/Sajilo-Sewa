from django import forms

class Regis(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password= forms.CharField()