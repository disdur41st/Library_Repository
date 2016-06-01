from django.shortcuts import render
from Library_App.models import LibraryEmployee
from Library_App.models import Reader
from Library_App.models import Operation
from Library_App.models import BookCopy
from Library_App.models import Author
from Library_App.forms import *
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'employees_list' : LibraryEmployee.objects.all(),   
                'readers_list' : Reader.objects.all(),
                'operations_list' : Operation.objects.all(),
                'book_copies_list' : BookCopy.objects.all(),
                'authors_list' : Author.objects.all()
            }
        )
        return context

# Добавление	
class addLibraryEmployee(CreateView):
	form_class = LibraryEmployeeForm
	model = LibraryEmployee
	template_name = 'lab3.html'
	success_url = "/"
	
class addReader(CreateView):
	form_class = ReaderForm
	model = Reader
	template_name = 'lab3.html'
	success_url = "/"
	
class addOperation(CreateView):
	form_class = OperationForm
	model = Operation
	template_name = 'lab3.html'
	success_url = "/"

class addBookCopy(CreateView):
	form_class = BookCopyForm
	model = BookCopy
	template_name = 'lab3.html'
	success_url = "/"

class addAuthor(CreateView):
	form_class = AuthorForm
	model = Author
	template_name = 'lab3.html'
	success_url = "/"


# Удаление
class delLibraryEmployee(DeleteView):
	form_class = LibraryEmployeeForm
	model = LibraryEmployee
	template_name = 'lab3.html'
	success_url = "/"
	
class delReader(DeleteView):
	form_class = ReaderForm
	model = Reader
	template_name = 'lab3.html'
	success_url = "/"
	
class delOperation(DeleteView):
	form_class = OperationForm
	model = Operation
	template_name = 'lab3.html'
	success_url = "/"

class delBookCopy(DeleteView):
	form_class = BookCopyForm
	model = BookCopy
	template_name = 'lab3.html'
	success_url = "/"

class delAuthor(DeleteView):
	form_class = AuthorForm
	model = Author
	template_name = 'lab3.html'
	success_url = "/"


# Редактирование	
class editLibraryEmployee(UpdateView):
	form_class = LibraryEmployeeForm
	model = LibraryEmployee
	template_name = 'lab3.html'
	success_url = "/"
	
class editReader(UpdateView):
	form_class = ReaderForm
	model = Reader
	template_name = 'lab3.html'
	success_url = "/"
	
class editOperation(UpdateView):
	form_class = OperationForm
	model = Operation
	template_name = 'lab3.html'
	success_url = "/"

class editBookCopy(UpdateView):
	form_class = BookCopyForm
	model = BookCopy
	template_name = 'lab3.html'
	success_url = "/"

class editAuthor(UpdateView):
	form_class = AuthorForm
	model = Author
	template_name = 'lab3.html'
	success_url = "/"
