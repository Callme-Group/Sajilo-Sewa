import urllib

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterUserFrom
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User, auth
import requests
import json
from django.conf import settings
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from .forms import CategoryForm
from .models import Category,Service,Worker

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def register(request):
    form = RegisterUserFrom()
    if request.method == 'POST':
        form = RegisterUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, firstname=user.first_name, lastname=user.last_name, email=user.email)
            messages.add_message(request, messages.SUCCESS, 'User created Successfully')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, "Failed to create an account, Check carefully and Try Again!")
            return render(request, 'dashboard/register.html', {'form': form})

    context = {
        'form': form
    }
    return render(request, 'dashboard/register.html', context)


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passwd = request.POST['password']
        user = auth.authenticate(username=uname, password=passwd)
        if user is not None:
            if not user.is_staff:

                auth.login(request, user)
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': settings.RECAPTCHA_PRIVATE_KEY,
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req = urllib.request.Request(url,data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
                print(result)

                ''' End reCAPTCHA validation '''
                if result['success']:
                    print('pass')
                    messages.success(request, "Welcome ...")
                    return redirect("/signup")

                else:
                    print('fail')
                    messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                    return redirect('/login')

                # return redirect("/signup")

                # return HttpResponse("Success")

            elif user.is_staff:
                auth.login(request, user)
                messages.success(request, "Welcome to ----.")
                return redirect('/admin')
                # return HttpResponse("Success")
        else:
            messages.add_message(request, messages.ERROR, "Invalid Username and Password!")
            # return render(request, 'dashboard/login.html')
            return HttpResponse("Failed")

    else:
        return render(request, 'dashboard/login.html')


def category(request):
    categ = Category.objects.all()
    ser_id = request.GET.get('service')
    if ser_id:
        service = Service.objects.filter(category=ser_id)
        context={
            'service':service
        }
        return render(request,'dashboard/rentalservices.html',context)
    return render(request,'dashboard/demo.html',{'cat':categ})


def searchMatch(query,service):
    if query in service.service_name or query in service.title:
        return True
    else:
        return False



def search(request):
    service = Service.objects.all()
    services_id = request.GET.get('query')
    if services_id:
        services = Service.objects.filter(searchMatch(services_id,service))
        return render(request,'dashboard/search.html',{'service':services})
    return render(request,'dashboard/search.html',{'services':service})








