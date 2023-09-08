from django.urls import path
from AppCoder.views import curso, listar_cursos, inicio, cursos, profesores, estudiantes, entregables, cursoFormulario, busquedaCamada, buscar, lista_profesores, crea_profesor, elimina_profesor, edita_profesor, CursoList, CursoDetail, CursoCreate, CursoUpdate, CursoDelete

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
    path('listaProfesores/', lista_profesores, name="ListarProfesores"),
    path('crea-profesores/', crea_profesor, name="CrearProfesores"),
    path('elimina-profesores/<int:id>', elimina_profesor, name="eliminarProfesores"),
    path('edita-profesores/<int:id>', edita_profesor, name="editararProfesores"),
    path('ListaCursos/', CursoList.as_view(), name="ListaCursos"),
    path('DetalleCursos/<pk>', CursoDetail.as_view(), name="DetalleCursos"),
    path('CrearCursos/', CursoCreate.as_view(), name="CrearCursos"),
    path('EditarCursos/<pk>', CursoUpdate.as_view(), name="EditarCursos"),
    path('EliminarCursos/<pk>', CursoDelete.as_view(), name="EliminarCursos"),

]