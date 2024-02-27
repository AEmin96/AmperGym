from django.contrib import sitemaps
from .models import Subscription, UserSubscription

class SubscriptionSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Subscription.objects.all()

    def lastmod(self, obj):
        return obj.last_modified_date

class UserSubscriptionSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return UserSubscription.objects.all()

    def lastmod(self, obj):
        return obj.last_modified_date
