from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *
# Register your models here.


class StudentAdmin(UserAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm
    model = Student
    list_display = ['username', 'email']


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Course Information', {'fields': ['crn', 'course_number', 'section_number']}),
        ('Students', {'fields': ['students']}),
    ]
    list_display = ('title', 'course_number')
    ordering = ('course_number',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
