from django.shortcuts import render
from .models import *
# Create your views here.
def market(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'marketapp/market.html', context)

def cart(request):
    context = {}
    return render(request, 'marketapp/cart.html',context)

def checkout(request):
    context = {}
    return render(request, 'marketapp/checkout.html', context)


