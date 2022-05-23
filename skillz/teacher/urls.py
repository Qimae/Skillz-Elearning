from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('', views.index, name='Tindex'),
    path('course-upload', views.CourseUpload, name='CourseUpload'),
    path('calendar/', views.calendar, name='calendar'),
    path('course-description/<str:pk>', views.CourseDescription, name='course-description'),
    path('login_teacher', views.LoginTeacher, name='login_teacher'),
    path('signup_teacher', views.SignupTeacher, name='signup_teacher'),
    path('profile_teacher/', views.Tprofile, name='Tprofile'),
    path('lesson-description/<str:pk>', views.LessonDescription, name='lesson-description'),
]

urlpatterns += staticfiles_urlpatterns()