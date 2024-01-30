from django.urls import path
from .views import create_checkout_session, session_status

urlpatterns = [
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('session-status/', session_status, name='session_status'),
]
