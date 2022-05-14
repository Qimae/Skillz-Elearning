from distutils.command.upload import upload
from django.db import models

# Create your models here.

class institution(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class course(models.Model):
    #main_course
    #introduction
    #thumbnai_file
    title = models.CharField(max_length=200) 
    #tags
    course_description = models.TextField(null=True)
    price = models.IntegerField(default=0.00)
    image = models.ImageField(null=True, blank=True, upload_to="images")
    video = models.FileField(null=True, blank=True, upload_to="images/%y")

    def __str__(self):
        return self.title  