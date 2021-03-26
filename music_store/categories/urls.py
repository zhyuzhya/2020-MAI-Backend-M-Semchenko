from django.urls import path, re_path, include
from .views import *

# Create your views here.

urlpatterns = [
    re_path('(\d+)/', CategoryView.as_view()),
    re_path('add/(\w+)/', CategoryAdd.as_view()),
    re_path('search/(\w+)/', CategorySearch.as_view()),
    path('', CategoriesView.as_view()),

]
