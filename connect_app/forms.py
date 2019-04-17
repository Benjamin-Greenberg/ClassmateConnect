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


class RemoveCourses(forms.Form):
    username = "temp"
    options = tuple()
    courses = None

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
