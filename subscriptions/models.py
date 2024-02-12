from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Subscription(models.Model):
    subscription_type = models.CharField(max_length=10, default='BA',blank= True)
    subscription_title = models.CharField(max_length=100, default='Basic Subscription',blank= True)
    subscription_desc = models.CharField(max_length=300 ,default='Access to basic gym facilities Personalized workout plans £14.99/month',blank= True)
    subscription_price = models.FloatField(default=14.99)
    start_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.subscription_type}"


class UserSubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) 

    def __str__(self):
        return f"{self.user.username} - {self.subscription.subscription_title}"
