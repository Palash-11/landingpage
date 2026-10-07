from django.db import models
from catalog.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(default=5)  # 1 to 5
    comment = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.rating}★"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order_number = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order_number']

    def __str__(self):
        return self.question

class SocialProof(models.Model):
    message = models.CharField(max_length=255)  # e.g., "ঢাকা থেকে রহিম ২ বক্স বিটরুট পাউডার অর্ডার করেছেন"
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

# Create your models here.
