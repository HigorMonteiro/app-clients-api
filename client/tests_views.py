from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


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
