from django.urls import path
from .views import subscriptions_view, cancel_subscription

app_name = 'subscriptions'

urlpatterns = [
    path('', subscriptions_view, name='subscriptions_view'),
    path('cancel/', cancel_subscription, name='cancel_subscription'),
]
