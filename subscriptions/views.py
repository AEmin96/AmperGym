from django.shortcuts import render
from . models import Subscriptions
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.

def subscriptions(request):
    return render(request, 'subscriptions/subscriptions.html')

@require_POST
@csrf_exempt 
def subscribe():
    subscription_name = request.POST.get('subscriptionName')
    subscription_price = request.POST.get('subscriptionPrice')
    
    
    
    return JsonResponse({"message": "Subscription successful!"})