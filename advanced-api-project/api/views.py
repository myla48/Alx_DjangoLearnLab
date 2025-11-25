# api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    CRUD for Author. Nested books are read-only via AuthorSerializer.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['post'])
    def add_book(self, request, pk=None):
        """
        Custom action to add a book to an author:
        POST /api/authors/{pk}/add_book/  with JSON { "title": "...", "publication_year": 2020 }
        """
        author = self.get_object()
        data = request.data.copy()
        data['author'] = author.id
        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD for Book.
    """
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
