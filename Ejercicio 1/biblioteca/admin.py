from django.contrib import admin
from biblioteca.models import Autor
from biblioteca.models import Libro
from biblioteca.models import Ejemplar
from biblioteca.models import Usuario

class LibroAdmin(admin.ModelAdmin):
    list_display = ('Titulo','Editorial')

class UsuarioAdmin(admin.ModelAdmin):
    fieldsets =(
    ('Datos',{
        'fields': ('Nombre',)
    }),
    ('Contacto',{
        'fields': ('Telefono','Direccion')
    })
    )




admin.site.register(Autor,)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Ejemplar,)
admin.site.register(Usuario,UsuarioAdmin)
