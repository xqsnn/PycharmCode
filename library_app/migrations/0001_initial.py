# Generated by Django 5.0.1 on 2024-01-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('book_author', models.CharField(max_length=20)),
                ('book_catalog', models.CharField(max_length=20)),
                ('time_into', models.DateField()),
            ],
        ),
    ]