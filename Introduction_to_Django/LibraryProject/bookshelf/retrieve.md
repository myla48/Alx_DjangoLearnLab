# Retrieve Operation: Accessing Book Data from the Database

This operation demonstrates how to retrieve and display a book instance using Django's ORM via the shell.

## Step 1: Open the Django Shell
```bash
python manage.py shell
Book.objects.get(title="1984")
