import http
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from datos_familiares.models import familiares
# Create your views here.

def datos_familiares(request):
    familiar = familiares.objects.all()
    coleccion = {'familiares':familiar}
    plantilla = loader.get_template("plantilla1.html")
    documento = plantilla.render(coleccion)
    return HttpResponse (documento)