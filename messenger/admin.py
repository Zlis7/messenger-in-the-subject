from django.contrib import admin
from .models import Message

@admin.register(Message)
class CustomMessageAdmin(admin.ModelAdmin):
    list_display = ['id_chat', 'uid', 'content_message', 'date']
    search_fields = ['id_chat', 'uid']
    list_filter = ['date']
    ordering = ['id_chat', 'date']

    readonly_fields = ['id_chat', 'uid', 'date', 'name_chat', 'content_message']

    fieldsets = (
        ('User', {'fields': ('uid',)}),
        ('Chat', {'fields': ('id_chat','name_chat')}),
        ('Content', {'fields': ('content_message', )}),
        ('Date', {'fields': ('date',)})
    )

    add_fieldsets = (
        ('It has recently been forbidden to add messages manually', {'fields': ()}),
    )

    def get_fieldsets(self, request, obj=None):
        if obj:
            return super().get_fieldsets(request, obj)
        else:
            return self.add_fieldsets

    def save_model(self, request, obj, form, change):
        pass