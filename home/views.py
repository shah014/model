from django.shortcuts import render


# Create your views here.
from home.models import Subject
from home.models import Teacher


def home(request):
    sub_info = Subject.objects.all()
    return render(request, template_name='home.html', context={'sub_info': sub_info})


def index(request):
    teacher_info = Teacher.objects.all()
    return render(request, template_name='base.html', context={'teacher_info': teacher_info})
