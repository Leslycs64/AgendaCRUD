# encoding:utf-8
from django import forms

class FormContacto ( forms.Form ) :
  nombre = forms.CharField ( widget=forms.TextInput (attrs={
    'class':'nombre',
    'onblur':'enablePaterno();',
  }) , label='Nombre' , required=True )

  apaterno = forms.CharField ( widget=forms.TextInput (attrs={
    'class':'apaterno',
    'disabled': 'disabled',
    'onblur':'enableMaterno();'
  }) , label='Apellido Parterno')

  amaterno = forms.CharField ( widget=forms.TextInput(attrs={
    'class':'amaterno',
    'disabled': 'disabled',
    'onblur' : 'enableCorreo();'
  }) , label='Apellido Materno')

  correo = forms.CharField ( widget=forms.TextInput (attrs={
    'class':'correo',
    'disabled': 'disabled',
    'onblur' : 'enableTelefono();'
  }) , label='Correo Electrónico', required=True )

  telefono = forms.CharField ( widget=forms.TextInput (attrs={
    'class':'telefono',
    'disabled': 'disabled'
  }) , label='Teléfono' )
