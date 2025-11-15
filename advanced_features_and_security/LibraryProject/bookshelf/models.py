from django.db import models

class Book(models.Model):
    """Book model with custom permissions for Task 1."""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title
