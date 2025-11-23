from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Keep the simple list view from Task 1
    path('books/', BookList.as_view(), name='book-list'),

    # Add all CRUD routes from the router
    path('', include(router.urls)),
]
