from django.contrib import admin
from .models import Prospecto

class ProspectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'tipo_inmueble', 'zona', 'fecha_registro')
    

    list_filter = ('tipo_inmueble', 'zona', 'preferencia_contacto', 'fecha_registro')
    

    search_fields = ('nombre', 'apellido', 'email', 'telefono')
    

    ordering = ('-fecha_registro',)
    
    readonly_fields = ('fecha_registro',)

admin.site.register(Prospecto, ProspectoAdmin)