from django.urls import path
from .views import *
urlpatterns = [
    path('friends', show_friends),
    path('products', show_products),
    path('product-details/<id>',product_details, name='product-detail'),
    path('add-product',add_product, name='add-product'),
    path('singup',user_creation_form, name='singup')
]