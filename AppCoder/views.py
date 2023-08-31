from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

def curso(req, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
    <p>Curso: {curso.nombre} - Camada: {curso.camada} creado con exito!!</p>
    """)

def listar_cursos(req):
    lista = Curso.objects.all()
    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def inicio(req):

    #return HttpResponse("Vista de Inicio")
    return render(req, "inicio.html")

def cursos(req):

    #return HttpResponse("Vista de cursos")
    return render(req, "cursos.html")

def profesores(req):

    #return HttpResponse("Vista de profesores")
    return render(req, "profesores.html")

def estudiantes(req):

    #return HttpResponse("Vista de estudiantes")
    return render(req, "estudiantes.html")

def entregables(req):

    #return HttpResponse("Vista de entregables")
    return render(req, "entregables.html")
