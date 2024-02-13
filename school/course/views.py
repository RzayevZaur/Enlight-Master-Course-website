from django.shortcuts import render,get_object_or_404
from .models import course_models,course_video_models
from teacher.models import teacher_models
# Create your views here.

def Course(request):
    course_video_views = course_video_models.objects.all()
    teacher_views = teacher_models.objects.all()[:4] 
    course_views = course_models.objects.all()
    Context = {"course_views": course_views,"teacher_views": teacher_views,"course_video_views":course_video_views}
    return render(request, "courses.html", context=Context)


def Course_single(request,pk):
    coursedetails = get_object_or_404(course_models, pk=pk)
    course_single_views = course_models.objects.all()
    Context = {"course_single_views": course_single_views,"coursedetails":coursedetails}
    return render(request, "course-single.html", context=Context)




