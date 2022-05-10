from django.urls import path
from .import views


urlpatterns = [
    path('login_student', views.login_student, name='login')
]

