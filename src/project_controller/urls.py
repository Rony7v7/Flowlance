from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.create_project, name="create_project"),
    path("my_projects/", views.my_projects, name="my_projects"),
    path("<int:project_id>/<str:section>",views.display_project,name="project")
]
