from django.db import models

class Prospecto(models.Model):
    OPCIONES_CONTACTO = [
        ('email', 'Por email'),
        ('telefono', 'Por teléfono'),
        ('whatsapp', 'Por WhatsApp'),
    ]
    
    ZONAS_INTERES = [
        ('comodoro_centro', 'Centro de Comodoro'),
        ('zona_norte', 'Zona Norte / Km 3'),
        ('zona_sur', 'Zona Sur / Rada Tilly'),
        ('otros', 'Otras zonas de Chubut'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    zona = models.CharField(max_length=50, choices=ZONAS_INTERES, default='comodoro_centro')
    telefono = models.CharField(max_length=20)
    preferencia_contacto = models.CharField(max_length=20, choices=OPCIONES_CONTACTO)
    mensaje = models.TextField(blank=True, help_text="¿Qué tipo de inmueble busca? (Casa, depto, local)")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.get_zona_display()}"