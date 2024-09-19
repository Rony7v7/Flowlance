from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import FreelancerProfile

# Create a freelancer profile only for users who are not superusers
@receiver(post_save, sender=User)
def create_freelancer_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:  # Avoid creation for superusers
        FreelancerProfile.objects.create(user=instance)

# Save the freelancer profile only if the user has one
@receiver(post_save, sender=User)
def save_freelancer_profile(sender, instance, **kwargs):
    try:
        if hasattr(instance, 'freelancerprofile'):
            instance.freelancerprofile.save()
    except FreelancerProfile.DoesNotExist:
        pass  # Do nothing if the freelancer profile does not exist
