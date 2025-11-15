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
# SECURITY SETTINGS

# Never run with DEBUG = True in production
DEBUG = False

# Browser-side protections
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensure cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


