from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('orders.urls')),  # আপনার অর্ডার অ্যাপের রাউট এখানে যুক্ত হবে
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)