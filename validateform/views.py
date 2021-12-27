from django.shortcuts import render
from . import forms

# Create your views here.
def showdata(request):
    fm=forms.StuReg()
    return render(request,'validateform/stureg.html',{'form':fm})
