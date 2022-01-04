#middleware use in order.py file if user exist then only access order page otherwise goint to login page by 
#middleware use in urls.py
#check by without login go to http://127.0.0.1:8000/orders/ hit enter you will redirect on Login page.
from django.shortcuts import redirect


def auth_middlewares(get_response):
    def middleware(request):
        # print('middleware')
        #1-returnUrl mainly used for when user pass order url in searchbar http://127.0.0.1:8000/orders/ 
        #2-withou login then middleware goes to login page 
        #3-after login user again go to same order page instead of homepage 
        #4-main purpose below for returnUrl is same
        print(request.session.get('customer')) # when user not available
        returnUrl=request.META['PATH_INFO']
        print(request.META['PATH_INFO'])

        if not request.session.get('customer'):
            return redirect(f'/login/?return_url={returnUrl}')

        response = get_response(request)

        return response

    return middleware