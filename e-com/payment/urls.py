from django.urls import path
from .import views

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('complete/', views.complete, name="complete"),
    path('purchase/<tran_id>/<val_id>/<card_type>/', views.purchase, name="purchase"),
  
]