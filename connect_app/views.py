import json
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .forms import *


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


# Student Profile Page
def profile(request):
    student = Student.objects.get(pk=request.user.username)
    student.connect()
    context = {'student': student}
    if request.user.is_authenticated:
        return render(request, 'connect_app/profile.html', context)
    else:
        return render(request, 'connect_app/index.html')


# Student SignUp Class
class SignUp(generic.CreateView):
    form_class = StudentCreationForm
    success_url = reverse_lazy('login')
    template_name = 'connect_app/signup.html'


# Student Change Info Page
class ChangeInfo(generic.CreateView):
    form_class = StudentChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'connect_app/changeinfo.html'


def add_courses(request):
    if request.method == "POST":
        student = Student.objects.get(pk=request.user.username)
        context = {'student': student}
        form = AddCourses(request.POST)
        if form.is_valid():
            courses = form.cleaned_data.get('courses')
            for course in courses:
                student.courses.add(Course.objects.get(pk=course))

        return render(request, 'connect_app/profile.html', context)
    else:
        context = {
            'form': AddCourses,
        }
        return render(request, 'connect_app/add_courses.html', context)


def remove_courses(request):
    student = Student.objects.get(pk=request.user.username)
    if request.method == "POST":
        context = {'student': student}
        form = RemoveCourses(request.POST, username=request.user.username)
        if form.is_valid():
            courses = form.cleaned_data.get('courses')
            if courses is not None:
                for course in courses:
                    student.courses.remove(course)
        return render(request, 'connect_app/profile.html', context)
    else:
        form = RemoveCourses(username=request.user.username)
        context = {
            'form': form,
        }
        return render(request, 'connect_app/add_courses.html', context)



