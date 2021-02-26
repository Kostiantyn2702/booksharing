from books.models import Book, Author
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(TemplateView):
    template_name = "index.html"


class BookList(ListView):
    queryset = Book.objects.all()


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    success_url = reverse_lazy("books:list")
    # form_class = BookForm
    fields = (
            'author',
            'title',
            'publish_year',
            'review',
            'condition',
        )


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    success_url = reverse_lazy("books:list")
    fields = (
            'author',
            'title',
            'publish_year',
            'review',
            'condition',
        )


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("books:list")


class AuthorList(ListView):
    queryset = Author.objects.all()


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    success_url = reverse_lazy("books:author-list")
    fields = (
        'first_name',
        'last_name',
        'country',
        'gender',
        'native_language',
        'date_of_birth',
        'date_of_death',
    )


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    success_url = reverse_lazy("books:author-list")
    fields = (
        'first_name',
        'last_name',
        'country',
        'gender',
        'native_language',
        'date_of_birth',
        'date_of_death',
    )


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy("books:author-list")
