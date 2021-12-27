from django.shortcuts import render

from post import forms

# Create your views here.
def register(request):
    fm=forms.Regis()
    return render(request,'post/userregistration.html',{'form':fm})
