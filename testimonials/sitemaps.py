from django.contrib import sitemaps
from .models import Testimonial

class TestimonialSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Testimonial.objects.all()

    def lastmod(self, obj):
        return obj.last_modified_date