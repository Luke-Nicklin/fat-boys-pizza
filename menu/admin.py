from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Class to display menu items
    """
    list_display = ('name', 'description', 'price', 'is_available')
    list_filter = ('is_available',)