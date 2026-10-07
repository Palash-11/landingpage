import uuid
from rest_framework import serializers
from django.db import transaction
from .models import Customer, Order, OrderItem, Payment, Lead, StockAdjustment
from catalog.models import Product, DeliveryZone, Coupon

class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity']

class OrderCreateSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(write_only=True)
    customer_phone = serializers.CharField(write_only=True)
    customer_address = serializers.CharField(write_only=True)
    delivery_zone_id = serializers.IntegerField(write_only=True)
    coupon_code = serializers.CharField(write_only=True, required=False, allow_blank=True)
    items = OrderItemSerializer(many=True, write_only=True)
    payment_method = serializers.CharField(write_only=True, default='cod')

    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'customer_name', 'customer_phone', 'customer_address',
            'delivery_zone_id', 'coupon_code', 'items', 'payment_method', 'note',
            'delivery_charge', 'discount_amount', 'total_amount', 'created_at'
        ]
        read_only_fields = ['id', 'order_number', 'delivery_charge', 'discount_amount', 'total_amount', 'created_at']

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        cust_name = validated_data.pop('customer_name')
        cust_phone = validated_data.pop('customer_phone')
        cust_address = validated_data.pop('customer_address')
        zone_id = validated_data.pop('delivery_zone_id')
        coupon_code = validated_data.pop('coupon_code', None)
        payment_method = validated_data.pop('payment_method', 'cod')

        # ১. Customer তৈরি বা বের করা
        customer, _ = Customer.objects.get_or_create(
            phone=cust_phone,
            defaults={'name': cust_name, 'address': cust_address}
        )

        # ২. Delivery Zone ও Coupon চেক
        delivery_zone = DeliveryZone.objects.get(id=zone_id)
        delivery_charge = delivery_zone.charge
        discount_amount = 0

        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code, is_active=True)
                discount_amount = coupon.discount_amount
            except Coupon.DoesNotExist:
                coupon = None
        else:
            coupon = None

        # ৩. প্রসেস প্রোডাক্ট ও টোটাল হিসাব
        subtotal = 0
        order_items_to_create = []

        for item in items_data:
            product = Product.objects.select_for_update().get(id=item['product_id'])
            if product.stock_quantity < item['quantity']:
                raise serializers.ValidationError(f"{product.name} এর স্টক পর্যাপ্ত নেই।")
            
            # স্টক কমিয়ে দেওয়া
            product.stock_quantity -= item['quantity']
            product.save()

            price = product.discount_price if product.discount_price else product.price
            subtotal += price * item['quantity']

            order_items_to_create.append({
                'product': product,
                'quantity': item['quantity'],
                'unit_price': price
            })

        total_amount = (subtotal + delivery_charge) - discount_amount

        # ৪. Order অবজেক্ট তৈরি
        order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"
        order = Order.objects.create(
            order_number=order_number,
            customer=customer,
            delivery_zone=delivery_zone,
            coupon=coupon,
            delivery_charge=delivery_charge,
            discount_amount=discount_amount,
            total_amount=total_amount,
            **validated_data
        )

        # ৫. OrderItems সংরক্ষণ
        for item_info in order_items_to_create:
            OrderItem.objects.create(order=order, **item_info)

        # ৬. Payment অবজেক্ট তৈরি
        Payment.objects.create(
            order=order,
            method=payment_method,
            amount=total_amount
        )

        return order

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'