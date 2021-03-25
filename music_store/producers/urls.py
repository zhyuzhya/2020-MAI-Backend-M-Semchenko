from django.urls import path, re_path, include
from .views import *

# Create your views here.

urlpatterns = [
    re_path('(\d+)/', producer_view),
    re_path('add/(\w+)/', producer_add),
    re_path('search/(\w+)/', producer_search),
    path('', producers_view),

]
