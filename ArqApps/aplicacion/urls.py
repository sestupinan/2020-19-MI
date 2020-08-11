from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('aplicaciones/', views.apps_list),
    path('aplicacioncreate/', csrf_exempt(views.aplicacion_create), name='aplicacionCreate'),

    path('fichastecnicas/', views.fichatecnica_list),
    path('fichatecnicacreate/', csrf_exempt(views.fc_create), name='fichatecnicaCreate'),

    path('basesdedatos/', views.basedatos_list),
    path('basedatoscreate/', csrf_exempt(views.basedatos_create), name='basedatosCreate'),

    path('clienteapp/', views.clienteapp_list),
    path('clienteappcreate/', csrf_exempt(views.clienteapp_create), name='clienteappCreate'),

    path('comptec/', views.comptecnologico_list),
    path('compteccreate/', csrf_exempt(views.comptecnologico_create), name='componentetecnologicocreate'),

    path('conexion/', views.conexion_list),
    path('conexioncreate/', csrf_exempt(views.conexion_create), name='conexionCreate'),

    path('entnegocio/', views.entnegocio_list),
    path('entnegociocreate/', csrf_exempt(views.entnegocio_create), name='entidadnegocioCreate'),

    path('servicioweb/', views.servicioweb_list),
    path('serviciowebcreate/', csrf_exempt(views.servicioweb_create), name='serviciowebCreate'),

    path('servidores/', views.servidor_list),
    path('servidorcreate/', csrf_exempt(views.servidor_create), name='servidorCreate'),

    path('tecnologia/', views.tecnologia_list),
    path('tecnologiacreate/', csrf_exempt(views.tecnologia_create), name='tecnologiaCreate'),

]