from django.db import models
from django.shortcuts import redirect

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=16)
    email=models.EmailField()
    password=models.CharField(max_length=500)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email) #get for get only single record instead of filter
        except:
            return False
    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False