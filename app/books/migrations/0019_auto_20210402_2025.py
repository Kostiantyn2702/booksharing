# Generated by Django 3.1.5 on 2021-04-02 20:25

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20210402_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coverage',
            field=models.FileField(default='/coverage/default/image.jpg', null='/coverage/default/image.jpg', upload_to=books.models.book_upload_coverage),
        ),
    ]
