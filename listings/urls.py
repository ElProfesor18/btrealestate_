from django.contrib import admin
from django.urls import path, include
from . import views
# from django.http import 

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_ind>', views.listing, name='listing'),
    path('search/', views.search, name='search'),
    
]
  