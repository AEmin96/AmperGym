from django.contrib import sitemaps
from .models import Subscription

class SubscriptionSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Subscription.objects.all()

    def lastmod(self, obj):
        return obj.last_modified_date

    def location(self, obj):
        return reverse('subscriptions:subscriptions_view')