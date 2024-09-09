# freelancer_profile_creation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear-proyecto/', views.crear_proyecto_portafolio, name='crear_proyecto_portafolio'),
    path('subir-curriculum/', views.subir_curriculum, name='subir_curriculum'),
    path('agregar-curso/', views.agregar_curso, name='agregar_curso'),
]
