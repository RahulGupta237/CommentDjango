from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser,TodoList,Item


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'mobile_number')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'mobile_number', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'mobile_number', 'is_staff')
    search_fields = ('email', 'name', 'mobile_number')
    ordering = ('email',)


class TodoListAdmin(admin.ModelAdmin):
    list_display =  ('title', 'description', 'start_date', 'end_date', 'status', 'is_active')


class ItemsListListAdmin(admin.ModelAdmin):
    list_display = ('item_title', 'todo', 'description', 'added_date')



# Now register the new UserModelAdmin...
admin.site.register(CustomUser, CustomUserAdmin)
#
admin.site.register(TodoList,TodoListAdmin)
admin.site.register(Item,ItemsListListAdmin)