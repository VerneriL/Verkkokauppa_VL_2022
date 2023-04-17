from django.db import models

from base.models import Product
from users.models import Profile


class ShoppingCartItem(models.Model):
    cart_item = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.cart_item.name}, {self.cart_item.price}'

class ShoppingCartOrder(models.Model):
    order_code = models.CharField(max_length=20)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)
    cart_items = models.ManyToManyField(ShoppingCartItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.cart_items.all()
        
    def cart_sum(self):
        return sum([item.cart_item.price for item in self.cart_items.all()])

    def __str__(self):
        return f"{self.owner}"


class Payment(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    post_code = models.CharField(max_length=10)
    post_address = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    card_number = models.CharField(max_length=12)
    card_exp_month = models.CharField(max_length=2)
    card_exp_year = models.CharField(max_length=2)
    card_ccs = models.CharField(max_length=3)
    payment_date = models.DateTimeField(auto_now=True)