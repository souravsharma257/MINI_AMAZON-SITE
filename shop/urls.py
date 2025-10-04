from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("add_to_cart/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("checkout_success/", views.checkout_success, name="checkout_success"),
]
