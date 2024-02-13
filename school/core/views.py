from django.shortcuts import render
from .models import index_models, about_models, galery_models,about_video_models
from news.models import news_models
from events.models import events_models
from course.models import course_models
from teacher.models import teacher_models




# Create your views here.


def Index(request):
    about_views = about_models.objects.all()
    teacher_views = teacher_models.objects.all()[:4]
    course_views = course_models.objects.all()[:4]
    events_views = events_models.objects.all()[:3]
    news_views = news_models.objects.all()[:3] 
    about_video_views = about_video_models.objects.all()
    index_views = index_models.objects.all()

    Context = {
        "index_views": index_views,
        "about_video_views":about_video_views,
        "news_views": news_views,
        "events_views": events_views,
        "course_views": course_views,
        "teacher_views": teacher_views,
         "about_views": about_views
    }

    return render(request, "index.html", context=Context)


def About(request):
    about_video_views = about_video_models.objects.all()
    about_views = about_models.objects.all()

    Context = {
        "about_views": about_views,
        "about_video_views":about_video_views
    }

    return render(request, "about.html", context=Context)


def Gallery(request):
    gallery_views = galery_models.objects.all()

    Context = {"gallery_views": gallery_views}
    return render(request, "gallery.html", context=Context)


