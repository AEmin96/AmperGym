from django.contrib import admin
from .models import Subscription, UserSubscription

# Optional: Create a custom admin class to customize the admin interface
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription_type', 'start_date')
    search_fields = ('subscription_type',) 
    list_filter = ('subscription_type',)

class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date')
    search_fields = ('user',) 
    list_filter = ('user',)

# Register the Subscription model with the custom admin class
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(UserSubscription, UserSubscriptionAdmin)
