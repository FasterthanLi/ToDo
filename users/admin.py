from django.contrib import admin
from django.contrib.auth import get_user_model

class UserAdmin(admin.ModelAdmin):
    fields = ('email', 'phone_number', 'is_active', 'is_admin', 'is_staff', 'is_superuser')
    list_display = ('email', 'phone_number', 'is_active', 'is_admin', 'is_staff', 'is_superuser')

admin.site.register(get_user_model(), UserAdmin)
