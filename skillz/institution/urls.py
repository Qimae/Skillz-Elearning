from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course-upload', views.CourseUpload, name='CourseUpload'),
]

urlpatterns += staticfiles_urlpatterns()