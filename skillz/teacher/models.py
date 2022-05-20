from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models

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
    # video = models.FileField(null=True, blank=True, upload_to="images/%y")
    # section = models.ForeignKey('Section', on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    
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
