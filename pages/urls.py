from django.contrib import admin
from django.urls import path, include
from . import views
# from django.http import 

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
  