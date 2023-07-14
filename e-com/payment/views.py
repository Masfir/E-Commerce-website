from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BillingAddressForm,OrderForm
from .models import BillingAddress
from cart.models import Cart,Order
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#SSLCommerze integration

import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket


def checkout(request):    
    billing_address = BillingAddress.objects.get_or_create(user=request.user)
    billing_address = billing_address[0]
    
    billing_form = BillingAddressForm(instance = billing_address)
    order_form = OrderForm()
    
    order_qs = Order.objects.filter(user=request.user, ordered = False)[0]
    
    order_item = order_qs.order_items.all().count()
    print("Total order item: ",order_item)
    order_item_name = order_qs.order_items.all()[0]
    print("Order item name: ",order_item_name)
   
    total_amount = order_qs.get_order_price_total()
    
    
    
    if request.method == 'POST':
        billing_form = BillingAddressForm(request.POST, instance=billing_address)
        order_form = OrderForm(request.POST, instance=order_qs)
         
        if not billing_address.is_fully_filled:
             return redirect('checkout')
         
        if billing_form.is_valid() and order_form.is_valid():
            billing_form.save()
            payment_form = order_form.save(commit = False)
             
            if payment_form.payment_method == 'Cash On Delivery':
                order_qs.ordered =True
                order_qs.paymentId = payment_form.payment_method
                order_qs.orderId = get_random_string(10)
                order_qs.save()
                cart_qs = Cart.objects.filter(user = request.user, purchase = False)
                for item in cart_qs:
                    item.purchase = True
                    item.save()
                return redirect('/')
                 
            if payment_form.payment_method == 'SSLCommerze':
                store_id = 'abc626e225657a3c'
                API_key = 'abc626e225657a3c@ssl'               
                mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)
                
                status_url = request.build_absolute_uri(reverse('complete'))               
                mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
                
                mypayment.set_product_integration(total_amount=total_amount, currency='BDT', product_category='None', product_name=order_item_name, num_of_item=order_item, shipping_method='NO', product_profile='None')
                
                current_user = request.user
                # print(current_user.username,"-->current user")               
                mypayment.set_customer_info(name=current_user.username, email=current_user.email, address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')

                mypayment.set_shipping_info(shipping_to=billing_address.first_name, address=billing_address.email, city='Dhaka', postcode='1209', country='Bangladesh')
                
                response_data = mypayment.init_payment()
                return redirect(response_data['GatewayPageURL'])
                    
    context ={
            'billing_form' : billing_form,
            'order_form' : order_form,
            'total_amount' : total_amount,
            'order_item' : order_item,
            'order_item_name' : order_item_name,           
            }
                            
    return render(request,'checkout.html', context)

@csrf_exempt
def complete(request):
    # print(request.POST)
    if request.method == 'POST':
        status = request.POST['status']
        
        if status == 'VALID':
            tran_id = request.POST['tran_id']
            val_id = request.POST['val_id']
            card_type = request.POST['card_type']
            return HttpResponseRedirect(reverse('purchase', kwargs = {'tran_id':tran_id, 'val_id':val_id, 'card_type':card_type}))
        
        elif status == 'FAILED':
            return redirect("Failed")
        
        elif status == 'CANCEL':
            return redirect("Cancel")            
    
    return render(request,'complete.html')

def purchase(request,tran_id,val_id,card_type):
    print("I am purchase")
    order_qs = Order.objects.filter(user=request.user, ordered = False)[0]
    order_qs.ordered = True
    order_qs.paymentId = tran_id 
    order_qs.orderId = val_id     
    order_qs.payment_type = card_type    
    order_qs.save()
    
    cart_qs = Cart.objects.filter(user = request.user, purchase = False)
    for item in cart_qs:
        item.purchase = True
        item.save()    
    
    return redirect('/')

