from django.db import models
from django.forms import forms

from . import validators as v


class Course(models.Model):
    crn = models.IntegerField(validators=[v.valid_crn])
    title = models.CharField(max_length=50)
    course_number = models.CharField(max_length=10)
    # FIXME section = models.IntegerField()
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
