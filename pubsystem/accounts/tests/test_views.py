from django.contrib.auth import SESSION_KEY, get_user_model
from django.test import TestCase
from django.urls import reverse


class TestAccountLoginView(TestCase):
    def setUp(self):
        self.view = reverse("accounts:login")

    def test_can_view(self):
        """すべてのユーザーが正しく表示できる"""
        response = self.client.get(self.view)
        self.assertEqual(response.status_code, 200)


class TestAccountLogoutView(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(
            username="testuser", email="testuser@example.com", password="test2023user"
        )

    def setUp(self):
        self.user = get_user_model().objects.get(username="testuser")
        self.view = reverse("accounts:logout")
    
    def test_can_logout(self):
        """POSTリクエストによってログアウトできる"""
        self.client.force_login(self.user)
        response = self.client.post(reverse("accounts:logout"))
        self.assertRedirects(response, reverse("posts:top"))
        self.assertNotIn(SESSION_KEY, self.client.session)
