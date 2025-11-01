# Create Operation: Adding a Book to the Database

## Step 1: Open the Django Shell
```bash
python manage.py shell
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
