# -*- encoding: utf-8 -*-
from io import BytesIO
from django.conf import settings
import os
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from django.shortcuts import HttpResponse
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table
from contacto.models import Contacto


def ExportarContactoPDF(_contacto):
    contacto = Contacto.objects.filter(id = _contacto.id)

    if contacto.__len__() == 0:
        response = HttpResponse(content_type='application/pdf')
        pdf_name = "datos_contacto_"+str(contacto.id)+".pdf"  # llamado clientes
        buff = BytesIO()
        estilo = getSampleStyleSheet()
        pdf = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=10,
                            bottomMargin=10,)
        contenido = []
        banner = Image(settings.MEDIA_ROOT+"images/banner.jpg")
        ancho = A4[0]-1*inch
        banner.drawHeight = ancho * banner.drawHeight/banner.drawWidth
        banner.drawWidth = ancho
        contenido.append(banner)
        contenido.append(Spacer(0, inch*.2))
        tabla = Paragraph("No hay datos disponibles.",estilo['Heading1'])
        contenido.append(tabla)

    else:
        response = HttpResponse(content_type='application/pdf')
        # pdf_name = "datos_contacto_%s.pdf" % (contacto.id)  # llamado clientes
        buff = BytesIO()
        estilo = getSampleStyleSheet()
        pdf = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=10,
                            bottomMargin=10,)
        contenido = []

        banner = Image ( settings.MEDIA_ROOT + "images/banner.jpg" )
        ancho = A4[0]-1*inch
        banner.drawHeight = ancho * banner.drawHeight/banner.drawWidth
        banner.drawWidth = ancho
        contenido.append(banner)
        contenido.append(Spacer(0, inch*.2))
        es_titulo = estilo['Heading1']
        es_titulo.alignment=TA_CENTER
        titulo = Paragraph("Datos de contacto: ", es_titulo)
        contenido.append(titulo)
        contenido.append(Spacer(0, inch*.2))
        nombre = Paragraph('Nombre: %s' % (contacto[0]),estilo['Heading2'])
        contenido.append(nombre)
        correo = Paragraph('Correo: %s' % (contacto[0].correo),estilo['Heading2'])
        contenido.append(correo)
        telefono = Paragraph('Tel&eacute;fono: %s' % (contacto[0].telefono),estilo['Heading2'])
        contenido.append(telefono)

    pdf.build(contenido)
    response.write(buff.getvalue())
    buff.close()
    return response