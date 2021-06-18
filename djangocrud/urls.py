from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('create/',views.createandshow,name='createandshow'),
    path('delete/<int:pk>/',views.delete,name='deletedata'),
    path('update/<int:id>/',views.update,name='updatedata'),



]