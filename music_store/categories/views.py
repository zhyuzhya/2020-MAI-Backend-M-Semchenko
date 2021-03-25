from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from products.models import Product, Category

# Поиск категории и её продуктов по её ID
def category_view(request, category_id):
    if request.method == 'GET' or request.method == 'POST':
        try:
            cur_category = Category.objects.get(id=category_id)
            try:
                products = Product.objects.all().filter(category=cur_category)
                s = []
                for p in products:
                    s.append(f"{p.name}, id = {p.id}")
                if len(s) > 0:
                    return JsonResponse({f"Found products of this category ({cur_category.name})": s})
                else:
                    return JsonResponse({f"No products of this category": cur_category.name})
            except Product.DoesNotExist:
                return JsonResponse({f"No products of this category": cur_category.name})
        except Category.DoesNotExist:
            return JsonResponse({"No such category": category_id})

# Ссылка на все категории
def categories_view(request):
        categories = Category.objects.all()
        s = []
        for p in categories:
            s.append(f"{p.name}, id = {p.id}")
        return JsonResponse({"All categories": s})

# Добавить категорию
def category_add(request, category_name):
    if request.method == 'GET' or request.method == 'POST':
        try:
            Category(name=category_name).save()
        except Exception as e:
            return JsonResponse({"Can't save category": str(e)})
        return JsonResponse({"Category created": category_name})

# Поиск категории по подстроке её имени
def category_search(request, category_name):
    if request.method == 'GET' or request.method == 'POST':
        try:
            categories = Category.objects.all().filter(name__contains=category_name)
            s = []
            for p in categories:
                s.append(f"{p.name}, id = {p.id}")
            if len(s) > 0:
                return JsonResponse({"Found categories": s})
            else:
                return JsonResponse({"No such category": category_name})
        except Exception as e:
            return JsonResponse({"Error": str(e)})
