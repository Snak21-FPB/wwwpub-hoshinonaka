from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase

from accounts.models import Account


class TestDjangoSettings(SimpleTestCase):
    def test_language(self):
        """言語設定"""
        self.assertEqual(settings.LANGUAGE_CODE, "ja")

    def test_timezone(self):
        """タイムゾーン設定"""
        self.assertEqual(settings.TIME_ZONE, "Asia/Tokyo")

    def test_auth_model(self):
        """認証ユーザーモデル設定"""
        self.assertEqual(get_user_model(), Account)

    def test_login_redirect(self):
        """ログイン後遷移先設定"""
        self.assertEqual(settings.LOGIN_REDIRECT_URL, "posts:home")
