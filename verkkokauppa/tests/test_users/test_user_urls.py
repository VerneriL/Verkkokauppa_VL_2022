from django.test import SimpleTestCase
from django.urls import resolve, reverse

from users.views import register, profile, update, contact

class TestUserUrls(SimpleTestCase):

    def test_register_resolve(self):
        url = reverse('register-page')
        self.assertEquals(resolve(url).func, register)

    def test_profile_resolve(self):
        url = reverse('profile-page')
        self.assertEquals(resolve(url).func, profile)

    def test_update_resolve(self):
        url = reverse('update-page')
        self.assertEquals(resolve(url).func, update)

    def test_contact_resolve(self):
        url = reverse('contact-page')
        self.assertEquals(resolve(url).func, contact)