from django.contrib import admin
from .models import Category,Worker,Service,BlogComment
# Register your models here.
@admin.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','description']


@admin.register(Worker)


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id','worker_name','phone','address']

@admin.register(Service)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','service_name','title','price','service_details','status','category','worker']


admin.site.register(BlogComment)