# urls.py
from django.urls import path
from .views import project_views , milestone_views , task_views , assigment_views, members_views

urlpatterns = [
    path("create/", project_views.create_project, name="create_project"),
    path("list/", project_views.project_list, name="list_projects"),# David changed this line from views.lists_projects to views.project_list because that does not exist in views.py
    path("<int:project_id>/<str:section>", project_views.display_project, name="project"),
    path("apply/<int:project_id>/", project_views.apply_project, name="apply_project"),
    path("my_projects/", project_views.project_list, name="my_projects"), 
    path("list/", project_views.project_list_availableFreelancer, name="available_projectsFreelancer"), 
    path('', project_views.project_list_availableFreelancer, name='project_list'),
    path('<int:project_id>/edit/', project_views.project_edit, name='project_edit'),
    path('<int:project_id>/delete/', project_views.project_delete, name='project_delete'),
    path('application/<int:application_id>/<str:action>/', project_views.update_application_status, name='update_application_status'),
    path('<int:project_id>/requirements/', project_views.project_requirements, name='project_requirements'),
    path("create_milestone/<int:project_id>", milestone_views.add_milestone, name="add_milestone"),
    path("edit_milestone/<int:milestone_id>", milestone_views.edit_milestone, name="edit_milestone"),
    path("delete_milestone/<int:milestone_id>", milestone_views.delete_milestone,name="delete_milestone"),
    path('task/<int:task_id>/add-description/', task_views.add_description, name='add_description'),
    path('task/<int:task_id>/add-file/', task_views.add_file, name='add_file'),
    path('description/<int:description_id>/edit/', task_views.edit_description, name='edit_description'),
    path('task/<int:task_id>/add-comment/', task_views.add_comment, name='add_comment'),
    path("task/create/<int:project_id>",task_views.create_task,name="create_task"),
    path('task/update_state/<int:task_id>/', task_views.update_task_state, name='update_task_state'),
    path("assigment/create/<int:milestone_id>",assigment_views.create_assigment, name= "create_assigment"),
    path('assigment/<int:assigment_id>/upload/', assigment_views.upload_assigment, name='upload_assigment'),
    path("assigment/edit/<int:assigment_id>",assigment_views.edit_assigment,name="edit_assigment"),
    path("assigment/delete/<int:assigment_id>",assigment_views.delete_assigment,name="delete_assigment"),
    path("assigment/<int:assigment_id>",assigment_views.get_assigment_information, name="assigment_information"),
    path('task/update_state/<int:task_id>/', task_views.update_task_state, name='update_task_state'),
    path('project/<int:project_id>/generate-report/', project_views.generate_project_report, name='generate_project_report'),
    path('project/<int:project_id>/report-settings/', project_views.report_settings, name='report_settings'),
    path('download-report/<int:project_id>/', project_views.download_project_report, name='download_project_report'),
    path('update_role/<int:member_id>/', members_views.update_role, name='update_role'),
    path('delete_member/<int:member_id>/', members_views.delete_member, name='delete_member'),
]

