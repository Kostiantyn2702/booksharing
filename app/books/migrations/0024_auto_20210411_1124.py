# Generated by Django 3.1.5 on 2021-04-11 11:24

import books.models
from django.db import migrations, models
import django.templatetags.static


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_auto_20210411_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coverage',
            field=models.FileField(default=django.templatetags.static.static, null=True, upload_to=books.models.book_upload_coverage),
        ),
    ]
