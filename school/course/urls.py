from django.urls import path

from . import views


urlpatterns = [
    path("course/",views.Course,name ="course_name"),
    path("course-single/<int:pk>/",views.Course_single,name="course_single_name")

]





