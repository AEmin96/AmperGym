from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('location/', views.location, name='location'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('user_profile_edit/', views.user_profile_edit, name='user_profile_edit'),

]