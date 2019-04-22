from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *
from django.forms import SelectMultiple


# Admin Interface for the Student Model
# Inherits from the UserAdmin class
# The Student Interface does not yet have the ability to edit password or assign courses
class StudentAdmin(UserAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm
    model = Student
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Information', {'fields': ['first_name', 'last_name']}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        # ('Courses', {'fields': ('courses',)})
    )
    # formfield_overrides = {models.ManyToManyField: {'widget': SelectMultiple(attrs={'size': '10'})}, }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'first_name', 'last_name', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


# Admin Interface for the Course model
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
