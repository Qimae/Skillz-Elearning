from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import course
from .models import Section
from .models import Lesson
from django.contrib.auth.models import User
from .forms import CourseForm, EnrollForm
from .forms import SectionForm
from .forms import LessonForm


def Tindex(request):
    courses = course.objects.all()[:3]
    context = { 'courses' : courses}
    return render(request , 'teacher/home_teacher.html', context)

def LoginTeacher(request):
    return render(request, "teacher/login_teacher.html")

def courses(request):
    courses = course.objects.all()
    context = { 'courses' : courses}
    return render(request , 'teacher/courses.html', context)


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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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
    current_user = request.user.get_username()
    courses = course.objects.get(id=pk)
    sections = Section.objects.filter(courses_id=pk)
    # lesson = sections.lesson.all()
    # test = course.objects.filter(Section_id=pk)
    description = courses.course_description
    # instructor = courses.instructor.get_short_name()



    context = { 
        'course' : courses,
        'desc' : description,
        'section' : sections,
    'user': current_user,
        # 'lesson' : lesson,
        # 'instructor': instructor,
        }
    return render(request, "student/course-description.html",context)    


@login_required(login_url='login')
def LessonDescription(request, pk):
    current_user = request.user.get_username()
    courses = course.objects.filter(section=pk).first()
    sections = Section.objects.get(id=pk)
    sec = Section.objects.filter(courses=courses.id)
    # sections = courses.section.all()
    # section_sub = courses.section.all()
    # les_dic = {}
    # for i in sec:
    lessons = Lesson.objects.filter(section_id=pk)
        
        # les_dic.update({'i' : lessons})
    # test = course.objects.filter(Section_id=pk)
    # description = courses.course_description[:50]
    # instructor = courses.instructor.get_short_name()
    

    context = { 
        'course' : courses,
        # 'desc' : description,
        'section' : sections,
        'lesson' : lessons,
        # 'instructor': instructor,
        'sec' : sec,
        'user': current_user,
        }
    return render(request, "student/les_list.html", context)  

def video(request, pk):
    current_user = request.user.get_username()
    lessons = Lesson.objects.get(id=pk)
    context={
        'vurl' : lessons,
        'user': current_user,
        }
    return render(request, "student/video.html", context)


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

def under_con(request):
    return render(request, "dashboard/under_con.html")
