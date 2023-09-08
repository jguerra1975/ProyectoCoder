from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

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
    
def lista_profesores(req):
    profesores = Profesor.objects.all()
    return render(req, "listaProfesores.html", {"profesores": profesores})

def crea_profesor(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        miFormulario = ProfesorFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesor.save()
            profesores = Profesor.objects.all()
            return render(req, "listaProfesores.html", {"profesores": profesores})
    else:
        miFormulario = ProfesorFormulario()
        return render(req, "profesorFormulario.html", {"miFormulario": miFormulario})
    
def elimina_profesor(req, id):
    if req.method == 'POST':
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        profesores = Profesor.objects.all()
        return render(req, "listaProfesores.html", {"profesores": profesores})

def edita_profesor(req, id):
    profesor = Profesor.objects.get(id=id)
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        miFormulario = ProfesorFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]
            profesor.profesion = data["profesion"]
            profesor.save()
            profesores = Profesor.objects.all()
            return render(req, "listaProfesores.html", {"profesores": profesores})
    else:

        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "apellido": profesor.apellido,
            "email": profesor.email,
            "profesion": profesor.profesion,
        })
        return render(req, "editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})
    
class CursoList(ListView):
    model = Curso
    template_name = "curso_list.html"
    context_object_name = "cursos"

class CursoDetail(DetailView):
    model = Curso
    template_name = "curso_detail.html"
    context_object_name = "curso"

class CursoCreate(CreateView):
    model = Curso
    template_name = "curso_create.html"
    fields = ['nombre', 'camada']
    success_url = '/app-coder/lista-cursos/'

class CursoUpdate(UpdateView):
    model = Curso
    template_name = "curso_update.html"
    fields = ('__all__')
    success_url = '/app-coder/lista-cursos/'

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_delete.html"
    success_url = '/app-coder/lista-cursos/'

