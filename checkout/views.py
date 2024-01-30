from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import stripe

# Create your views here.
stripe.api_key = 'pk_live_51OeDfNHcbPs5lobJhCwdNKUUs7IeLUtqkJuKx8Na81dRQQSFXrMeHTUcdppoYvaXsBcti7v4NwBCTSWqAaudNXAb00J41vX203'

YOUR_DOMAIN = 'http://localhost:4242'

@require_POST
@csrf_exempt
def create_checkout_session(request):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': 'price_1OeDyRHcbPs5lobJBsK84xoq',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/return.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return HttpResponseBadRequest(str(e))

    return JsonResponse({'clientSecret': session.client_secret})

def session_status(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return HttpResponseBadRequest("Missing session_id parameter")

    try:
        session = stripe.checkout.Session.retrieve(session_id)
        status = session.status
        customer_email = session.customer_details.email
        return JsonResponse({'status': status, 'customer_email': customer_email})
    except stripe.error.InvalidRequestError as e:
        return HttpResponseBadRequest(str(e))
