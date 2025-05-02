from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order
from .form import MenuOrderForm


# Function for showing menu items
def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})
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

# In your views.py
from django.shortcuts import render, redirect
from .models import MenuItem, Order
from django.contrib.auth.decorators import login_required

# views.py
from django.shortcuts import render, redirect
from .models import Order


def place_order(request):
    order = request.session.get('pending_order')
    if not order:
        return redirect('menu')

    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        phone = request.POST.get('user_phone')

        # Save the order in the database
        for item in order['items']:
            menu_item = item['menu_item']
            quantity = item['quantity']
            Order.objects.create(
                menu_item=menu_item,
                quantity=quantity,
                user_name=name,
                user_email=email,
                user_phone=phone
            )

        # Clear the session
        del request.session['pending_order']

        # Redirect to the order success page
        return redirect('order_success')  # Ensure this name matches the URL pattern name

    return render(request, 'place_order.html', {'order': order})


def order_success(request):
    return render(request, 'order_success.html', {'message': 'Your order has been successfully placed!'})


# Add this view to show the user's orders


def my_orders(request):
    user_email = request.session.get('user_email')

    orders = []
    if user_email:
        orders_queryset = Order.objects.filter(user_email=user_email).order_by('-order_date')
        for order in orders_queryset:
            total = order.quantity * order.menu_item.price
            orders.append({
                'item_name': order.menu_item.name,
                'price': order.menu_item.price,
                'quantity': order.quantity,
                'total': total
            })

    return render(request, 'my_orders.html', {'orders': orders})



