from django.contrib import admin
from .models import CalendarEvent, Plan, Member, Equipment, GymMember

@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'created_at')
    search_fields = ('title',)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'get_validity_display', 'amount', 'created_at')
    ordering = ('validity',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_id', 'plan', 'price', 'payment_status')
    list_filter = ('plan', 'payment_status')
    search_fields = ('name', 'member_id')
    ordering = ('name',)
    list_editable = ('payment_status',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_no', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('name',)


@admin.register(GymMember)
class GymMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_id', 'date_join', 'plan')
    search_fields = ('name', 'member_id')
    list_filter = ('plan',)