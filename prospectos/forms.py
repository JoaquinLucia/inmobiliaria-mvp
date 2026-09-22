from django import forms
from .models import Prospecto

class ProspectoForm(forms.ModelForm):
    class Meta:
        model = Prospecto
        fields = ['nombre', 'apellido', 'zona', 'telefono', 'preferencia_contacto', 'mensaje']