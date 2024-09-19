from django.contrib import admin
from .models import PortfolioProject, CurriculumVitae, Course, Skill, WorkExperience, FreelancerProfile

admin.site.register(PortfolioProject)
admin.site.register(CurriculumVitae)
admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(FreelancerProfile)

