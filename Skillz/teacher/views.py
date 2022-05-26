from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import course
from .models import Section
from .models import Lesson
from django.contrib.auth.models import User
from .forms import CourseForm, EnrollForm
from .forms import SectionForm
from .forms import LessonForm


def Tindex(request):
    courses = course.objects.all()
    context = { 'courses' : courses}
    return render(request , 'teacher/home_teacher.html', context)

def LoginTeacher(request):
    return render(request, "teacher/login_teacher.html")


def SignupTeacher(request):
    return render(request, "teacher/signup_teacher.html")

def calendar(request):
    current_user = request.user.get_username()
    context = {
        'user':current_user,
        # 'profile': profile
        }
    return render(request, "dashboard/calendar.html", context)

def Tprofile(request):
    current_user = request.user.get_username()
    # pk = current_user.id
    # profile = Profile.objects.get(id=pk)
    context = {
        'user': current_user,
        # 'profile': profile
        }
    return render(request, 'teacher/profilefinal.html', context)

def CourseUpload(request):
    current_user = request.user
    course_form = CourseForm(request.POST, request.FILES)
    # section_form = SectionForm(request.POST, request.FILES)
    # lesson_form = LessonForm(request.POST, request.FILES)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.students = current_user
            course.save()
            
            return redirect('SectionUpload')

    context = { 
        # "lesson_form" : lesson_form,
        "course_form" : course_form,
        # "section_form" : section_form,
        'user': current_user,

    }
    return render(request, "courses/new-upload.html", context)


def SectionUpload(request):
    current_user = request.user.get_username()
    courses = course.objects.last()
    section_form = SectionForm(request.POST, request.FILES)
    
    
    if request.method == 'POST':
        section_form = SectionForm(request.POST, request.FILES)
        if section_form.is_valid():
            section = section_form.save(commit=False)
            section.courses = courses
            section.save()
            return redirect('LessonUpload')
   
    
    context = { 
        'course' : courses,
        
        
        "section_form" : section_form,
        'user': current_user,

    }
    return render(request, "courses/new-section.html", context)

def LessonUpload(request):
    current_user = request.user.get_username()
    section = Section.objects.last()
    lesson_form = LessonForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, request.FILES)
        if lesson_form.is_valid():
            lesson = lesson_form.save(commit=False)
            lesson.section = section
            lesson.save()
            return redirect('LessonUpload')


    context = { 
        "lesson_form" : lesson_form,
        'section' : section,
        'user': current_user,

    }
    return render(request, "courses/new-lessons.html", context)





def CourseDescription(request, pk):
    courses = course.objects.get(id=pk)
    sections = Section.objects.filter(courses_id=pk)
    # lesson = sections.lessons.all()
    # test = course.objects.filter(Section_id=pk)
    description = courses.course_description[:50]
    # instructor = courses.instructor.get_short_name()



    context = { 
        'course' : courses,
        'desc' : description,
        'section' : sections,
        # 'lesson' : lesson,
        # 'instructor': instructor,
        }
    return render(request, "student/course-description.html",context)    

def LessonDescription(request, pk):
    sections = Section.objects.get(id=pk)
    # sections = courses.section.all()
    # section_sub = courses.section.all()
    lessons = Lesson.objects.filter(section_id=pk)
    # test = course.objects.filter(Section_id=pk)
    # description = courses.course_description[:50]
    # instructor = courses.instructor.get_short_name()
    

    context = { 
        # 'course' : courses,
        # 'desc' : description,
        'section' : sections,
        'lesson' : lessons,
        # 'instructor': instructor,
        }
    return render(request, "student/lesson.html", context)    

def enroll(request, pk):
    current_user = request.user.get_username()
    section = Section.objects.last()
    enroll_form = EnrollForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        enroll_form = EnrollForm(request.POST, request.FILES)
        if enroll_form.is_valid():
            lesson = enroll_form.save(commit=False)
            lesson.section = section
            lesson.save()
            return redirect('LessonUpload')


    context = { 
        "enroll_form" : enroll_form,
        'section' : section,
        'user': current_user,

    }
    return render(request, "courses/enroll.html", context)