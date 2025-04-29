from django.urls import path
from . import views

urlpatterns = [
    path('', views.market, name="ecommrce market"),
    path('', views.checkout, name="payment page"),
    path('', views.cart, name="cart page")
]
