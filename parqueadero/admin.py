from django.contrib import admin
from .models import Usuario, Punto, Facultade, Programa, Parkine

class UserFields(admin.ModelAdmin):
    list_display = ('nombre','apellido','código','identificación','email', 'status')
    
class SedeFields(admin.ModelAdmin):
    list_display = ('id_sede','nombre', 'dirección')
    
class EstaciónFields(admin.ModelAdmin):
    list_display = ('id_estación', 'nombre', 'id_sede')
    
class PuntoFields(admin.ModelAdmin):
    list_display = ('id_punto', 'id_estacion', 'estado','codigo_punto')
    
class FacultadFields(admin.ModelAdmin):
    list_display = ('id_facultad', 'nombre', 'abrebiación','estado')
    
class ProgramaFields(admin.ModelAdmin):
    list_display = ('id_programa', 'nombre', 'abrebiación', 'id_facultad')
    
class ParkineFields(admin.ModelAdmin):
    list_display = ('id_parking', 'id_usurio', 'id_punto')
    
# Register your models here.
admin.site.register(Usuario, UserFields)
admin.site.register(Punto, PuntoFields)
admin.site.register(Facultade, FacultadFields)
admin.site.register(Programa, ProgramaFields)
admin.site.register(Parkine, ParkineFields)