from django.conf import settings
from django.test import TestCase
from accounts.models import Account


class TestDjangoSettings(TestCase):
    def test_language_setting(self):
        self.assertEqual(settings.LANGUAGE_CODE, "ja")

    def test_timezone_setting(self):
        self.assertEqual(settings.TIME_ZONE, "Asia/Tokyo")
    
    def test_auth_model_setting(self):
        self.assertIsInstance(settings.AUTH_USER_MODEL, Account)
