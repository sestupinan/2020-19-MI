from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)
    def __str__(self):
        return '%s' % (self.nombre)

class Atributo(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False, default=None, primary_key=True)
    tipo = models.CharField(max_length=30)
    clase=models.ForeignKey(Clase, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.nombre)

class Relacion(models.Model):
    clase_saliente = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='%(class)s_claseSaliente')
    clase_entrante = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='%(class)s_claseEntrante')
    rol = models.CharField(max_length=30, null=False, blank=False, default=None, primary_key=True)
    cardinalidad = models.CharField(max_length=30)

    def __str__(self):
        return '%s-%s' % (self.clase_saliente, self.clase_entrante)