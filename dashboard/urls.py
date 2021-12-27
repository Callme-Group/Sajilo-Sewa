from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='Home'),
    path('signup/', views.register, name='Signup'),
    path('login/', views.login, name='Login'),
    path('about/', views.about, name='About')

]
