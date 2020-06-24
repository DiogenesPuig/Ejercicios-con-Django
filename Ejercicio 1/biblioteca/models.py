from django.db import models

# Create your models here.

class Autor(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Libro(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=50)
    Editorial = models.CharField(max_length=50)
    Paginas = models.IntegerField()
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

class Ejemplar(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Localizacion = models.CharField(max_length=50)
    Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def NombreLibro(self):
        return self.Libro.Titulo
    NombreLibro.short_description = "Libro"

    def NombreEditorial(self):
        return self.Libro.Editorial
    NombreEditorial.short_description = "Editorial"

    class Meta:
        verbose_name = "Ejemplar"
        verbose_name_plural = "Ejemplares"

class Usuario(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)
    Ejemplar =models.ManyToManyField(Ejemplar)

    def get_Codigo(self):
        return Usuario.Codigo
    get_Codigo.short_description = "id"
