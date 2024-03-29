from django.urls import reverse
from django.contrib import sitemaps
from .models import Subscription

class SubscriptionSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Subscription.objects.all()

    def lastmod(self, obj):
        return obj.start_date

    def location(self, obj):
        return reverse('subscriptions:subscriptions_view')