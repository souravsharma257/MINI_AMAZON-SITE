from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})

def cart(request):
    cart_items = request.session.get("cart", [])
    return render(request, "shop/cart.html", {"cart": cart_items})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get("cart", [])
    cart.append({"id": product.id, "name": product.name, "price": float(product.price)})
    request.session["cart"] = cart
    return redirect("cart")

def checkout_success(request):
    request.session["cart"] = []
    return render(request, "shop/checkout_success.html")
