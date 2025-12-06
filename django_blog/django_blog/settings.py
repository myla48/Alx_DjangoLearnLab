INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',   # 👈 added here
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',   # Database backend
        'NAME': 'mydatabase',                        # Database name
        'USER': 'myuser',                            # 👈 your DB username
        'PASSWORD': 'mypassword',                    # 👈 your DB password
        'HOST': 'localhost',                         # 👈 or your DB server IP
        'PORT': '5432',                              # 👈 default PostgreSQL port
    }
}
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]   # for global static files
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',        # your blog app
    'taggit',      # 👈 add this line
]


