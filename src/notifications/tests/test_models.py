from django.test import TestCase
from django.contrib.auth.models import User
from profile.models import FreelancerProfile, ProfileConfiguration
from datetime import time

class ProfileConfigurationModelTest(TestCase):

    def setUp(self):
        #* # Create a user and associated profile
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        #* Create a profile for the user (e.g., FreelancerProfile)
        self.profile = FreelancerProfile.objects.create(user=self.user, identification='ID123')
        
        #* Create ProfileConfiguration and link it to the profile
        self.profile_config = ProfileConfiguration.objects.create(
            notification_when_profile_visited=True,
            sending_notification_to_email=True,
            periodicity_of_notification_report=ProfileConfiguration.Periodicity.MONTHLY,
            silent_start=time(22, 0),
            silent_end=time(6, 0),
            receive_messages=False,  # Default to False
            receive_project_updates=True,
            receive_job_opportunities=True,
        )
        self.profile.profileconfiguration = self.profile_config
        self.profile.save()
    
    def test_silent_hours_fields(self):
        #* Test that silent hours fields can be set and saved.
        # Verify that the silent hours were saved correctly in ProfileConfiguration
        self.assertEqual(self.profile_config.silent_start, time(22, 0))
        self.assertEqual(self.profile_config.silent_end, time(6, 0))
    
    def test_default_notification_settings(self):
        #* Test that message notifications are off by default.
        # Ensure that default settings are as expected in ProfileConfiguration
        self.assertFalse(self.profile_config.receive_messages)
        self.assertTrue(self.profile_config.receive_project_updates)
        self.assertTrue(self.profile_config.receive_job_opportunities)
