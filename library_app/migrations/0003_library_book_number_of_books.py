# Generated by Django 5.0.1 on 2024-01-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_admin_account_user_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='library_book',
            name='number_of_books',
            field=models.IntegerField(default=5, max_length=8),
            preserve_default=False,
        ),
    ]