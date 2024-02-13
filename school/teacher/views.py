from django.shortcuts import render,get_object_or_404
from .models import teacher_models,teacher_video_models

# Create your views here.



def Teacher(request):
    teacher_video_views = teacher_video_models.objects.all()
    teacher_views = teacher_models.objects.all()
    Context = {"teacher_views": teacher_views,"teacher_video_views":teacher_video_views}
    return render(request, "teachers.html", context=Context)



def Teacher_single(request,pk):
    teacherdetails = get_object_or_404(teacher_models, pk=pk)
    teacher_single_views = teacher_models.objects.all()
    Context = {"teacher_single_views": teacher_single_views,"teacherdetails":teacherdetails}
    return render(request, "teacher-single.html", context=Context)





















