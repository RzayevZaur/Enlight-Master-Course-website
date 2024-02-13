from django.shortcuts import render,get_object_or_404
from .models import news_models,news_video_models

# Create your views here.


def News(request):
    news_views = news_models.objects.all()
    news_video_views = news_video_models.objects.all()
    Context = {"news_views": news_views,'news_video_views':news_video_views}
    return render(request, "news.html", context=Context)


def News_single(request,pk):
    newsdetails = get_object_or_404(news_models,pk=pk)
    news_single_views = news_models.objects.all()
    Context = {"news_single_views": news_single_views,'newsdetails':newsdetails}
    return render(request, "news-single.html", context=Context)
