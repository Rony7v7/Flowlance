from django.urls import path
from . import views

urlpatterns = [
    path('calificar/<int:freelancer_id>/', views.calificar_freelancer, name='calificar_freelancer'),

    # La ruta es asi debido a la logica anterior donde el cliente le tiene que dar click en la pantalla a que freelancer quiere calificar
]
