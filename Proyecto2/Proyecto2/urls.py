"""Proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto2.views import saludo, segundoSaludo, diaDeHoy, miNombre, primerTemplate #Para acceder a la vista hay que importar el modulo y el metodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), #ojo la url   no hace falta que se llame saludo/ el nombre es libre,
    path('segundosaludo/', segundoSaludo),#pero la vista si debe llamarse por su nombre
    path('diaDeHoy/', diaDeHoy),
    path('miNombre/<nombre>', miNombre),
    path('primerTemplate/', primerTemplate),
]

