from django.db import models
from store.models.products import Prodcuts
from store.models.customers import Customer
import datetime

class Orders(models.Model):
    product=models.ForeignKey(Prodcuts,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=450,default='',blank=True)
    phone=models.CharField(max_length=10,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    #call this fun from checkout.py for post request.
    def place_Order(self):
        self.save()

    #call this fun from order.py view file
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders.objects.filter(customer=customer_id).order_by('-date') #last order id show first 