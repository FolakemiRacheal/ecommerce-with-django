from django.db import models
from django .contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length= 200, null=True)
    email = models.CharField(max_length= 200, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=True, null=True, blank=False)
    image = models.ImageField(null=True,blank= True)


    def __str__ (self):
        return self.name
    
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url        

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True, )
    transaction_id = models.CharField(max_length=200, null = True)


    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderlists = self.orderlist_set.all()
        #looping through the list, so we are saying calculate the total value of the list and return the total
        total = sum([list.get_total for list in orderlists])
        return total
    
    @property
    def get_cart_list(self):
        orderlists = self.orderlist_set.all()
        total = sum([list.quantity for list in orderlists])
        return total
    
class OrderList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)

@property
def get_total(self):
    total = self.product.price * self.quantity
    return total




class ShippingLocation(models.Model):
    client = models.ForeignKey(Client,on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length= 200, null=True)
    city = models.CharField(max_length= 200, null=True)
    state = models.CharField(max_length= 200, null=True)
    zipcode = models.CharField(max_length= 200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location