from django.contrib import admin

# Register your models here.

from .models import course_models,course_video_models

admin.site.register(course_models)
admin.site.register(course_video_models)
