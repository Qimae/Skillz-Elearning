from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('', views.Tindex, name='Tindex'),
    path('courses/', views.courses, name='courses'),

    path('calendar/', views.calendar, name='calendar'),
    path('course-description/<str:pk>', views.CourseDescription, name='course-description'),
    path('login_teacher', views.LoginTeacher, name='login_teacher'),
    path('signup_teacher', views.SignupTeacher, name='signup_teacher'),
    path('profile_teacher/', views.Tprofile, name='Tprofile'),
    path('lesson-description/<str:pk>', views.LessonDescription, name='lesson-description'),

    path('enroll/<str:pk>', views.enroll, name='enroll'),

    path('video/<str:pk>', views.video, name='video'),


    path('course-upload', views.CourseUpload, name='CourseUpload'),
    path('section-upload', views.SectionUpload, name='SectionUpload'),
    path('lesson-upload', views.LessonUpload, name='LessonUpload'),

    path('under_con', views.under_con, name='under_con'),
]

urlpatterns += staticfiles_urlpatterns()