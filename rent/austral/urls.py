from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('registro/', views.registro, name='registro'),
]
