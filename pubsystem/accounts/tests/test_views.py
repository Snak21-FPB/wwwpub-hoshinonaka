from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model, SESSION_KEY


class TestAccountLoginView(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(username="testuser", email="testuser@example.com", password="test2023user")
    
    def setUp(self):
        self.user = get_user_model().objects.get(username="testuser")
        self.view = reverse("accounts:login")

    def test_can_view(self):
        response = self.client.get(self.view)
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        response = self.client.post(self.view,{"email":"testuser@example.com","password":"test2023user"})
        form = response.context["form"]
        self.assertRedirects(response, reverse("posts:home"), 302, 200)
        self.assertTrue(form.is_valid())
        self.assertIn(SESSION_KEY, self.client.session)
    
    def test_invalid_login(self):
        response = self.client.post(self.view,{"email":"testuser@example.com","password":"invalidpass"})
        form = response.context["form"]
        self.assertEqual(response.status_code, 200)
        self.assertFalse(form.is_valid())
        self.assertNotIn(SESSION_KEY,self.client.session)
    
