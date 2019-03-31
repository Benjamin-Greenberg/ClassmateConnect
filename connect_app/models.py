from django.db import models
from . import validators as v


class Course(models.Model):
    crn = models.IntegerField(validators=[v.valid_crn])
    title = models.CharField(max_length=50)
    course_number = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    students = models.ManyToManyField('Student', related_name="courses")

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=50)
    netId = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
