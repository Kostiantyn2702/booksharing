# Generated by Django 3.1.5 on 2021-04-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0026_auto_20210411_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]