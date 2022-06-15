from django.contrib import admin

from .models import Categories, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "price", "product_category"]

admin.site.register(Product, ProductAdmin)

admin.site.register(Categories)