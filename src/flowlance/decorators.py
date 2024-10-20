from functools import wraps

from django.shortcuts import get_object_or_404, render

from project.models import Project # temporal render

def attach_profile_info(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        profile, profile_type = user.get_profile_info()
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

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            project = get_object_or_404(Project, id=kwargs['project_id'])
            member = project.memberships.get(user=request.user)
            
            if member.role == role:
                return func(request, *args, **kwargs)
            
            return render(request, 'errors/error_generic.html', {'error_type':'custom_permission'}) # temporal render
        return wrapper
    return decorator