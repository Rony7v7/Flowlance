from django import forms
from .models import Project
from django.utils.translation import gettext as _
from .models import ProjectReportSettings

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
            'title': _('Titulo del Proyecto'),
            'description': _('Descripción'),
            'requirements': _('Requerimientos'),
            'budget': _('Presupuesto'),
            'start_date': _('Fecha de Inicio'),
            'end_date': _('Fecha de Finalización'),
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


class ProjectReportSettingsForm(forms.ModelForm):
    class Meta:
        model = ProjectReportSettings
        fields = [
            'include_milestone_progress',
            'include_task_progress',
            'include_milestones_and_tasks',
            'include_kanban_board',
            'include_gantt_chart',
            'report_frequency'
        ]
        widgets = {
            'report_frequency': forms.Select(choices=ProjectReportSettings.report_frequency.field.choices)
        }