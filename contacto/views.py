# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response , render
from django.template import RequestContext
from django.template.context_processors import csrf
from contacto.export_contacto_pdf import ExportarContactoPDF
from .forms import FormContacto
from .models import Contacto

def main(request):
  formulario = FormContacto()
  title = ':: Agenda'
  contexto = {
    'title': title,
    'formulario': formulario,
  }
  contexto.update(csrf(request))
  return render_to_response('contacto_main.html',contexto,context_instance=RequestContext(request))

def GuardaContacto(request):
  title = '::Guardando Contacto'
  if request.method == 'POST':
    frmContacto = FormContacto(request.POST or None)

    if frmContacto.is_valid():
      contacto = Contacto (
        nombre = request.POST.get('nombre'),
        apaterno = request.POST.get('apaterno'),
        amaterno = request.POST.get('amaterno'),
        correo = request.POST.get('correo'),
        telefono = request.POST.get('telefono'),
      )

      contacto.save()

      contexto={
        'title': 'Contacto guardado',
        'contenido': 'Contacto Guardado Correctamente'
      }
      return render_to_response('contacto_guardado.html',contexto)

    else:
      contexto ={
        'title': '::Error',
        'contenido':'Revisa la información, parece que no es válida'
      }
      contexto.update(csrf(request))
      return render_to_response('contacto_main.html',contexto,context_instance=RequestContext(request))
  else:
    formulario = FormContacto
    contexto={
      'title': 'Nuevo Contacto',
      'formulario': formulario,
    }
    contexto.update(csrf(request))
    return render_to_response('contacto_main.html',contexto,context_instance=RequestContext(request))

def ListaContactos(request):
  todos = Contacto.objects.all()
  title = ':: Lista de Contactos'
  contexto = {
    'title': title,
    'lista':todos
  }
  return render_to_response('contacto_lista_todos.html',contexto)


def EditarContacto(request):
  contacto = Contacto.objects.get(id=request.GET['id'])
  form = FormContacto({
    'nombre': contacto.nombre,
    'apaterno': contacto.apaterno,
    'amaterno': contacto.amaterno,
    'correo': contacto.correo,
    'telefono': contacto.telefono
  })
  contexto = {
  'formulario': form,
  'contacto':contacto
  }
  contexto.update(csrf(request))

  return render_to_response('contacto_edita.html',contexto)

def ActualizaContacto(request):
  title = '::Actualizando Contacto'
  if request.method == 'POST':
    frmContacto = FormContacto(request.POST or None)

    if frmContacto.is_valid():
      contacto = Contacto.objects.get(id = request.POST['id'])
      contacto.nombre = request.POST['nombre']
      contacto.apaterno = request.POST [ 'apaterno' ]
      contacto.amaterno = request.POST [ 'amaterno' ]
      contacto.correo = request.POST [ 'correo' ]
      contacto.telefono = request.POST [ 'telefono' ]
      contacto.save()

      contexto={
        'title': 'Contacto guardado',
        'contenido': 'Contacto Guardado Correctamente',
        'contacto':contacto
      }
      return render_to_response('contacto_guardado.html',contexto)

    else:
      contexto ={
        'title': '::Error',
        'contenido':'Revisa la información, parece que no es válida'
      }
      contexto.update(csrf(request))
      return render_to_response('contacto_main.html',contexto,context_instance=RequestContext(request))
  else:
    formulario = FormContacto
    contexto={
      'title': 'Nuevo Contacto',
      'formulario': formulario
    }
    contexto.update(csrf(request))
    return render_to_response('contacto_main.html',contexto,context_instance=RequestContext(request))

def EliminarContacto ( request ) :
  title = '::Eliminando Contacto'

  if request.method == 'GET' :
    contacto = Contacto.objects.get ( id=request.GET [ 'id' ] )
    print contacto
    contacto.delete()

    contexto = {
      'title' : 'Contacto Eliminado' ,
      'contenido' : 'Contacto Eliminado Correctamente' ,
    }
    return render_to_response ( 'contacto_guardado.html' , contexto )

  else :
    contexto = {
      'title' : '::Error' ,
      'contenido' : 'Revisa la información, parece que no es válida'
    }
    return render_to_response ( 'contacto_lista_todos.html' , contexto , context_instance=RequestContext ( request ) )

from reportlab.pdfgen import canvas

def ExportarContacto(request):
  title = '::Exportar Contacto a PDF'

  if request.method == 'GET' :
    contacto = Contacto.objects.get ( id=request.GET [ 'id' ] )
    pdf = ExportarContactoPDF(contacto)
    return pdf

  else :
    contexto = {
      'title' : '::Error' ,
      'contenido' : 'Revisa la información, parece que no es válida'
    }
    return render_to_response ( 'base.html' , contexto , context_instance=RequestContext ( request ) )