import os
import csv

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from client.models import Client


class Command(BaseCommand):
    help = 'Import clients'

    def get_current_app_path(self):
        return apps.get_app_config('client').path

    def get_csv_file(self, filename):
        app_path = self.get_current_app_path()
        file_path = os.path.join(
            app_path, "management",
            "commands", filename)
        return file_path

    def handle(self, *args, **kwargs):
        filename = "clients.csv"
        file_path = self.get_csv_file(filename)
        try:
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                total_clients = 0
                for row in csv_reader:
                    words = [word.strip() for word in row]
                    total_clients += 1
                    client = Client(
                        name=words[0],
                        age=words[1],
                        city=words[2]
                    )
                    client.save()
                print(""" Parabéns você acabou de cadastrar %s clientes novos!!!""" % total_clients)
        except FileNotFoundError:
            raise CommandError("O arquivo {} não foi encontrado :(".format(
                    file_path))
