from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from teacher.models import course

from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.

def index(request):
    # courses = course.objects.all()
    # context = { 'courses' : courses}
    return render(request , 'student/home_stu.html')

def login_student(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exit')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There was an error while trying to login. Check your user name and password or create an account.'))
            return redirect('login')
    else:
        return render(request, 'student/login.html', {})

def logout_student(request):
    logout(request)
    messages.error(request, 'user logout')
    return redirect('login')

def register_student(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "user student was created!")

            login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'An error has occured')

    context = { 'page' : page, 'form': form}
    return render(request, 'student/signup.html', context)

def profile(request):
    current_user = request.user.get_username()
    # pk = current_user.id
    # profile = Profile.objects.get(id=pk)
    user = {
        'user':current_user,
        # 'profile': profile
        }
    return render(request, 'student/profile.html',{'user': user})
    # return render(request, 'student/profile.html', context)

def mycourses(request, pk):
    current_user = request.user.get_username()
    courses = course.objects.get(id=pk)
    sections = courses.section.all()
    # lesson = sections.lessons.all()
    test = course.objects.filter(Section_id=pk)
    description = courses.course_description[:50]
    # instructor = courses.instructor.all()
    context = { 
        'user': current_user,
        'course' : courses,
        'desc' : description,
        'section' : sections,
        # 'lesson' : lesson,
        'test' : test,
        }

    return render(request, 'dashboard/my-courses.html', context)