from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rating, RatingResponse, Skill, FreelancerProfile, CompanyProfile, WorkExperience, CurriculumVitae, PortfolioProject, Course
from django.db import IntegrityError
from django.utils.translation import gettext as _, gettext_lazy as __


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_description', 'organization', 'course_link', 'course_image', 'expedition_date']
        widgets = {
            'expedition_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'course_name': _('Nombre del Curso'),
            'course_description': _('Descripción'),
            'organization': _('Organización'),
            'course_link': _('Enlace del Curso'),
            'course_image': _('Imagen del Curso'),
            'expedition_date': _('Fecha de Expedición'),
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
            'project_name': _('Nombre del Proyecto'),
            'client': _('Cliente'),
            'project_description': _('Descripción del Proyecto'),
            'start_date': _('Fecha de Inicio'),
            'end_date': _('Fecha de Finalización'),
            'activities_done': _('Actividades Realizadas'),
            'attached_files': _('Archivos Adjuntos'),
            'external_link': _('Enlace Externo'),
            'project_image': _('Imagen del Proyecto'),
        }


class UploadCVForm(forms.ModelForm):
    class Meta:
        model = CurriculumVitae
        fields = ['file'] 
        labels = {
            'file': _('Sube tu CV (PDF)'),
        }
        widgets = {
            'file': forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),
        }

class AddSkillsForm(forms.ModelForm):
    predefined_skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.filter(is_custom=False),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=__("Habilidades Predeterminadas")
    )
    custom_skills = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': __('Escribe tus habilidades personalizadas separadas por comas')}),
        required=False,
        label=__("Habilidades Personalizadas")
    )
    job_title = forms.CharField(
        max_length=255,
        required=False,
        label=__("Título Profesional"),
        widget=forms.TextInput(attrs={'placeholder': __('Ej: Desarrollador Full Stack')})
    )
    about_me = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': __('Escribe una breve descripción sobre ti')}),
        required=False,
        label=__("Acerca de mí")
    )
    location = forms.CharField(
        max_length=255,
        required=False,
        label=__("Ubicación"),
        widget=forms.TextInput(attrs={'placeholder': __('Ciudad, País')})
    )
    linkedin = forms.URLField(
        required=False,
        label=__("LinkedIn"),
        widget=forms.URLInput(attrs={'placeholder': __('URL de tu LinkedIn')})
    )
    github = forms.URLField(
        required=False,
        label=__("GitHub"),
        widget=forms.URLInput(attrs={'placeholder': __('URL de tu GitHub')})
    )
    twitter = forms.URLField(
        required=False,
        label=_("Twitter"),
        widget=forms.URLInput(attrs={'placeholder': _('URL de tu perfil de Twitter')})
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

            # Populate the profile information fields
            self.fields['job_title'].initial = profile.job_title
            self.fields['about_me'].initial = profile.about_me
            self.fields['location'].initial = profile.location
            self.fields['linkedin'].initial = profile.linkedin
            self.fields['github'].initial = profile.github
            self.fields['twitter'].initial = profile.twitter


            if not self.fields['predefined_skills'].queryset.exists():
                self.all_skills_selected = True

    def save(self, commit=True, user=None):
        profile = FreelancerProfile.objects.get(user=user)
        
        # Update profile information
        profile.job_title = self.cleaned_data.get('job_title')
        profile.about_me = self.cleaned_data.get('about_me')
        profile.location = self.cleaned_data.get('location')
        profile.linkedin = self.cleaned_data.get('linkedin')
        profile.github = self.cleaned_data.get('github')
        profile.twitter = self.cleaned_data.get('twitter')  


        # Save predefined skills
        predefined_skills = self.cleaned_data.get('predefined_skills')
        if predefined_skills:
            profile.skills.add(*predefined_skills)

        # Save custom skills
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
            'title': _('Título del trabajo'),
            'company': _('Compañía'),
            'start_date': _('Fecha de inicio'),
            'end_date': _('Fecha de finalización (opcional)'),
            'description': _('Descripción del trabajo'),
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
    identification = forms.CharField(max_length=20, required=True, label=_('ID de Identificación'))
    phone = forms.CharField(max_length=15, required=True, label=_('Teléfono'))
    photo = forms.ImageField(required=False, label=_('Foto de Perfil'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': _('Nombre de Usuario'),
            'email': _('Correo Electrónico'),
            'password1': _('Contraseña'),
            'password2': _('Confirmar Contraseña'),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = _('Contraseña') 
        self.fields['password2'].label = _('Confirmar Contraseña') 
        self.order_fields(['username', 'identification', 'phone', 'email', 'password1', 'password2', 'photo'])

        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Este correo electrónico ya está registrado. Por favor, usa otro.'))
        return email

    def clean_identification(self):
        identification = self.cleaned_data.get('identification')
        if FreelancerProfile.objects.filter(identification=identification).exists():
            raise forms.ValidationError(_('Este ID ya está registrado. Por favor, usa otro.'))
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
                    self.add_error('identification', _('Este ID ya está registrado. Por favor, usa otro.'))
                    user.delete() 
                return user  
        return user



class CompanyRegisterForm(UserCreationForm):
    company_name = forms.CharField(max_length=100, required=True, label=_('Nombre de la Empresa'))
    nit = forms.CharField(max_length=20, required=True, label=_('NIT'))
    business_type = forms.CharField(max_length=50, required=True, label=_('Tipo de Empresa'))
    country = forms.CharField(max_length=50, required=True, label=_('País'))
    business_vertical = forms.CharField(max_length=50, required=True, label=_('Vertical de Negocio'))
    address = forms.CharField(max_length=150, required=True, label=_('Dirección'))
    legal_representative = forms.CharField(max_length=100, required=True, label=_('Representante Legal'))
    phone = forms.CharField(max_length=15, required=True, label=_('Teléfono'))
    photo = forms.ImageField(required=False, label=_('Imagen de la Empresa'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': _('Nombre de Usuario'),
            'email': _('Correo Electrónico'),
            'password1': _('Contraseña'),
            'password2': _('Confirmar Contraseña'),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = _('Contraseña') 
        self.fields['password2'].label = _('Confirmar Contraseña') 
        self.order_fields(['username', 'company_name', 'nit', 'business_type', 'country', 'business_vertical', 'address', 'legal_representative', 'phone', 'email', 'password1', 'password2', 'photo'])
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Este correo electrónico ya está registrado. Por favor, usa otro.'))
        return email
    
    def clean_nit(self):
        nit = self.cleaned_data.get('nit')
        if CompanyProfile.objects.filter(nit=nit).exists():
            raise forms.ValidationError(_('Este NIT ya está registrado. Por favor, usa otro.'))
        return nit

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
                self.add_error('nit', _('Este NIT ya está registrado. Por favor, usa otro.'))
            raise e  
        return user




class CompanyProfileForm(forms.ModelForm):
    email = forms.EmailField(label="Correo Electrónico", required=True)

    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'business_type', 'business_vertical', 'address', 'phone', 'nit', 'legal_representative']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CompanyProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        company_profile = super(CompanyProfileForm, self).save(commit=False)
        user = company_profile.user
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            company_profile.save()
        return company_profile
