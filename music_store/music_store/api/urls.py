"""music_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from music_store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('profile/(\d+)/', profile_view),
    path('products/', products_view),
    re_path('product/(\d+)/', product_view),
    path('categories/', categories_view),
    re_path('category/(\d+)/', category_view),
]
