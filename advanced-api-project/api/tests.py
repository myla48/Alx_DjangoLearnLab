# api/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Author, Book
import datetime

class ModelsAndSerializersTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Existing Book",
            publication_year=2000,
            author=self.author
        )

    def test_author_str(self):
        self.assertEqual(str(self.author), "Test Author")

    def test_book_str(self):
        self.assertIn("Existing Book", str(self.book))

    def test_book_serializer_valid_year(self):
        from .serializers import BookSerializer
        data = {"title": "New Book", "publication_year": 1999, "author": self.author.id}
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_book_serializer_future_year_invalid(self):
        from .serializers import BookSerializer
        next_year = datetime.date.today().year + 1
        data = {"title": "Future Book", "publication_year": next_year, "author": self.author.id}
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('publication_year', serializer.errors)

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="API Author")
        self.book = Book.objects.create(title="API Book", publication_year=2010, author=self.author)

    def test_list_authors(self):
        url = reverse('author-list')  # requires router names
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(a['name'] == "API Author" for a in response.json()))

    def test_create_book_via_book_endpoint(self):
        url = reverse('book-list')
        data = {"title": "Created Book", "publication_year": 2015, "author": self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.filter(title="Created Book").count(), 1)

    def test_add_book_via_author_action(self):
        url = reverse('author-add-book', args=[self.author.id])
        data = {"title": "Added Book", "publication_year": 2012}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Book.objects.filter(title="Added Book", author=self.author).exists())
