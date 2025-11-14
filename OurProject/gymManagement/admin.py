from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'description_short')
    list_filter = ('start_date',)
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'

    def description_short(self, obj):
        # Display the first 50 characters of the description
        return obj.description[:50] + '...' if obj.description and len(obj.description) > 50 else obj.description
    description_short.short_description = 'Description'

