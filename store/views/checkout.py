from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.views.generic.base import View #for save password in db with hashing
from django.views import View
from store.models.orders import Orders
from store.models.products import Prodcuts
from store.models.customers import Customer

class CheckoutView(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        cust_customer=request.session.get('customer')
        cart=request.session.get('cart')
        pro=Prodcuts.get_product_by_id(list(cart.keys()))
        print(address,phone,cust_customer,cart,pro)

        for product in pro:
            order=Orders(
                product=Prodcuts(id=product.id),
                customer=Customer(id=cust_customer),
                quantity=cart.get(str(product.id)),
                price=product.price,
                address=address,
                phone=phone)  
            order.save()
            # order.place_Order()
        #after order placed then cart will be empty
        request.session['cart']={}
        return redirect('cart')
        

