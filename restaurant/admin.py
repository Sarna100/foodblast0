# Register your models here.
from django.contrib import admin
from .models import MenuItem, Order


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order)
