from django.shortcuts import render
from .models import UserSubscription, Subscription
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


@login_required
def subscriptions_view(request):
    # Define custom ordering for subscriptions
    custom_ordering = Case(
        When(subscription_type='BA', then=1),
        When(subscription_type='PR', then=2),
        When(subscription_type='EL', then=3),
    )
    
    subscription_list = Subscription.objects.all().annotate(
        custom_order=custom_ordering
    ).order_by('custom_order')
    
    current_subscription = None
    user_subscription = UserSubscription.objects.filter(user=request.user).first()
    if user_subscription:
        current_subscription = user_subscription.subscription.subscription_type

    return render(request, 'subscriptions/subscriptions.html', {
        'current_subscription': current_subscription,
        'subscriptions': subscription_list
    })

@login_required
def cancel_subscription(request):
    user_subscription = UserSubscription.objects.filter(user=request.user).first()
    if user_subscription:
        user_subscription.delete()
        messages.success(request, 'Your subscription has been successfully canceled.')
    else:
        messages.error(request, 'You do not have an active subscription to cancel.')
    
    return HttpResponseRedirect(reverse('subscriptions:subscriptions_view'))
