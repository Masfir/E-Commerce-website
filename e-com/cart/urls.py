from django.urls import path
from .import views

urlpatterns = [
   path('add_to_cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
   path('cart_view/',views.cart_view,name='cart_view'),
   path('item_increase/<int:id>/',views.item_increase,name='item_increase'),
   path('item_decrease/<int:id>/',views.item_decrease,name='item_decrease'),
   path('item_remove/<int:id>/',views.item_remove,name='item_remove'),
  
]