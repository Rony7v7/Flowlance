from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "requirements",
            "budget",
            "start_date",
            "end_date",
        ]
        labels = {
            'title': 'Titulo del Proyecto',
            'description': 'Descripción',
            'requirements': 'Requerimientos',
            'budget': 'Presupuesto',
            'start_date': 'Fecha de Inicio',
            'end_date': 'Fecha de Finalización',
        }
        widgets = {
            "start_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md ",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md  "},
                ),
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md ",
                    "placeholder": "nombre del proyecto",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "especificaciones del proyecto",
                    "rows": 4,
                }
            ),
            "requirements": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "requerimientos del proyecto",
                    "rows": 4,
                }
            ),
            "budget": forms.NumberInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "presupuesto del proyecto",
                }
            ),
        }
