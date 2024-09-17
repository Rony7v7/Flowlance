from django.db import models
from django.contrib.auth.models import User

# Skills (predefined and custom)
class Skill(models.Model):
    name = models.CharField(max_length=100)
    is_custom = models.BooleanField(default=False)  # True if the skill is custom, False if it's predefined

    def __str__(self):
        return self.name


class FreelancerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, related_name='freelancers', blank=True)
    portfolio_projects = models.ManyToManyField('PortfolioProject', related_name='freelancer_portfolio', blank=True)
    curriculum_vitae = models.OneToOneField('CurriculumVitae', on_delete=models.SET_NULL, null=True, blank=True)
    courses = models.ManyToManyField('Course', related_name='freelancer_courses', blank=True)
    califications = models.ManyToManyField('Calificacion', related_name='freelancer_califications', blank=True)


class WorkExperience(models.Model):
    freelancer = models.ForeignKey(FreelancerProfile, on_delete=models.CASCADE, related_name="work_experiences")
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} en {self.company}"

class PortfolioProject(models.Model):
    profile = models.ForeignKey(FreelancerProfile, on_delete=models.CASCADE, related_name="freelancer_portfolio_projects")  
    project_name = models.CharField(max_length=100)
    client = models.CharField(max_length=100, blank=True, null=True)
    project_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    activities_done = models.TextField()
    attached_files = models.FileField(upload_to='portfolio/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name


class CurriculumVitae(models.Model):
    profile = models.OneToOneField(FreelancerProfile, on_delete=models.CASCADE, related_name="freelancer_cv")  
    file = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return f"Curriculum Vitae de {self.profile.user.username}"


class Course(models.Model):
    profile = models.ForeignKey(FreelancerProfile, on_delete=models.CASCADE, related_name="freelancer_courses")  
    course_name = models.CharField(max_length=100)
    course_description = models.TextField(blank=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    course_link = models.URLField(blank=True, null=True)
    course_image = models.ImageField(upload_to='courses/', blank=True, null=True)

    def __str__(self):
        return self.course_name
    

class Calificacion(models.Model):
    freelancer = models.ForeignKey(User, related_name="calificaciones", on_delete=models.CASCADE)  # Freelancer a quien se califica
    usuario = models.ForeignKey(User, related_name="calificador", on_delete=models.CASCADE)  # Usuario que hace la calificación
    estrellas = models.IntegerField()  # Número de estrellas
    comentario = models.TextField(null=True, blank=True)  # Comentario opcional
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la calificación

    def __str__(self):
        return f'{self.estrellas} estrellas para {self.freelancer.user.username} por {self.user.username}'
    

    
   