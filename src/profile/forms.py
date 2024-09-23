from django import forms
from .models import Rating, RatingResponse, Skill, FreelancerProfile, WorkExperience, CurriculumVitae, PortfolioProject, Course

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_description', 'organization', 'course_link', 'course_image', 'expedition_date']
        widgets = {
            'expedition_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'course_name': 'Nombre del Curso',
            'course_description': 'Descripción',
            'organization': 'Organización',
            'course_link': 'Enlace del Curso',
            'course_image': 'Imagen del Curso',
            'expedition_date': 'Fecha de Expedición',
        }


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = PortfolioProject
        fields = ['project_name', 'client', 'project_description', 'start_date', 'end_date', 'activities_done', 'attached_files', 'external_link', 'project_image']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'project_name': 'Nombre del Proyecto',
            'client': 'Cliente',
            'project_description': 'Descripción del Proyecto',
            'start_date': 'Fecha de Inicio',
            'end_date': 'Fecha de Finalización',
            'activities_done': 'Actividades Realizadas',
            'attached_files': 'Archivos Adjuntos',
            'external_link': 'Enlace Externo',
            'project_image': 'Imagen del Proyecto',
        }


class UploadCVForm(forms.ModelForm):
    class Meta:
        model = CurriculumVitae
        fields = ['file'] 
        labels = {
            'file': 'Sube tu CV (PDF)',
        }
        widgets = {
            'file': forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),
        }

class AddSkillsForm(forms.ModelForm):
    predefined_skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.filter(is_custom=False),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Habilidades Predeterminadas"
    )
    custom_skills = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Escribe tus habilidades personalizadas separadas por comas'}),
        required=False,
        label="Habilidades Personalizadas"
    )
    all_skills_selected = False  

    class Meta:
        model = FreelancerProfile
        fields = []

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddSkillsForm, self).__init__(*args, **kwargs)

        if user:
            profile = FreelancerProfile.objects.get(user=user)
            predefined_skills_queryset = Skill.objects.filter(is_custom=False)
            
            if not predefined_skills_queryset.exists():
                predefined_skills = [
                    Skill(name='Python', is_custom=False),
                    Skill(name='Django', is_custom=False),
                    Skill(name='JavaScript', is_custom=False)
                ]
                Skill.objects.bulk_create(predefined_skills)
                predefined_skills_queryset = Skill.objects.filter(is_custom=False)

            self.fields['predefined_skills'].queryset = predefined_skills_queryset.exclude(freelancers=profile)

            if not self.fields['predefined_skills'].queryset.exists():
                self.all_skills_selected = True

    def save(self, commit=True, user=None):
        profile = FreelancerProfile.objects.get(user=user)
        predefined_skills = self.cleaned_data.get('predefined_skills')
        if predefined_skills:
            profile.skills.add(*predefined_skills)

        custom_skills_text = self.cleaned_data.get('custom_skills')
        if custom_skills_text:
            custom_skills = [skill.strip() for skill in custom_skills_text.split(',') if skill.strip()]
            for skill_name in custom_skills:
                skill, created = Skill.objects.get_or_create(name=skill_name, is_custom=True)
                profile.skills.add(skill)

        if commit:
            profile.save()
        return profile




class AddWorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['title', 'company', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Título del trabajo',
            'company': 'Compañía',
            'start_date': 'Fecha de inicio',
            'end_date': 'Fecha de finalización (opcional)',
            'description': 'Descripción del trabajo',
        }

    def save(self, commit=True, user=None):
        profile = FreelancerProfile.objects.get(user=user)
        work_experience = super().save(commit=False)
        work_experience.freelancer = profile 
        if commit:
            work_experience.save()
        return work_experience

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars', 'comment']
        widgets = {
            'stars': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class RatingResponseForm(forms.ModelForm):
    class Meta:
        model = RatingResponse
        fields = ['response_text']

