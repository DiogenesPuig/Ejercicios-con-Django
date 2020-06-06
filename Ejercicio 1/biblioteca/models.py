from django.db import models

# Create your models here.

class Autor(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return "Autor: codigo: " + str(self.Codigo) + ", nombre: " + str(self.Nombre)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Libro(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=50)
    Editorial = models.CharField(max_length=50)
    Paginas = models.IntegerField()
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return "Libro: codigo: " + str(self.Codigo) + ", titulo: " + self.Titulo + ", editorial: " + self.Editorial + ", paginas: " + str(self.Paginas) + ", " + str(self.Autor)

class Ejemplar(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Localizacion = models.CharField(max_length=50)
    Libro = models.ForeignKey(Libro, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "Ejemplar : codigo: " + str(self.Codigo) +",  localizacion: "+self.Localizacion + ", " + str(self.Libro)

    class Meta:
        verbose_name = "Ejemplar"
        verbose_name_plural = "Ejemplares"

class Usuario(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)
    Ejemplar =models.ManyToManyField(Ejemplar)

    def __str__(self):
        return "Usuario : codigo: " + str(self.Codigo) + ", nombre: " + self.Nombre + ", telefono: " + self.Telefono + ", direccion: " + self.Direccion + ", " + str(self.Ejemplar)
