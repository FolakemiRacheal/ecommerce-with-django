from django.urls import path
from . import views

urlpatterns = [
    path('', views.market, name="market"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart")
]
