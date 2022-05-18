from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import course
from .forms import CourseForm

# Create your views here.

def index(request):
    courses = course.objects.all()
    context = { 'courses' : courses}
    return render(request , 'institution/home_insti.html', context)

def LoginInstitution(request):
    return render(request, "institution/login_institution.html")


def SignupInstitution(request):
    return render(request, "institution/signup_institution.html")

def CourseUpload(request):
    form = CourseForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('index')
    context = { 
        "form":form
    }
    return render(request, "institution/new-upload.html", context)

def CourseDescription(request, pk):
    courses = course.objects.get(id=pk)
    context = { 'courses' : courses}
    return render(request, "institution/course-description.html", context)    

