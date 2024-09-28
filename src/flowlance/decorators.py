from functools import wraps

def attach_profile_info(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        profile, profile_type = user.get_profile_info()
        request.profile = profile
        request.profile_type = profile_type
        return func(request, *args, **kwargs)
    return wrapper