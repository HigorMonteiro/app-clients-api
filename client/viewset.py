from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import ClientSerializer
from .models import Client


@csrf_exempt
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        clients_serializer = ClientSerializer(clients, many=True)
        return JsonResponse(clients_serializer.data, safe=False)

    elif request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse(
                client_serializer.data,
                status=status.HTTP_201_CREATED
                )
        return JsonResponse(
            client_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    elif request.method == 'DELETE':
        Client.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        client_serializer = ClientSerializer(client)
        return JsonResponse(client_serializer.data)

    elif request.method == 'PUT':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(client, data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse(client_serializer.data)
        return JsonResponse(
            client_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    elif request.method == 'DELETE':
        client.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
