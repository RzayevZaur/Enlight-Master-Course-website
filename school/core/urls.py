from django.urls import path

from . import views



urlpatterns = [
    path("",views.Index,name='Index_name'),
    path("about/",views.About,name='About_name'),
    path("gallery/",views.Gallery,name='Gallery_name'),   
]