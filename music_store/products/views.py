from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category
from .serializer import ProductSerializer
from .forms import ProductForm

# Поиск продукта по его ID
class ProductView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product)
            if product.name:
                return Response({ f"Product #{product_id}": serializer.data})
        except Product.DoesNotExist:
            return Response({"No such product": product_id})

# Ссылка на все продукты
class ProductsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"All products": serializer.data})

# Добавление нового продукта
class ProductAdd(APIView):
    def post(self, request, new_product):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return Response({'error': None, 'result': 'success'})

# Поиск продукта по подстроке
class ProductSearch(APIView):
    def get(self, request, product_name):
        try:
            products = Product.objects.all().filter(name__contains=product_name)
            serializer = ProductSerializer(products, many=True)
            return Response({"Found products": serializer.data})
        except Exception as e:
            return Response({"Error": str(e)})
