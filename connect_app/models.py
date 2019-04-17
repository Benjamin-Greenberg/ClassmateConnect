from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from . import validators as v
from .manager import StudentManager
from heapq import nsmallest


class Course(models.Model):
    crn = models.IntegerField(validators=[v.valid_crn], default=00000, primary_key=True)
    title = models.CharField(max_length=50, default="Title")
    course_number = models.CharField(max_length=10, default="Major XXX")
    section_number = models.IntegerField(default=000)
    students = models.ManyToManyField('Student', related_name="courses", blank=True)

    class Meta:
        ordering = ['course_number']

    def __str__(self):
        return self.title


class Student(AbstractUser):
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

        for course in self.courses.all():
            for classmate in course.students.all():
                if classmate == self:
                    continue
                else:
                    if classmate in classmates.keys():
                        classmates[classmate] += 1
                    else:
                        classmates[classmate] = 1
        if len(classmates) < 5:
            minDisplay = len(classmates)
        else:
            minDisplay = 5

        heap = [(-value, key) for key, value in classmates.items()]
        self.temp_classmates = nsmallest(minDisplay, heap)
        self.temp_classmates = [(key, -value) for value, key in self.temp_classmates]
