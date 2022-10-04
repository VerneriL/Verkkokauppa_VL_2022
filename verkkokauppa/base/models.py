from django.db import models

# Categories for products
class Categories(models.Model):
    product_category = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.product_category


# Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=500, blank=True, null=True)
# Maybe add a picture of the product
    product_category = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

