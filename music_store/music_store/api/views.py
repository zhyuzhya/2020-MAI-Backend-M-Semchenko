from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def profile_view(request, profile_id):
    return JsonResponse({"profile_id": profile_id})

def category_view(request, category_id):
    return JsonResponse({"category_id": category_id})

def product_view(request, product_id):
    return JsonResponse({"product_id": product_id})

def categories_view(request):
    return JsonResponse({"category_id": 0})

def products_view(request):
    return JsonResponse({"product_id": 0})
