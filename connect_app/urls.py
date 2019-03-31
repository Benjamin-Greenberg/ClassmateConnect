from django.urls import path
from . import views


# Urls for connect_app app
urlpatterns = [
    path('', views.index, name='index')
]
