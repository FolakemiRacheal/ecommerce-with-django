from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderList)
admin.site.register(ShippingLocation)
