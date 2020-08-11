from django.db import models
#from djongo import models
#from mongoengine import Document, EmbeddedDocument, fields
# Create your models here.
class Actor(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)
    def __str__(self):
        return '%s' % (self.nombre)

class ServicioNegocio(models.Model):
    id = models.CharField(max_length=30, null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    actor=models.ForeignKey(Actor, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.nombre)

class ObjetoNegocio(models.Model):
    servicio = models.ForeignKey(ServicioNegocio, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return '%s' % (self.servicio)


class Operacion(models.Model):
    id = models.CharField(max_length=30, null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    servicio = models.ForeignKey(ServicioNegocio, on_delete=models.CASCADE)
    def __str__(self):
        return '%s-%s' % (self.id, self.nombre)

