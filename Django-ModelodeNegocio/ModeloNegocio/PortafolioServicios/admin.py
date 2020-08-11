from django.contrib import admin
from .models import ServicioNegocio, Actor, ObjetoNegocio, Operacion
# Register your models here.
admin.site.register(ServicioNegocio)
admin.site.register(Actor)
admin.site.register(ObjetoNegocio)
admin.site.register(Operacion)