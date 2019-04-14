from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .forms import StudentCreationForm


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
