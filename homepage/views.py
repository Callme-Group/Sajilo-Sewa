from django.shortcuts import render,redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from dashboard.auth import user_only
from .models import Profile


# Create your views here.

@login_required
def profile(request):
    profile = request.user.profile
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
