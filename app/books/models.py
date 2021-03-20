from django.db import models
from books import model_choices as mch


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    gender = models.CharField(max_length=6)
    native_language = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()
    category = models.ForeignKey('books.Category', on_delete=models.CASCADE,
                                 null=True, default=None)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE,
                             null=True, default=None)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               null=True, default=None)

    def __str__(self):
        return f"{self.id} {self.title} {self.author_id}"


class RequestBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recipient = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=mch.REQUEST_STATUSES)


class Log(models.Model):
    path = models.CharField(max_length=128)
    method = models.CharField(max_length=128)
    time = models.PositiveIntegerField()


class Category(models.Model):
    name = models.CharField(max_length=128)
