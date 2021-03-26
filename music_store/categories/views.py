from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product, Category
from .serializer import CategorySerializer

# Поиск категории и её продуктов по её ID
class CategoryView(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            serializer = CategorySerializer(category)
            return Response({"All categories": serializer.data})
        except Exception as e:
            return Response({"Error": str(e)})


# Ссылка на все категории
class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"All categories": serializer.data})

# Добавить категорию
class CategoryAdd(APIView):
    def post(self, request, category_name):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return Response({'error': None, 'result': 'success'})

# Поиск категории по подстроке её имени
class CategorySearch(APIView):
    def get(self, request, category_name):
        try:
            categories = Category.objects.all().filter(name__contains=category_name)
            serializer = CategorySerializer(categories, many=True)
            return Response({"Found categories": serializer.data})
        except Exception as e:
            return Response({"Error": str(e)})
