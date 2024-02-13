from django.db import models

# Create your models here.

class contact_forms_models(models.Model):
    name = models.CharField(max_length=255, verbose_name='Title of the your core', help_text='max character limit 255')
    Message = models.TextField(verbose_name='your user description')
    Email = models.EmailField(max_length=255, verbose_name='Title of the your core', help_text='max character limit 255')
    Subject = models.CharField(max_length=255, verbose_name='Title of the your core',help_text='max character limit 255')



    class Meta:
        verbose_name='corepost' 
        verbose_name_plural='All contact fomrs'

    def __str__(self):
        return self.name
