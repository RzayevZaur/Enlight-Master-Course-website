from django.db import models
from teacher.models import teacher_models

# Create your models here.




class course_models(models.Model):
    course = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    img = models.ImageField(upload_to= 'img',null=True, blank = True,  verbose_name="course img")

    def __str__(self):
        return self.course




class course_video_models(models.Model):
    title = models.CharField(max_length=50)
    courses_name = models.CharField(max_length=50)
    title2 = models.CharField(max_length=100)
    description = models.TextField(max_length=100000000)
    video = models.FileField(upload_to= 'video',null=True, blank = True,  verbose_name="course video")
   

    def __str__(self):
        return self.title


