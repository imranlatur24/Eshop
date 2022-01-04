from django.db import models
from .category import Category

class Prodcuts(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1) #if products already available then add 1 bydefault
    name = models.CharField(max_length=100,default='')
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=450,default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    class Meta:
        db_table='products'

    @staticmethod
    def get_all_products():
        return Prodcuts.objects.all()
    @staticmethod
    def get_products_by_category_id(category_id):
        if category_id:
            return Prodcuts.objects.filter(category=category_id)
        else:
            return Prodcuts.objects.all()
            
    @staticmethod #this is for cart
    def get_product_by_id(ids):
        print('# ids = ',ids)
        return Prodcuts.objects.filter(id__in=ids)