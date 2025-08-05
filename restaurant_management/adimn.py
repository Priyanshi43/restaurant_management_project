from django.contrib import admin
from .models imort Menu, Order

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','price')

@admin.register(order)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu_item', 'quantity', 'order_date')    