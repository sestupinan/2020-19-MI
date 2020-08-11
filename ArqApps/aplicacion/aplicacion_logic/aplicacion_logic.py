from ..models import Aplicacion, FichaTecnica, Conexion, BaseDatos, ClienteApp, ComponenteTecnologico, EntidadNegocio, ServicioWeb, Servidor, Tecnologia

def get_aplicaciones():
    objects=Aplicacion.objects.all()
    return objects

def create_object(form):
    object=form.save()
    object.save()
    msg='Objeto creado'

    return msg

def get_fichatecnica():
    objects=FichaTecnica.objects.all()
    return objects

def create_fichatecnica(form):
    object=form.save()
    object.save()
    msg='Objeto creado'

    return msg

def get_conexiones():
    objects=Conexion.objects.all()
    return objects

def get_basedatos():
    objects=BaseDatos.objects.all()
    return objects

def get_clienteapp():
    objects=ClienteApp.objects.all()
    return objects

def get_comptecnologico():
    objects=ComponenteTecnologico.objects.all()
    return objects

def get_entnegocio():
    objects=EntidadNegocio.objects.all()
    return objects

def get_servicioweb():
    objects=ServicioWeb.objects.all()
    return objects

def get_servidor():
    objects=Servidor.objects.all()
    return objects

def get_tecnologia():
    objects=Tecnologia.objects.all()
    return objects