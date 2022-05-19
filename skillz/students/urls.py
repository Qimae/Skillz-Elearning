from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('login_student/', views.login_student, name='login'),
    path('logout_student/', views.logout_student, name='logout'),
    path('register_student/', views.register_student, name='register'),
    path('profile_student/', views.profile, name='profile'),
    path('mycourses/<str:pk>', views.mycourses, name='mycourses'),
    
]
urlpatterns += staticfiles_urlpatterns()