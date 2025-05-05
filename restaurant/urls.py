# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('order/<int:item_id>/', views.order_item, name='order_item'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),

    path('menu/', views.menu_view, name='menu'),
    path('menu/order/<int:item_id>/', views.order_item, name='order_item'),
]


