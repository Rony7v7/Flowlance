# freelancer_profile_creation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path(
        "create_project/",
        views.crear_proyecto_portafolio,
        name="create_project_portfolio",
    ),
    path("upload_curriculum/", views.subir_curriculum, name="upload_curriculum"),
    path("add_course/", views.agregar_curso, name="add_course"),
]
