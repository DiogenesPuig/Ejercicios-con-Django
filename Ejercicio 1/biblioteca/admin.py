from django.contrib import admin
from biblioteca.models import Autor
from biblioteca.models import Libro
from biblioteca.models import Ejemplar
from biblioteca.models import Usuario

class LibroInline(admin.TabularInline):
    model = Libro


class LibroAdmin(admin.ModelAdmin):
    list_display = ('Titulo','Editorial','Autor')
    list_display_links = ('Titulo','Editorial')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Telefono')
    fieldsets =(
    ('Datos',{
        'fields': ('Nombre',)
    }),
    ('Contacto',{
        'fields': ('Telefono','Direccion')
    })
    )

class EjemplarAdmin(admin.ModelAdmin):
    list_display = ('NombreLibro', 'NombreEditorial')
    list_filter = ('Libro',)

class AutorAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Nombre')
    inlines = [LibroInline]
    search_fields = ['Nombre',]

admin.site.register(Autor,AutorAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Ejemplar,EjemplarAdmin)
admin.site.register(Usuario,UsuarioAdmin)
