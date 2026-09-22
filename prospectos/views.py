from django.shortcuts import render, HttpResponse
from .forms import ProspectoForm

def pagina_inicio(request):
    if request.method == 'POST':
        formulario = ProspectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponse("¡Gracias! Tus datos se enviaron a la base de datos del administrador.")
    else:
        formulario = ProspectoForm()
    
    return render(request, 'inicio.html', {'formulario': formulario})