from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MinUser

@admin.register(MinUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['uid', 'username', 'is_active', 'is_blocked']
    list_filter = ['is_active', 'is_blocked', 'last_login']
    search_fields = ['uid', 'username']
    ordering = ['uid']

    readonly_fields = ['uid', 'username', 'groups', 'user_permissions', 'last_login']

    fieldsets = (
        (None, {'fields': ('uid', 'username')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_blocked', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        ('It has recently been forbidden to add users manually', {'fields':()}),
    )