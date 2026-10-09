from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # আপনার অন্যান্য API রাউট...
]

# Production এবং Local উভয় পরিবেশেই Static ফাইল সার্ভ করার নিশ্চিতকরণ
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)