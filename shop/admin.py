from django.contrib import admin
from .models import Product, Wishlist, Order, OrderItem

admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
