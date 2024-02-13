from django.contrib import admin

# Register your models here.


from .models import index_models,about_models,galery_models,about_video_models

admin.site.register(index_models)
admin.site.register(about_models)
admin.site.register(galery_models)
admin.site.register(about_video_models)
