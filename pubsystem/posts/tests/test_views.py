from django.conf import settings
from django.contrib.auth import SESSION_KEY, get_user_model
from django.test import TestCase
from django.urls import reverse


class TestTopView(TestCase):
    def test_can_view(self):
        """すべてのユーザーが正しく表示できる"""
        response = self.client.get(reverse("posts:top"))
        self.assertEqual(response.status_code, 200)


class TestHomeView(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(
            username="testuser", email="testuser@example.com", password="test2023user"
        )

    def setUp(self):
        self.testuser = get_user_model().objects.get(username="testuser")
        self.view_url = reverse("posts:home")

    def test_user_can_view(self):
        """認証されたユーザーが正しく表示できる"""
        self.client.force_login(self.testuser)
        response = self.client.get(self.view_url)
        self.assertIn(SESSION_KEY, self.client.session)
        self.assertEqual(response.status_code, 200)

    def test_anonymous_redirect_login(self):
        """認証されていないユーザーがログインページに遷移される"""
        response = self.client.get(self.view_url)
        self.assertNotIn(SESSION_KEY, self.client.session)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url.split("?")[0], reverse(settings.LOGIN_URL))
