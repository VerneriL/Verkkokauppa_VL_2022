from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm


def shopping_cart(request):
    title = "shopping-cart"
    context = {
        'title': title
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
def add_to_cart(request):
    messages.success(request, "Added to cart")

#TODO: Create remove from cart functionality
@login_required
def remove_from_cart(request):
    messages.success(request, "Removed from cart")
