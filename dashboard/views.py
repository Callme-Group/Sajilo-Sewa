from django.shortcuts import render, redirect
from .forms import RegisterUserFrom
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User, auth


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
                return redirect("/")

            elif user.is_staff:
                auth.login(request, user)
                return redirect('/admin')

        else:
            messages.add_message(request, messages.ERROR, "Invalid Username and Password!")
            return render(request, 'dashboard/login.html')

    else:
        return render(request, 'dashboard/login.html')
