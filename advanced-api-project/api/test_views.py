from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="tester", password="testpass123")
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

    def test_list_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_requires_login(self):
        # Try without login
        data = {"title": "New Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Now login
        login_success = self.client.login(username="tester", password="testpass123")
        self.assertTrue(login_success)

        # Try again with login
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_requires_login(self):
        data = {"title": "Updated Book", "publication_year": 2022, "author": self.author.id}

        # Without login
        response = self.client.put(reverse('book-update', args=[self.book.id]), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # With login
        self.client.login(username="tester", password="testpass123")
        response = self.client.put(reverse('book-update', args=[self.book.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_requires_login(self):
        # Without login
        response = self.client.delete(reverse('book-delete', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # With login
        self.client.login(username="tester", password="testpass123")
        response = self.client.delete(reverse('book-delete', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
