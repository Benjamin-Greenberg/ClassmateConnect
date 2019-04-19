# This page contains custom forms for ClassmateConnect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *


# Form for users to create new accounts with
class StudentCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Student
        fields = ('username', 'email', 'first_name', 'last_name')


# Form for users to change their information
class StudentChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = ('username', 'email', 'first_name', 'last_name')


# Form to allow users to add any course to their courses field
class AddCourses(forms.Form):
    options = tuple((course.crn, course.title) for course in Course.objects.all())

    courses = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=options
    )


# Form to allow users to remove courses from their courses field
class RemoveCourses(forms.Form):

    def __init__(self, *args, **kwargs):
        self.username = kwargs.pop("username")
        self.options = tuple(
            (course.crn, course.title) for course in Student.objects.get(pk=self.username).courses.all()
        )
        super(RemoveCourses, self).__init__(*args, **kwargs)
        self.fields['courses'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=self.options
        )
