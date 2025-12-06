from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views

urlpatterns += [
    path("posts/<int:post_id>/comments/new/", views.add_comment, name="add-comment"),
    path("comments/<int:pk>/edit/", views.edit_comment, name="edit-comment"),
    path("comments/<int:pk>/delete/", views.delete_comment, name="delete-comment"),
]

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
