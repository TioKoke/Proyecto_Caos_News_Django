from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=20)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Socio(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)
    password = models.CharField(max_length=60)
    correo = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre