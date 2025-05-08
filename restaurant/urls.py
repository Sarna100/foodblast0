# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),

    path('order/success/', views.order_success, name='order_success'),
    path('place_order/<int:item_id>/', views.place_order, name='place_order'),
    path('menu/', views.menu_view, name='menu'),
    path('menu/order/<int:item_id>/', views.order_item, name='order_item'),
    path('register/', views.register_view, name='register'),
path('order/<int:item_id>/', views.order_item, name='order'),  # name="order" must be there


]
