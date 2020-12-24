from django.shortcuts import render
from django.http import HttpResponse

def Courses(request):
    return HttpResponse('<h1> This is my Home Page</h1>')

# Create your views here.
def detail(request, course_id):
    return HttpResponse('<h2> These are the course details for course id:' + str(course_id)+ '</h2>')
