#from django.db import models
from djongo import models
from mongoengine import Document, EmbeddedDocument, fields
# Create your models here.

class Aplicacion(models.Model):
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    #ficha_tecnica = models.EmbeddedField(model_container=FichaTecnica, default=None)
    #factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.nombre)

class FichaTecnica(models.Model):
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    descripcion = models.CharField(max_length=100)
    version = models.CharField(max_length=30)
    lenguaje = models.CharField(max_length=30)
    urlAcceso = models.CharField(max_length=30)
    sistemaOperativo = models.CharField(max_length=30)
    tamanio = models.FloatField(max_length=30)
    empaquetamiento = models.CharField(max_length=30)
    politicaBackup = models.CharField(max_length=30)
    def __str__(self):
        return '%s-%s' % (self.aplicacion, self.version)


class EntidadNegocio(models.Model):
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.nombre)

class Servidor(models.Model):
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    tipo = models.CharField(max_length=30)
    capacidad = models.FloatField(max_length=30)
    estado = models.BooleanField(max_length=30)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
    def __str__(self):
        return '%s-%s' % (self.aplicacion, self.tipo)

class BaseDatos(models.Model):
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    tipo = models.CharField(max_length=30)
    capacidad = models.FloatField(max_length=30)
    puerto = models.CharField(max_length=30)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
    def __str__(self):
        return '%s-%s' % (self.aplicacion, self.tipo)

class Tecnologia(models.Model):
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    version = models.CharField(max_length=30)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.nombre)

class ClienteApp(models.Model):
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    version = models.CharField(max_length=30)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.nombre)

class ServicioWeb(models.Model):
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.nombre)

class Conexion(models.Model):
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    descripcion = models.CharField(max_length=100)
    aplicacionEntrante = models.ForeignKey(Aplicacion, on_delete=models.CASCADE, related_name='%(class)s_aplicacionEntrante')
    aplicacionSaliente = models.ForeignKey(Aplicacion, on_delete=models.CASCADE, related_name='%(class)s_aplicacionSaliente')
    def __str__(self):
        return '%s-%s' % (self.aplicacionEntrante, self.aplicacionSaliente)


class ComponenteTecnologico(models.Model):
    id = models.BigIntegerField(null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    conexion = models.ForeignKey(Conexion, on_delete=models.CASCADE)
    def __str__(self):
        return '%s-%s' % (self.nombre, self.conexion)
