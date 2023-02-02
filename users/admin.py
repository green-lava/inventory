from django.contrib import admin

from .models import User, Profile, Bus_profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_superuser','is_garage', 'is_vendor']


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Bus_profile)
