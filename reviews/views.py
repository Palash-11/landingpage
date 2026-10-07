from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Review, FAQ, SocialProof
from .serializers import ReviewSerializer, FAQSerializer, SocialProofSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.filter(is_approved=True)
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer
    permission_classes = [AllowAny]

class SocialProofListView(generics.ListAPIView):
    queryset = SocialProof.objects.filter(is_active=True)
    serializer_class = SocialProofSerializer
    permission_classes = [AllowAny]

# Create your views here.
