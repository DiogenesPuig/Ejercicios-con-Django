from django.db import models

# Create your models here.

class Autor(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.Nombre,self.Codigo)

class Libro(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=50)
    Editorial = models.CharField(max_length=50)
    Paginas = models.IntegerField()
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Codigo,self.Titulo,self.Editorial,self.Autor,self.Paginas)

class Ejemplar(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Localizacion = models.CharField(max_length=50)
    Libro = models.ForeignKey(Libro, on_delete=models.CASCADE, default="")

    def __str__(self):
        return '{}'.format(self.Codigo,self.Localizacion,self.Libro)

class Usuario(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.Codigo,self.Nombre,self.Telefono,self.Direccion)

class Ejem_Usua(models.Model):
    id = models.AutoField(primary_key=True)
    Ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id,self.Ejemplar,self.Usuario)
