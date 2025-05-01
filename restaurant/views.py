from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order
from .form import MenuOrderForm


# Function for showing menu items
def menu(request):
    rice_items = MenuItem.objects.filter(category='rice')
    fastfood_items = MenuItem.objects.filter(category='fastfood')
    drinks_items = MenuItem.objects.filter(category='drinks')

    context = {
        'rice_items': rice_items,
        'fastfood_items': fastfood_items,
        'drinks_items': drinks_items
    }
    return render(request, 'menu.html', context)
# views.py
from django.shortcuts import render

# Home page view function
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def add_to_cart(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    else:
        cart[str(item_id)] = {
            'name': item.name,
            'price': float(item.price),
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect('menu')

def view_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'view_item.html', {'item': item})

# Function for displaying the order page
def order_item(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)

    if request.method == 'POST':
        # Create the order
        order = Order(
            menu_item=item,
            quantity=request.POST.get('quantity'),
            user_name=request.POST.get('user_name'),
            user_email=request.POST.get('user_email'),
            user_phone=request.POST.get('user_phone')
        )
        order.save()
        return redirect('order_success')  # Redirect to order success page

    return render(request, 'order.html', {'item': item})


# Success page after order is placed
def order_success(request):
    return render(request, 'order_success.html')
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


