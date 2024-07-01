from django.contrib import admin
from django.urls import path, include
from austral.views import *
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
]