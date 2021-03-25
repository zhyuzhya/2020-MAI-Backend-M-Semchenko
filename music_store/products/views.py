from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import Product, Category

# Поиск продукта по его ID
def product_view(request, product_id):
    if request.method == 'GET' or request.method == 'POST':
        try:
            product = Product.objects.get(id=product_id)
            if product.name:
                return JsonResponse({ f"Product #{product_id}": product.name,
                    "category": product.category.name})
        except Product.DoesNotExist:
            return JsonResponse({"No such product": product_id})

# Ссылка на все продукты
def products_view(request):
        products = Product.objects.all()
        s = []
        for p in products:
            s.append(f"{p.name}, id = {p.id}")
        return JsonResponse({"All products": s})

# Добавление нового продукта
def product_add(request, product_name):
    if request.method == 'GET' or request.method == 'POST':
        try:
            unknown_category = Category.objects.get(name='Unknown')
            Product(name=product_name, current_price=0.0, category=unknown_category).save()
        except Exception as e:
            return JsonResponse({"Can't save product": str(e)})
        return JsonResponse({"Product created": product_name})

# Поиск продукта по подстроке
def product_search(request, product_name):
    if request.method == 'GET' or request.method == 'POST':
        try:
            products = Product.objects.all().filter(name__contains=product_name)
            s = []
            for p in products:
                s.append(f"{p.name}, id = {p.id}")
            if len(s) > 0:
                return JsonResponse({"Found products": s})
            else:
                return JsonResponse({"No such product": product_name})
        except Exception as e:
            return JsonResponse({"Error": str(e)})
