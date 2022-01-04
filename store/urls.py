from django.urls import path

from store.models.orders import Orders
from .views import login,signup,home,cart,checkout,order
#use middlewares
from store.middlewares.auth import auth_middlewares

urlpatterns = [
    path('',home.Index.as_view(),name='homepage'),
    path('signup/',signup.Signup.as_view(),name='signup'),
    path('cart/',cart.Cart.as_view(),name='cart'),
    path('login/',login.Login.as_view(),name='login'),
    path('logout/',login.logout,name='logout'),
    path('checkout/',checkout.CheckoutView.as_view(),name='checkout'),
    path('orders/',auth_middlewares(order.OrderView.as_view()),name='orders'),
]
