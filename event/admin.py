

from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'organizer', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
