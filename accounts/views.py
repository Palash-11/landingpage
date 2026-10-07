from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderCreateView(APIView):

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "অর্ডারটি সফলভাবে গৃহীত হয়েছে।",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class DashboardCountsView(APIView):

    def get(self, request):
        total_orders = Order.objects.count()
        return Response({"total_orders": total_orders})