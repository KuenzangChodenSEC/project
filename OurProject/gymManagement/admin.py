from django.contrib import admin
from .models import Event, Plan, UserPayment, Equipment, Member

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

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'validity_months', 'amount', 'created_at')
    list_filter = ('plan_name', 'validity_months')
    search_fields = ('plan_name', 'amount')
    ordering = ('validity_months',)


@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'plan', 
        'price', 
        'payment_status', 
        'payment_date'
    )
    list_filter = ('plan', 'payment_status')
    search_fields = ('user_name', 'member_id')
    ordering = ('-payment_date',)
    actions = ['mark_as_paid', 'mark_as_pending']

    # Custom Admin Actions
    def mark_as_paid(self, request, queryset):
        queryset.update(payment_status='paid')
        self.message_user(request, "Selected payments were successfully marked as Paid.")
    mark_as_paid.short_description = "Mark selected payments as Paid"

    def mark_as_pending(self, request, queryset):
        queryset.update(payment_status='pending')
        self.message_user(request, "Selected payments were successfully marked as Pending.")
    mark_as_pending.short_description = "Mark selected payments as Pending"

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_no', 'status')  # Show these fields in the list view
    search_fields = ('name',)  # Allow searching by name
    list_filter = ('status',)  # Filter by status (Active/Inactive)
    
admin.site.register(Equipment, EquipmentAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_id', 'date_join', 'plan')
    search_fields = ('name', 'member_id')
    list_filter = ('plan',)

admin.site.register(Member, MemberAdmin)