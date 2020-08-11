from django.contrib import admin
from .models import Aplicacion, FichaTecnica, Conexion, BaseDatos, ClienteApp, ComponenteTecnologico, EntidadNegocio, ServicioWeb, Servidor, Tecnologia

# Register your models here.
admin.site.register(Aplicacion)
admin.site.register(FichaTecnica)
admin.site.register(Conexion)
admin.site.register(BaseDatos)
admin.site.register(ClienteApp)
admin.site.register(ComponenteTecnologico)
admin.site.register(EntidadNegocio)
admin.site.register(ServicioWeb)
admin.site.register(Servidor)
admin.site.register(Tecnologia)

