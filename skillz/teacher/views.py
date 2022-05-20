from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import course
from .models import Section
from django.contrib.auth.models import User
from .forms import CourseForm
from .forms import SectionForm
from .forms import LessonForm


def index(request):
    courses = course.objects.all()
    context = { 'courses' : courses}
    return render(request , 'teacher/home_teacher.html', context)

def LoginTeacher(request):
    return render(request, "teacher/login_teacher.html")


def SignupTeacher(request):
    return render(request, "teacher/signup_teacher.html")

def CourseUpload(request):
    course_form = CourseForm(request.POST, request.FILES)
    section_form = SectionForm(request.POST, request.FILES)
    lesson_form = LessonForm(request.POST, request.FILES)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        if course_form.is_valid():
            course_form.save()
            redirect('index')
    if request.method == 'POST':
        section_form = SectionForm(request.POST, request.FILES)
        if section_form.is_valid():
            section_form.save()
            redirect('index')
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, request.FILES)
        if lesson_form.is_valid():
            lesson_form.save()
            redirect('index')
    context = { 
        "lesson_form" : lesson_form,
        "course_form" : course_form,
        "section_form" : section_form,

    }
    return render(request, "teacher/course_form.html", context)

def CourseDescription(request, pk):
    courses = course.objects.get(id=pk)
    sections = courses.section.all()
    # lesson = sections.lessons.all()
    # test = course.objects.filter(Section_id=pk)
    description = courses.course_description[:50]
    instructor = courses.instructor.get_short_name()
    context = { 
        'course' : courses,
        'desc' : description,
        'section' : sections,
        # 'lesson' : lesson,
        'instructor': instructor,
        }
    return render(request, "student/course-description.html",context)    

def LessonDescription(request, pk):
    courses = course.objects.get(id=pk)
    sections = courses.section.all()
    section_sub = courses.section.all()
    # lesson = Section.lessons.title
    # test = course.objects.filter(Section_id=pk)
    description = courses.course_description[:50]
    instructor = courses.instructor.get_short_name()
    context = { 
        'course' : courses,
        'desc' : description,
        'section' : sections,
        'lesson' : section_sub,
        'instructor': instructor,
        }
    return render(request, "student/lesson.html",context)    
