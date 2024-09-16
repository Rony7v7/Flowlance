from django.apps import AppConfig


class FreelancerProfileCreationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'freelancer_profile_creation'
    
    def ready(self):
        import freelancer_profile_creation.signals  

    
