from django.contrib import admin
from .models import events_models,events_video_models
# Register your models here.

admin.site.register(events_models)
admin.site.register(events_video_models)