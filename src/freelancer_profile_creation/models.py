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
    skills = models.ManyToManyField('Skill', related_name='freelancers', blank=True)
    bio = models.TextField(blank=True, null=True)  
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  
    location = models.CharField(max_length=100, blank=True, null=True)  
    contact_email = models.EmailField(blank=True, null=True) 

    def __str__(self):
        return f"Perfil de {self.user.username}"

class WorkExperience(models.Model):
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_experiences")
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} en {self.company}"

class PortfolioProject(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="portfolio_projects")
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
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return f"CurriculumVitae of {self.profile.username}"

class Course(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    course_name = models.CharField(max_length=100)
    course_description = models.TextField(blank=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    course_link = models.URLField(blank=True, null=True)
    course_image = models.ImageField(upload_to='courses/', blank=True, null=True)

    def __str__(self):
        return self.course_name