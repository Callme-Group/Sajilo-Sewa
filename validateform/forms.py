from django import forms

class StuReg(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()