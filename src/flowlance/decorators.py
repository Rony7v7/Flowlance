from functools import wraps

from django.shortcuts import get_object_or_404, render

from project.models import Milestone, Project, ProjectMember, Task # temporal render

def attach_profile_info(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        profile, profile_type = user.get_profile_info()
        unread_notifications = user.notifications.filter(is_read=False).count()
        profile.unread_notifications = unread_notifications
        request.profile = profile
        request.profile_type = profile_type
        return func(request, **kwargs)
    return wrapper

def freelancer_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        profile, user_type = request.user.get_profile_info()
        if user_type == 'freelancer':
            return func(request, *args, **kwargs)
        return render(request, 'errors/error_generic.html', {'error_type':'custom_permission'}) # temporal render
    return wrapper

def client_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        profile, user_type = request.user.get_profile_info()
        if user_type == 'company':
            return func(request, *args, **kwargs)
        return render(request, 'errors/error_generic.html', {'error_type':'custom_permission'}) # temporal render
    return wrapper

def role_required(roles):
    """
    Decorador que verifica si el usuario tiene el rol necesario en el proyecto asociado.
    Funciona con diferentes tipos de IDs (project_id, milestone_id, task_id, etc.).
    
    Args:
        roles (list): Lista de roles permitidos para la vista.
    
    Returns:
        Una función que verifica si el usuario tiene el rol adecuado en el proyecto.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            project = None

            # Maneja diferentes tipos de IDs para obtener el proyecto
            if 'project_id' in kwargs:
                project = get_object_or_404(Project, id=kwargs['project_id'])
            elif 'milestone_id' in kwargs:
                milestone = get_object_or_404(Milestone, id=kwargs['milestone_id'])
                project = milestone.project 
            elif 'task_id' in kwargs:
                task = get_object_or_404(Task, id=kwargs['task_id'])
                project = task.milestone.project
            elif 'member_id' in kwargs:
                project_member = get_object_or_404(ProjectMember, id=kwargs['member_id'])
                project = project_member.project

            # Verificar si el usuario es miembro del proyecto
            if project:
                project_member = ProjectMember.objects.filter(user=request.user, project=project).first()
                if not project_member or project_member.role not in roles:
                    return render(request, 'errors/error_generic.html', {'error_type': 'custom_permission'})  # Render temporal
            
            return view_func(request, *args, **kwargs)

        return _wrapped_view
    return decorator