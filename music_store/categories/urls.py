from django.urls import path, re_path, include
from .views import *

# Create your views here.

urlpatterns = [
    re_path('(\d+)/', category_view),
    re_path('add/(\w+)/', category_add),
    re_path('search/(\w+)/', category_search),
    path('', categories_view),

]
