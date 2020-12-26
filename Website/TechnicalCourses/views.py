from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Allcourses


def Courses(request):
    ac= Allcourses.objects.all()
    template=loader.get_template("/TechnicalCourses/Courses.html")
    context={
         'ac':ac,
    }

    return HttpResponse(template.render(context,request))

# Create your views here.
def detail(request, course_id):
    return HttpResponse('<h2> These are the course details for course id:' + str(course_id)+ '</h2>')
