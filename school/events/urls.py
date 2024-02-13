from django.urls import path

from . import views


urlpatterns = [
    path("events/",views.Events,name ="events_name"),
    path("events-single/<int:pk>/",views.Events_single,name="events_single_name")

]

