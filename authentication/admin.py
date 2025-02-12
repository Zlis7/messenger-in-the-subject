from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MinUser

class CustomUserAdmin(UserAdmin):
    model = MinUser
    list_display = ['email', 'username', 'is_active', 'is_staff', 'is_superuser', 'is_blocked']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'is_blocked']
    search_fields = ['email', 'username']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_blocked', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )

admin.site.register(MinUser, CustomUserAdmin)