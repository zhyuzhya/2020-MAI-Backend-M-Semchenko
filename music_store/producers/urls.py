from django.urls import path, re_path, include
from .views import *

# Create your views here.

urlpatterns = [
    re_path('(\d+)/', ProducerView.as_view()),
    re_path('add/(\w+)/', ProducerAdd.as_view()),
    re_path('search/(\w+)/', ProducerSearch.as_view()),
    path('', ProducersView.as_view()),

]
