from rest_framework import serializers

class ProducerSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
