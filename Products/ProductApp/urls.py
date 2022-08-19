from django.conf.urls import *

from django.urls import path, include, re_path

from ProductApp.views import ProductView, PriceView

urlpatterns=[
    re_path(r'product/getAllProducts', ProductView.as_view(({'get': 'getAllProducts'}))),
    re_path(r'product/addProduct', ProductView.as_view(({'post': 'addProduct'}))),
    re_path(r'product/deleteProduct', ProductView.as_view(({'post': 'deleteProduct'}))),
    re_path(r'product/updateProduct', ProductView.as_view(({'post': 'updateProduct'}))),
    re_path(r'price/addPrice', PriceView.as_view(({'post': 'addPrice'}))),
    re_path(r'price/calculatePrice', PriceView.as_view(({'post': 'calculatePrice'}))),
]