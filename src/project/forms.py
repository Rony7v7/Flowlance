from django import forms
from .models import Project, Event
from django.utils.translation import gettext as _
from .models import ProjectReportSettings

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start', 'end', 'description']  
        widgets = {
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

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
            "image",
        ]
        labels = {
            'title': _('Titulo del Proyecto'),
            'description': _('Descripción'),
            'requirements': _('Requerimientos'),
            'budget': _('Presupuesto'),
            'start_date': _('Fecha de Inicio'),
            'end_date': _('Fecha de Finalización'),
            'image': _('Imagen'),
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
            "image": forms.FileInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "nombre del proyecto",
                }
            ),
            
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if end_date and start_date and end_date <= start_date:
            self.add_error('end_date', "Your starting date must be before your ending date.")

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5 MB
                raise forms.ValidationError("El archivo es demasiado grande ( > 5 MB ).")
            if not image.content_type in ["image/jpeg", "image/png"]:
                raise forms.ValidationError("El archivo debe ser JPEG o PNG.")
        return image


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

from .models import ProjectUpdate

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = ProjectUpdate
        fields = ['content', 'is_important']  
