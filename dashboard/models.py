from django.db import models


from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from django.db.models.signals import post_save




class Profile(models.Model): #Model to create profile for users
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    district = models.CharField(max_length=30, default="Kathmandu")
    city = models.CharField(max_length=30, default="Sundarijal")
    profile_pic = models.FileField(upload_to='images/profiles', default='sample_user.jpg')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + " "+ self.lastname

# Create your models here.
