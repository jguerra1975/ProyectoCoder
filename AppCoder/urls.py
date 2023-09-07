from django.urls import path
from AppCoder.views import curso, listar_cursos, inicio, cursos, profesores, estudiantes, entregables, cursoFormulario, busquedaCamada, buscar

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', listar_cursos, name="Lista-Cursos"),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('curso-formulario/', cursoFormulario, name="CursoFormulario"),
    path('busqueda-camada/', busquedaCamada, name="BusquedaCamada"),
    path('buscar/', buscar, name="Buscar"),
]