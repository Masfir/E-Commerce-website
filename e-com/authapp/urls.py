from django.urls import path
from .import views

urlpatterns = [

    path('signup/',views.signup,name='signup'),
    path('authlogin/',views.authlogin,name='authlogin'),
    path('authlogout/',views.authlogout,name='authlogout'),
]