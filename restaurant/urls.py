# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('order/<int:item_id>/', views.order_item, name='order_item'),
    path('place_order/', views.place_order, name='place_order'),
<<<<<<< HEAD
    path('order_success/', views.order_success, name='order_success'),  # Add this line
    path('my_orders/', views.my_orders, name='my_orders'),
    # Add other URLs here...
=======
    path('order_success/', views.order_success, name='order_success'),
>>>>>>> 409254e5e77b00e7a7443e9748ea2daa8f28491d
]
