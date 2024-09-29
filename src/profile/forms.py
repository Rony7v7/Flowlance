from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rating, RatingResponse, Skill, FreelancerProfile, CompanyProfile, WorkExperience, CurriculumVitae, PortfolioProject, Course
from django.db import IntegrityError


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

class FreelancerRegisterForm(UserCreationForm):
    identification = forms.CharField(max_length=20, required=True, label='ID de Identificación')
    phone = forms.CharField(max_length=15, required=True, label='Teléfono')
    photo = forms.ImageField(required=False, label='Foto de Perfil')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar Contraseña'
        self.order_fields(['username', 'identification', 'phone', 'email', 'password1', 'password2', 'photo'])

        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado. Por favor, usa otro.')
        return email

    def clean_identification(self):
        identification = self.cleaned_data.get('identification')
        if FreelancerProfile.objects.filter(identification=identification).exists():
            raise forms.ValidationError('Este ID ya está registrado. Por favor, usa otro.')
        return identification

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            try:
                FreelancerProfile.objects.create(
                    user=user,
                    identification=self.cleaned_data['identification'],
                    phone=self.cleaned_data['phone'],
                    photo=self.cleaned_data.get('photo')
                )
            except IntegrityError as e:
                if 'unique constraint' in str(e).lower() and 'identification' in str(e).lower():
                    self.add_error('identification', 'Este ID ya está registrado. Por favor, usa otro.')
                    user.delete() 
                return user  
        return user



class CompanyRegisterForm(UserCreationForm):
    company_name = forms.CharField(max_length=100, required=True, label='Nombre de la Empresa')
    nit = forms.CharField(max_length=20, required=True, label='NIT')
    business_type = forms.CharField(max_length=50, required=True, label='Tipo de Empresa')
    country = forms.CharField(max_length=50, required=True, label='País')
    business_vertical = forms.CharField(max_length=50, required=True, label='Vertical de Negocio')
    address = forms.CharField(max_length=150, required=True, label='Dirección')
    legal_representative = forms.CharField(max_length=100, required=True, label='Representante Legal')
    phone = forms.CharField(max_length=15, required=True, label='Teléfono')
    photo = forms.ImageField(required=False, label='Imagen de la Empresa')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar Contraseña'
        self.order_fields(['username', 'company_name', 'nit', 'business_type', 'country', 'business_vertical', 'address', 'legal_representative', 'phone', 'email', 'password1', 'password2', 'photo'])
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado. Por favor, usa otro.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        try:
            if commit:
                user.save()
                CompanyProfile.objects.create(
                    user=user,
                    company_name=self.cleaned_data['company_name'],
                    nit=self.cleaned_data['nit'],
                    business_type=self.cleaned_data['business_type'],
                    country=self.cleaned_data['country'],
                    business_vertical=self.cleaned_data['business_vertical'],
                    address=self.cleaned_data['address'],
                    legal_representative=self.cleaned_data['legal_representative'],
                    phone=self.cleaned_data['phone'],
                    photo=self.cleaned_data.get('photo')
                )
        except IntegrityError as e:
            if 'unique constraint' in str(e).lower() and 'nit' in str(e).lower():
                self.add_error('nit', 'Este NIT ya está registrado. Por favor, usa otro.')
            raise e  
        return user
