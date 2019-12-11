from django.db import models

# Create your views here.
#modelo extra

class Carrera(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = "carreras"

class Alumnos(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50, null=False)
    carrera_id = models.ForeignKey(Carrera, on_delete=models.SET(-1))#, related_name='inventario'

    class Meta:
        db_table = "alumnos"




