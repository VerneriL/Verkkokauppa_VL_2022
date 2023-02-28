from django.contrib import admin

from .models import Categories, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "price", "product_category", "age", "description", "image"]

admin.site.register(Product, ProductAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    fields = ["categories", "description"]
admin.site.register(Categories)