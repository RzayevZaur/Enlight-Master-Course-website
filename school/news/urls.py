from django.urls import path

from . import views


urlpatterns = [
    path("news/",views.News,name ="news_name"),
    path("news-single/<int:pk>/",views.News_single,name="news_single_name")

]

