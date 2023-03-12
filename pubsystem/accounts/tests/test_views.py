from django.conf import settings
from django.contrib.auth import SESSION_KEY, get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy


class TestAccountLoginView(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(
            username="testuser", email="testuser@example.com", password="test2023user"
        )

    def setUp(self):
        self.user = get_user_model().objects.get(username="testuser")
        self.view = reverse("accounts:login")

    def test_can_view(self):
        response = self.client.get(self.view)
        self.assertEqual(response.status_code, 200)
