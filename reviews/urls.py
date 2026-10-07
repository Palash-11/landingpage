from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, FAQListView, SocialProofListView, create_order

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq_list'),
    path('social-proofs/', SocialProofListView.as_view(), name='social_proof_list'),
    path('', include(router.urls)),
    path('api/orders/', create_order, name='create_order'),
]