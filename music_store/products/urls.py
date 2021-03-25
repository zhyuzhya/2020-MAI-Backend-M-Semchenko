from django.urls import path, re_path, include
from .views import *

# Create your views here.

urlpatterns = [
    re_path('(\d+)/', product_view),
    re_path('add/(\w+)/', product_add),
    re_path('search/(\w+)/', product_search),
    path('', products_view),

]
