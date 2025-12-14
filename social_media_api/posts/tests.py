from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class PostCommentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='tester', password='pass123')
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        response = self.client.post('/api/posts/', {'content': 'My first post'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_comment(self):
        post = self.client.post('/api/posts/', {'content': 'Another post'}).data
        response = self.client.post('/api/comments/', {'post': post['id'], 'text': 'Nice post!'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
