from django import forms
from .models import MenuItem

class MenuOrderForm(forms.Form):
    menu_items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Items to Order"
    )
    user_name = forms.CharField(max_length=100, label="Your Name")
    user_email = forms.EmailField(label="Your Email")
    user_phone = forms.CharField(max_length=15, label="Phone Number")