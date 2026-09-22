from django import forms
from .models import Prospecto

class ProspectoForm(forms.ModelForm):
    class Meta:
        model = Prospecto
        fields = ['nombre', 'apellido', 'email', 'zona', 'tipo_inmueble', 'telefono', 'preferencia_contacto', 'mensaje']
        
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Opcional: Detalles breves de lo que busca...'}),
        }