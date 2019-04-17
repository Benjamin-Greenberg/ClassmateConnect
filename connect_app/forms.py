from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *


class StudentCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Student
        fields = ('username', 'email', 'first_name', 'last_name')


class StudentChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = ('username', 'email', 'first_name', 'last_name')


class AddCourses(forms.Form):
    options = tuple((course.crn, course.title) for course in Course.objects.all())

    courses = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=options
    )


