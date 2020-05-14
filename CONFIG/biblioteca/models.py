from django.db import models

# Create your models here.

class Autor(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

class Libro(object):
    Codigo = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=50)
    Editorial = models.CharField(max_length=50)
    Paginas = models.BigIntegerField()
    Autor = Autor()

class Ejemplar(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Localizacion = models.CharField(max_length=50)

class Usuario(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)
