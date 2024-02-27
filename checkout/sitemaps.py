from django.urls import reverse
from django.contrib import sitemaps
from .models import Checkout

class CheckoutSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Checkout.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('create-checkout-session')
