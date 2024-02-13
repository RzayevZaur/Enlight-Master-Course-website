from django.urls import path

from . import views


urlpatterns = [
    path("teachers/",views.Teacher,name ="Teacher_name"),
    path("teachers-single/<int:pk>/",views.Teacher_single,name="Teacher_single_name")


]



