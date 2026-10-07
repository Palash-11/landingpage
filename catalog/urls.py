from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, DeliveryZoneViewSet, CouponViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'delivery-zones', DeliveryZoneViewSet, basename='deliveryzone')
router.register(r'coupons', CouponViewSet, basename='coupon')

urlpatterns = [
    path('', include(router.urls)),
]