from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('cancel/', cancel_subscription, name='cancel_subscription'),
]