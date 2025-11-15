# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your app containing the CustomUser model
    'bookshelf',
]

# Custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

