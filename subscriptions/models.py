from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Subscription(models.Model):
    class SubscriptionTypes(models.TextChoices):
        BASIC = 'BA', _('Basic Subscription')
        PREMIUM = 'PR', _('Premium Subscription')
        ELITE = 'EL', _('Elite Subscription')

    # Define a class attribute for subscription prices
    SUBSCRIPTION_PRICES = {
        'BA': 14.99,
        'PR': 24.99,
        'EL': 34.99,
    }

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscription'
    )
    subscription_type = models.CharField(
        max_length=2,
        choices=SubscriptionTypes.choices,
        default=SubscriptionTypes.BASIC,
    )
    start_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s subscription"

    @property
    def price(self):
        """Return the price of the current subscription."""
        return self.SUBSCRIPTION_PRICES.get(self.subscription_type)
