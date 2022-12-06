from django.urls import path
from .views import Home, Cart, Store, Checkout

urlpatterns = [
    path('', Home, name='home' ),
    path('store/store/', Store, name='store'),
    path('store/cart/', Cart, name='cart'),
    path('store/checkout/', Checkout, name='checkout'),
]
