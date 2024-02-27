from django.contrib import sitemaps
from .models import Checkout

class CheckoutSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Subscription.objects.all()

    def lastmod(self, obj):
        return obj.last_modified_date
