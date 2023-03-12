import datetime

import freezegun
from django.contrib.auth import get_user_model
from django.test import TestCase


class TestAuthUserModel(TestCase):
    @classmethod
    @freezegun.freeze_time("2023-02-01 12:12:12")
    def setUpTestData(cls):
        get_user_model().objects.create(
            username="testuser",
            email="testuser@example.com",
            password="testuserspassword",
        )

    def setUp(self):
        self.testuser = get_user_model().objects.get(username="testuser")

    def test_date_joined(self):
        """登録日時のテスト"""
        self.assertEqual(
            self.testuser.date_joined,
            datetime.datetime(2023, 2, 1, 12, 12, 12, tzinfo=datetime.timezone.utc),
        )

    @freezegun.freeze_time("2023-02-01 12:12:21")
    def test_last_login(self):
        """最終ログイン日時のテスト"""
        self.client.force_login(self.testuser)
        self.assertEqual(
            self.testuser.last_login,
            datetime.datetime(2023, 2, 1, 12, 12, 21, tzinfo=datetime.timezone.utc),
        )
