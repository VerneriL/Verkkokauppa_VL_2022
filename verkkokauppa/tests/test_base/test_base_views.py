from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestBaseViews(TestCase):

    def setUp(self):
        self.client = Client() # Django testing client
        self.home_url = reverse('home-page')
        self.store_url = reverse('store-page')
        self.about_url = reverse('about-page')
        self.product_url = reverse('product-page', args=['1234567']) # Dummy product id arg

    def test_home_GET(self):      
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')

    def test_store_GET(self):
        response = self.client.get(self.store_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/store.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/about.html')

    # Fix later
    # def test_product_GET(self):
    #     self.user = User.objects.create_user(username="test_user", password="test_password")
    #     self.client.login(username="test_user", password="test_password")
    #     response = self.client.get(self.product_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'base/product.html')
