from functools import wraps

from django.shortcuts import render # temporal render

def attach_profile_info(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        profile, profile_type = user.get_profile_info()
        request.profile = profile
        request.profile_type = profile_type
        return func(request, *args, **kwargs)
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
        if user_type == 'client':
            return func(request, *args, **kwargs)
        return render(request, 'errors/error_generic.html', {'error_type':'custom_permission'}) # temporal render
    return wrapper