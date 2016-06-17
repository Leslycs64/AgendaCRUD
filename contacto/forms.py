# encoding:utf-8
from django import forms
apaterno = '"apaterno"'
class FormContacto ( forms.Form ) :
  nombre = forms.CharField ( widget=forms.TextInput (attrs={
    'class':'nombre',
    'onblur':'getElementByName('+apaterno+').value=21',
  }) , label='Nombre' , required=True )
  apaterno = forms.CharField ( widget=forms.TextInput (attrs={'class':'apaterno',
                                                              'onblur':'alert(1);'}) , label='Apellido Parterno')
  amaterno = forms.CharField ( widget=forms.TextInput(attrs={'class':'amaterno','disabled': 'disabled'}) , label='Apellido Materno')
  correo = forms.CharField ( widget=forms.TextInput (attrs={'class':'correo','disabled': 'disabled'}) , label='Correo Electrónico', required=True )
  telefono = forms.CharField ( widget=forms.TextInput (attrs={'class':'telefono','disabled': 'disabled'}) , label='Teléfono' )

#'disabled': 'disabled',