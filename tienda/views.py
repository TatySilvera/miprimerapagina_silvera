#inicio
from django.shortcuts import render
from .models import Necesser, ArticuloBebé, Estuche 

def inicio(request):
    # clases 
    lista_necesseres = Necesser.objects.all()
    lista_bebes = ArticuloBebé.objects.all()
    lista_estuches = Estuche.objects.all()
    
    contexto = {
        'necesseres': lista_necesseres,
        'articulos_bebe': lista_bebes,
        'estuches': lista_estuches, 
    }
    return render(request, 'tienda/inicio.html', contexto)

def buscar_producto(request):
    query = request.GET.get('nombre', '')
    productos = []
    if query:
        # Esto busca en las tres categorías
        necesseres = Necesser.objects.filter(nombre__icontains=query)
        bebes = ArticuloBebé.objects.filter(nombre__icontains=query)
        estuches = Estuche.objects.filter(nombre__icontains=query)
        
        # Juntamos todo en una sola lista para el buscador
        productos = list(necesseres) + list(bebes) + list(estuches)
        
    return render(request, 'tienda/buscar.html', {'productos': productos, 'query': query})