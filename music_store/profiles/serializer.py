from rest_framework import serializers

class ProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
