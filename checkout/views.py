from django.shortcuts import render,redirect
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
import stripe
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from subscriptions.models import Subscription, UserSubscription
from checkout.models import Checkout
from django.utils import timezone
from datetime import timedelta


class PaymentFormView(View):
    def get(self, request, *args, **kwargs):
        subscription_type = request.GET.get('type')
        subscription = Subscription.objects.filter(subscription_type=subscription_type).first()
        context = {'stripe_public_key': settings.STRIPE_PUBLIC_KEY,'subscription':subscription}
        if subscription_type:
            request.session['subscription_type'] = subscription_type

        if not request.user.is_authenticated and subscription_type:
            login_url = reverse('account_login') + f"?next={reverse('create-checkout-session')}&type={subscription_type}"
            print(request.session.get('subscription_type'))
            return redirect(login_url)

        
        print(request.session.get('subscription_type'))
        return render(request, 'payment_form.html', context)


@csrf_exempt
@require_POST
def process_payment(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = json.loads(request.body)
    try:
        # Convert amount from dollars to cents for Stripe
        amount_in_dollars = float(data['amount'])
        amount_in_cents = int(amount_in_dollars * 100)
        
        # Create a Stripe charge
        charge = stripe.Charge.create(
            amount=amount_in_cents,
            currency="usd",
            description="Subscription charge",
            source=data['stripeToken'],
        )

        # If charge is successful, create a Checkout record
        if charge:
            checkout = Checkout.objects.create(
                user=request.user,
                subscription=Subscription.objects.get(id=data['subscription_id']),
                amount_paid=amount_in_dollars,
            )

            # Update or create a UserSubscription record
            current_time = timezone.now()
            UserSubscription.objects.update_or_create(
                user=request.user,
                defaults={
                    'subscription': checkout.subscription,
                    'start_date': current_time,
                    'end_date': current_time + timedelta(days=30),  # Approximation for one month
                }
            )
        
        return JsonResponse({"message": "Successfully charged and subscription updated"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


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
