from django.contrib import admin
from .models import Product, DeliveryZone, Coupon  # নিজের অ্যাপের models থেকে ইমপোর্ট
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_price', 'stock_quantity', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}  # Name টাইপ করলেই Slug অটোমেটিক তৈরি হয়ে যাবে

@admin.register(DeliveryZone)
class DeliveryZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'charge', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_amount', 'is_active', 'valid_from', 'valid_to')
    list_filter = ('is_active',)
    search_fields = ('code',)