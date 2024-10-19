import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from flowlance.decorators import attach_profile_info, client_required, freelancer_required
from project.models import Project, Task

from project.views.project_views import getProjectProgress

from profile.models import Rating

# Archivo HTML base
building = "navigation/building.html"

@login_required
@attach_profile_info
def dashboard(request):
    if request.profile_type == 'freelancer':
        return freelancer_dashboard(request)
    elif request.profile_type == 'company':
        return company_dashboard(request)
    else:
        return render(request, building)

@freelancer_required
def freelancer_dashboard(request):

    # Get first 10 projects that are not deleted and not has the freelancer as member
    available_projects = Project.objects.filter(is_deleted=False).exclude(members=request.user).order_by('-created_at')[:5]

    freelancer_projects = Project.objects.filter(members=request.user).order_by('-created_at')[:5]

    freelancer_pending_tasks = Task.objects.filter(responsible=request.user, state='pendiente') #TODO: Va a causar problemas en la traducción

    tasks_done_count = Task.objects.filter(responsible=request.user, state='Completada').count()
    tasks_pending_count = freelancer_pending_tasks.count()

    for project in freelancer_projects:
        project.pending_tasks = Task.objects.filter(responsible=request.user, milestone__project=project, state='pendiente' ).count() #TODO: Va a causar problemas en la traducción
        project.progress = getProjectProgress(project.milestones.all(), Task.objects.filter(milestone__project=project))[0]

    freelancer_progress = [tasks_done_count, tasks_pending_count]

    context = {
        'available_projects': available_projects,
        'freelancer_projects': freelancer_projects,
        'freelancer_pending_tasks': freelancer_pending_tasks,
        'freelancer_progress': freelancer_progress
    }
    return render(request, 'dashboard/freelancer_dashboard.html', context)


def freelancer_projects_test(): # Add new TEMPORAL projects to the list 
    projects = []
    for i in range(10):
        project = Project()
        project.title = f'Project {i}'
        project.description = f'This is the description of the project {i}'
        project.progress = random.randint(0, 100)
        project.pending_tasks = random.randint(0, 50)
        project.is_deleted = False
        project.budget = random.randint(100, 1000)
        projects.append(project)
    return projects
    
def freelancer_pending_tasks_test(): # Add new TEMPORAL tasks to the list 
    tasks = []

    for i in range(10):
        task = Task()
        task.title = f'Task {i}'
        task.description = f'This is the description of the task {i}'
        task.start_date = '2021-10-10'
        task.end_date = '2021-10-20'
        task.priority = random.choice(['Low', 'Medium', 'High'])
        task.state = random.choice(['To Do', 'In Progress', 'Done'])
        task.is_deleted = False
        tasks.append(task)

    return tasks

@client_required
def company_dashboard(request):
    
    # Get all freelancers that are members of some project of the company withouth duplicates
    freelancers = []
    for project in request.user.projects.all():
        project.freelancers_users = project.members.all().exclude(id=request.user.id)
        for user in project.freelancers_users:
            freelancer = user.freelancerprofile

            if freelancer not in freelancers:
                
                # Calculate the rating of the freelancer
                ratings = Rating.objects.filter(freelancer=freelancer)
                rating = 0
                for rate in ratings:
                    rating += rate.stars

                if ratings.count() > 0:
                    rating = rating / ratings.count()

                freelancer.rating = rating

                freelancers.append(freelancer)

    company_projects = request.user.projects.all()

    pending_applications = []

    # calc the progress of the projects
    for project in company_projects:
        project.pending_tasks = Task.objects.filter(milestone__project=project, state='pendiente' ).count()
        project.progress = getProjectProgress(project.milestones.all(), Task.objects.filter(milestone__project=project))[0]
        pending_applications += project.applications.filter(is_deleted=False, status='Pendiente')
        

    context = {
        'recent_freelancers': freelancers,
        'company_projects': company_projects,
        'pending_applications': pending_applications

    }
    return render(request, 'dashboard/company_dashboard.html', context)
