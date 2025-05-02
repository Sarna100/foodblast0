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
    path('order_success/', views.order_success, name='order_success'),



]
