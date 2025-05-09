from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        ordered_items = obj.menu_items.all()
        item_list = ", ".join([f"{item.name} (Qty: {item.quantity})" for item in ordered_items])
        total_price = sum([item.price * item.quantity for item in ordered_items])

        self.message_user(
            request,
            f"Order placed by {obj.user_name} → {item_list} | Total: {total_price}৳",
        )
