from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("create_project/", views.create_project_portfolio, name="create_project_portfolio"),
    path("upload_curriculum/", views.upload_curriculum, name="upload_curriculum"),
    path("add_course/", views.add_course, name="add_course"),
    path("freelancer/<str:username>/", views.freelancer_profile, name="freelancer_profile"),  # URL del perfil del freelancer
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
