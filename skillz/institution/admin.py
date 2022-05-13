from django.contrib import admin
from .models import institution
from .models import course

# Register your models here.

admin.site.register(institution)
admin.site.register(course)
