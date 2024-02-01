from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
import stripe
from django.conf import settings


class PaymentFormView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        }
        return render(request, 'payment_form.html', context)



@csrf_exempt
@require_POST
def process_payment(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = json.loads(request.body)
    try:
        charge = stripe.Charge.create(
            amount=1000,  # amount in cents
            currency="usd",
            description="Example charge",
            source=data['stripeToken'],  # obtained with Stripe.js
        )
        return JsonResponse({"message": "Successfully charged"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
