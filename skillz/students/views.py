from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib import messages
from .aforms import CustomUserCreationForm
# Create your views here.


def login_student(request):
    page = 'register'
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
        return render(request, 'account/login.html', {})

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

            messages.success(request, "user account was created!")

            login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'An error has occured')

    context = { 'page' : page, 'form': form}
    return render(request, 'account/signup.html', context)