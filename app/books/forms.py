from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'author',
            'title',
            'publish_year',
            'review',
            'condition',
        )


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = (
#             'first_name',
#             'last_name',
#             'country',
#             'gender',
#             'native_language',
#             'date_of_birth',
#             'date_of_death',
#         )
