from django.urls import path
from .import views

urlpatterns = [

    path('',views.index,name='index'),
    path('product_details/<int:id>/',views.product_details,name='product_details'),
    path('category_wise_product/<int:id>/',views.category_wise_product,name='category_wise_product'),
    path('product_search/',views.product_search,name='product_search'),
    path('product_price_search/',views.product_price_search,name='product_price_search'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),

]