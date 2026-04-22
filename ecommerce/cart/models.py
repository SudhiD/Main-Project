from django.db import models
from django.contrib.auth.models import User 
from shope.models import Products

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.quantity * self.product.price    

    def __str__(self):
        return f"Cart of {self.user.username}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    order_data = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=20,null=True,)
    payment_method = models.CharField(max_length=20,null=True,)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20,null=True)
    is_ordered = models.BooleanField(default=False)
    delivery_status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.user.username

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.order_id}"      