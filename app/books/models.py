from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()


# class Author(models.Model):
#     first_name = models.CharField(max_length=128)
#     last_name = models.CharField(max_length=128)
#     country = models.CharField(max_length=128)
#     gender = models.CharField(max_length=6)
#     native_language = models.CharField(max_length=128)
#     date_of_birth = models.PositiveSmallIntegerField()
#     date_of_death = models.PositiveSmallIntegerField()
