from django.contrib import admin
from .models import User,UserProfile
# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]
    resource_class = User
    list_display = ('id', 'username', 'last_login','email', 'first_name', 'last_name', 'is_active', 'is_staff','is_superuser')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)