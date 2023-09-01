from django.contrib import admin
from .models import Curso, Estudiante, Profesor, Entregable
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'camada')
    search_fields = ('nombre', 'camada')
    list_filter =  ('nombre',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
