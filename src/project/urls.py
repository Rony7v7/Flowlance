from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.create_project, name="create_project"),
    path("list/", views.list_projects, name="list_projects"),
    path("<int:project_id>/<str:section>",views.display_project,name="project"),
    path("create_milestone/<int:project_id>",views.add_milestone,name="add_milestone"),
    path("edit_milestone/<int:milestone_id>",views.edit_milestone, name="edit_milestone"),
    path("delete_milestone/<int:milestone_id>",views.delete_milestone,name="delete_milestone")
]
