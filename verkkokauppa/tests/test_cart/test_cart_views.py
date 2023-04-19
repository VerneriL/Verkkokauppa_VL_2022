from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date
import datetime

from cart.views import generate_order_id



class TestCartViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(
            id=1,
            username="test_user",
            password="test_password"
        )

        self.order_details_url = reverse('shopping-cart-page')
        self.add_to_cart_url = reverse('add_to_cart', args=['1'])
        self.remove_from_cart_url = reverse('remove_from_cart', args=['1'])
        self.checkout_url = reverse('checkout-page')
        self.process_payment_url = reverse('payment-page', args=['1'])
        self.payment_processed_url = reverse('payment-processed')
        self.update_transaction_records_url = reverse('update-transaction-records', args=['1'])

    def test_generate_order_id(self):
        date_string = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
        random_id = generate_order_id()
        self.assertEquals(date_string, random_id[0:8])

    def test_order_details_GET_404(self):
        # Gets 404 since object doesn't exist
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('shopping-cart-page')
        self.assertEquals(response.status_code, 404)

    def test_add_to_cart_POST_404(self):
        # Gets 404 since object doesn't exist
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('add_to_cart')
        self.assertEquals(response.status_code, 404)
