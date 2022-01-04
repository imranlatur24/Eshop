from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View #for save password in db with hashing
from store.models.customers import Customer
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request,'store/signup.html')

    def post(self,request):
        POST_DATA=request.POST
        fn=POST_DATA.get('firstname')
        ln=POST_DATA.get('lastname')
        ph=POST_DATA.get('phone')
        em=POST_DATA.get('email')
        ps=POST_DATA.get('password')
        print(fn,ln,ph,em,ps)

        value={
                'fn':fn,
                'ln':ln,
                'ph':ph,
                'em':em,
                'ps':ps
                # 'ps':ps not required each time it will be blank
            }
        #validation
        error_messages=None
        customer=Customer(
                first_name=fn,
                last_name=ln,
                phone=ph,
                email=em,
                password=ps
            )
        #validation function here
        error_messages=self.validation(customer)

        #saving when all validation is correct
        if not error_messages:
            #hashing for password field ---------------------------------------------------
            customer.password=make_password(customer.password)
            customer.save()
            return redirect('homepage')
        else:
            data={
                    'error':error_messages, #handling error messages
                    'values':value          #fields value does not clean on validation page 
                }
            return render(request,'store/signup.html',data)

    def validation(self,customer):
        error_messages=None
        if (not customer.first_name):
            error_messages='First Name Required'
        elif len(customer.first_name)<4:
            error_messages='First Name must be 4 char long'
        elif not customer.last_name:
            error_messages='Last Name Required'
        elif len(customer.last_name)<4:
            error_messages='Last Name must be 4 char long'
        elif not customer.phone:
            error_messages='Mobile No. Required'
        elif not customer.email:
            error_messages='Email Required'
        elif not customer.password:
            error_messages='Password Required'
        elif len(customer.phone)<9:
            error_messages='Mobile No must be 10 numbers long'
        elif len(customer.password)<8:
            error_messages='Password must be 8 char long'
        elif len(customer.email)<5:
            error_messages='Email must be 5 char long'
        elif customer.isExist():
            error_messages='Email already with us please try another mail'
        return error_messages   

    
