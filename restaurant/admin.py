# Register your models here.
from django.contrib import admin
from .models import MenuItem, Order

# Customizing the admin for MenuItem
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')

# Registering the MenuItem model with the customized admin (Remove the previous registration)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order)
