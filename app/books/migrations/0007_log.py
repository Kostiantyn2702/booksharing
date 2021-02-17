# Generated by Django 3.1.5 on 2021-02-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210205_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=128)),
                ('method', models.CharField(max_length=128)),
                ('time', models.PositiveIntegerField()),
            ],
        ),
    ]
