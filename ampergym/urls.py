"""ampergym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404
from django.contrib.sitemaps.views import sitemap
from testimonials.sitemaps import TestimonialSitemap
from subscriptions.sitemaps import SubscriptionSitemap
from checkout.sitemaps import CheckoutSitemap


sitemaps = {
    'testimonials': TestimonialSitemap,
    'subscription': SubscriptionSitemap,
    'checkout' : CheckoutSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('subscriptions/', include('subscriptions.urls')),
    path('checkout/', include('checkout.urls')),
    path('robots.txt/', include('robots.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'ampergym.views.handler404'
