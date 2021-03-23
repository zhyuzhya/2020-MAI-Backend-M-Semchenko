from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def profile_view(request, profile_id):
    if request.method == 'GET' or request.method == 'POST':
        return JsonResponse({"profile_id": profile_id})

def category_view(request, category_id):
    if request.method == 'GET' or request.method == 'POST':
        return JsonResponse({"category_id": category_id})

def product_view(request, product_id):
    if request.method == 'GET' or request.method == 'POST':
        return JsonResponse({"product_id": product_id})

def categories_view(request):
    if request.method == 'GET' or request.method == 'POST':
        return JsonResponse({"category_id": 0})

def products_view(request):
    if request.method == 'GET' or request.method == 'POST':
        return JsonResponse({"product_id": 0})
