from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderCreateView, LeadCreateView, OrderAdminViewSet

router = DefaultRouter()
router.register(r'admin-orders', OrderAdminViewSet)

urlpatterns = [
    path('checkout/', OrderCreateView.as_view(), name='checkout'),
    path('leads/', LeadCreateView.as_view(), name='lead_create'),
    path('', include(router.urls)),
]