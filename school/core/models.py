from django.db import models

# Create your models here.





class index_models(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to= 'img',null=True, blank = True,  verbose_name="index img")
    img1 = models.ImageField(upload_to= 'img',null=True, blank = True,  verbose_name="index img")
    img2 = models.ImageField(upload_to= 'img',null=True, blank = True,  verbose_name="index img")


    
    def __str__(self):
        return self.title





class about_models(models.Model):


    title = models.CharField(max_length=50)
    Description = models.TextField(max_length=10000)


    def __str__(self):
        return self.title





class galery_models(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to= 'img',null=True, blank = True,  verbose_name="gallery img")
    def __str__(self):
        return self.name
    


class about_video_models(models.Model):
    title = models.CharField(max_length=50)
   
    video = models.FileField(upload_to= 'video',null=True, blank = True,  verbose_name="about video")
   

    def __str__(self):
        return self.title

