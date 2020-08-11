from django.db import models
#from djongo import models
#from mongoengine import Document, EmbeddedDocument, fields
# Create your models here.

class Componente(models.Model):
    nombre = models.CharField(max_length=30, default=None, primary_key=True)
    def __str__(self):
        return '%s' % (self.nombre)

class Canal(models.Model):
    componente1 = models.ForeignKey(Componente, on_delete=models.CASCADE, related_name='%(class)s_componenteEntrante')
    componente2 = models.ForeignKey(Componente, on_delete=models.CASCADE, related_name='%(class)s_componenteSaliente')
    id = models.CharField(max_length=30, null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return '%s-%s' % (self.id, self.nombre)


class Actividad(models.Model):
    id = models.CharField(max_length=30, null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE)
    def __str__(self):
        return '%s-%s' % (self.id, self.nombre)

class Participante(models.Model):
    id = models.CharField(max_length=30, null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    def __str__(self):
        return '%s-%s' % (self.nombre, self.actividad)

class Recurso(models.Model):
    id = models.CharField(max_length=30, null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    def __str__(self):
        return '%s-%s' % (self.nombre, self.actividad)
