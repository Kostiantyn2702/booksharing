from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from books.api.filters import BookFilter
from books.api.serializers import BookSerializer
from books.models import Book


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
