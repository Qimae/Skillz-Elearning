from django.contrib import admin

from .models import Lesson, course, Section

# Register your models here.
admin.site.register(course)
admin.site.register(Section)
admin.site.register(Lesson)