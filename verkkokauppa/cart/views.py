from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm


def generate_order_id():
    date_string = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    random_string = "".join([random.choice(string.digits) for _ in range(1,5)])
    return date_string + random_string

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
def remove_from_cart(request):
    messages.success(request, "Removed from cart")
