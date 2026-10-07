from django.contrib import admin
from .models import Review, FAQ, SocialProof

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewer_name', 'product', 'rating', 'is_approved', 'created_at']
    list_editable = ['is_approved']
    list_filter = ['rating', 'is_approved']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order_number', 'is_active']
    list_editable = ['order_number', 'is_active']

@admin.register(SocialProof)
class SocialProofAdmin(admin.ModelAdmin):
    list_display = ['message', 'is_active', 'created_at']
    list_editable = ['is_active']

# Register your models here.
