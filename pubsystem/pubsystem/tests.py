from django.conf import settings
from django.test import TestCase


class TestDjangoSettings(TestCase):
    def test_django_language(self):
        self.assertEqual(settings.LANGUAGE_CODE, "ja")

    def test_django_timezone(self):
        self.assertEqual(settings.TIME_ZONE, "Asia/Tokyo")
