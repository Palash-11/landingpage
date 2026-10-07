from django.urls import path
from .views import DashboardCountsView, OrderCreateView

urlpatterns = [
    # ১. ফ্রন্টএন্ড ফর্ম থেকে আসা অর্ডারের endpoint
    path("orders/", OrderCreateView.as_view(), name="order-create"),
    # ২. এডমিন ড্যাশবোর্ডের সামারির endpoint (ঐচ্ছিক)
    path(
        "dashboard/counts/",
        DashboardCountsView.as_view(),
        name="dashboard-counts",
    ),
]