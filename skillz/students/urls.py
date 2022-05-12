from django.urls import path
from .import views


urlpatterns = [
    path('login_student/', views.login_student, name='login'),
    path('logout_student/', views.logout_student, name='logout'),
    path('register_student/', views.register_student, name='register'),
]

