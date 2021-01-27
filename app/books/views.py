from django.shortcuts import render
# from django.http import HttpResponseRedirect
from books.models import Book
from books.forms import BookForm


def book_list(request):
    context = {
        "book_list": Book.objects.all(),
    }

    return render(request, "books_list.html", context=context)
