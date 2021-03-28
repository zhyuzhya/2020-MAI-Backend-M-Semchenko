from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
    current_price = serializers.FloatField()
    absolute_url = serializers.CharField(source="get_absolute_url", read_only=True)
    picture = serializers.ImageField()
