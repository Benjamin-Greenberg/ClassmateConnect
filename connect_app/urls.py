from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
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
    # Student Profile Page
    path('profile/', views.profile, name='profile'),
    # Course Detail Page
    path('<int:crn>/', views.detail, name='detail'),
]
