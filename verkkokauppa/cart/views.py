from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#TODO: Create add to cart functionality
@login_required
def add_to_cart(request):
    messages.success(request, "Added to cart")

#TODO: Create remove from cart functionality
@login_required
def remove_from_cart(request):
    messages.success(request, "Removed from cart")
