from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into Json format."""

    class Meta:
        model = Client
        fields = ('id', 'name', 'age', 'city', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
