from django.shortcuts import render
from django.http import HttpResponse
from django.db import Curso


# Create your views here.
def curso(request, generacion):
    curso = Curso(nombre="Desarrollo web", generacion=2000)
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Generacion: {curso.generacion}"
    
    return HttpResponse(documentoDeTexto)