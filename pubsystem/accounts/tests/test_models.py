from django.test import TestCase
import freezegun
import datetime
from django.contrib.auth import get_user_model

class TestAuthUserModel(TestCase):
    @classmethod
    @freezegun.freeze_time("2023-02-01 12:34:56")
    def setUpTestData(cls):
        get_user_model().objects.create(username="user1", email="user1@example.com", password="user1spassword")
    
    def setUp(self):
        self.user = get_user_model().objects.get(username="user1")
        
    def test_date_joined(self):
        self.assertEqual(self.user.date_joined, datetime.datetime(2023,2,1,12,34,56,tzinfo=datetime.timezone.utc))
    
    def test_last_login(self):
        # logged_in = self.client.login(email="user1@example.com", password="user1spassword")
        # self.assertTrue(logged_in)
        self.assertEqual(self.user.last_login, datetime.datetime(2023,2,1,12,34,56,tzinfo=datetime.timezone.utc))