from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)

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
