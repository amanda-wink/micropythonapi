from django.core.management.base import BaseCommand, CommandError
from ...models import Book
import csv
import os

class Command(BaseCommand):
    help = 'Loads bestseller books'

    def handle(self, *args, **kwargs):
        topdir = os.path.dirname('micropythonapi')
        with open(str(topdir) + 'bestsellers-with-categories.csv') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                _, created = Book.objects.get_or_create(
                    name = row[0],
                    author = row[1],
                    rating = row[2],
                    reviews = row[3],
                    price = row[4],
                    year = row[5],
                    genre = row[6]
                )