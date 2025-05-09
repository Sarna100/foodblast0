from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order
from .forms import MenuOrderForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')


def order_item(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)

    if request.method == 'POST':
        form = MenuOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.menu_item = item
            order.save()
            return redirect('order_success')

    else:
        form = MenuOrderForm()

    return render(request, 'order.html', {'item': item, 'form': form})


def menu_view(request, popular_items=None):
    starters_items = MenuItem.objects.filter(category='🥗 Starters')
    main_course_items = MenuItem.objects.filter(category='🍛 Main Course')
    noodles_pasta_items = MenuItem.objects.filter(category='🍝 Noodles & Pasta')
    sides_items = MenuItem.objects.filter(category='🍟 Sides')
    drinks_items = MenuItem.objects.filter(category='🍹 Drinks')
    desserts_items = MenuItem.objects.filter(category='🍨 Desserts')
    healthy_foods_items = MenuItem.objects.filter(category='Healthy Foods')
    popular_items = MenuItem.objects.filter(category='Our Popular Dishes')

    return render(request, 'menu.html', {
        'starters_items': starters_items,
        'main_course_items': main_course_items,
        'noodles_pasta_items': noodles_pasta_items,
        'sides_items': sides_items,
        'drinks_items': drinks_items,
        'desserts_items': desserts_items,
        'healthy_foods_items': healthy_foods_items,
        'popular_items': popular_items,
    })



from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order
from .forms import MenuOrderForm

def place_order(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_phone = request.POST['user_phone']

        # Step 1: Create the order without total_price
        order = Order.objects.create(
            user_name=user_name,
            user_email=user_email,
            user_phone=user_phone,
            quantity=quantity,
            total_price=0  # Temporary value
        )

        order.menu_items.add(item)


        total = sum(menu_item.price for menu_item in order.menu_items.all()) * quantity


        order.total_price = total
        order.save()

        return redirect('order_success')

    return render(request, 'order.html', {'item': item})

# Order Success Page
def order_success(request):
    return render(request, 'order_success.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def order_page(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')

        # Normally, save data to the database here
        Order.objects.create(
            menu_item_name=item_name,
            quantity=quantity,
            user_name=user_name,
            user_email=user_email,
            user_phone=user_phone
        )

        messages.success(request, 'Your order has been placed successfully!')
        return redirect('order_page')

    return render(request, 'order.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import MenuOrderForm

# View to update an order
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = MenuOrderForm(request.POST, instance=order)
        if form.is_valid():
            updated_order = form.save(commit=False)
            updated_order.save()
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = MenuOrderForm(instance=order)

    return render(request, 'update_order.html', {'form': form})


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    return render(request, 'delete_order.html', {'order': order})

# Optional: View to list all orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


from django.shortcuts import render, get_object_or_404
from .models import Order

from django.shortcuts import render, get_object_or_404
from .models import Order

def order_confirmation(request, order_id):

    order = get_object_or_404(Order, id=order_id)


    item_names = [item.name for item in order.menu_items.all()]


    return render(request, 'order_confirmation.html', {'order': order, 'item_names': item_names})


