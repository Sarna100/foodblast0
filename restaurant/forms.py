from django import forms
from .models import MenuItem

from django import forms
from .models import MenuItem, Order

class MenuOrderForm(forms.ModelForm):
    menu_items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Items to Order"
    )
    user_name = forms.CharField(max_length=100, label="Your Name")
    user_email = forms.EmailField(label="Your Email")
    user_phone = forms.CharField(max_length=15, label="Phone Number")

    class Meta:
        model = Order
        fields = ['menu_items', 'user_name', 'user_email', 'user_phone']




from django import forms
from .models import Order, MenuItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu_items', 'quantity', 'user_name', 'user_email', 'user_phone']

