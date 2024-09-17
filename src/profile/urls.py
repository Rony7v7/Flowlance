# profile/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path(
        "create_project/",
        views.create_project_portfolio,
        name="create_project_portfolio",
    ),
    path("upload_curriculum/", views.upload_curriculum, name="upload_curriculum"),
    path("add_course/", views.add_course, name="add_course"),
]
