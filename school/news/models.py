from django.db import models

# Create your models here.


class news_models(models.Model):
    title = models.CharField(max_length=50)
    Description = models.TextField(max_length=100000)
    history = models.CharField(max_length=100)
    img = models.ImageField(upload_to= 'img',null=True, blank = True,  verbose_name="news img")


    def __str__(self):
        return self.title




class news_video_models(models.Model):
    title = models.CharField(max_length=50)
   
    video = models.FileField(upload_to= 'video',null=True, blank = True,  verbose_name="news video")
   

    def __str__(self):
        return self.title



