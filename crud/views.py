from django.shortcuts import render,HttpResponseRedirect
from .forms import ServiceRegisterForm
from .models import ServiceUser
# Create your views here.


def add_show(request):
    if request.method == "POST":
        fm = ServiceRegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = ServiceRegisterForm()
    return render(request,'crud/addandshow.html',{'form':fm})


def show(request):
    if request.method=="POST":
        fm = ServiceRegisterForm(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm=ServiceRegisterForm()
    stud = ServiceUser.objects.all()
    return render(request,'crud/show.html',{'stu':stud})


def delete(request,id):
    pi = ServiceUser.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')


def update(request,id):
    if request.method=="POST":
        pi = ServiceUser.objects.get(pk=id)
        fm = ServiceRegisterForm(request.POST,instance=pi)

        if fm.is_valid():
            fm.save()
        else:
            print("Not Valid")
    else:
        pi = ServiceUser.objects.get(pk=id)
        fm = ServiceRegisterForm(instance=pi)
    return render(request,'crud/update.html', {'form':fm})
