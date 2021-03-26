from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from products.models import Product, Producer
from .serializer import ProducerSerializer

# Поиск поставщика и его продуктов по его ID
class ProducerView(APIView):
    def get(self, request, producer_id):
        try:
            producer = Producer.objects.get(id=producer_id)
            serializer = ProducerSerializer(producer)
            if producer.name:
                return Response({ f"Producer #{producer_id}": serializer.data})
        except Producer.DoesNotExist:
            return Response({"No such producer": producer_id})

# Ссылка на всех поставщиков
class ProducersView(APIView):
    def get(self, request):
        producers = Producer.objects.all()
        serializer = ProducerSerializer(producers, many=True)
        return Response({"All producers": serializer.data})

# Добавить поставщика
class ProducerAdd(APIView):
    def post(self, request, new_producer):
        form = ProducerForm(request.POST)
        if form.is_valid():
            producer = form.save()
            return Response({'error': None, 'result': 'success'})

# Поиск поставщика по подстроке его имени
class ProducerSearch(APIView):
    def get(self, request, producer_name):
        try:
            producers = Producer.objects.all().filter(name__contains=producer_name)
            serializer = ProducerSerializer(producers, many=True)
            return Response({"Found producers": serializer.data})
        except Exception as e:
            return Response({"Error": str(e)})
