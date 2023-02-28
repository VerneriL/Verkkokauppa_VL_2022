from django.db import models
from django.contrib.auth.models import User

from base.models import Product


class ShoppingCart(models.Model):
    pass


class ShoppingCartItem(models.Model):
    pass


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
    payment_date = models.DateTimeField(editable=False)
    payment_number = models.IntegerField(editable=False)