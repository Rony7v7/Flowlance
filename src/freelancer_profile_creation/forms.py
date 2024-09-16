from django import forms
from .models import PortfolioProject, CurriculumVitae, Course
from django.core.exceptions import ValidationError

class CurriculumVitaeForm(forms.ModelForm):
    class Meta:
        model = CurriculumVitae
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.endswith('.pdf'):
                raise ValidationError('El currículum debe estar en formato PDF.')
        return file

class PortfolioProjectForm(forms.ModelForm):
    class Meta:
        model = PortfolioProject
        fields = ['project_name', 'client', 'project_description', 'start_date', 'end_date', 'activities_done', 'attached_files', 'external_link']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_attached_files(self):
        file = self.cleaned_data.get('attached_files')
        if file:
            if not file.name.endswith(('.png', '.jpg', '.jpeg', '.pdf', '.docx')):
                raise ValidationError('El archivo adjunto debe ser una imagen o documento (png, jpg, pdf, docx).')
        return file


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_description', 'organization', 'course_link', 'course_image']


# forms.py
from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estrellas', 'comentario']
        widgets = {
            'estrellas': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'comentario': forms.Textarea(attrs={'rows': 3}),
        }





