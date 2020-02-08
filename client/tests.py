from django.test import TestCase
from .models import Client


class ModelClientTestCase(TestCase):
    """This class defines the test suite for the client model."""

    def setUp(self):
        self.client_name = "Higor Vinicius"
        self.client_age = 26
        self.client_city = "Altos-PI"
        self.client = Client(
            name=self.client_name,
            age=self.client_age,
            city=self.client_city
        )

    def test_model_can_create_a_client(self):
        """Test the client model can create a Client."""

        old_count = Client.objects.count()
        self.client.save()

        new_count = Client.objects.count()
        self.assertNotEqual(old_count, new_count)


