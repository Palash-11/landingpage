from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from accounts.permissions import IsStaffOrAdmin
from .models import Order, Lead
from .serializers import OrderCreateSerializer, LeadSerializer

class OrderCreateView(generics.CreateAPIView):
    """ল্যান্ডিং পেজ থেকে পাবলিকলি অর্ডার সাবমিট করার জন্য"""
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [AllowAny]

class LeadCreateView(generics.CreateAPIView):
    """চেকআউট ইনকমপ্লিট হলে লিড সেভ করার জন্য"""
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny]

class OrderAdminViewSet(viewsets.ModelViewSet):
    """অ্যাডমিন ও স্টাফদের অর্ডার ম্যানেজ করার জন্য"""
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderCreateSerializer
    permission_classes = [IsStaffOrAdmin]

# Create your views here.
