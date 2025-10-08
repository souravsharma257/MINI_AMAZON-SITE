from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Wishlist, Order, OrderItem
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required


def product_list(request):
    category = request.GET.get('category', '')
    query = request.GET.get('q', '')  
    products = Product.objects.all()
    

    if category and category != 'All Categories':
        products = products.filter(category=category)  
    
    # Filter by search query
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    wishlist_products = []
    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user)
        wishlist_products = [item.product for item in wishlist_items]
    
    context = {
        "products": products,
        "wishlist_products": wishlist_products,
        "categories": ['Electronics', 'Fashion', 'Books', 'Home'],  # 4 options
        "query": query,  # Pass query to template for display
        "current_category": category,  # Optional: Highlight active category in template
    }
    return render(request, "shop/product_list.html", context)

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

@login_required
def checkout(request):
    cart_items = request.session.get("cart", [])
    if not cart_items:
        return redirect('cart')
    
    total_price = sum(item['price'] for item in cart_items)
    order = Order.objects.create(user=request.user, total_price=total_price)
    
    for item in cart_items:
        product = Product.objects.get(id=item['id'])
        OrderItem.objects.create(order=order, product=product, quantity=1)
    
    request.session['cart'] = []
    return render(request, "shop/checkout_success.html")

def search_results(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products, 'query': query})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('product_list')  
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
     auth_logout(request)
    return redirect('/product/')

@login_required
def add_to_wishlist(request, pk):
    product = get_object_or_404(Product, pk=pk)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product
    )
    if not created:
        wishlist_item.delete()  
    return redirect('product_list')

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    products = [item.product for item in wishlist_items]
    return render(request, 'shop/wishlist.html', {'wishlist_products': products})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/order_history.html', {'orders': orders})

def checkout_success(request):
    return render(request, "shop/checkout_success.html")