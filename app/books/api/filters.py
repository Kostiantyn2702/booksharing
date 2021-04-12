from django_filters import rest_framework as filters

from books.models import Book, Author, Category


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains', 'exact'],  # filter(title='awda'), filter(title__exact='awda')
            'condition': ['gt', 'gte', 'lt', 'lte'],
        }


class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author
        fields = {
            'country': ['icontains', 'exact'],  # filter(title='awda'), filter(title__exact='awda')
        }


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'name': ['icontains', 'exact'],  # filter(title='awda'), filter(title__exact='awda')
        }
