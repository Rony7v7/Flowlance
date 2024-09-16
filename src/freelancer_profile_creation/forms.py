from django import forms
from .models import PortfolioProject, CurriculumVitae, Course, Skill, WorkExperience
from django.core.exceptions import ValidationError


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa una nueva habilidad...'}),
        }

# 44545
class FreelancerSkillsForm(forms.Form):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.filter(is_custom=False),  # Predefined skills
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label="Selecciona habilidades predefinidas"
    )
    custom_skills = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Añadir habilidades personalizadas separadas por comas...'}),
        required=False,
        label="Habilidades personalizadas"
    )

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['title', 'company', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if end_date and start_date and end_date < start_date:
            raise forms.ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio.")
        
        return cleaned_data


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

