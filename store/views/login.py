from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views.generic.base import View #for save password in db with hashing
from store.models.customers import Customer
from django.views import View

class Login(View):
    #1-middelware
    return_Url=None
    def get(self,request):
        Login.return_Url=request.GET.get('return_url')
        return render(request,'store/login.html')

    def post(self,request):
        # POSTdATA=request.POST
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        print('customer ',customer)
        error_message=None
        if customer:
            flag = check_password(password,customer.password)
            print(flag)
            if flag:
                request.session['customer']=customer.id
                request.session['email']=customer.email
                if Login.return_Url: #2-middelware
                    return HttpResponseRedirect(Login.return_Url)
                else:
                    Login.return_Url=None
                    return redirect('homepage')
            else:
                error_message='Email or Password is invalid'
        else:
            error_message='Email or Password is invalid'
        print(email,password)
        return render(request,'store/login.html',{'error':error_message})

def logout(request):
    request.session.clear()
    return redirect('/login')
