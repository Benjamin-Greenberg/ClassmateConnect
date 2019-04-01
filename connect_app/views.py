from django.shortcuts import render, get_object_or_404
from .models import Course


def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    render(request, 'connect_app/index.html', context)


def detail(request, crn):
    course = get_object_or_404(Course, pk=crn)
    context = {'course': course}
    render(request, 'connect_app/detail.html', context)
