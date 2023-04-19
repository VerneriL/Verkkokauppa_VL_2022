from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import home, store, about, account, products

# TEST IF URLS RESOLVE VIEWS
class TestBaseUrls(SimpleTestCase):
    # base.views and base.urls
    def test_home_resolved(self):
        url = reverse('home-page')
        self.assertEquals(resolve(url).func, home)
    
    def test_store_resolved(self):
        url = reverse('store-page')
        self.assertEquals(resolve(url).func, store)

    def test_about_resolved(self):
        url = reverse('about-page')
        self.assertEquals(resolve(url).func, about)

    def test_account_resolved(self):
        url = reverse('account-page')
        self.assertEquals(resolve(url).func, account)

    def test_products_resolved(self):
        url = reverse('product-page', args=['1']) # Product page takes additional arguments. 1 here is a dummy
        self.assertEquals(resolve(url).func, products)
