from django.test import SimpleTestCase
from django.urls import resolve, reverse

from cart.views import order_details, add_to_cart, remove_from_cart, process_payment, checkout, payment_processed, update_transaction_records

class TestCartUrls(SimpleTestCase):

    def test_order_details_resolve(self):
        url = reverse('shopping-cart-page')
        self.assertEquals(resolve(url).func, order_details)

    def test_add_to_cart_resolve(self):
        url = reverse('add_to_cart', args=['1'])
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_remove_from_cart_resolve(self):
        url = reverse('remove_from_cart', args=['1'])
        self.assertEquals(resolve(url).func, remove_from_cart)

    def test_process_payment_resolve(self):
        url = reverse('payment-page', args=['1'])
        self.assertEquals(resolve(url).func, process_payment)

    def test_checkout_resolve(self):
        url = reverse('checkout-page')
        self.assertEquals(resolve(url).func, checkout)

    def test_payment_processed_resolve(self):
        url = reverse('payment-processed')
        self.assertEquals(resolve(url).func, payment_processed)

    def test_update_transaction_records_resolve(self):
        url = reverse('update-transaction-records', args=['1'])
        self.assertEquals(resolve(url).func, update_transaction_records)