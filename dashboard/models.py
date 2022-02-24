from django.db import models

from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
def profile_pic_directory(self, filename):
    return "user{0}/profile_pic/{1}".format(self.user.username, filename)

class Profile(models.Model):  # Model to create profile for users
    objects = None
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10, default="1234567890")
    district = models.CharField(max_length=30, default="Kathmandu")
    city = models.CharField(max_length=30, default="Sundarijal")
    profile_pic = models.ImageField(blank=True, upload_to='static/profile/images', default='static/images/shaswot.jpg')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    service_details = models.CharField(max_length=200)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    service_img = models.ImageField(upload_to='static/category/images', blank=True, null=True)
    count = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.service_name

class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_post = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    top = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default=now)
    like = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.comment_post[0:10] + "..." + "by" + " " + self.user.username


# one customer have multipe order
class Order(models.Model):
    objects = None
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=230, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.service.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

# for cart which hase multiple services with order
class OrderItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.service.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
