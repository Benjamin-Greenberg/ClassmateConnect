from django.urls import path
from . import views


# Urls for connect app
urlpatterns = [
    path('', views.index, name='index')
]
