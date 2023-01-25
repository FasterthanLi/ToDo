from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fields = ('email', 'phone_number', 'is_active', 'is_admin', 'is_staff', 'is_superuser')
    list_display = ('email', 'phone_number', 'is_active', 'is_admin', 'is_staff', 'is_superuser')
    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
