from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_project, name="create_project"),
    path("my_projects/", views.project_list, name="my_projects"), 
    path("list/", views.project_list_availableFreelancer, name="available_projectsFreelancer"), 
    path('', views.project_list_availableFreelancer, name='project'),
    path("create_milestone/<int:project_id>",views.add_milestone,name="add_milestone"),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('project/<int:project_id>/requirements/', views.project_requirements, name='project_requirements'),
    path("<int:project_id>/<str:section>",views.display_project,name="project"),
    path("create_milestone/<int:project_id>",views.add_milestone,name="add_milestone"),
    path("edit_milestone/<int:milestone_id>",views.edit_milestone, name="edit_milestone"),
    path("delete_milestone/<int:milestone_id>",views.delete_milestone,name="delete_milestone"),
    path("task/create/<int:project_id>",views.create_task,name="create_task")
]
