from django.contrib import admin
from contacto.models import Contacto,EstadosMunicipios

from import_export.admin import ExportMixin,ImportExportModelAdmin,ImportExportActionModelAdmin,ExportActionModelAdmin , \
    ImportExportMixin

class EstadosMunicipiosAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
  list_display = ('nombre_estado','nombre_municipio')
  search_fields = ('nombre_estado','nombre_municipio')
  list_filter = ('nombre_estado',)
  list_display_links = ('nombre_estado','nombre_municipio')

class ContactoAdmin(admin.ModelAdmin):
  list_display = ('nombre','apaterno','amaterno','correo')


admin.site.register(Contacto,ContactoAdmin)
admin.site.register(EstadosMunicipios,EstadosMunicipiosAdmin)