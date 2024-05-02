from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True,primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField()


class Estudiante(models.Model):
    rut = models.CharField(max_length=9, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(auto_now_add=True, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now=True, null=False, blank=False)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso, verbose_name="cursos", blank=True)

class Profesor(models.Model):    
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso, verbose_name="cursos", blank=False)


class Direccion (models.Model):
    calle = models.CharField(max_length=50,null=False, blank=False)
    numero = models.CharField(max_length=10,null=False, blank=False)
    dpto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50,null=False, blank=False)
    ciudad = models.CharField(max_length=50,null=False, blank=False)
    region = models.CharField(max_length=50,null=False, blank=False)
    estudiante_id = models.OneToOneField(Estudiante, verbose_name="rut", null=False, blank=False, unique=True, on_delete=models.CASCADE)

