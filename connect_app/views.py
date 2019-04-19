# Contains the views for ClassmateConnect
from django.shortcuts import render, get_object_or_404, redirect
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


# Student Add Courses Form Page
def add_courses(request):

    # Take the information from the form and add the selected courses to the student's courses field
    if request.method == "POST":
        student = Student.objects.get(pk=request.user.username)
        form = AddCourses(request.POST)
        if form.is_valid():
            courses = form.cleaned_data.get('courses')
            for course in courses:
                student.courses.add(Course.objects.get(pk=course))

        return redirect(to='/profile/')
    # Pass the AddCourse form to the view to let the student select courses to add
    else:
        context = {
            'form': AddCourses,
            'title': "Add Courses",
            'message': "Add courses here.",
        }
        return render(request, 'connect_app/courses_edit.html', context)


# Student Remove Courses Form Page
def remove_courses(request):
    student = Student.objects.get(pk=request.user.username)

    # Take the information from the form and remove the selected courses
    if request.method == "POST":
        form = RemoveCourses(request.POST, username=request.user.username)
        if form.is_valid():
            courses = form.cleaned_data.get('courses')
            if courses is not None:
                for course in courses:
                    student.courses.remove(course)
        return redirect(to='/profile/')
    # Pass the RemoveCourses form to the view to let the student select courses to remove
    else:
        form = RemoveCourses(username=request.user.username)
        context = {
            'form': form,
            'title': "Remove Courses",
            'message': "Remove courses here.",
        }
        return render(request, 'connect_app/courses_edit.html', context)

# Information used in this page
# https://stackoverflow.com/questions/15393134/django-how-can-i-create-a-multiple-select-form
# Django Documentation: https://docs.djangoproject.com/en/2.1/



