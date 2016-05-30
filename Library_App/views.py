from django.shortcuts import render
from Library_App.models import LibraryEmployee
from Library_App.models import Reader
from Library_App.models import Operation
from Library_App.models import BookCopy
from Library_App.models import Author
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    #Activity.objects.all().delete()
    #Participant.objects.all().delete()
    #Place.objects.all().delete()
    #Activity.objects.create (id = 1, name = "Подъем", time = "08:00", date = "2014-10-12")
    #Activity.objects.create (id = 2, name = "Сходить на фильм", time = "16:00", date = "2015-10-12")
    #Activity.objects.create (id = 3, name = "Подъем", time = "08:00", date = "2015-09-12")
    #Place.objects.create (id = 1, name = "Кинотеатр Киномакс", city = "Томск", street = "Розы Люксембург", house = "73")
    #Place.objects.create (id = 2, name = "Администрация г. Томска", city = "Томск", street = "Ленина", house = "73")
    #Place.objects.create (id = 3, name = "Родильный ном №1", city = "Томск", street = "Ленина", house = "65")
    #Participant.objects.create (id = 1, first_name = "Павел", second_name = "Павлов", third_name = "Павлович", sex = "М", phone = "89131162233")
    #Participant.objects.create (id = 2, first_name = "Анастасия", second_name = "Павлова", third_name = "Олеговна", sex = "Ж", phone = "89132162233")
    #Participant.objects.create (id = 3, first_name = "Илья", second_name = "Ильин", third_name = "Ильич", sex = "М", phone = "+73332221199")
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'employees_list' : LibraryEmployee.objects.all(),   
                'readers_list' : Reader.objects.all(),
                'operations_list' : Operation.objects.all(),
                'book_copies_list' : BookCopy.objects.all(),
                'authors_list' : Author.objects.all(),
            }
        )
        return context
