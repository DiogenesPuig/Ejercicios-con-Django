from django.db import models

# Create your models here.

class Autor(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return "Autor: " + str(self.Codigo) + " " + str(self.Nombre)

class Libro(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=50)
    Editorial = models.CharField(max_length=50)
    Paginas = models.IntegerField()
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return "Libro: " + str(self.Codigo) + " " + self.Titulo + " " + self.Editorial + " " + str(self.Paginas) + " " + str(self.Autor)

class Usuario(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)

    def __str__(self):
        return "Usuario : " + str(self.Codigo) + " " + self.Nombre + " " + self.Telefono + " " + self.Direccion

class Ejemplar(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Localizacion = models.CharField(max_length=50)
    Libro = models.ForeignKey(Libro, on_delete=models.CASCADE, default="")
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "Ejemplar : " + str(self.Codigo) +" "+self.Localizacion + " " + str(self.Libro) + " " + str(self.Usuario)
