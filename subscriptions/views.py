from django.shortcuts import render
from .models import UserSubscription,Subscription
from django.contrib.auth.decorators import login_required

@login_required
def subscriptions(request):
    subscriptions = Subscription.objects.all()
    current_subscription = None
    if UserSubscription.objects.filter(user=request.user).exists():
        user_subscription = UserSubscription.objects.get(user=request.user)
        current_subscription = user_subscription.subscription.subscription_type
    
    return render(request, 'subscriptions/subscriptions.html', {'current_subscription': current_subscription,'subscriptions':subscriptions})
