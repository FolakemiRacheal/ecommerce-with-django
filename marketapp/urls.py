from django.urls import path
from . import views

urlpatterns = [
    path('', views.market, name="market"),
    path('checkout/', views.checkout, name="payment page"),
    path('cart/', views.cart, name="cart page")
]
