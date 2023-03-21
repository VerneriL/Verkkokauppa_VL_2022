from django.contrib import admin
from .models import ShoppingCartOrder

# Register your models here.
@admin.register(ShoppingCartOrder)
class CartAdmin(admin.ModelAdmin):
    fields = ['owner', 'cart_items']