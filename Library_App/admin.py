from django.contrib import admin
from Library_App.models import LibraryEmployee
from Library_App.models import Reader
from Library_App.models import Operation
from Library_App.models import BookCopy
from Library_App.models import Author
from Library_App.models import SubjectClass
from Library_App.models import Value

admin.site.register(LibraryEmployee)
admin.site.register(Reader)
admin.site.register(Operation)
admin.site.register(BookCopy)
admin.site.register(Author)
