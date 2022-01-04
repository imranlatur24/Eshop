from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.views.generic.base import View #for save password in db with hashing
from django.views import View
from store.models.products import Prodcuts

class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        print('card product ids = ',ids)
        products=Prodcuts.get_product_by_id(ids)
        print(products)
        return render(request,'store/cart.html',{'products':products})

