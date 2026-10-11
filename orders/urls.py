from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderCreateView, LeadCreateView, OrderAdminViewSet

router = DefaultRouter()
router.register(r"admin", OrderAdminViewSet, basename="order-admin")

urlpatterns = [
    path("checkout/", OrderCreateView.as_view(), name="order-checkout"),
    path("leads/", LeadCreateView.as_view(), name="lead-create"),
    path("", include(router.urls)),
]