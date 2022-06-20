from django.shortcuts import render

from .models import Categories, Product

# Test data (ignore for now)
posts = [
    {
        'author': 'Me',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }    
]
# Home page for the store
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

# Store page
def store(request):
    # Store items from database (maybe categories?)
    categories = Categories.objects.all()
    # Shows categories (Need product page)
    context = {
        'title': 'Store',
        'categories': categories
    }
    return render(request, 'store.html', context)

# About page
def about(request):
    context = {
        'title': 'About',
    }    
    return render(request, 'about.html', context)

# Profile page (eventually)
def account(request):
    context = {
        'title': 'Account',
    }    
    return render(request, 'account.html', context)

# Contact us page (in a way connected to account)
def contact(request):
    context = {
        'title': 'Contact us',
    }        
    return render(request, 'contact.html', context)

#TODO Make a page for products (accessible from store page through categories)
def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product.html', context)