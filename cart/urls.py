from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('add-to-cart/', views.add_to_cart, name="add-to-cart"),
    path('remove-from-cart/', views.remove_from_cart, name="remove-from-cart"),
    path('delete-cart-item/', views.delete_cart_item, name="delete-cart-item"),

    path('cart/', views.cartPage, name="cart"),
    path('checkout/', views.checkoutPage, name="checkout"),
    path('result/', views.resultPage, name="result"),
    path('past-orders/', views.pastOrders, name="past-orders"),

    path('apply-coupon/', views.apply_coupon, name="apply-coupon"),
    path('buy-now/', views.buy_now, name="apply-coupon"),
]