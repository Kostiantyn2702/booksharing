from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book
from books.forms import BookForm


def index(request):
    return render(request, 'index.html')


def book_list(request):

    context = {
        'books_list': Book.objects.all(),
    }

    return render(request, 'books_list.html', context=context)


def book_create(request):
    form_data = request.POST

    if request.method == 'POST':
        form = BookForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('books-list')
    elif request.method == 'GET':
        form = BookForm()

    context = {
        'message': 'BOOK CREATE',
        'form': form,
    }
    return render(request, 'books_create.html', context=context)


def book_update(request, pk):

    # try:
    #     book_obj = Book.objects.get(pk=pk)
    # except Book.DoesNotExist:
    #     raise Http404(f'Object with id: {pk} not found')
    instance = get_object_or_404(Book, pk=pk)

    form_data = request.POST
    if request.method == 'POST':
        form = BookForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('books-list')
    elif request.method == 'GET':
        form = BookForm(instance=instance)

    context = {
        'message': 'BOOK UPDATE',
        'form': form,
    }
    return render(request, 'books_create.html', context=context)


def book_delete(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    instance.delete()
    return redirect('books-list')


# GET
'''
Request URL: http://127.0.0.1:8000/books/create/?name=Dima&age=29
Request Method: GET
Remote Address: 127.0.0.1:8000
Referrer Policy: same-origin
'''


# POST
'''
Request URL: http://127.0.0.1:8000/books/create/
Request Method: POST
Remote Address: 127.0.0.1:8000
Referrer Policy: same-origin
name=Dima&age=29
'''


"""
C - create - POST
R - read - GET
U - update - PUT/PATCH
D - delete - DELETE
HEAD, OPTIONS
"""
