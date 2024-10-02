from django.db import models
from django.contrib.auth.models import User

User.add_to_class('get_profile_info', lambda self: self._get_profile_info())

def _get_profile_info(self):
    """
    Get the profile of the user, if the user is a freelancer or a company
    """
    if hasattr(self, 'freelancerprofile'):
        return self.freelancerprofile, 'freelancer'
    elif hasattr(self, 'companyprofile'):
        return self.companyprofile, 'company'
    return None, None

User._get_profile_info = _get_profile_info