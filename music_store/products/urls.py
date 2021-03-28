from django.urls import path, re_path, include
from django.conf.urls import url
from .views import *

# Create your views here.

urlpatterns = [
    re_path('(\d+)/', ProductView.as_view()),
    re_path('add/(\w+)/', ProductAdd.as_view()),
    re_path('search/(\w+)/', ProductSearch.as_view()),
    path('add/', ProductAdd.as_view(), name="product_add"),
    path('', ProductsView.as_view(), name="all_products"),

]
