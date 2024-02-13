from django.db import models


# Create your models here.


class events_models(models.Model):
    title = models.CharField(max_length=50)
    Description = models.TextField(max_length=1000000)
    img = models.ImageField(upload_to= 'img',null=True, blank = True,  verbose_name="events img")
    history = models.CharField(max_length=50)
    location_name = models.CharField(max_length=50)
    location  = models.URLField(max_length=100)


    def __str__(self):
        return self.title
    


class events_video_models(models.Model):
    title = models.CharField(max_length=50)
   
    video = models.FileField(upload_to= 'video',null=True, blank = True,  verbose_name="events video")
   

    def __str__(self):
        return self.title


