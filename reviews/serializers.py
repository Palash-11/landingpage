from rest_framework import serializers
from .models import Review, FAQ, SocialProof

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'reviewer_name', 'rating', 'comment', 'created_at']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class SocialProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialProof
        fields = '__all__'