#buscar en la BD

from django import forms

class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(label="Buscar accesorio", max_length=100)

    
