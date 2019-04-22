from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from . import validators as v
from .manager import StudentManager
from heapq import nsmallest
from collections import OrderedDict


# Course model to represent each course offered
class Course(models.Model):
    # Crn will act as primary key
    crn = models.IntegerField(validators=[v.valid_crn], default=00000, primary_key=True)
    title = models.CharField(max_length=50, default="Title")
    course_number = models.CharField(max_length=10, default="Major XXX")
    section_number = models.IntegerField(default=000)
    # Students is a M2M field that can link to many Student objects to each course
    # and each Student object can link to many Course objects with the related name, courses
    students = models.ManyToManyField('Student', related_name="courses", blank=True)

    class Meta:
        ordering = ['course_number']

    def __str__(self):
        return self.title + ' ' + str(self.crn)


# Student model is a custom user model that inherits from Django's AbstractUser class
class Student(AbstractUser):
    # Username will act as primary key for Student model
    username = models.CharField(max_length=10, unique=True, primary_key=True)
    email = models.EmailField(_('email_address'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    classmates = models.ManyToManyField('self', blank=True)
    temp_classmates = []

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = StudentManager()

    def __str__(self):
        return self.username

    def add_course(self, crn):
        course = Course.objects.get(pk=crn)
        course.students.add(self)

    # Function to build the list of students w/ similar schedules
    def connect(self):
        classmates = {}
        self.temp_classmates = []

        # Build the classmates dictionary with with value being the number of classes taken together
        # and the key being the classmate
        for course in self.courses.all():
            for classmate in course.students.all():
                if classmate == self:
                    continue
                else:
                    if classmate in classmates.keys():
                        classmates[classmate] += 1
                    else:
                        classmates[classmate] = 1
        # If the number of classmates is less than 5, only get that many similar classmates
        if len(classmates) < 5:
            minDisplay = len(classmates)
        # Else, get the 5 most similar classmates
        else:
            minDisplay = 5

        # Turn the classmates dictionary into a heap and pop the most similar classmates from the heap

        # heap = [(-value, key) for key, value in classmates.items()]
        # self.temp_classmates = nsmallest(minDisplay, heap)

        # Heap method is having issues at the moment, so an ordered dict is being used instead
        heap = sorted(classmates.items(), key=lambda kv: kv[1], reverse=True)
        for i in range(0, minDisplay):
            self.temp_classmates.append((heap[i][0], heap[i][1]))


# ManytoMany Field Information: https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/
# Django Custom User Model: https://testdriven.io/blog/django-custom-user-model/
#                           https://wsvincent.com/django-custom-user-model-tutorial/
# Django Documentation: https://docs.djangoproject.com/en/2.1/
