from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from products.models import Product, Producer

# Поиск поставщика и его продуктов по его ID
def producer_view(request, producer_id):
    if request.method == 'GET' or request.method == 'POST':
        try:
            cur_producer = Producer.objects.get(id=producer_id)
            try:
                products = Product.objects.all().filter(producer=cur_producer)
                s = []
                for p in products:
                    s.append(f"{p.name}, id = {p.id}")
                if len(s) > 0:
                    return JsonResponse({f"Found products of this producer ({cur_producer.name})": s})
                else:
                    return JsonResponse({f"No products of this producer": cur_producer.name})
            except Product.DoesNotExist:
                return JsonResponse({f"No products of this producer": cur_producer.name})
        except Producer.DoesNotExist:
            return JsonResponse({"No such producer": producer_id})

# Ссылка на всех поставщиков
def producers_view(request):
        producers = Producer.objects.all()
        s = []
        for p in producers:
            s.append(f"{p.name}, id = {p.id}")
        return JsonResponse({"All producers": s})

# Добавить поставщика
def producer_add(request, producer_name):
    if request.method == 'GET' or request.method == 'POST':
        try:
            Producer(name=producer_name).save()
        except Exception as e:
            return JsonResponse({"Can't save producer": str(e)})
        return JsonResponse({"Producer created": producer_name})

# Поиск поставщика по подстроке его имени
def producer_search(request, producer_name):
    if request.method == 'GET' or request.method == 'POST':
        try:
            producers = Producer.objects.all().filter(name__contains=producer_name)
            s = []
            for p in producers:
                s.append(f"{p.name}, id = {p.id}")
            if len(s) > 0:
                return JsonResponse({"Found producers": s})
            else:
                return JsonResponse({"No such producer": producer_name})
        except Exception as e:
            return JsonResponse({"Error": str(e)})
