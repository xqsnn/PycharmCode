from django.db import models

# Create your models here.
class admin_account(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class user_account(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
class library_book(models.Model):
    book_name = models.CharField(max_length=20)
    book_author = models.CharField(max_length=20)
    book_catalog = models.CharField(max_length=20)
    time_into = models.DateField()
    def __str__(self):
        # 在这里使用 strftime 来自定义日期的显示格式
        return self.time_into.strftime("%Y-%m-%d")
    number_of_books = models.IntegerField(max_length=8)
class library_book_catalog(models.Model):
    library_book_catalog=models.CharField(max_length=20)