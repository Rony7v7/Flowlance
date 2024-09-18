from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.create_project, name="create_project"),
    path("my_projects/", views.project_list, name="my_projects"), # ya ahora es donde se ve "Mis Proyectos" : SE DEJA 

    path("list/", views.project_list_availableFreelancer, name="available_projectsFreelancer"), # Esta es para que el cliente vea "Disponibles" : SE DEJA

    #path("my_projects_client/", views.project_list, name="my_projects"), # La misma URL de la path("my_projects/", views.project_list, name="my_projects")

    
    #path("listRony/", views.list_projects_Rony, name="list_projects_Rony"), # Esta tira error, pero era para ver "Disponibles" y "Mis Proyectos": SE ELIMINA
    #path("available_projects/", views.project_list_availableFreelancer, name="available_projectsFreelancer"), # Esta es para que el freelancer vea "Disponibles" SE ELIMINA

    path("<int:project_id>/<str:section>",views.display_project,name="project"),
    path("create_milestone/<int:project_id>",views.add_milestone,name="add_milestone"),


    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('<int:project_pk>/milestone/add/', views.milestone_add, name='milestone_add'),
    path('<int:project_pk>/milestone/<int:milestone_pk>/edit/', views.milestone_edit, name='milestone_edit'),
    path('<int:project_pk>/milestone/<int:milestone_pk>/delete/', views.milestone_delete, name='milestone_delete'),
    path('project/<int:project_id>/requirements/', views.project_requirements, name='project_requirements'),

]
