from django.urls import path
from . import views


# Urls for connect_app app
app_name = 'connect_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_crn>/', views.detail, name='detail'),
]
