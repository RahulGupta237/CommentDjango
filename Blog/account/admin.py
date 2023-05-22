from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'mobile_number','profile_photo')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'mobile_number','profile_photo', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'mobile_number','profile_photo', 'is_staff')
    search_fields = ('email', 'name', 'mobile_number')
    ordering = ('email',)




# Now register the new UserModelAdmin...
admin.site.register(CustomUser, CustomUserAdmin)
#
