from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import course
from .models import Section
from .forms import CourseForm



def index(request):
    courses = course.objects.all()
    context = { 'courses' : courses}
    return render(request , 'teacher/home_teacher.html', context)

def LoginTeacher(request):
    return render(request, "teacher/login_teacher.html")


def SignupTeacher(request):
    return render(request, "teacher/signup_teacher.html")

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
    return render(request, "teacher/new-upload.html", context)

def CourseDescription(request, pk):
    courses = course.objects.get(id=pk)
    sections = course.section.through.objects.filter(course_id=pk)
    description = courses.course_description[:50]
    context = { 
        'course' : courses,
        'desc' : description,
        'section' : sections,
        }
    return render(request, "student/course-description.html",context)    
