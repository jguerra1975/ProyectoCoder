from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    

    def __str__(self) -> str:
        return f'{self.nombre} - {self.camada}'

    class Meta():
        ordering = ('nombre', 'camada')
        unique_together = ('nombre', 'camada')    
    

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.nombre} | {self.apellido} | {self.email}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)

# para ver cuales son las modificaciones a la base de datos pendientes
# C:\Users\javie\AppData\Local\Programs\Python\Python311\python.exe .\manage.py showmigrations

# para crear el archivo de migraciones de la base de datos
# C:\Users\javie\AppData\Local\Programs\Python\Python311\python.exe .\manage.py makemigrations 



# agregar  AppCoder en el archivo settings.py del ProyectoCoder para que tome los cambios que agregamos

# para cargar los cambios realizados
# C:\Users\javie\AppData\Local\Programs\Python\Python311\python.exe .\manage.py migrate

# para guardar datos atravez de la shell de python
# C:\Users\javie\AppData\Local\Programs\Python\Python311\python.exe .\manage.py shell
# from AppCoder.models import Curso
# nuevo_curso = Curso(nombre="Pythom Basico", camada=12312)
# nuevo_curso.save()

# git init para iniciar el git
# git status 
# git branch -M main  para cambiar el nombre del master
# git remote add origin https://github.com/jguerra1975/ProyectoCoder.git para llevar el proyecto a gitbub
# git add . para agregar los cambio
# git commit -m "first commit"  para comitiar los cambios
# git push origin main   para subir los cambios

# python .\manage.py createsuperuser  para crear el super usuario de la consola de Django

