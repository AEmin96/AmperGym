from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('location/', views.location, name='location'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('aboutus/', views.aboutus, name='aboutus'),
]