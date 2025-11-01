# Update Operation: Modifying Book Data in the Database

This operation demonstrates how to update an existing book entry using Django's ORM via the shell.

## Step 1: Open the Django Shell
```bash
python manage.py shell
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
