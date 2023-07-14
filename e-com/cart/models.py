from django.db import models
from django.contrib.auth.models import User
from ecommerceapp.models import *
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    cart_item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchase = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def get_cart_total(self):
        return float(self.quantity * self.cart_item.price)
    
    def __str__(self):
        return f'{self.cart_item.product_name} x {self.quantity}'
    
class Order(models.Model):
    PAYMENT_METHOD=(
        ('Cash On Delivery', 'Cash On Delivery'),
        ('SSLCommerze', 'SSLCommerze'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    order_items = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    orderId = models.CharField(max_length=30, blank=True, null=True)
    paymentId = models.CharField(max_length=30,blank=True,null=True)
    payment_type = models.CharField(max_length=30,blank=True,null=True)
    payment_method = models.CharField(max_length=26,choices=PAYMENT_METHOD,default='Cash On Delivery')
    created = models.DateTimeField(auto_now_add=True)
    
    def  get_order_price_total(self):
        total = 0
        for cart_item in self.order_items.all():
            total += float(cart_item.get_cart_total())
        return total
