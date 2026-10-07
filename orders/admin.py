from django.contrib import admin
from .models import Customer, Order, OrderItem, Payment, OrderStatusLog, Lead, StockAdjustment

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_number', 'customer__name', 'customer__phone']
    inlines = [OrderItemInline, PaymentInline]

admin.site.register(Customer)
admin.site.register(Lead)
admin.site.register(StockAdjustment)

# Register your models here.
