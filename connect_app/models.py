from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from . import validators as v
from .manager import StudentManager


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
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(_('email_address'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = StudentManager()

    def __str__(self):
        return self.username
