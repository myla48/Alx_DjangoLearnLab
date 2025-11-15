# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add your app here
    'yourapp',   # replace with the actual app name where CustomUser is defined
]

# Custom user model
AUTH_USER_MODEL = 'yourapp.CustomUser'
