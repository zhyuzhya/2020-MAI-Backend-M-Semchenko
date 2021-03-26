from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
