from django.contrib import admin
from .models import PortfolioProject, CurriculumVitae, Course, Skill, WorkExperience, FreelancerProfile, CompanyProfile

admin.site.register(PortfolioProject)
admin.site.register(CurriculumVitae)
admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(FreelancerProfile)
admin.site.register(CompanyProfile)

