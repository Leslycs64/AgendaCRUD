# encoding:utf-8
from django import forms
from contacto.models import EstadosMunicipios


class SelectEstadoMunicipio ( forms.Form ) :
  estado = forms.ModelChoiceField (
    queryset=EstadosMunicipios.objects.distinct().values_list('nombre_estado',flat=True),
    empty_label=' -- Selecciona -- ' ,
    label= 'Estado',
    to_field_name='estado',
    widget=forms.Select ( attrs={
      'onchange' : 'getMunicipio()'
    } )
  )
  municipio = forms.ModelChoiceField (
    queryset=EstadosMunicipios.objects.values_list ( 'nombre_municipio',flat=True ) ,
    empty_label=' -- Selecciona -- '
  )


class FormContacto ( forms.Form ) :
  nombre = forms.CharField ( widget=forms.TextInput ( attrs={
    'class' : 'nombre' ,
    'onblur' : 'enablePaterno();' ,
  } ) , label='Nombre' , required=True )

  apaterno = forms.CharField ( widget=forms.TextInput ( attrs={
    'class' : 'apaterno' ,
    'disabled' : 'disabled' ,
    'onblur' : 'enableMaterno();'
  } ) , label='Apellido Parterno' )

  amaterno = forms.CharField ( widget=forms.TextInput ( attrs={
    'class' : 'amaterno' ,
    'disabled' : 'disabled' ,
    'onblur' : 'enableCorreo();'
  } ) , label='Apellido Materno' )

  correo = forms.CharField ( widget=forms.TextInput ( attrs={
    'class' : 'correo' ,
    'disabled' : 'disabled' ,
    'onblur' : 'enableTelefono();'
  } ) , label='Correo Electrónico' , required=True )

  telefono = forms.CharField ( widget=forms.TextInput ( attrs={
    'class' : 'telefono' ,
    'disabled' : 'disabled'
  } ) , label='Teléfono' )
