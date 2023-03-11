from django.test import TestCase
from django.urls import reverse


class TestTopView(TestCase):
    def test_can_view(self):
        response = self.client.get(reverse("posts:top"))
        self.assertEqual(response.status_code, 200)
