from django.shortcuts import render
from .models import *
# Create your views here.
def market(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'marketapp/market.html', context)

def cart(request):
    if request.user.is_authenticated:
        client = request.user.client
        #creating an object or querying one
        order, created= Order.objects.get_or_create(client=client,complete=False)
        lists = order.orderlist_set.all()

    else:
        lists =[]
        order = {'get_cart_total': 0,'get_cart_lists':0}
    context = {'lists':lists, 'order':order}
    return render(request, 'marketapp/cart.html',context)

def checkout(request):

    if request.user.is_authenticated:
        client = request.user.client
        #creating an object or querying one
        order, created= Order.objects.get_or_create(client=client,complete=False)
        lists = order.orderlist_set.all()

    else:
        lists =[]
        order = {'get_cart_total': 0,'get_cart_lists':0}
    context = {'lists':lists, 'order':order}
    context = {}
    return render(request, 'marketapp/checkout.html', context)


