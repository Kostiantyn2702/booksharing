from django.http import HttpResponseRedirect
from django.shortcuts import render
from books.models import Book
from books.forms import BookForm


def book_list(request):

    context = {
        'books_list': Book.objects.all(),
    }

    return render(request, 'books_list.html', context=context)


def book_create(request):
    form_data = request.GET

    if form_data:
        form = BookForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/list/')
    else:
        form = BookForm()

    context = {
        'message': 'BOOK CREATE',
        'form': form,
    }
    return render(request, 'books_create.html', context=context)