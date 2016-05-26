# encoding:utf-8
from django import forms

class FormContacto ( forms.Form ) :
  nombre = forms.CharField ( widget=forms.TextInput (attrs={'class':'nombre'} ) , label='Nombre' , required=True )
  apaterno = forms.CharField ( widget=forms.TextInput (attrs={'class':'apaterno'}) , label='Apellido Parterno')
  amaterno = forms.CharField ( widget=forms.TextInput(attrs={'class':'amaterno'}) , label='Apellido Materno')
  correo = forms.CharField ( widget=forms.TextInput (attrs={'class':'correo'}) , label='Correo Electrónico', required=True )
  telefono = forms.CharField ( widget=forms.TextInput (attrs={'class':'telefono'}) , label='Teléfono' )

  # class Meta:
  #   model = Contacto
  #   fields = ('nombre','apaterno','amaterno','correo','telefono')

  # def save(self,commit=True):
  #   contacto = super(Contacto,self).save(commit=False)
  #
  #   contacto.save()
  #   return contacto