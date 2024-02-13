from django.contrib import admin

# Register your models here.

from .models import news_models,news_video_models

admin.site.register(news_models)
admin.site.register(news_video_models)
