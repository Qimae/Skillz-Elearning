from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course-upload', views.CourseUpload, name='CourseUpload'),
    path('course-description/<str:pk>', views.CourseDescription, name='course-description'),
    path('login_institution', views.LoginInstitution, name='login_insti'),
    path('signup_institution', views.SignupInstitution, name='signup_insti'),
]

urlpatterns += staticfiles_urlpatterns()