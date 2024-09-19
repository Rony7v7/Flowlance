from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.create_project, name="create_project"),
    path("my_projects/", views.project_list, name="my_projects"), 
    path("list/", views.project_list_availableFreelancer, name="available_projectsFreelancer"), 
    path('', views.project_list, name='project_list'),
    path("create_milestone/<int:project_id>",views.add_milestone,name="add_milestone"),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('<int:project_pk>/milestone/add/', views.milestone_add, name='milestone_add'),
    path('<int:project_pk>/milestone/<int:milestone_pk>/edit/', views.milestone_edit, name='milestone_edit'),
    path('<int:project_pk>/milestone/<int:milestone_pk>/delete/', views.milestone_delete, name='milestone_delete'),
    path('project/<int:project_id>/requirements/', views.project_requirements, name='project_requirements'),

]
