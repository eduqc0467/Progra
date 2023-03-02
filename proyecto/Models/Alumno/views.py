from django.http import HttpRequest
from django.shortcuts import render
from django import forms

from .forms import  FormularioAlumno
from .models import Carpeta


class FormularioCarpeta:
    pass


class FormularioAlumnoView(HttpRequest):
    def index(request):
        alumno = FormularioAlumno()
        return render(request, "AlumnoIndex.html", {"form": alumno})

    def procesar_formulario(request):
        alumno = FormularioAlumno(request.POST)
        if alumno.is_valid():
            alumno.save()
            alumno = FormularioAlumno()

        return render(request, "AlumnoIndex.html", {"form": alumno, "mensaje": 'OK'})

    def listar_serv(request):
        serv = Carpeta.objects.all()
        return render(request,"ListaInscritos.html",)
        
