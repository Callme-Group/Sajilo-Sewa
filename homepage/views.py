from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import PasswordResetForm

from django.contrib.auth.forms import PasswordChangeForm

from dashboard.models import Profile
from dashboard.models import Category
from dashboard.models import Service


# Create your views here.


def profile(request):
    profile = request.user.profile
    print(profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            print('save')
            return redirect('/homepage/profile')
    context = {
        'form': ProfileForm(instance=profile)
    }
    return render(request, 'homepage/profile.html', context)


def changepass(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            return render(request, 'homepage/profile.html')

    fm = PasswordChangeForm(user=request.user)
    return render(request, 'homepage/changepass.html', {'form': fm})
