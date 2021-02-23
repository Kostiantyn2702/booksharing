from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Author
from books.forms import AuthorForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView


class Index(TemplateView):
    template_name = "index.html"


class BookList(ListView):
    queryset = Book.objects.all()


class BookCreate(CreateView):
    model = Book
    success_url = reverse_lazy("books:books-list")
    # form_class = BookForm
    fields = (
            'author',
            'title',
            'publish_year',
            'review',
            'condition',
        )


class BookUpdate(UpdateView):
    model = Book
    success_url = reverse_lazy("books:books-list")
    fields = (
            'author',
            'title',
            'publish_year',
            'review',
            'condition',
        )


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy("books:books-list")


def author_list(request):

    context = {
        'author_list': Author.objects.all(),
    }

    return render(request, 'author_list.html', context=context)


def author_create(request):
    form_data = request.POST

    if request.method == 'POST':
        form = AuthorForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    elif request.method == 'GET':
        form = AuthorForm()

    context = {
        'message': 'AUTHOR CREATE',
        'form': form,
    }
    return render(request, 'author_create.html', context=context)


def author_update(request, pk):
    instance = get_object_or_404(Author, pk=pk)

    form_data = request.POST
    if request.method == 'POST':
        form = AuthorForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    elif request.method == 'GET':
        form = AuthorForm(instance=instance)

    context = {
        'message': 'AUTHOR UPDATE',
        'form': form,
    }
    return render(request, 'author_create.html', context=context)


def author_delete(request, pk):
    instance = get_object_or_404(Author, pk=pk)
    instance.delete()
    return redirect('author-list')


# def login_view(request):
#     form_data = request.POST
#     form_class = LoginForm
#
#     if request.method == 'POST':
#         form = form_class(form_data)
#         if form.is_valid():
#             user = authenticate(**form.cleaned_data)
#             if user:
#                 login(request, user)
#             return redirect('books-list')
#     elif request.method == 'GET':
#         form = form_class()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'login.html', context=context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect("login")