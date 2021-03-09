from books.forms import BookForm
from books.models import Book, Author
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class FormUserKwargMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class Index(TemplateView):
    template_name = "index.html"


class BookList(ListView):
    queryset = Book.objects.all().select_related('author')


class MyBooksList(LoginRequiredMixin, ListView):
    queryset = Book.objects.all().select_related('author')
    template_name = 'books/my_books.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class BookCreate(FormUserKwargMixin, LoginRequiredMixin, CreateView):
    model = Book
    success_url = reverse_lazy("books:list")
    form_class = BookForm


class BookUpdate(FormUserKwargMixin, LoginRequiredMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm


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
