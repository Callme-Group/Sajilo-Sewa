from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def profile_pic_directory(self,filename):

    return "user{0}/profile_pic/{1}".format(self.user.username,filename)

class Profile(models.Model):  # Model to create profile for users
    objects = None
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    district = models.CharField(max_length=30, default="Kathmandu")
    city = models.CharField(max_length=30, default="Sundarijal")
    profile_pic = models.ImageField(blank=True, upload_to=profile_pic_directory, default='shaswot.png')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + " " + self.lastname
