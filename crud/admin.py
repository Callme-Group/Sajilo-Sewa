from django.contrib import admin
from .models import ServiceUser
# Register your models here.


@admin.register(ServiceUser)
class ServiceUserAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']
