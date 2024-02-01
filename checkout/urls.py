from django.urls import path
from .views import PaymentFormView
from .views import process_payment

urlpatterns = [
    path('create-checkout-session/', PaymentFormView.as_view(), name='create-checkout-session'),
    path('process-payment/', process_payment, name='process-payment'),

]
