# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_project, name="create_project"),
    path("list/", views.list_projects, name="list_projects"),
    path("<int:project_id>/<str:section>", views.display_project, name="project"),
    path("create_milestone/<int:project_id>", views.add_milestone, name="add_milestone"),
    path('task/<int:task_id>/add-description/', views.add_description, name='add_description'),
    path('task/<int:task_id>/add-file/', views.add_file, name='add_file'),
    path('description/<int:description_id>/edit/', views.edit_description, name='edit_description'),
    path('task/<int:task_id>/add-comment/', views.add_comment, name='add_comment'),
    path("apply/<int:project_id>/", views.apply_project, name="apply_project"),
    path("my_projects/", views.project_list, name="my_projects"), 
    path("list/", views.project_list_availableFreelancer, name="available_projectsFreelancer"), 
    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('project/<int:project_id>/requirements/', views.project_requirements, name='project_requirements'),
    path("edit_milestone/<int:milestone_id>", views.edit_milestone, name="edit_milestone"),
    path("delete_milestone/<int:milestone_id>", views.delete_milestone,name="delete_milestone"),
    path("task/create/<int:project_id>", views.create_task, name="create_task")
]
