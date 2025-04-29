from django.shortcuts import render

# Create your views here.
def market(request):
    return render(request, 'marketapp/market.html')

def cart(request):
    return render(request, 'marketapp/cart.html')

def checkout(request):
    return render(request, 'marketapp/checkout.html')

