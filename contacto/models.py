# -*- encoding: utf-8 -*-
from django.db import models

class Contacto(models.Model):
  nombre = models.CharField(max_length=60,blank=False,help_text="NOMBRE")
  apaterno = models.CharField(max_length=60, blank=True,help_text="APELLIDO PATERNO")
  amaterno = models.CharField(max_length=60,blank=True,help_text="APELLIDO MATERNO")
  correo = models.EmailField(help_text="CORREO ELECTRÓNICO",max_length=150)
  telefono = models.CharField(max_length=60,blank=True,help_text="TELÉFONO")

  def __unicode__(self):
    return self.nombre+' '+self.apaterno+' '+self.amaterno

# class EstadosMunicipios(models.Model):
#   CVE_ENT = models.IntegerField(default=0,help_text="Clave del Estado")
#   NOM_ENT = models.CharField(max_length=255,help_text="Nombre del Estado")
#   NOM_ABR = models.CharField(max_length=50,help_text="Abreviatura del Estado")
#   CVE_MUN = models.IntegerField(default=0,help_text="Clave del Municipio")
#   NOM_MUN = models.CharField(max_length=255,help_text="Nombre del Municipio")
#   CVE_LOC = models.IntegerField(default=0,help_text="Clave de la Localidad")
#   NOM_LOC = models.CharField(max_length=255,help_text="Nombre de la Localidad")
#   AMBITO = models.CharField(max_length=10,help_text="Tipo de ambito")
#
#   def __unicode__(self):
#     return self.NOM_ENT+' '+self.NOM_MUN


class EstadosMunicipios(models.Model):
  clave_estado = models.IntegerField(default=0)
  nombre_estado = models.CharField(max_length=150,help_text = 'Estado')
  clave_municipio = models.IntegerField(default=0)
  nombre_municipio = models.CharField(max_length=150,help_text='Municipio')

  def __unicode__(self):
    return 'Estado: %s - Municipio: %s'% (self.nombre_estado,self.nombre_municipio)

