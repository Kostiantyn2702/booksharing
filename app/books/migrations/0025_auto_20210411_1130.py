# Generated by Django 3.1.5 on 2021-04-11 11:30

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_auto_20210411_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coverage',
            field=models.FileField(default='media/coverage/default/image.jpg', null=True, upload_to=books.models.book_upload_coverage),
        ),
    ]
