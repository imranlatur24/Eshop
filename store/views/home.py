from django.shortcuts import redirect, render
from django.views.generic.base import View
from store.models.category import Category
from store.models.products import Prodcuts


class Index(View):
    def post(self,request):
        prod_id=request.POST.get('product')
        remove=request.POST.get('remove')
        print('prod_id',prod_id)
        cart = request.session.get('cart')

        if cart:
            quantity=cart.get(prod_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(prod_id)
                    else:
                        cart[prod_id]=quantity-1
                else:
                    cart[prod_id]=quantity+1
            else:
                cart[prod_id]=1
        else:
            cart={}
            cart[prod_id]=1

            # cart['cart']=cart
        request.session['cart']=cart
        print('cart = ',request.session['cart'])
        return redirect('homepage')

    def get(self,request):
        products=None
        #if cart is empty or not found
        cart=request.session.get('cart')
        if not cart:
            cart=request.session['cart']={}

            
        categories=Category.get_all_categories()
        # print(pro)
        category_id=request.GET.get('category')
        if category_id:
            products=Prodcuts.get_products_by_category_id(category_id)
        else:
            products=Prodcuts.get_all_products()
        data={}
        data['products']=products
        data['categories']=categories
        print('you are ',request.session.get('email'))
        return render(request,'store/index.html',data)

    
    

