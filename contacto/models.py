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





