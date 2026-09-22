from django.shortcuts import render, redirect
from .forms import ProspectoForm
import urllib.parse  # Esto sirve para convertir espacios y tildes a formato web

def pagina_inicio(request):
    if request.method == 'POST':
        formulario = ProspectoForm(request.POST)
        if formulario.is_valid():
            # Guardamos el formulario y lo metemos en una variable para extraer sus datos
            prospecto = formulario.save()
            
            # 1. El número de WhatsApp del vendedor
            # Tiene que empezar con 549 (código de Argentina y celular) y no llevar espacios ni guiones.
            numero_whatsapp = "5492974171484"
            
            # 2. mensaje dinámico inteligente
            mensaje = f"¡Hola! Acabo de completar el formulario en la web. Mi nombre es {prospecto.nombre} y estoy interesado en buscar un/a {prospecto.get_tipo_inmueble_display()} en la zona de {prospecto.get_zona_display()}."
            
            # 3. Codificamos el texto para que los espacios se conviertan en %20 (formato de links)
            mensaje_codificado = urllib.parse.quote(mensaje)
            
            # 4. Creamos el link de WhatsApp
            link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensaje_codificado}"
            
            # 5. En vez de mostrar un texto blanco, lo pateamos directo a WhatsApp
            return redirect(link_whatsapp)
    else:
        formulario = ProspectoForm()
    
    return render(request, 'inicio.html', {'formulario': formulario})