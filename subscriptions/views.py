from django.shortcuts import render
from .models import UserSubscription, Subscription
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When

@login_required
def subscriptions(request):
    # Define custom ordering for subscriptions
    custom_ordering = Case(
        When(subscription_type='BA', then=1),
        When(subscription_type='PR', then=2),
        When(subscription_type='EL', then=3),
    )
    
    subscriptions = Subscription.objects.all().annotate(
        custom_order=custom_ordering
    ).order_by('custom_order')
    
    current_subscription = None
    if UserSubscription.objects.filter(user=request.user).exists():
        user_subscription = UserSubscription.objects.get(user=request.user)
        current_subscription = user_subscription.subscription.subscription_type

    return render(request, 'subscriptions/subscriptions.html', {'current_subscription': current_subscription, 'subscriptions': subscriptions})
