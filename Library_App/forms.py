from django.forms import ModelForm
from Library_App.models import *

class LibraryEmployeeForm(ModelForm):
	class Meta:
		model = LibraryEmployee
		fields = '__all__'
		
class ReaderForm(ModelForm):
	class Meta:
		model = Reader
		fields = '__all__'
		
class OperationForm(ModelForm):
	class Meta:
		model = Operation
		fields = '__all__'
class BookCopyForm(ModelForm):
	class Meta:
		model = BookCopy
		fields = '__all__'
class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = '__all__'
