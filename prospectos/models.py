from django.db import models

class Prospecto(models.Model):
    OPCIONES_CONTACTO = [
        ('email', 'Por email'),
        ('telefono', 'Por teléfono'),
        ('whatsapp', 'Por WhatsApp'),
    ]
    
    ZONAS_INTERES = [
        ('centro_bajadas', 'Centro / Bajadas 1 a 3'),
        ('terraza_mar', 'Terraza al Mar / Los Acantilados'),
        ('barrio_peumayen', 'Barrio Peumayén / Zona Sur'),
        ('san_antonio', 'San Antonio Oeste'),
        ('otros', 'Otras zonas'),
    ]

    TIPO_INMUEBLE = [
        ('depto', 'Departamento'),
        ('casa', 'Casa'),
        ('duplex', 'Dúplex'),
        ('local', 'Local Comercial'),
        ('terreno', 'Lote / Terreno'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(default="")
    zona = models.CharField(max_length=50, choices=ZONAS_INTERES, default='centro_bajadas')
    
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE, default='depto') 
    
    telefono = models.CharField(max_length=20)
    preferencia_contacto = models.CharField(max_length=20, choices=OPCIONES_CONTACTO)
    
    mensaje = models.TextField(blank=True) 
    
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.get_zona_display()}"