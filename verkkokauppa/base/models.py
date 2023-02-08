from django.db import models
from PIL import Image

# Categories for products
class Categories(models.Model):
    product_category = models.CharField(max_length=100)
    description = models.TextField(max_length=300, default="No description available")
    image = models.ImageField(default='default_no_image.png', upload_to='category_images')

    def __str__(self):
        return self.product_category



# Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    age = models.CharField(max_length=30, default="Not specified.")
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(default='default_no_image.png', upload_to='product_images')

    product_category = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

