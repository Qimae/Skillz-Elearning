from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models
# from embed_video.fields import EmbedVideoField
import uuid




class course(models.Model):
    #main_course
    #introduction
    #thumbnai_file
    title = models.CharField(max_length=200) 
    #tags
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    course_description = models.TextField(null=True)
    price = models.IntegerField(default=0.00)
    image = models.ImageField(null=True, blank=True, upload_to="images")
    video = models.FileField(null=True, blank=True, upload_to="images/%y")
    # section = models.ForeignKey('Section', on_delete=models.CASCADE)
    students = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    
    # class Meta:
    #     ordering = ['section']

    def __str__(self):
        return self.title 

class Section(models.Model):
    title = models.CharField(max_length=200)
    number = models.IntegerField(blank=True, null=True)
    courses = models.ForeignKey(course, on_delete=models.CASCADE)
    
    def __str__(self):
        return f" {self.number} {self.title}"
        
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(null=True, blank=True, upload_to="videos/%y")
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    def __str__(self):
        return self.title 

class Instructor(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(course)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return  f" {self.instructor} "


class Course_Learner(models.Model):
    Note = models.CharField(max_length=200)
    learner = models.ForeignKey(User, on_delete=models.CASCADE)
    CourseLearner = models.ForeignKey(course, on_delete=models.CASCADE, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return  f" {self.learner} "
