from django.shortcuts import render, get_object_or_404
from .models import Course


# Home Index
def index(request):
    return render(request, 'connect_app/index.html')


# Courses Index
def course_index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'connect_app/course_index.html', context)


# Course Details
def detail(request, crn):
    course = get_object_or_404(Course, pk=crn)
    context = {'course': course}
    return render(request, 'connect_app/detail.html', context)


# Student Login Page
def profile(request):
    return render(request, 'connect_app/profile.html')

