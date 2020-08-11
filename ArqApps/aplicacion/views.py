from django.shortcuts import render
from .aplicacion_logic.aplicacion_logic import create_fichatecnica, create_object, get_aplicaciones, get_basedatos, get_clienteapp, get_comptecnologico, get_conexiones, get_entnegocio, get_fichatecnica, get_servicioweb, get_servidor, get_tecnologia
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AplicacionForm, BaseDatosForm, TecnologiaForm, ServidorForm, ServicioWebForm, FichaTecnicaForm, EntidadNegocioForm, ConexionForm, ComponenteTecnologicoForm, ClienteAppForm



# Create your views here.
def apps_list(request):
    apps = get_aplicaciones()
    context = {
    'apps_list': apps,
    }
    return render(request, 'Aplicacion/aplicacion.html', context)

def aplicacion_create(request):
    if request.method == 'POST':
        form = AplicacionForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('aplicacionCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('aplicacionCreate'))
        else:
            print(form.errors)
    else:
        form = AplicacionForm()
    context = {
        'form': form,
    }
    return render(request, 'Aplicacion/aplicacionCreate.html', context)

def fichatecnica_list(request):
    lista = get_fichatecnica()
    context = {
    'fc_list': lista,
    }
    return render(request, 'FichaTecnica/fichatecnica.html', context)

def fc_create(request):
    if request.method == 'POST':
        form = FichaTecnicaForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('fichatecnicaCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('fichatecnicaCreate'))
        else:
            print(form.errors)
    else:
        form = FichaTecnicaForm()
    context = {
        'form': form,
    }
    return render(request, 'FichaTecnica/fichatecnicaCreate.html', context)

def basedatos_list(request):
    lista = get_basedatos()
    context = {
    'basedatos_list': lista,
    }
    return render(request, 'BaseDatos/basedatos.html', context)

def basedatos_create(request):
    if request.method == 'POST':
        form = BaseDatosForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('basedatosCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('basedatosCreate'))
        else:
            print(form.errors)
    else:
        form = BaseDatosForm()
    context = {
        'form': form,
    }
    return render(request, 'BaseDatos/basedatosCreate.html', context)

def clienteapp_list(request):
    lista = get_clienteapp()
    context = {
    'clienteapp_list': lista,
    }
    return render(request, 'ClienteApp/clienteapp.html', context)

def clienteapp_create(request):
    if request.method == 'POST':
        form = ClienteAppForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('clienteappCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('clienteappCreate'))
        else:
            print(form.errors)
    else:
        form = ClienteAppForm()
    context = {
        'form': form,
    }
    return render(request, 'ClienteApp/clienteappCreate.html', context)

def comptecnologico_list(request):
    lista = get_comptecnologico()
    context = {
    'comptecnologico_list': lista,
    }
    return render(request, 'ComponenteTecnologico/componentetecnologico.html', context)

def comptecnologico_create(request):
    if request.method == 'POST':
        form = ComponenteTecnologicoForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('componentetecnologicocreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('componentetecnologicocreate'))
        else:
            print(form.errors)
    else:
        form = ComponenteTecnologicoForm()
    context = {
        'form': form,
    }
    return render(request, 'ComponenteTecnologico/componentetecnologicocreate.html', context)

def conexion_list(request):
    lista = get_conexiones()
    context = {
    'conexion_list': lista,
    }
    return render(request, 'Conexion/conexion.html', context)

def conexion_create(request):
    if request.method == 'POST':
        form = ConexionForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('conexionCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('conexionCreate'))
        else:
            print(form.errors)
    else:
        form = ConexionForm()
    context = {
        'form': form,
    }
    return render(request, 'Conexion/conexionCreate.html', context)

def entnegocio_list(request):
    lista = get_entnegocio()
    context = {
    'entnegocio_list': lista,
    }
    return render(request, 'EntidadNegocio/entidadnegocio.html', context)

def entnegocio_create(request):
    if request.method == 'POST':
        form = EntidadNegocioForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('entidadnegocioCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('entidadnegocioCreate'))
        else:
            print(form.errors)
    else:
        form = EntidadNegocioForm()
    context = {
        'form': form,
    }
    return render(request, 'EntidadNegocio/entidadnegocioCreate.html', context)

def servicioweb_list(request):
    lista = get_servicioweb()
    context = {
    'servicioweb_list': lista,
    }
    return render(request, 'ServicioWeb/servicioweb.html', context)

def servicioweb_create(request):
    if request.method == 'POST':
        form = ServicioWebForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('serviciowebCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('serviciowebCreate'))
        else:
            print(form.errors)
    else:
        form = ServicioWebForm()
    context = {
        'form': form,
    }
    return render(request, 'ServicioWeb/serviciowebCreate.html', context)

def servidor_list(request):
    lista = get_servidor()
    context = {
    'servidor_list': lista,
    }
    return render(request, 'Servidor/servidor.html', context)

def servidor_create(request):
    if request.method == 'POST':
        form = ServidorForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('servidorCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('servidorCreate'))
        else:
            print(form.errors)
    else:
        form = ServidorForm()
    context = {
        'form': form,
    }
    return render(request, 'Servidor/servidorCreate.html', context)

def tecnologia_list(request):
    lista = get_tecnologia()
    context = {
    'tecnologia_list': lista,
    }
    return render(request, 'Tecnologia/tecnologia.html', context)

def tecnologia_create(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST)
        if form.is_valid():
            rta=create_object(form)
            if rta=='Objeto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('tecnologiaCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('tecnologiaCreate'))
        else:
            print(form.errors)
    else:
        form = TecnologiaForm()
    context = {
        'form': form,
    }
    return render(request, 'Tecnologia/tecnologiaCreate.html', context)