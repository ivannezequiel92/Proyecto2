from django.http import HttpResponse
from datetime import datetime
#from django.template import Template, Context
from django.template import loader


def saludo(request):
    return HttpResponse("Hola Ivancito sos un crack de la programacion")

def segundoSaludo(request):
    return HttpResponse("Esto esta muy bueno asi podes escribir creando nuevas paginas")

def diaDeHoy(request):
    
    dia = datetime.now()
    documentoDeTexto = f"El dia de hoy es : <br> {dia}"
    
    return HttpResponse(documentoDeTexto)
    
def miNombre(self, nombre):
    documentoDeTexto = f"Su nombre es: <br>{nombre}"
    return HttpResponse(documentoDeTexto)

def primerTemplate(self):
       
    nom = "Ivan"
    ape = "Barboza"
    listaDeNotas = [1,7,9,3,6,8,2,4,9.8]
    diccionario = {"nombre":nom, "apellido":ape, "FechaHora":datetime.now(), "notas": listaDeNotas}
    
   # miHtml = open(r'C:\Users\Ivan\OneDrive\Desktop\Proyecto2\Proyecto2\Plantillas\template1.html')
    
    
    plantilla = loader.get_template('template1.html')
    
   # miHtml.close()
   # miContexto = Context(diccionario)
    
    documento = plantilla.render(diccionario)
  
   
    return HttpResponse(documento)
     