from django.shortcuts import render,get_object_or_404
from .models import events_models,events_video_models

# Create your views here.


def Events(request):
    
    events_views = events_models.objects.all()
    events_video_views = events_video_models.objects.all()
    Context = {"events_views": events_views,"events_video_views":events_video_views}
    return render(request, "events.html", context=Context)


def Events_single(request,pk):
    eventsdetails = get_object_or_404(events_models,pk=pk)
    events_single_views = events_models.objects.all()
    Context = {"events_single_views": events_single_views,"eventsdetails":eventsdetails}
    return render(request, "events-single.html", context=Context)




 
                                            
                                                             