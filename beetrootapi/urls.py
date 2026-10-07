# beetrootapi/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('catalog.urls')),  # 'api/v1/' এর জায়গায় 'api/' দিন
]