from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from . import views


# Urls for connect_app app
app_name = 'connect_app'
urlpatterns = [
    # Index page
    path('', views.index, name='index'),
    # Courses Index Page
    path('courses/', views.course_index, name='courses'),
    # Student Login Page
    path('login/', LoginView.as_view(template_name='connect_app/login.html'), name='student_login'),
    # Student Sign Up Page
    path('signup/', views.SignUp.as_view(), name='signup'),
    # Student Profile Page
    path('profile/', views.profile, name='profile'),
    # Student Change Info Page
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    # Change Password Page
    re_path(r'^password/$', views.change_password, name='password_change'),
    # Add Courses From Student Perspective
    path('add_courses/', views.add_courses, name='add_courses'),
    # Remove Courses From Student Perspective
    path('remove_courses/', views.remove_courses, name='remove_courses'),
    # Course Detail Page
    path('<int:crn>/', views.detail, name='detail'),
]
