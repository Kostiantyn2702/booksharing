# Generated by Django 3.1.5 on 2021-04-11 11:13

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20210402_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coverage',
            field=models.FileField(default=books.models.Book.coverage_url, null=True, upload_to=books.models.book_upload_coverage),
        ),
    ]
