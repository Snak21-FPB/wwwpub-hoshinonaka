from django.test import TestCase
from django.conf import settings

class TestDjangoSettings(TestCase):
    def test_django_language(self):
        self.assertEqual(settings.LANGUAGE_CODE, "ja")
    
    def test_django_timezone(self):
        self.assertEqual(settings.TIME_ZONE, "Asia/Tokyo")
