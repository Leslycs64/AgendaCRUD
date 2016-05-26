from django.contrib import admin
from contacto.models import Contacto

class ContactoAdmin(admin.ModelAdmin):
  list_display = ('nombre','apaterno','amaterno','correo')


admin.site.register(Contacto,ContactoAdmin)
