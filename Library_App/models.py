from django.db import models
class LibraryEmployee(models.Model):
    name = models.CharField(max_length=30)
    patronymic_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    position = models.TextField(max_length=30)

class Reader(models.Model):
    library_card_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    patronymic_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    passport_number = models.IntegerField()
    date_of_birth = models.DateField()
    group_number = models.IntegerField()

class Operation(models.Model):
    book_copy = models.ForeignKey('BookCopy')
    library_card_number= models.ForeignKey('Reader')
    library_employee = models.ForeignKey('LibraryEmployee')
    operation_date = models.DateField()
    required_return_date = models.DateField()
    operation_type = models.CharField(max_length=15)

class BookCopy(models.Model):
   # author = models.ForeignKey('Author', on_delete=models.SET_DEFAULT('no'))
    name = models.CharField(max_length=30)
    year_of_publication = models.IntegerField()

class Author(models.Model):
    name = models.CharField(max_length=30)
    patronymic_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
