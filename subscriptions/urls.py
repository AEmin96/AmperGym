from django.urls import path, reverse
from .views import subscriptions, cancel_subscription


app_name = 'subscriptions'

urlpatterns = [
    path('', subscriptions, name='subscriptions'),
    path('cancel/', cancel_subscription, name='cancel_subscription'),
]