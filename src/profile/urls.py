from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("create_project/", views.create_project_portfolio, name="create_project_portfolio"),
    path("upload_curriculum/", views.upload_curriculum, name="upload_curriculum"),
    path("add_course/", views.add_course, name="add_course"),
    path("freelancer/<str:username>/", views.freelancer_profile, name="freelancer_profile"),  # Ver perfil de un freelancer específico
    path("my_profile/", views.freelancer_own_profile, name="freelancer_own_profile"),  # Ver el perfil del freelancer logueado
    path("add_skills/", views.add_skills, name="add_skills"),
    path("add_experience/", views.add_experience, name="add_experience"),
    path("no_freelancer_profile/", views.no_freelancer_profile, name="no_freelancer_profile"),

    path('calificar/<str:username>/', views.calificar_freelancer, name='calificar_freelancer'),
    

]