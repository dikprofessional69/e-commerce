from django.urls import path

from products_app.views import index, cart, checkout, cart_save

urlpatterns = [path('', index, name='index'),
               path('cart/', cart, name='cart'),
               path('cart-save/', cart_save, name='cart_save'),
               path('checkout/', checkout, name='checkout'),
]


