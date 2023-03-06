from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .forms import PaymentForm
from users.models import Profile
from base.models import Product
from .models import ShoppingCartItem, ShoppingCartOrder

import random
import string
from datetime import date
import datetime

def generate_order_id():
    date_string = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    random_string = "".join([random.choice(string.digits) for _ in range(1,5)])
    return date_string + random_string

@login_required
def shopping_cart(request):
    # This can probably be done much cleaner
    title = "shopping-cart"
    user = get_object_or_404(Profile, user=request.user)
    # Queryset of cart_items
    cart_orders = ShoppingCartOrder.objects.filter(owner=user).first()
    cart = []
    # Loop through items in queryset
    for queryset in cart_orders.get_cart_items():
        # Create a list of items in cart
        cart.append(queryset.cart_item.name)
    context = {
        'title': title,
        'items_in_cart': cart,
    }
    return render(request, "cart/shopping_cart.html", context)

@login_required
def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment successful')
            return redirect('home-page')
    else:
        form = PaymentForm()
    title = "payment"
    context = {
        'form': form,
        'title': title
    }
    return render(request, "cart/payment.html", context)


#TODO: Create add to cart functionality
@login_required
def add_to_cart(request, **kwargs):
    profile = get_object_or_404(Profile, user=request.user)
    
    product = Product.objects.filter(id=kwargs.get('id', "")).first()
    order_item, status = ShoppingCartItem.objects.get_or_create(cart_item=product)

    user_order, status = ShoppingCartOrder.objects.get_or_create(owner=profile, ordered=True)
    user_order.cart_items.add(order_item)
    # Make an order code generator
    if status:
        user_order.order_code = generate_order_id()
        user_order.save()
    messages.success(request, "Added to cart")
    # Create urls
    return redirect(reverse('store-page'))

#TODO: Create remove from cart functionality
@login_required
def remove_from_cart(request, id):
    remove_item = ShoppingCartItem.objects.filter(id=id)
    if remove_item.exists():
        remove_item[0].delete()
        messages.success(request, "Removed from cart")
    return redirect(reverse('shopping-cart'))
