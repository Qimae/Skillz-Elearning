from django.forms import ModelForm
from .models import course


class CourseForm(ModelForm):
    class Meta:
        model = course
        fields = [ 'title', 'course_description', 'price', 'image', 'section', 'instructor']

