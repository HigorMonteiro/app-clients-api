from rest_framework import generics
from .serializers import ClientSerializer
from .models import Client


class CreateView(generics.ListCreateAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save()
