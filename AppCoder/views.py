from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Curso
from .forms import CursoFormulario
# Create your views here.

def curso(req, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
    <p>Curso: {curso.nombre} - Camada: {curso.camada} creado con exito!!</p>
    """)

def listar_cursos(req):

    lista = Curso.objects.all()
    print('method', req.method)
    print('GET', req.GET)
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

def cursoFormulario(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        miFormulario = CursoFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()
        return render(req, "inicio.html")
    else:
        miFormulario = CursoFormulario()
        return render(req, "cursoFormulario.html", {"miFormulario": miFormulario})
    
def busquedaCamada(req):
    print('method', req.method)
    print('GET', req.GET)
    return render(req, "busquedaCamada.html")

def buscar(req: HttpRequest):
    print('method', req.method)
    print('GET', req.GET)
    if req.GET["camada"]:
        camada = req.GET["camada"]
        #cursos = Curso.objects.get(camada=camada)
        #cursos = Curso.objects.filter(camada=camada)
        cursos = Curso.objects.filter(camada__icontains=camada)
        print (f'{cursos}')
        return render(req, "resultadoBusqueda.html", {"cursos": cursos})
    else:
        return HttpResponse(f'no hay resultados en la busqueda {req.GET["camada"]}')