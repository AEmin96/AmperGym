from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import UserProfile

@receiver(user_signed_up)
def user_signed_up_request(sender, request, user, **kwargs):
    newsletter_subscription = request.POST.get('newsletter_subscription', False) == 'on'
    UserProfile.objects.create(user=user, newsletter=newsletter_subscription)