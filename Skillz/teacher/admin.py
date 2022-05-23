from django.contrib import admin

from .models import Lesson, course, Section, Instructor, Course_Learner

# Register your models here.
admin.site.register(course)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Course_Learner)