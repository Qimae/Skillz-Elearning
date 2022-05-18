from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course-upload', views.CourseUpload, name='CourseUpload'),
    path('course-description/<str:pk>', views.CourseDescription, name='course-description'),
    path('login_teacher', views.LoginTeacher, name='login_teacher'),
    path('signup_teacher', views.SignupTeacher, name='signup_teacher'),
]

urlpatterns += staticfiles_urlpatterns()