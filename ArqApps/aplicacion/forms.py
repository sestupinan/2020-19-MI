from django import forms
from .models import Aplicacion, FichaTecnica, Conexion, BaseDatos, ClienteApp, ComponenteTecnologico, EntidadNegocio, ServicioWeb, Servidor, Tecnologia

class AplicacionForm(forms.ModelForm):
    class Meta:
        model = Aplicacion
        fields = [
            'id',
            'nombre',
        ]

        labels = {
            'id' : 'ID',
            'nombre' : 'Nombre',
        }

class FichaTecnicaForm(forms.ModelForm):
    class Meta:
        model = FichaTecnica
        fields = [
            'id',
            'descripcion',
            'version',
            'lenguaje',
            'urlAcceso',
            'sistemaOperativo',
            'tamanio',
            'empaquetamiento',
            'politicaBackup',
        ]

        labels = {
            'id' : 'id',
            'descripcion' : 'descripcion',
            'version' : 'version',
            'lenguaje' : 'lenguaje',
            'urlAcceso':'urlAcceso',
            'sistemaOperativo': 'sistemaOperativo',
            'tamanio': 'tamanio',
            'empaquetamiento': 'empaquetamiento',
            'politicaBackup': 'politicaBackup',
        }

class ConexionForm(forms.ModelForm):
    class Meta:
        model = Conexion
        fields = [
            'id',
            'descripcion',
            'aplicacionEntrante',
            'aplicacionSaliente',
        ]

        labels = {
            'id' : 'ID',
            'descripcion' : 'descripcion',
            'aplicacionEntrante': 'aplicacionEntrante',
            'aplicacionSaliente': 'aplicacionSaliente',
        }

class BaseDatosForm(forms.ModelForm):
    class Meta:
        model = BaseDatos
        fields = [
            'id',
            'tipo',
            'capacidad',
            'puerto',
            'aplicacion',
        ]

        labels = {
            'id' : 'ID',
            'tipo' : 'tipo',
            'capacidad': 'capacidad',
            'puerto': 'puerto',
            'aplicacion': 'aplicacion',
        }


class ClienteAppForm(forms.ModelForm):
    class Meta:
        model = ClienteApp
        fields = [
            'id',
            'nombre',
            'descripcion',
            'version',
            'aplicacion',
        ]

        labels = {
            'id': 'ID',
            'nombre': 'nombre',
            'descripcion': 'descripcion',
            'version': 'version',
            'aplicacion': 'aplicacion',
        }

class ComponenteTecnologicoForm(forms.ModelForm):
    class Meta:
        model = ComponenteTecnologico
        fields = [
            'id',
            'nombre',
            'descripcion',
            'conexion',
        ]

        labels = {
            'id': 'ID',
            'nombre': 'nombre',
            'descripcion': 'descripcion',
            'conexion': 'conexion',
        }

class EntidadNegocioForm(forms.ModelForm):
    class Meta:
        model = EntidadNegocio
        fields = [
            'id',
            'nombre',
            'aplicacion',
        ]

        labels = {
            'id': 'ID',
            'nombre': 'nombre',
            'aplicacion': 'aplicacion',
        }

class ServicioWebForm(forms.ModelForm):
    class Meta:
        model = ServicioWeb
        fields = [
            'id',
            'nombre',
            'descripcion',
            'aplicacion',
        ]

        labels = {
            'id': 'ID',
            'nombre': 'nombre',
            'descripcion': 'descripcion',
            'aplicacion': 'aplicacion',
        }

class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = [
            'id',
            'tipo',
            'capacidad',
            'estado',
            'aplicacion',
        ]

        labels = {
            'id': 'ID',
            'tipo': 'tipo',
            'capacidad': 'capacidad',
            'estado': 'estado',
            'aplicacion': 'aplicacion',
        }

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = [
            'id',
            'nombre',
            'descripcion',
            'version',
            'aplicacion',
        ]

        labels = {
            'id': 'ID',
            'nombre': 'nombre',
            'descripcion': 'descripcion',
            'version': 'version',
            'aplicacion': 'aplicacion',
        }