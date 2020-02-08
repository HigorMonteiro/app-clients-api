from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from .models import Client


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):

        self.client = APIClient()
        self.client_data = {
            'name': 'Higor Vinicius',
            'age': 26,
            'city': 'Altos-PI'
        }
        self.response = self.client.post(
            reverse('create'),
            self.client_data,
            format="json")

    def test_api_can_create_a_client(self):
        """Test the api has client creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_client(self):
        """Test the api can get a given client."""
        client = Client.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': client.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, client)

    def test_api_can_update_client(self):
        """Test the api can update a given client."""
        client = Client.objects.get()
        change_client = {
            'name': 'Higor Vinicius',
            'age': 26,
            'city': 'Altos-PI'
        }
        res = self.client.put(
            reverse('details', kwargs={'pk': client.id}),
            change_client, format='json'
        )
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_client(self):
        """Test the api can delete a given client."""
        client = Client.objects.get()

        res = self.client.delete(
            reverse('details', kwargs={'pk': client.id}),
            format='json',
            follow=True
        )
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)

