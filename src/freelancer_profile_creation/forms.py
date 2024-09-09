from django import forms
from .models import PortfolioProject, CurriculumVitae, Curso

class PortfolioProjectForm(forms.ModelForm):
    class Meta:
        model = PortfolioProject
        fields = ['nombre_proyecto', 'cliente', 'descripcion_proyecto', 'fecha_inicio', 'fecha_fin', 'actividades_realizadas', 'archivos_adjuntos', 'enlace_externo']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class CurriculumVitaeForm(forms.ModelForm):
    class Meta:
        model = CurriculumVitae
        fields = ['archivo']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre_curso', 'descripcion_curso', 'organizacion', 'enlace_curso', 'imagen_curso']
