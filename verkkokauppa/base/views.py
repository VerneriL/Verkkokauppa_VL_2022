from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Categories, Product


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
    # Get category id from database based on given parameter
    products_id = Product.objects.filter(product_category=category_id)
    # Get all products of the same category
    products = products_id.all()
    context = {
        'title': 'Store/Cats',
        'products': products,
    }
    return render(request, 'base/product.html', context)

#TODO: Create add to cart functionality
@login_required
def add_to_cart(request):
    messages.success(request, "Added to cart")

#TODO: Create remove from cart functionality
@login_required
def remove_from_cart(request):
    messages.success(request, "Removed from cart")
