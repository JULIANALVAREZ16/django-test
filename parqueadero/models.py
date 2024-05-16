from django.db import models

# Create your models here.

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True
        
class Usuario(DateTimeModel):
    id_usuario= models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    apellido = models.CharField(max_length=150, blank=False, null=False)
    código = models.CharField(max_length=11,  blank=False, null=False)
    identificación = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField(max_length=200, unique=True, blank=False, null=False)
    status = models.BooleanField(default=True)
    #jave foranea de programa 
    id_programas = models.ForeignKey('Programa', on_delete=models.CASCADE, blank=False, null=False)
    
class Punto(DateTimeModel):
    id_punto = models.AutoField(primary_key=True, unique= True, blank= False, null=False)
    codigo_punto = models.CharField(max_length=50, blank=False, null=False)
    id_estacion = models.CharField(max_length=50, blank=False, null=False)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo_punto


class Facultade(DateTimeModel):
    id_facultad = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    abrebiación = models.CharField(max_length=10, blank=False, null=False)
    estado = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre

class Programa(DateTimeModel):
    id_programa = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    abrebiación = models.CharField(max_length=10, blank=False, null=False)
    id_facultad = models.ForeignKey(Facultade, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Parkine(DateTimeModel):
    id_parking = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    id_usurio = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, null=False)
    id_punto = models.ForeignKey(Punto, on_delete=models.CASCADE, blank=False, null=False)
    password = models.CharField(max_length=6, blank=False, null=False)
    
