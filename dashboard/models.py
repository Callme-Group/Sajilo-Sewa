from django.db import models


from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from django.db.models.signals import post_save


class Profile(models.Model): #Model to create profile for users
    objects = None
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


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/category/images')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Worker(models.Model):
    worker_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.worker_name


class Service(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    service_name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    service_details = models.CharField(max_length=200)
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    service_img = models.ImageField(upload_to='static/category/images',blank=True,null=True)
