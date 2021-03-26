from rest_framework import serializers
from .views import Product

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
