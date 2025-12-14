from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # existing accounts routes
    path('api/', include('posts.urls')),             # ✅ add posts routes
]
