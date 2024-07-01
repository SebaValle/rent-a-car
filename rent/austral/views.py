# rent/views.py

from django.shortcuts import render

def index(request):
    context = {
        'title': 'Austral Rent a Car - Inicio',
    }
    return render(request, 'index.html', context)

def admin(request):
    context = {
        'title': 'Austral Rent a Car - Administración',
    }
    return render(request, 'html/admin.html', context)

def vehiculos(request):
    context = {
        'title': 'Austral Rent a Car - Vehículos',
    }
    return render(request, 'vehiculos.html', context)

def nosotros(request):
    context = {
        'title': 'Austral Rent a Car - Nosotros',
    }
    return render(request, 'nosotros.html', context)

def registro(request):
    context = {
        'title': 'Austral Rent a Car - Registro',
    }
    return render(request, 'registro.html', context)
