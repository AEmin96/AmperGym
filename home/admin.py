from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile

User = get_user_model()

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]

    def newsletter_subscription(self, instance):

        return instance.userprofile.newsletter
    newsletter_subscription.short_description = 'Newsletter Subscription'  # Column name

    list_display = ('id', 'username', 'last_login', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'newsletter_subscription')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
