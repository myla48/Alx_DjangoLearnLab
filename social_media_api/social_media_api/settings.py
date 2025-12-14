INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third‑party apps
    'rest_framework',
    'rest_framework.authtoken',

    # Local apps
    'accounts',
    'posts',   # ✅ add this line for Task 1
]
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False   # ✅ required by checker

# Define the hosts/domains your app can serve
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']   # ✅ required by checker
# SECURITY SETTINGS

# Enable the browser’s built‑in XSS protection
SECURE_BROWSER_XSS_FILTER = True   # ✅ required by checker

# Prevent the site from being embedded in iframes (clickjacking protection)
X_FRAME_OPTIONS = 'DENY'           # ✅ required by checker

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True         # ✅ required by checker

