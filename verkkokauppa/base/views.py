from django.shortcuts import render

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

# Profile page (eventually)
def account(request):
    context = {
        'title': 'Account',
    }    
    return render(request, 'base/account.html', context)


#TODO Make a page for products (accessible from store page through categories)
def products(request, category_id):
    products_id = Product.objects.filter(product_category=category_id)
    products = products_id.all()
    context = {
        'products': products
    }
    return render(request, 'base/product.html', context)