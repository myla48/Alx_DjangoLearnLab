from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class AccountsTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password': 'testpass123',
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_login_user(self):
        self.client.post(reverse('register'), {
            'username': 'testuser',
            'password': 'testpass123',
            'email': 'test@example.com'
        })
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
