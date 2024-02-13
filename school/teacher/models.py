from django.db import models

# Create your models here.


class teacher_models(models.Model):
    fullname = models.CharField(max_length=50)
    img = models.ImageField(upload_to= 'img',null=True, blank = True,  verbose_name="teacher img")
    course = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    twitter_field = models.URLField(max_length = 200)
    facebook_field = models.URLField(max_length = 200) 
    instaqram_field = models.URLField(max_length = 200) 
    description = models.TextField(max_length=10000)
    def __str__(self):
        return self.fullname




class teacher_video_models(models.Model):
    title = models.CharField(max_length=50)
    title2 = models.CharField(max_length=100)
    description = models.TextField(max_length=100000000)
    video = models.FileField(upload_to= 'video',null=True, blank = True,  verbose_name="teacher video")
   

    def __str__(self):
        return self.title

