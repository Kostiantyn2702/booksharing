from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'publish_year',
            'review',
            'condition',
        )

    # def create(self):
    # def update(self):
    # def validate(  # -> clean
    # def validate(self, attrs: dict):
    #     attrs['title'] = attrs['title'].lower()
    #     return attrs
    # def validate_title(  # -> clean
