from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('🥗 Starters', '🥗 Starters'),
        ('🍛 Main Course', '🍛 Main Course'),
        ('🍝 Noodles & Pasta', '🍝 Noodles & Pasta'),
        ('🍟 Sides', '🍟 Sides'),
        ('🍹 Drinks', '🍹 Drinks'),
        ('🍨 Desserts', '🍨 Desserts'),
        ('Healthy Foods', 'Healthy Foods'),
        ('Our Popular Dishes','Our Popular Dishes')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='🍹 Drinks')

    def __str__(self):
        return self.name
from django.db import models

class Order(models.Model):
    menu_items = models.ManyToManyField(MenuItem)
    quantity = models.PositiveIntegerField(default=1)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order by {self.user_name} ({self.id})"

    def calculate_total(self):
        self.total_price = self.menu_item.price * self.quantity
        self.save()




