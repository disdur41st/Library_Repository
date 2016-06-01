from django.contrib import admin
from Library_App.models import LibraryEmployee
from Library_App.models import Reader
from Library_App.models import Operation
from Library_App.models import BookCopy
from Library_App.models import Author

admin.site.register([LibraryEmployee, Reader, Operation, BookCopy, Author])
# Register your models here.
