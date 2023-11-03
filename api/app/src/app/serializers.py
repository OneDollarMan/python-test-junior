from rest_framework import serializers
from src.app.models import UserEventModel


class UserEventSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose')
    date_created = serializers.DateTimeField()
    user_ip = serializers.CharField(max_length=200)

