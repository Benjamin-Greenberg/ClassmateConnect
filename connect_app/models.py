from django.db import models
from django.forms import forms

from . import validators as v


class Course(models.Model):
    crn = models.IntegerField(validators=[v.valid_crn], default=00000, primary_key=True)
    title = models.CharField(max_length=50, default="Title")
    course_number = models.CharField(max_length=10, default="Major XXX")
    section_number = models.IntegerField(default=000)
    students = models.ManyToManyField('Student', related_name="courses", blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=50)
    netId = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
