from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # List all posts
    path("posts/", PostListView.as_view(), name="post-list"),

    # View a single post
    path("post/<int:pk>/delete/", PostDetailView.as_view(), name="post-detail"),

    # Create a new post
    path("post/new/", PostCreateView.as_view(), name="post-create"),

    # Update an existing post
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),

    # Delete a post
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
