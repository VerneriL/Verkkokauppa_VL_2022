from django.shortcuts import render, get_object_or_404

from .models import Categories, Product
from cart.models import ShoppingCartOrder
from users.models import Profile


# Home page for the store
def home(request):
    context = {
        'title': '',      
    }
    return render(request, 'base/home.html', context)

# Store page
def store(request):
    # Store items from database (maybe categories?)
    categories = Categories.objects.all()
    # Shows categories (Need product page)
    context = {
        'title': 'Store',
        'categories': categories,
    }
    return render(request, 'base/store.html', context)

# About page
def about(request):
    context = {
        'title': 'About',
    }    
    return render(request, 'base/about.html', context)

# Profile page
def account(request):
    context = {
        'title': 'Account',
    }    
    return render(request, 'base/account.html', context)


def products(request, category_id):
    in_cart_list=[]
    # Get category id from database based on given parameter
    products_id = Product.objects.filter(product_category=category_id)
    # Get all products of the same category
    profile = get_object_or_404(Profile, user=request.user)
    order = ShoppingCartOrder.objects.filter(owner=profile, ordered=False).first()
    # Create cart_item_id list to check if product is already in cart
    # If already in cart, add_to_cart button won't be shown
    if order:
        order_cart_items = order.cart_items.all()
        in_cart = order_cart_items.filter()
        in_cart_list = [item.cart_item_id for item in in_cart]
    products = products_id.all()

    context = {
        'title': 'Store/Cats',
        'products': products,
        'in_cart': in_cart_list
    }
    return render(request, 'base/product.html', context)
