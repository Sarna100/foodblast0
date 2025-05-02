<<<<<<< HEAD

=======
>>>>>>> 409254e5e77b00e7a7443e9748ea2daa8f28491d
from django.db import models
from django.utils import timezone

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=15)

    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user_name} - {self.menu_item.name}"
<<<<<<< HEAD
=======


>>>>>>> 409254e5e77b00e7a7443e9748ea2daa8f28491d
