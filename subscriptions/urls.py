from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('cancel/', views.cancel_subscription, name='cancel_subscription'),
]