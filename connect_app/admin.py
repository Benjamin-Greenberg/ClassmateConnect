from django.contrib import admin
from .models import *

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Course Information', {'fields': ['crn', 'course_number', 'section_number']}),
        ('Students', {'fields': ['students']}),
    ]
    list_display = ('title', 'course_number')
    list_filter = ['course_number']
    ordering = ('course_number',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
