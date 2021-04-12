from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from books.api.filters import BookFilter, AuthorFilter, CategoryFilter
from books.api.serializers import BookSerializer, AuthorSerializer, CategorySerializer
from books.models import Book, Author, Category


# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookInstanceView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['condition', 'title']
    filterset_class = BookFilter
    # filterset_fields = ['condition']
    # filterset_fields = {
    #     'title': ['icontains', 'exact'], # filter(title='awda'), filter(title__exact='awda')
    #     'condition': ['gt', 'gte', 'lt', 'lte'],
    # }


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['full_name', 'country']
    filterset_class = AuthorFilter


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name']
    filterset_class = CategoryFilter
