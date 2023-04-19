from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

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
    user = get_object_or_404(Profile, user=request.user)
    cart_orders = ShoppingCartOrder.objects.filter(owner=user, ordered=False)
    if cart_orders.exists():
        return cart_orders[0]
    return 0

@login_required
def order_details(request, **kwargs):
    existing_order = shopping_cart(request)
    context = {
        'title': 'shopping-cart',
        'order': existing_order
    }
    return render(request, "cart/shopping_cart.html", context)


@login_required
def add_to_cart(request, **kwargs):
    profile = get_object_or_404(Profile, user=request.user)
    
    product = Product.objects.filter(id=kwargs.get('id', "")).first()
    order_item, status = ShoppingCartItem.objects.get_or_create(cart_item=product)
    user_order, status = ShoppingCartOrder.objects.get_or_create(owner=profile, ordered=False)
    user_order.cart_items.add(order_item)
    if status:
        user_order.order_code = generate_order_id()
        user_order.save()
    messages.success(request, "Added to cart")
    return redirect(reverse('store-page'))

@login_required
def remove_from_cart(request, id):
    remove_item = ShoppingCartItem.objects.filter(id=id)
    if remove_item.exists():
        remove_item[0].delete()
        messages.success(request, "Removed from cart")
    else:
        messages.warning(request, 'Removal failed')
    return redirect(reverse('shopping-cart-page'))

@login_required
def process_payment(request, order_id):
    return redirect(reverse('update-transaction-records', kwargs={
        'order_id': order_id,
    }))

@login_required
def checkout(request):
    existing_order = shopping_cart(request)
    context = {
        'title': 'checkout',
        'order': existing_order
    }
    return render(request, "cart/checkout.html", context)

# This could be included in other views instead of being separate
@login_required
def payment_processed(request):
    return render(request, "cart/payment_processed.html")

@login_required
def update_transaction_records(request, order_id):
    order_to_purchase = ShoppingCartOrder.objects.filter(pk=order_id).first()

    order_to_purchase.ordered = True
    order_to_purchase.date_ordered = datetime.datetime.now()
    order_to_purchase.save()

    order_items = order_to_purchase.cart_items.all()

    order_items.update(ordered=True)

    messages.info(request, 'Thank you for your purchase!')
    return redirect(reverse('payment-processed'))
