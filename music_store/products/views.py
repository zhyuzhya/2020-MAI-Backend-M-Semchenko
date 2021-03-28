from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializer import ProductSerializer
from .forms import ProductForm

# Поиск продукта по его ID
class ProductView(APIView):
    def get(self, request, product_id):
        renderer_classes = [TemplateHTMLRenderer]
        tmp = 'products/product.html'
        product = Product.objects.all().filter(id=product_id)
        serializer = ProductSerializer(product, many=True)
        return TemplateResponse(request, tmp, {'products': serializer.data})
    def post(self, request):
        product = Product.objects.get(id=product_id)
        product.delete()


# Ссылка на все продукты
class ProductsView(APIView):
    def get(self, request):
        renderer_classes = [TemplateHTMLRenderer]
        tmp = 'products/index.html'
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return TemplateResponse(request, tmp, {'products': serializer.data})

# Добавление нового продукта
class ProductAdd(APIView):
    def get(self, request):
        form = ProductForm()
        return TemplateResponse(request, 'products/add_product.html', {'form': form})
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
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
