from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import course
from .forms import CourseForm

# Create your views here.

def index(request):
    courses = course.objects.all()
    context = { 'courses' : courses}
    return render(request , 'institution/home.html', context)

def CourseUpload(request):
    form = CourseForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('CourseUpload')
    context = { 
        "form":form
    }
    return render(request, "institution/course_form.html", context)

