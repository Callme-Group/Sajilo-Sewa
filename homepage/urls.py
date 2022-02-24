from django.urls import path
from . import views
urlpatterns = [
    path('profile/', views.profile, name='Profile'),
    path('changepass/',views.changepass,name='changepass'),


    ]