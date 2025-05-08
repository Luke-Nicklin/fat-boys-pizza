from django.contrib import admin
from .models import Table, Booking

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_booked')
    search_fields = ('table_number',)
    list_filter = ('is_booked',)
    ordering = ('table_number',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'phone_number', 'table', 'booking_time', 'date', 'guests')
    search_fields = ('name', 'phone_number')
    list_filter = ('date', 'booking_time')
    ordering = ('date', 'booking_time')
