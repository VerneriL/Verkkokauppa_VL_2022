from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestUserViews(TestCase):

    def setUp(self):
        self.client = Client()
        # Create a test user for @login_required authenticated views
        self.user = User.objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.register_url = reverse('register-page')
        self.profile_url = reverse('profile-page')
        self.update_url = reverse('update-page')
        self.contact_url = reverse('contact-page')

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_profile_GET(self):
        # Emulate user logged in with 
        # self.client.login(username="test_user", password="test_password")
        self.client.login(username="test_user", password="test_password")
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_update_GET(self):
        self.client.login(username="test_user", password="test_password")
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')

    def test_contact_GET(self):
        self.client.login(username="test_user", password="test_password")
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/contact.html')