from django import forms
from .models import Modulo, Contenido

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['titulo', 'descripcion', 'orden', 'publicado']

class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = ['titulo', 'descripcion', 'tipo', 'archivo', 'imagen', 'url_video', 'orden']
