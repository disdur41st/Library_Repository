"""Library_Database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import IndexView
from .views import addStudent, delStudent, editStudent
from .views import addSubjectClass, delSubjectClass, editSubjectClass
from .views import addValue, delValue, editValue

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', IndexView.as_view()),
	url(r'^addStudent/$', addStudent.as_view()),
	url(r'^delStudent/(?P<pk>\d+)/$', delStudent.as_view(), name = 'del_student'),
    url(r'^editStudent/(?P<pk>\d+)/$', editStudent.as_view(), name = 'edit_Student'),
    url(r'^addSubjectClass/$', addSubjectClass.as_view()),
    url(r'^delSubjectClass/(?P<pk>\d+)/$', delSubjectClass.as_view(), name = 'del_Subject_Class'),
    url(r'^editSubjectClass/(?P<pk>[0-9]+)/$', editSubjectClass.as_view(), name = 'edit_Subject_Class'),
    url(r'^addValue/$', addValue.as_view()),
    url(r'^delValue/(?P<pk>\d+)/$', delValue.as_view(), name = 'del_value'),
    url(r'^editValue/(?P<pk>\d+)/$', editValue.as_view(), name = 'edit_value'),
]
