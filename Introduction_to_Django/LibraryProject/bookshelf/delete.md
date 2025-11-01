# Delete Operation: Removing a Book from the Database

This operation demonstrates how to delete a book entry using Django's ORM via the shell.

## Step 1: Open the Django Shell
```bash
python manage.py shell
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
