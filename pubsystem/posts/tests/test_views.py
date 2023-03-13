from django.conf import settings
from django.contrib.auth import SESSION_KEY, get_user_model
from django.test import TestCase
from django.urls import reverse

from posts.models import Bureau


class TestTopView(TestCase):
    @classmethod
    def setUpTestData(cls):
        bureaus = [
            Bureau(name=f"開発局{i}", keyword=f"dev-{i}", sort_num=99 - i)
            for i in range(10)
        ]
        Bureau.objects.bulk_create(bureaus)

    def setUp(self):
        self.client_response = self.client.get(reverse("posts:top"))

    def test_can_view(self):
        """すべてのユーザーが正しく表示できる"""
        self.assertEqual(self.client_response.status_code, 200)

    def test_can_display_all_bureau(self):
        """全ての局を正しく表示できる"""
        self.assertQuerysetEqual(
            self.client_response.context["bureaus"], Bureau.objects.all(), ordered=False
        )

    def test_ordering_bureau(self):
        """局のソート値の昇順で表示できる"""
        self.assertEqual(
            self.client_response.context["bureaus"].first(),
            Bureau.objects.order_by("sort_num").first(),
        )
        self.assertEqual(
            self.client_response.context["bureaus"].last(),
            Bureau.objects.order_by("sort_num").last(),
        )


class TestHomeView(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(
            username="testuser", email="testuser@example.com", password="test2023user"
        )
        bureaus = [
            Bureau(name=f"開発局{i}", keyword=f"dev-{i}", sort_num=99 - i)
            for i in range(10)
        ]
        Bureau.objects.bulk_create(bureaus)

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

    def test_can_display_all_bureau(self):
        """全ての局を正しく表示できる"""
        self.client.force_login(self.testuser)
        response = self.client.get(self.view_url)
        self.assertQuerysetEqual(
            response.context["bureaus"], Bureau.objects.all(), ordered=False
        )

    def test_ordering_bureau(self):
        """局のソート値の昇順で表示できる"""
        self.client.force_login(self.testuser)
        response = self.client.get(self.view_url)
        self.assertEqual(
            response.context["bureaus"].first(),
            Bureau.objects.order_by("sort_num").first(),
        )
        self.assertEqual(
            response.context["bureaus"].last(),
            Bureau.objects.order_by("sort_num").last(),
        )
