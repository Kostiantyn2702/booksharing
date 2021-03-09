from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import datetime

from books.models import Book, Author


class Command(BaseCommand):
    help = 'Generate Random Data'  # noqa

    '''
    class Book(models.Model):  # DO NOT TOUCH ME
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()
    '''

    def add_arguments(self, parser):
        parser.add_argument("data", nargs="?", type=int)

    def handle(self, *args, **options):
        fake = Faker()

        argument = options["data"]
        data_range = 1 if not argument else argument

        # create authors
        authors = []
        for _ in range(data_range):
            author_name = fake.name()

            authors.append(Author(
                first_name=author_name.split(" ")[0],
                last_name=author_name.split(" ")[1],
            ))

        Author.objects.bulk_create(authors)

        # create books with random author
        books_list = []

        for _ in range(data_range):
            author = Author.objects.order_by('?').last()
            title = fake.word().capitalize()
            publish_year = random.randint(0, datetime.now().year)
            review = fake.text()
            condition = random.randint(1, 5)

            books_list.append(Book(
                author=author,
                title=title,
                publish_year=publish_year,
                review=review,
                condition=condition,
            ))

        Book.objects.bulk_create(books_list)
