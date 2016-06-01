from django.shortcuts import render
from Library_App.models import LibraryEmployee
from Library_App.models import Reader
from Library_App.models import Operation
from Library_App.models import BookCopy
from Library_App.models import Author
from django.views.generic.base import TemplateView

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
