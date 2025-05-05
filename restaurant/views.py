from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order
 # form.py নামের ফাইল থেকে ফর্মটি ইম্পোর্ট করা

from .forms import MenuOrderForm  # If you decide to use a form

# Home page view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

# Function for displaying the order page
 # ফর্মটি ইম্পোর্ট করো

# Function for displaying the order page
def order_item(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)

    if request.method == 'POST':
        form = MenuOrderForm(request.POST)
        if form.is_valid():
            # অর্ডারটি সেভ করা
            order = form.save(commit=False)
            order.menu_item = item  # সঠিক মেনু আইটেম সেট করা
            order.save()
            return redirect('order_success')  # অর্ডার সাকসেস পেজে রিডিরেক্ট করা

    else:
        form = MenuOrderForm()

    return render(request, 'order.html', {'item': item, 'form': form})


# Success page after order is placed
def order_success(request):
    return render(request, 'order_success.html')

# Function for displaying menu items based on category
def menu_view(request):
    rice_items = MenuItem.objects.filter(category='rice')
    chicken_items = MenuItem.objects.filter(category='chicken')
    beef_items = MenuItem.objects.filter(category='beef')
    mutton_items = MenuItem.objects.filter(category='mutton')
    fastfood_items = MenuItem.objects.filter(category='fastfood')
    drinks_items = MenuItem.objects.filter(category='drinks')

    return render(request, 'menu.html', {
        'rice_items': rice_items,
        'chicken_items': chicken_items,
        'beef_items': beef_items,
        'mutton_items': mutton_items,
        'fastfood_items': fastfood_items,
        'drinks_items': drinks_items
    })

# Place order functionality (can be merged with order_item function)
def place_order(request):
    if request.method == 'POST':
        menu_item_id = request.POST.get('menu_item_id')
        menu_item = MenuItem.objects.get(id=menu_item_id)

        order = Order(
            menu_item=menu_item,
            quantity=request.POST['quantity'],
            user_name=request.POST['user_name'],
            user_email=request.POST['user_email'],
            user_phone=request.POST['user_phone']
        )
        order.save()

        return redirect('order_success')  # Redirect to order confirmation page after placing order

    return redirect('menu')  # If GET request, redirect to menu

