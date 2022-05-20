from django.forms import ModelForm
from .models import course
from .models import Section
from .models import Lesson


class CourseForm(ModelForm):
    class Meta:
        model = course
        fields = [ 'title', 'course_description', 'price', 'image', 'instructor']

class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = [ 'title', 'courses' ]
class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = [ 'title', 'video', 'section']
