from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    gender = models.CharField(max_length=6)
    native_language = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()
    # category = models.ForeignKey('books.Category', on_delete=models.CASCADE,
    #                              null=True, default=None)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE,
                             null=True, default=None)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               null=True, default=None)


class Log(models.Model):
    path = models.CharField(max_length=128)
    method = models.CharField(max_length=128)
    time = models.PositiveIntegerField()


# class Category(models.Model):
#     name = models.CharField(max_length=128)
