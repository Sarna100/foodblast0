from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order


from .forms import MenuOrderForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages




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





from .models import MenuItem

def menu_view(request):
    starters_items = MenuItem.objects.filter(category='🥗 Starters')
    main_course_items = MenuItem.objects.filter(category='🍛 Main Course')
    noodles_pasta_items = MenuItem.objects.filter(category='🍝 Noodles & Pasta')
    sides_items = MenuItem.objects.filter(category='🍟 Sides')
    drinks_items = MenuItem.objects.filter(category='🍹 Drinks')
    desserts_items = MenuItem.objects.filter(category='🍨 Desserts')

    return render(request, 'menu.html', {
        'starters_items': starters_items,
        'main_course_items': main_course_items,
        'noodles_pasta_items': noodles_pasta_items,
        'sides_items': sides_items,
        'drinks_items': drinks_items,
        'desserts_items': desserts_items
    })





from django.contrib import messages
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import MenuItem, Order
from django.contrib import messages


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MenuItem  # বা যেটা তোমার মডেল
from .models import Order  # যদি অর্ডার সংরক্ষণ করো

def place_order(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)

    if request.method == 'POST':
        quantity = request.POST['quantity']
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_phone = request.POST['user_phone']

        Order.objects.create(
            menu_item=item,
            quantity=quantity,
            user_name=user_name,
            user_email=user_email,
            user_phone=user_phone
        )

        # Redirect to order_success page without showing any messages
        return redirect('order_success')  # Ensure it redirects to order_success page

    return render(request, 'order.html', {'item': item})




def order_success(request):
    return render(request, 'order_success.html')



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

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def order_page(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')

        # Normally database save korben ekhane (jodi model thake)

        messages.success(request, 'Your order has been placed successfully!')
        return redirect('order_page')

    return render(request, 'order.html')

