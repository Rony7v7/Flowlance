from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Skill(models.Model):
    name = models.CharField(max_length=100)
    is_custom = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name


#En esta tabla podemos encontrar las cofiguraciones del perfil
class ProfileConfiguration(models.Model):

    class Periodicity(models.TextChoices):
        DAILY = 'D', _('Diariamente')
        WEEKLY = 'W', _('Semanalmente')
        MONTHLY = 'M', _('Mensualmente')

    id = models.AutoField(primary_key=True)
    notification_when_profile_visited = models.BooleanField(default=True)
    sending_notification_to_email = models.BooleanField(default=False)
    periodicity_of_notification_report = models.CharField(max_length=20,choices=Periodicity.choices,default=Periodicity.MONTHLY)
    silent_start = models.TimeField(null=True, blank=True, help_text="Start of silent hours")
    silent_end = models.TimeField(null=True, blank=True, help_text="End of silent hours")
    receive_project_updates = models.BooleanField(default=True)
    receive_messages = models.BooleanField(default=False)  # Default to False as required
    receive_job_opportunities = models.BooleanField(default=True)
    
    

class FreelancerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=False, null=False)
    identification = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='freelancers/', blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='freelancers', blank=True)
    portfolio = models.OneToOneField('Portfolio', on_delete=models.SET_NULL, null=True, blank=True)
    curriculum_vitae = models.OneToOneField('CurriculumVitae', on_delete=models.SET_NULL, null=True, blank=True)
    ratings = models.ManyToManyField('Rating', related_name='freelancer_rating', blank=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    profileconfiguration = models.OneToOneField(ProfileConfiguration, on_delete=models.CASCADE,null=True)

    has_2FA_on = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.user.username

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    nit = models.CharField(max_length=20, unique=True)
    business_type = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    business_vertical = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    legal_representative = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    has_2FA_on = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='companies/', blank=True, null=True)
    profileconfiguration = models.OneToOneField(ProfileConfiguration, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.username

class Portfolio(models.Model):
    freelancer_profile = models.OneToOneField(
        FreelancerProfile, 
        on_delete=models.CASCADE, 
        related_name="portfolio_profile"  
    )
    
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"Portfolio of {self.freelancer_profile}"

class PortfolioProject(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, 
        on_delete=models.CASCADE, 
        related_name="projects"
    ) 
    project_name = models.CharField(max_length=100)
    client = models.CharField(max_length=100, blank=True, null=True)
    project_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    activities_done = models.TextField()
    attached_files = models.FileField(upload_to='portfolio/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)
    project_image = models.ImageField(upload_to='portfolio/projects/', blank=True, null=True)  
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.project_name

class Course(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="courses", null=True, blank=True)  
    course_name = models.CharField(max_length=100)
    course_description = models.TextField(blank=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    course_link = models.URLField(blank=True, null=True)
    course_image = models.ImageField(upload_to='courses/', blank=True, null=True)
    expedition_date = models.DateField(null=True, blank=True) 
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.course_name

class WorkExperience(models.Model):
    freelancer = models.ForeignKey(FreelancerProfile, on_delete=models.CASCADE, related_name="freelancer_work_experience")  
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"{self.title} en {self.company}"

class CurriculumVitae(models.Model):
    profile = models.OneToOneField(FreelancerProfile, on_delete=models.CASCADE, related_name="freelancer_cv")  
    file = models.FileField(upload_to='resumes/', blank=True, null=True)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"Curriculum Vitae de {self.profile.user.username}"

class Rating(models.Model):
    freelancer = models.ForeignKey(FreelancerProfile, on_delete=models.CASCADE, related_name='received_ratings')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_ratings')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"{self.client.username}'s rating for {self.freelancer.user.username}"


class RatingResponse(models.Model):
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE, related_name='response')
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.estrellas} estrellas para {self.freelancer.username} por {self.usuario.username}'

