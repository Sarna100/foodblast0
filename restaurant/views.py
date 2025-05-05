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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # login successful → go to home page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


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



def order_success(request):
    return render(request, 'order_success.html')

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


from django.contrib import messages
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import MenuItem, Order
from django.contrib import messages


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

        return redirect('order_success')

    return redirect('menu')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
