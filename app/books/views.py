import csv
import xlwt
from books.utils import display
from books.forms import BookForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from books.models import Book, Author, RequestBook
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, \
    ListView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin


class FormUserKwargMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class Index(TemplateView):
    template_name = "index.html"


class BookList(ListView):
    queryset = Book.objects.all().select_related('author', 'category')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(user=self.request.user)


class MyBooksList(LoginRequiredMixin, ListView):
    queryset = Book.objects.all().select_related('author', 'category')
    template_name = 'books/my_books.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class MyRequestedBooks(LoginRequiredMixin, ListView):
    queryset = RequestBook.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(recipient=self.request.user)


class RequestedBooks(LoginRequiredMixin, ListView):
    queryset = RequestBook.objects.all()
    template_name = 'books/requested_book_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(book__user=self.request.user)


class BookCreate(FormUserKwargMixin, LoginRequiredMixin, CreateView):
    model = Book
    success_url = reverse_lazy("books:my-books")
    form_class = BookForm


class BookUpdate(FormUserKwargMixin, LoginRequiredMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("books:list")


class RequestBookCreate(LoginRequiredMixin, View):

    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        if not RequestBook.objects.filter(book=book, recipient=request.user).exists():
            RequestBook.objects.create(book=book, recipient=request.user, status=1)
        return redirect('books:list')


class RequestBookConfirm(LoginRequiredMixin, View):
    def get(self, request, request_id):
        request_obj = get_object_or_404(RequestBook, pk=request_id, status=10)  # TODO
        request_obj.status = 20
        request_obj.save(update_fields=('status', ))
        return redirect('books:requested-books')


class RequestBookReject(LoginRequiredMixin, View):
    def get(self, request, request_id):
        request_obj = get_object_or_404(RequestBook, pk=request_id, status=10)  # TODO
        request_obj.status = 30
        request_obj.save(update_fields=('status', ))
        return redirect('books:requested-books')


class DownloadCSVBookView(View):

    HEADERS = (
        'id',
        'title',
        'author.full_name',
        'author.get_full_name',
        'publish_year',
        'condition',
    )

    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)

        writer.writerow(self.HEADERS)

        for book in Book.objects.all().select_related('author').iterator():  # TODO add only method!
            writer.writerow([
                display(book, header)
                for header in self.HEADERS
            ])

        return response


class DownloadXlSXBookView(View):

    HEADERS = (
        'id',
        'author.full_name',
        'title',
        'publish_year',
        'review',
        'condition',
        'category',
    )

    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="book_list.xlsx"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("sheet1")

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num in range(len(self.HEADERS)):
            ws.write(row_num, col_num, self.HEADERS[col_num], font_style)

        # get your data, from database or from a text file...
        book_list = Book.objects.all().select_related('author').iterator()
        for book in book_list:
            row_num = row_num + 1
            ws.write(row_num, 0, book.id)
            ws.write(row_num, 1, book.author.full_name)
            ws.write(row_num, 2, book.title)
            ws.write(row_num, 3, book.publish_year)
            ws.write(row_num, 4, book.review)
            ws.write(row_num, 5, book.condition)
            ws.write(row_num, 6, book.category)

        wb.save(response)
        return response


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
