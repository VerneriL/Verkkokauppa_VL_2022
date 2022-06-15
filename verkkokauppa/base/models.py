from django.db import models


class Categories(models.Model):
    product_category = models.CharField(max_length=100)

    def __str__(self):
        return self.product_category


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
# Maybe add a picture of the product
# Add a category of products
    product_category = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

