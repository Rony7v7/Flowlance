from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estrellas', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Añadir un comentario'}),
        }
