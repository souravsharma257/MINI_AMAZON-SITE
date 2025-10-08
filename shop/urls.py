from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("add_to_cart/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("checkout_success/", views.checkout_success, name="checkout_success"),
    path('search/', views.search_results, name='search'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('wishlist/add/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),path("checkout/", views.checkout, name="checkout"),
    path("checkout-success/", views.checkout_success, name="checkout_success"),
    path('orders/', views.order_history, name='order_history'), 

    
]
