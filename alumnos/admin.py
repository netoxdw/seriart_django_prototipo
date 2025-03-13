from django.contrib import admin
from .models import Generaciones, Escuela, Grupo, Alumno

@admin.register(Generaciones)
class GeneracionesAdmin(admin.ModelAdmin):
    list_display = ('año',)

@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'nivel', 'generacion')
    list_filter = ('nivel', 'generacion')
    search_fields = ('nombre', 'ciudad')

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'escuela', 'generacion', 'mes_graduacion')
    list_filter = ('escuela', 'generacion')
    search_fields = ('nombre',)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'folio_camara', 'grupo', 'escuela', 'generacion')
    list_filter = ('grupo', 'escuela', 'generacion')
    search_fields = ('nombre', 'telefono', 'folio_camara')