from django import forms
from .models import BillingAddress
from cart.models import Order



class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = '__all__'
        exclude = ('user',)
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']