from django.urls import path
from . import views

urlpatterns=[
    path('crud1/',views.add_show,name='addandshow'),
    path('curd2/',views.show,name='show'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
]