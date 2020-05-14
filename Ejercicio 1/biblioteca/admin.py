from django.contrib import admin
from biblioteca.models import Autor
from biblioteca.models import Libro
from biblioteca.models import Ejemplar
from biblioteca.models import Usuario

# Register your models here.
admin.site.register(Autor,)
admin.site.register(Libro,)
admin.site.register(Ejemplar,)
admin.site.register(Usuario,)
