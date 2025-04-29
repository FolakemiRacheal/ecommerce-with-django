from django.shortcuts import render

# Create your views here.
def market(request):
    context={}
    return render(request, 'marketapp/market.html', context)

def cart(request):
    context = {}
    return render(request, 'marketapp/cart.html',context)

def checkout(request):
    context = {}
    return render(request, 'marketapp/checkout.html', context)

