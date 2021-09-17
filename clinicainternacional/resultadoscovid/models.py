from django.db import models


class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=2)
    ci = models.CharField(max_length=13)
    direccion = models.TextField(max_length=500)
    municipio = models.CharField(max_length=50)
    provincia = models.CharField(max_length=30)
    condicion = models.CharField(max_length=50)
    procedencia = models.CharField(max_length=60)
    inicio_sintoma = models.CharField(max_length=50)
    toma_muestra = models.DateField()
    tipo_muestra = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    resultado = models.CharField(max_length=50)

