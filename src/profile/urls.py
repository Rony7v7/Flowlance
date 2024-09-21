from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('freelancer_profile/', views.freelancer_profile, name='freelancer_profile'), # URL for viewing the own freelancer profile
    path('freelancer_profile/<str:username>/', views.freelancer_profile, name='freelancer_profile_view'),  # URL for viewing another freelancer profile
    path("add_skills/", views.add_skills, name="add_skills"),
    path("add_experience/", views.add_experience, name="add_experience"),
    path('upload_curriculum/', views.upload_curriculum, name='upload_curriculum'),
    path('add_project/', views.add_project, name='add_project'),
    path('add_course/', views.add_course, name='add_course'),   
    path('notifications/', views.notifications, name='notifications'),
]