from store.models.orders import Orders
from django.views import View
from django.shortcuts import render



class OrderView(View):
    def get(self,request):
        customer=request.session.get('customer')
        print('customer order no ',customer)
        orders=Orders.get_orders_by_customer(customer)
        print('orders by id ',orders)
        return render(request,'store/order.html',{'orders':orders})